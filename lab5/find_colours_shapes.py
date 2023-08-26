import cv2
import numpy as np
import imutils

DEBUG = False

samples = np.loadtxt("generalsamples.data", np.float32)
responses = np.loadtxt("generalresponses.data", np.float32)
responses = responses.reshape((responses.size, 1))

model = cv2.ml.KNearest_create()
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

colors = {
    "yellow": (np.array([20, 100, 100]), np.array([40, 255, 255])),
    "raspberry": (np.array([140, 100, 100]), np.array([200, 255, 255])),
    "green": (np.array([53, 100, 100]), np.array([80, 255, 255])),
    "blue": (np.array([80, 100, 100]), np.array([140, 255, 255])),
    "red": (np.array([0, 50, 50]), np.array([15, 255, 255]))
}

relatives = {
    1: "number one",
    2: "number three",
    3: "square",
    4: "triangle",
    5: "circle",
    6: "star"
}

d_colors = {
    "number one": [],
    "number three": [],
    "square": [],
    "triangle": [],
    "circle": [],
    "star": []
}

image = cv2.imread("../images/img7var.png")
image = imutils.resize(image, width=600)
out_image = image.copy()


def color_check(fig_clrs_dict):
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv image", hsv)
    # cv2.waitKey(0)

    for color in colors:
        mask = cv2.inRange(hsv, colors.get(color)[0], colors.get(color)[1])

        if DEBUG:
            if color == "red":
                print("Red colour checked")
                cv2.imshow("red mask", mask)
                cv2.waitKey(0)
            if color == "yellow":
                print("Yellow colour checked")
                cv2.imshow("yellow mask", mask)
                cv2.waitKey(0)
            if color == "raspberry":
                print("Raspberry colour checked")
                cv2.imshow("raspberry mask", mask)
                cv2.waitKey(0)
            if color == "green":
                print("Green colour checked")
                cv2.imshow("green mask", mask)
                cv2.waitKey(0)
            if color == "blue":
                print("Blue colour checked")
                cv2.imshow("blue mask", mask)
                cv2.waitKey(0)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
        contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 50]
        cv2.drawContours(out_image, contours, -1, (0, 0, 255), 2)
        find_fig(contours, mask, color, fig_clrs_dict)


def find_fig(contours, mask, color, fig_clrs_dict):
    for cnt in contours:
        [x, y, w, h] = cv2.boundingRect(cnt)

        if h > 28:
            try:
                cv2.rectangle(image,(x, y), (x + w, y + h), (200, 200, 120), 2)
                roi = mask[y:y + h, x:x + w]
                coeff = float(w) / h
                roismall = cv2.resize(roi, (10, 10))
                roismall = roismall.reshape((1, 100))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k=1)
                num = int(results[0])
                result = relatives[num]
                if color not in fig_clrs_dict[result]:
                    fig_clrs_dict[result].append(color)
                text = "{} {}".format(color, result)
                cv2.putText(out_image, text, (x + w // 2, y + h // 2), 0, 0.6, (255, 0, 120))
            except cv2.Error:
                print("Can not detect figure with color {}".format(color))


color_check(d_colors)
am = 0
for key, val in d_colors.items():
    print("Figure: " + key, end="; ")
    print("Figure colors: ", end="")
    for clr in val:
        print(clr, end=", ")
    print("; Amount: " + str(len(val)))
    am += len(val)
print("Overall amount: " + str(am))
cv2.putText(out_image, "Родичев Ярослав Михайлович, гр. 1044", (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0))
cv2.imshow("out image", out_image)
cv2.waitKey(0)

