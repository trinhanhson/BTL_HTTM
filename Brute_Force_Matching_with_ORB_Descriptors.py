import cv2


ratio = 0.5


def create(image):
    orb = cv2.ORB_create()

    kp, des = orb.detectAndCompute(image, None)

    return (kp, des)


def calculate(kp1, matches, threshold):

    good_matches = 0

    for i in matches:
        if i < threshold:
            good_matches += 1

    if good_matches/len(kp1)*100 > ratio:
        return (True, good_matches/len(kp1))
    else:
        return (False, 0)


def calculate1(des1, des2):

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(des1, des2)

    matches = sorted(matches, key=lambda x: x.distance)

    matches = [i.distance for i in matches]

    return matches


def calculate2(matches):

    score = 0
    lenMatches = int(len(matches)*((ratio+0.1)/25))
    for i in range(lenMatches):
        score += matches[i]

    return score, lenMatches
