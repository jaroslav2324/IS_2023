

testPoints = [(0, 0), (0, -500), (1, 0), (1, 5), (-100, 5), (-100, -245), (3, -2)]

for point in testPoints:
    x = point[0]
    y = point[1]
    print(f"Testing point ({x}, {y}):", end=" ")
    if x == 0 and y == 0:
        print("The point lies on both OX and OY axes")
    elif x == 0 and y != 0:
        print("The point lies on OY axis")
    elif x != 0 and y == 0:
        print("The point lies on OX axis")
    elif x > 0 and y > 0:
        print("The point lies in 1st quarter")
    elif x < 0 and y > 0:
        print("The point lies in 2nd quarter")
    elif x < 0 and y < 0:
        print("The point lies in 3rd quarter")
    elif x > 0 and y < 0:
        print("The point lies in 4th quarter")

