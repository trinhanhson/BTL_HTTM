import cv2


def create(image):
    sift = cv2.SIFT_create()

    kp, des = sift.detectAndCompute(image, None)

    return (kp, des)


def calculate(kp1, des1, kp2, des2):
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

    if len(good)/keypoints*100 > 2.2:  # thay đổi chỉ số đc
        return (True, len(good)/keypoints*100)

    return (False, -1)
