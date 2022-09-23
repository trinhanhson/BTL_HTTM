import cv2


def create(image):
    sift = cv2.SIFT_create()

    kp, des = sift.detectAndCompute(image, None)

    return (kp, des)


def calculate(keypoints_1, descriptors_1, keypoints_2, descriptors_2):
    sift = cv2.SIFT_create()

    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                                    dict()).knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []

    for p, q in matches:
        if p.distance < 0.75*q.distance:  # thay đổi chỉ số đc
            match_points.append(p)

    keypoints = len(keypoints_1)

    if len(keypoints_1) > len(keypoints_2):
        keypoints = len(keypoints_2)
    else:
        keypoints = len(keypoints_1)

    if len(match_points)/keypoints*100 > 2.1:  # thay đổi chỉ số đc
        return (True, len(match_points)/keypoints*100)

    return (False, -1)
