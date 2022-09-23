import cv2


def calculate(test_original, fingerprint_database_image):
    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(
        fingerprint_database_image, None)

    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                                    dict()).knnMatch(descriptors_1, descriptors_2, k=2)

    match_points = []

    for p, q in matches:
        if p.distance < 0.74*q.distance:
            match_points.append(p)

    keypoints = len(keypoints_1)

    # if len(keypoints_1) > len(keypoints_2):
    #     keypoints = len(keypoints_2)
    # else:
    #     keypoints = len(keypoints_1)

    # print(len(match_points)/keypoints*100)

    if len(match_points)/keypoints*100 > 2:
        return (True, len(match_points)/keypoints*100)

    return (False, -1)
