import os
import shutil


path = "D:/VScode project/python/BTL_HTTM/Database/Train/UareU_2/"
path1 = "D:/VScode project/python/BTL_HTTM/Database/Test/UareU_2/"
dir_list = os.listdir(path)



print(dir_list)

for x in dir_list:
    if x.endswith("_1.tif") or x.endswith("_2.tif"):
        shutil.move(path + x, path1)