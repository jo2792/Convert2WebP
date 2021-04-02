import os
from PIL import Image
from tqdm import tqdm

path = os.getcwd()

if not os.path.isdir(os.path.join(path,'Input')):
    print("Initialize I/O folders")
    os.mkdir(os.path.join(path,'Input'))
if not os.path.isdir(os.path.join(path,'Output')):
    os.mkdir(os.path.join(path,'Output'))

file_list = os.listdir(os.path.join(path,'Input'))

for file in tqdm(file_list, disable=not len(file_list), unit='Image', desc="Convert"):
    try:
        file_path = os.path.join(path,'Input',file)
        file_destination = os.path.join(path,'Output',file.rsplit('.')[0]+'.webp')

        img = Image.open(file_path)
        img.save(file_destination, format = "WebP", lossless = True)
    except:
        print(f"\nFile {file} can't be converted!")