import cv2
import os
from fingerprint_enhancer import *

def enhance_fingerprint(imageAdd):
    imageAdd = enhance_Fingerprint(imageAdd,resize=True)

    for i in range(imageAdd.shape[0]):
        for j in range(imageAdd.shape[1]):         
            imageAdd[i,j]=255-imageAdd[i,j]

    return imageAdd

test_original = cv2.imread("./BTL_HTTM/Database/Test/DB2_B_2004/106_2.tif",cv2.IMREAD_GRAYSCALE)

path = "D:/VScode project/python/BTL_HTTM/Database/Train/"

dir_list = os.listdir(path)

file_name=None
image = None
best_score =0
kp1, kp2, mp= None, None,None

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(16,16))

test_original = clahe.apply(test_original)

test_original = clahe.apply(test_original)

for folder in dir_list:
    for file_name1 in os.listdir(path+folder):
        print(folder+"/"+file_name1)
    
        fingerprint_database_image = cv2.imread(path+"/"+folder+"/"+file_name1,cv2.IMREAD_GRAYSCALE)

        fingerprint_database_image = clahe.apply(fingerprint_database_image)

        fingerprint_database_image = clahe.apply(fingerprint_database_image)
    
        sift = cv2.SIFT_create()
    
        keypoints_1, descriptors_1 = sift.detectAndCompute(test_original,None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image,None)

        matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=5), 
            dict()).knnMatch(descriptors_1, descriptors_2, k=2)

        match_points = []

        for p, q in matches:
            if p.distance < 0.75*q.distance:
                match_points.append(p)

        print(len(match_points))

        keypoints = 0
        if len(keypoints_1) < len(keypoints_2):
            keypoints = len(keypoints_1)            
        else:
            keypoints = len(keypoints_2)

        print(keypoints)

        if len(match_points)>50:
            best_score = len(match_points)

            file_name=folder+"/"+file_name1
            image=fingerprint_database_image

            kp1,kp2,mp= keypoints_1,keypoints_2, match_points

            break
    if best_score >50:
        break
    

print("BEST MATCH: ",file_name)
print("SCORE: ",best_score)

result = cv2.drawMatches(test_original, kp1, fingerprint_database_image, 
                            kp2, mp, None) 
result = cv2.resize(result, None, fx=2, fy=2)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

