import cv2


def calculate(test_original, fingerprint_database_image):
    sift = cv2.SIFT_create()

    kp1, des1 = sift.detectAndCompute(test_original, None)
    kp2, des2 = sift.detectAndCompute(fingerprint_database_image, None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    good = []
    for m, n in matches:
        if m.distance < 0.75*n.distance:  # thay đổi chỉ số đc
            good.append([m])

    keypoints = len(kp1)

    if len(kp1) > len(kp2):
        keypoints = len(kp2)
    else:
        keypoints = len(kp1)

    # print(len(good)/keypoints*100)

    if len(good)/keypoints*100 > 4:  # thay đổi chỉ số đc
        return (True, len(good)/keypoints*100)

    return (False, -1)
