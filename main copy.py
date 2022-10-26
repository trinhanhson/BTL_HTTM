import cv2
import os
import numpy as np
from time import *
from cal import *
# from FLANN_based_Matcher import *
from Brute_Force_Matching_with_ORB_Descriptors import *
# from Brute_Force_Matching_with_SIFT_Descriptors import *

sumSample = 0
preArray = [0 for i in range(15)]
recArray = [0 for i in range(15)]

pathTrain = "D:/VScode project/python/BTL_HTTM/Database/Train/"

dir_listTrain = os.listdir(pathTrain)

pathTest = "D:/VScode project/python/BTL_HTTM/Database/Test/"

dir_listTest = os.listdir(pathTest)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

kpanddestrain = list()

kpanddestest = list()

print("start")
start_time = time()

for folder in dir_listTrain:
    for file_name in os.listdir(pathTrain+folder):
        fingerprint_database_image = cv2.imread(
            pathTrain+"/"+folder+"/"+file_name, cv2.IMREAD_GRAYSCALE)

        fingerprint_database_image = clahe.apply(
            fingerprint_database_image)

        (kp, des) = create(fingerprint_database_image)

        kpanddestrain.append((folder, kp, des))

for folder in dir_listTest:
    for file_name in os.listdir(pathTest+folder):
        test_original = cv2.imread(
            pathTest+"/"+folder+"/"+file_name, cv2.IMREAD_GRAYSCALE)

        test_original = clahe.apply(test_original)

        (kp, des) = create(test_original)

        kpanddestest.append((folder, kp, des))
        sumSample += 1

print("finish cal kp and des")
print((time()-start_time)/60)

xx, yy = [], []
listCompare = [[0 for i in range(len(kpanddestrain))]
               for j in range(len(kpanddestest))]

counti = 0
countj = 0
for i in kpanddestest:
    for j in kpanddestrain:
        x, y, z = calculate1(
            i[1], i[2], j[1], j[2])

        xx.append(x)
        yy.append(y)

        listCompare[counti][countj] = (i[0], j[0], z)
        countj += 1

    # print(listCompare[counti][0][0])
    countj = 0
    counti += 1

print("finish cal threshold")
print((time()-start_time)/60)

mean_threshold = round((max(xx)+min(xx))/(max(yy)+min(yy)))

print(mean_threshold)

list_result = list()

for k in range(-10, 11):
    count = 0

    sum_tp = 0

    testList = list()

    for i in listCompare:
        # print(i[0][0])
        tag_name = "Fake"
        best_score = mean_threshold+k

        match_bool = False

        for j in i:
            score = j[2]

            if score < best_score:
                tag_name = j[1]
                best_score = score

        # print(i[0][0], tag_name)

        testList.append((i[0][0], tag_name))

    # for i in kpanddestest:
    #     # print(i[0])
    #     tag_name = "Fake"
    #     best_score = mean_threshold+k

    #     match_bool = False
    #     for j in kpanddestrain:
    #         (match_bool, score) = calculate(
    #             i[1], i[2], j[1], j[2], mean_threshold+k)

    #         if match_bool and score < best_score:
    #             tag_name = j[0]
    #             best_score = score

    #         # print(i[0], tag_name)
    #     testList.append((i[0], tag_name))

    count = 0

    for trueTag in dir_listTest:

        tp = 0
        fp = 0
        fn = 0

        for j in range(len(testList)):

            if trueTag == testList[j][0] == testList[j][1]:
                tp += 1
            elif trueTag == testList[j][0] != testList[j][1]:
                fn += 1
            elif trueTag == testList[j][1] != testList[j][0]:
                fp += 1

        print(trueTag, tp)

        sum_tp += tp

        if fp == 0 and tp == 0:
            fp += 1
        if(fn == 0) and tp == 0:
            fn += 1

        preArray[count] = pre(tp, fp)

        recArray[count] = rec(tp, fn)

        count += 1

    avg_acc = acc(sum_tp, sumSample)

    avg_pre = meanCal(preArray, sumSample)

    avg_rec = meanCal(recArray, sumSample)

    f1 = f1Cal(avg_pre, avg_rec)

    list_result.append((avg_acc, avg_pre, avg_rec, f1, mean_threshold+k))

    print("finish cal", mean_threshold+k)
    print((time()-start_time)/60)

for i in list_result:
    print(i)

print(max(list_result, key=lambda x: x[3]))
