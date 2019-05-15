import os
import shutil

fp_original = 'E:/OneDrive - National University of Singapore/Shopee IET Machine Learning/Training Images/'
fp_to_find = 'E:/OneDrive - National University of Singapore/Shopee IET Machine Learning/multi_pass_train/to_process/'

directory_original = os.listdir(fp_original)
directory_to_find = os.listdir(fp_to_find)

files_original = []
files_to_find = []

for folder in directory_original:
    files = os.listdir(fp_original + folder)
    for file in directory_original:
        files_original.append(file)

print(len(files_original))

for folder in directory_to_find:
    files = os.listdir(fp_to_find + folder)
    for file in files:
        if '_ne2x' in file:
            file_restored = file.split('_ne2x')[0]
        else:
            file_restored = file.split('.')[0]
        files_to_find.append(file_restored)

print(len(files_to_find))

print(files_original)
print(files_to_find)

for file in files_original:
    for file_to_find in files_to_find:
        if file_to_find in file:
            files_to_find.remove(file_to_find)
            files_original.remove(file)
            continue
        else:
            pass

print(files_original)
print(files_to_find)
print(len(files_original))
print(len(files_to_find))

# folder_new = 'to_move'
# os.makedirs(folder_new, exist_ok=True)
#
# for item in tqdm(files_original):
#     folder_name = item.split('_')[0]
#     shutil.copy(fp_original + folder_name + item, folder_new)
