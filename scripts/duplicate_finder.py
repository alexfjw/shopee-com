import os, errno
import sys
import logging
import shutil
import numpy

from image_match.goldberg import ImageSignature
from tqdm import tqdm


class Pair:
    def __init__(self):
        signature = numpy.ndarray
        file = ''


args = sys.argv[1]

fp = "/C:/Users/kazes/Documents/Test/Test Images/"
destination = args + "/"
destination_clean = args + "Clean/"
destination_dupe = args + "Dupe/"

if not os.path.exists(fp + destination_dupe):
    os.makedirs(fp + destination_dupe)

imutable_dir = os.listdir(fp + destination)
log = open((fp + destination_dupe + 'log.txt'), 'w')

gis = ImageSignature()

master = []
clean = []
duplicates = []

# Create signature arrays of the image files
for file in tqdm(imutable_dir):
    signature = gis.generate_signature(fp + destination + file)
    pair = Pair()
    pair.signature = signature
    pair.file = file
    master.append(pair)

# Iterate through and compare with the reference file
for i, reference_pair in enumerate(tqdm(master)):
    log.write("========================================\n")
    log.write("Reference File: " + reference_pair.file + "\n")
    for j, comparison_pair in enumerate(tqdm(master)):
        if not (reference_pair.file in comparison_pair.file):
            normalized_distance = gis.normalized_distance(reference_pair.signature, comparison_pair.signature)
            if normalized_distance < 0.3:
                log.write("Duplicate: " + comparison_pair.file + "\n")
                duplicates.append(comparison_pair)
            else:
                clean.append(comparison_pair)
    del master[i]
    log.write("========================================\n")

duplicates = list(dict.fromkeys(duplicates))
for i, file_pair in enumerate(tqdm(duplicates)):
    shutil.move(fp + destination + file_pair.file, fp + destination_dupe + file_pair.file)
