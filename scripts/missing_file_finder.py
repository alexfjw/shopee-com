import os
import shutil
from tqdm import tqdm

fp_original = 'E:/OneDrive - National University of Singapore/Shopee IET Machine Learning/Training Images/'
fp_to_find = 'E:/OneDrive - National University of Singapore/Shopee IET Machine Learning/multi_pass_train/to_process/'

directory_original = os.listdir(fp_original)
directory_to_find = os.listdir(fp_to_find)

files_original_array = []
files_to_find_array = []

for folder in tqdm(directory_original):
    files = os.listdir(fp_original + folder)
    for file in files:
        files_original_array.append(file)

print(len(files_original_array))

for folder in tqdm(directory_to_find):
    files = os.listdir(fp_to_find + folder)
    for file in tqdm(files):
        if '_ne2x' in file:
            file_restored = file.split('_ne2x')[0]
        else:
            file_restored = file.split('.')[0]
        files_to_find_array.append(file_restored)

for file_to_find in tqdm(files_to_find_array):
    for file in tqdm(files_original_array):
        if file_to_find in file:
            files_original_array.remove(file)
            continue
    files_to_find_array.remove(file_to_find)

print(len(files_original_array))

folder_new = 'to_move'
if not os.path.exists(folder_new):
    os.makedirs(folder_new)

for item in tqdm(files_original_array):
    shutil.copy(fp_original + item, folder_new)
