import cv2
import os
import time
from cal import *
# from FLANN_based_Matcher import *
# from Brute_Force_Matching_with_ORB_Descriptors import *
from Brute_Force_Matching_with_SIFT_Descriptors import *

sum_tp = 0
preArray = [0 for i in range(15)]
recArray = [0 for i in range(15)]

pathTrain = "D:/VScode project/python/BTL_HTTM/Database/Train/"

dir_listTrain = os.listdir(pathTrain)

pathTest = "D:/VScode project/python/BTL_HTTM/Database/Test/"

dir_listTest = os.listdir(pathTest)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

count = 0

sumSample = 3*20

testList = [("", "") for i in range(sumSample)]

kpanddes = list()

for folder in dir_listTrain:
    for file_name1 in os.listdir(pathTrain+folder):
        fingerprint_database_image = cv2.imread(
            pathTrain+"/"+folder+"/"+file_name1, cv2.IMREAD_GRAYSCALE)

        fingerprint_database_image = clahe.apply(
            fingerprint_database_image)

        (kp, des) = create(fingerprint_database_image)

        kpanddes.append((folder, kp, des))

for fd in dir_listTest:
    for file_name in os.listdir(pathTest+fd):
        print(fd+"/"+file_name)
        tag_name = "Fake"
        best_score = -1

        test_original = cv2.imread(
            pathTest+"/"+fd+"/"+file_name, cv2.IMREAD_GRAYSCALE)

        test_original = clahe.apply(test_original)

        (kp, des) = create(test_original)

        match_bool = False

        for i in kpanddes:
            (match_bool, score) = calculate(
                kp, des, i[1], i[2])

            if match_bool and score > best_score:
                tag_name = i[0]
                best_score = score

        print(fd, tag_name)
        testList[count] = (fd, tag_name)

        count += 1


count = 0

for trueTag in dir_listTest:

    tp = 0
    fp = 0
    fn = 0

    for i in range(len(testList)):

        if trueTag == testList[i][0] == testList[i][1]:
            tp += 1
        elif trueTag == testList[i][0] != testList[i][1]:
            fn += 1
        elif trueTag == testList[i][1] != testList[i][0]:
            fp += 1

    sum_tp += tp

    preArray[count] = pre(tp, fp)

    recArray[count] = rec(tp, fn)

    count += 1


avg_acc = acc(sum_tp, sumSample)

avg_pre = meanCal(preArray, sumSample)

avg_rec = meanCal(recArray, sumSample)

f1 = f1(avg_pre, avg_rec)

print(avg_acc, avg_pre, avg_rec, f1)
