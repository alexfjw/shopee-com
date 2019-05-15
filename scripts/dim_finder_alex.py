import os
import subprocess
from tqdm import tqdm
from PIL import Image
import sys


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


fp = './to_process/'

dirs = os.listdir(fp)
count = 0
to_resize = []
for folder in tqdm(dirs):
    folders = os.listdir(fp + folder)
    for file in tqdm(folders):
        file_dir = fp + folder + '/' + file
        img = Image.open(file_dir)
        width, height = img.size
        if (width > 224 and height > 224):
            pass
        else:
            to_resize.append(file_dir)

print(len(to_resize))
to_resize = list(set(to_resize))
print(len(to_resize))
to_resize = sorted(to_resize)

chunked = chunks(to_resize, 500)
# subprocess.call(['./enhance.py',
#                 '--type=photo',
#                 '--zoom=2',
#                 '--model=default',
#                 '--device=cuda0',
#                 *to_resize])
try:
    for chunk in tqdm(chunked):
        model = '--model=default'

        subprocess.call(['./enhance.py',
                         '--type=photo',
                         model,
                         '--zoom=2',
                         '--device=cuda0',
                         *chunk])
except:
    sys.exit()

for d in to_resize:
    os.remove(d)
