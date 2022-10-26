import os
import shutil


path = "D:/VScode project/python/BTL_HTTM/Database/Train/DB4_B_2002/"
path1 = "D:/VScode project/python/BTL_HTTM/Database/Test/DB4_B_2002/"

pathTrain = "D:/VScode project/python/BTL_HTTM/Database/Train/"

pathTest = "D:/VScode project/python/BTL_HTTM/Database/Test/"

dir_listTrain = os.listdir(pathTrain)
dir_listTest = os.listdir(pathTest)


# print(dir_list)

# for x in dir_list:
#     if x.endswith("_3.tif"):
#         shutil.move(path + x, path)

for folder in dir_listTrain:
    for file_name in os.listdir(pathTrain+folder):
        if file_name.endswith("_1.tif") or file_name.endswith("_2.tif"):
            shutil.move(pathTrain+folder+"/" + file_name, pathTest+folder)
