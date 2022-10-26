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
        # print(type(kp), type(des))

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

# listMatches = [[0 for i in range(len(kpanddestrain))]
#                for j in range(len(kpanddestest))]

# counti = 0
# countj = 0
# for i in kpanddestest:
#     for j in kpanddestrain:
#         matches = calculate1(i[2], j[2])

#         listMatches[counti][countj] = (i[0], j[0], matches)
#         countj += 1

#     countj = 0
#     counti += 1

# np.save("D:/VScode project/python/BTL_HTTM/MatchData",
#         listMatches, allow_pickle=True)

listMatches = np.load(
    "D:/VScode project/python/BTL_HTTM/MatchData.npy", allow_pickle=True)

xx, yy = [], []

for i in range(len(listMatches)):
    for j in range(len(listMatches[i])):
        x, y = calculate2(listMatches[i][j][2])

        xx.append(x)
        yy.append(y)

print("finish cal threshold")
print((time()-start_time)/60)

mean_threshold = round((max(xx)+min(xx))/(max(yy)+min(yy)))

# mean_threshold = 50

print(mean_threshold)

list_result = list()

for k in range(-20, 21):
    count = 0

    sum_tp = 0

    testList = list()

    for i in range(len(listMatches)):
        tag_name = "Fake"
        best_score = 0

        match_bool = False

        for j in range(len(listMatches[i])):
            match_bool, score = calculate(
                kpanddestest[i][1], listMatches[i][j][2], mean_threshold+k)

            if match_bool and score > best_score:
                tag_name = listMatches[i][j][1]
                best_score = score

        print(listMatches[i][0][0], tag_name)
        testList.append((listMatches[i][0][0], tag_name))

    count = 0

    fake_count = 0

    fake_total = 0

    sumArray = []

    for trueTag in dir_listTest:

        tp = 0
        fp = 0
        fn = 0

        trueTagCount = 0

        for j in range(len(testList)):

            if trueTag == testList[j][0]:
                trueTagCount += 1

            if trueTag == "Fake" and testList[j][0] == "Fake":
                fake_total += 1

            if trueTag == testList[j][0] == testList[j][1]:
                tp += 1
            elif trueTag == testList[j][0] != testList[j][1]:
                fn += 1
            elif trueTag == testList[j][1] != testList[j][0]:
                fp += 1

        sumArray.append(trueTagCount)

        if(trueTag == "Fake"):
            fake_count = tp*100/fake_total

        sum_tp += tp

        if fp == 0 and tp == 0:
            fp += 1
        if(fn == 0) and tp == 0:
            fn += 1

        preArray[count] = pre(tp, fp)

        recArray[count] = rec(tp, fn)

        count += 1

    avg_acc = acc(sum_tp, sumSample)

    avg_pre = meanCal(preArray, sumSample, sumArray)

    avg_rec = meanCal(recArray, sumSample, sumArray)

    f1 = f1Cal(avg_pre, avg_rec)

    list_result.append((avg_acc, avg_pre, avg_rec, f1,
                       mean_threshold+k, fake_count))

    print("finish cal", mean_threshold+k)
    print((time()-start_time)/60)

list_result_fake_high = []

for i in list_result:
    print(i)
    if(i[5] >= 75):
        list_result_fake_high.append(i)

print(max(list_result_fake_high, key=lambda x: x[3]))
