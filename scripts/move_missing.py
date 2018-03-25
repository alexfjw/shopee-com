import os
import shutil
from tqdm import tqdm

fp_src = ''
fp_dst = 'E:/OneDrive - National University of Singapore/Shopee IET Machine Learning/Training Images/'

dir_src = os.listdir(fp_src)

for file in tqdm(dir_src):
    folder_name = file.split('_')[0]
    shutil.move(fp_src + file, fp_dst + folder_name + file)