
import cv2

import numpy as np

img_folder_path = "images/"
image_name = "3.png"

text = "1044 Родичев Ярослав Михайлович, количество контуров: "

img = cv2.imread(img_folder_path + image_name)
src_img = img.copy()

# find contours
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret_val, thresh_img = cv2.threshold(img_gray, 220, 255, 0)
thresh_img = cv2.bitwise_not(thresh_img)


contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw text
text += str(len(contours))

text_pos = (0, 20)
text_color = (0, 0, 0)
font_face = cv2.FONT_HERSHEY_COMPLEX
font_scale = 0.55
cv2.putText(img, text, text_pos, font_face, font_scale, text_color)
print(text)

# draw contours
red = (255, 0, 255)
cv2.drawContours(img, contours, -1, red, 3)

img_height = img.shape[0]
img_width = img.shape[1]

# draw point
point_colour = (0, 0, 0)
point_y = img_height - 20
point_x = 20

img[point_y, point_x] = point_colour

# draw rect
rect_colour = (200, 0, 0)

rect_width = 50
rect_height = 50

rect_x = int(img_width / 2 - rect_width / 2)
rect_y = int(img_height / 2 - rect_height / 2)

rect = cv2.rectangle(img, (rect_x, rect_y), (rect_x + rect_width, rect_y + rect_height), rect_colour, -1)

# draw src and modified images
black_separating_line = np.zeros((img_height, 1, 3), dtype=np.uint8)
images = np.concatenate((src_img, black_separating_line), axis=1)
images = np.concatenate((images, img), axis=1)

cv2.imshow("images", images)
cv2.waitKey(0)
