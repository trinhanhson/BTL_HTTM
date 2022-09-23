import cv2


def calculate(test_original, fingerprint_database_image):
    orb = cv2.ORB_create()

    kp1, des1 = orb.detectAndCompute(test_original, None)
    kp2, des2 = orb.detectAndCompute(fingerprint_database_image, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)

    match_points = []

    for p in matches:
        if p.distance < 45: # thay đổi chỉ số đc
            match_points.append(p)

    keypoints = len(kp1)

    # if len(kp1) > len(kp2):
    #     keypoints = len(kp2)
    # else:
    #     keypoints = len(kp1)

    # print(len(match_points)/keypoints*100)

    if len(match_points)/keypoints*100 > 1:  # thay đổi chỉ số đc
        return (True, len(match_points)/keypoints*100)

    return (False, -1)
