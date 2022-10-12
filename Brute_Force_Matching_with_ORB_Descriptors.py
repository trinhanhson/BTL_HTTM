import cv2


def create(image):
    orb = cv2.ORB_create()

    kp, des = orb.detectAndCompute(image, None)

    return (kp, des)


def calculate(kp1, des1, kp2, des2):

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    match_points = []

    for p in matches:
        if p.distance < 56:  # thay đổi chỉ số đc
            match_points.append(p)

    keypoints = len(kp1)

    # if len(kp1) > len(kp2):
    #     keypoints = len(kp2)
    # else:
    #     keypoints = len(kp1)

    if len(match_points)/keypoints*100 > 1.5:  # thay đổi chỉ số đc
        return (True, len(match_points)/keypoints*100)

    # print([i.distance for i in matches])

    # if len(match_points) > 4:
    #     return (True, len(match_points))

    # if matches[0].distance < 50:
    #     return (True, matches[0].distance)

    return (False, -1)
