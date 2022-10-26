import cv2


def create(image):
    orb = cv2.ORB_create()

    kp, des = orb.detectAndCompute(image, None)

    return (kp, des)


def calculate(kp1, des1, kp2, des2, threshold):

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    score = 0
    for i in range(len(matches)//10):
        score += matches[i].distance
    score_threshold = threshold  # score/lend(mathches).mean()
    lenMatches = 20
    # return score, lenMatches
    if score/20 < score_threshold:  # score: 10000-15000 ;
        # print("Fingerprint matches.")
        return (True, score/lenMatches)
    else:
        # print("Fingerprint does not match.")
        return (False, threshold)


def calculate1(kp1, des1, kp2, des2):

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    score = 0
    lenMatches = len(kp1)//100
    for i in range(lenMatches):
        score += matches[i].distance

    return score, lenMatches, score/lenMatches
