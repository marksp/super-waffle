from math import degrees, atan2


def gb(x, y, center_x, center_y):
    angle = degrees(atan2(y - center_y, x - center_x))
    bearing1 = (angle + 360) % 360
    bearing2 = (90 - angle) % 360
    print ("gb: x=%2d y=%2d angle=%6.1f bearing1=%5.1f bearing2=%5.1f" % (
        x, y, angle, bearing1, bearing2))

for pt in ((0, 1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1, 0),(-1,1)):
    gb(pt[0], pt[1], 0, 0)