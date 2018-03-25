import os
import subprocess
from tqdm import tqdm
from PIL import Image


fp = '/home/riveria/Documents/Code_Playground/'

dir = os.listdir(fp)

resize_array = []

for folder in tqdm(dir):
	folders = os.listdir(fp + folder)
	for file in tqdm(folders):
		if not file.endswith('py'):
			file_dir = fp + folder + '/' + file
			img = Image.open(file_dir)
			width, height = img.size
			if (width > 224 and height > 224):
				pass
			else:
				resize_array.append(file_dir)

subprocess.call(['./enhance.py', *resize_array])
