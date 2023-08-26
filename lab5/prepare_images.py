import sys
import imutils
import numpy as np
import cv2

img = cv2.imread("../images/samples.png")

resized_img = imutils.resize(img, width=600)

gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray_img, (5, 5), 0)

ret, thresh = cv2.threshold(blur, 250, 255, cv2.THRESH_BINARY)
thresh = cv2.bitwise_not(thresh)
# cv2.imshow("img", thresh)
# cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
# cv2.imshow("img", img)
# cv2.waitKey(0)

samples = np.empty((0, 100))
responses = []
keys = [i for i in range(48, 58)]

for cnt in contours:
    if cv2.contourArea(cnt) > 50:
        [x, y, w, h] = cv2.boundingRect(cnt)

        if h > 28:
            cv2.rectangle(resized_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            roi = thresh[y:y+h, x:x+w]

            roismall = cv2.resize(roi, (10, 10))
            cv2.imshow('roi', roismall)
            cv2.imshow('norm', resized_img)
            key = cv2.waitKey(0)

            if key == 27:
                sys.exit()
            elif key in keys:
                responses.append(int(chr(key)))
                sample = roismall.reshape((1, 100))
                # print(sample)
                samples = np.append(samples, sample, 0)

responses = np.array(responses, np.float32)
responses = responses.reshape((responses.size, 1))

np.savetxt("generalsamples.data", samples)
np.savetxt("generalresponses.data", responses)


