import cv2


def find_shape(contour) -> str:
    perimeter = cv2.arcLength(contour, True)
    approx_seg_list = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

    if len(approx_seg_list) == 3:
        return "triangle"

    if len(approx_seg_list) == 4:
        (x, y, w, h) = cv2.boundingRect(approx_seg_list)
        ar = w / float(h)
        if 0.95 < ar < 1.05:
            return "square"
        return "rectangle"

    return "circle"


img_folder_path = "images/"
image_name = "3.png"

img = cv2.imread(img_folder_path + image_name)

# find contours
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)

ret_val, thresh_img = cv2.threshold(img_blurred, 220, 255, 0)
thresh_img = cv2.bitwise_not(thresh_img)

contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

triangle_cnt = 0
square_cnt = 0
rect_cnt = 0
circle_cnt = 0
contours_color = (255, 0, 0)  # BGR
center_colour = (255, 255, 0)  # BGR

for contour in contours:
    shape = find_shape(contour)
    if shape == "circle":
        circle_cnt += 1
    if shape == "rectangle":
        rect_cnt += 1
    if shape == "square":
        square_cnt += 1
    if shape == "triangle":
        triangle_cnt += 1

    M = cv2.moments(contour)
    x = int(M["m10"] / M["m00"])
    y = int(M["m01"] / M["m00"])

    cv2.drawContours(img, [contour], -1, contours_color, 3)
    cv2.circle(img, (x, y), 5, center_colour, -1)  # draw center point
    cv2.putText(img, shape, (x + 10, y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.75, center_colour, 2)  # put shape name

print("Amount triangles: ", str(triangle_cnt))
print("Amount squares: ", str(square_cnt))
print("Amount rectangles: ", str(rect_cnt))
print("Amount circles: ", str(circle_cnt))

cv2.imshow("Img", img)
cv2.waitKey(0)


