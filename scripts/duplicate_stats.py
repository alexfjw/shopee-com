import os
import sys

args = sys.argv[1]

fp = "/media/riveria/7C4095214094E2E6/OneDrive - National University of Singapore/Shopee IET Machine Learning/Test Images/"
destination = args + "/"
destination_dupe = args + "Dupe/"

total = len(os.listdir(fp + destination)) + len(os.listdir(fp + destination_dupe))
dupe = len(os.listdir(fp + destination_dupe))
delta = dupe / total

print(delta)
