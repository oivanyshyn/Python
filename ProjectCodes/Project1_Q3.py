def centroid():
    x1 = int(input("Enter x1:"))
    y1 = int(input("Enter y1:"))
    x2 = int(input("Enter x2:"))
    y2 = int(input("Enter y1:"))
    x3 = int(input("Enter x3:"))
    y3 = int(input("Enter y3:"))

    xCoord = (x1 + x2 + x3) / 3
    yCoord = (y1 + y2 + y3) / 3

    print(str(xCoord) + ',' + str(yCoord))
    print('The best meeting point of 3 points is ' + str(round(xCoord)) + ',' + str(round(yCoord)))

centroid()