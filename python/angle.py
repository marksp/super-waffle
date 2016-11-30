import numpy as np
import psycopg2
import math
import matplotlib.pyplot as plt

DSN = "dbname='paul' user='postgres' host='localhost' password='postgres'"
con = psycopg2.connect(DSN)
cur = con.cursor()

'''

get_points_sql = "SELECT ST_AsText((line.a).geom) FROM (SELECT ST_DumpPoints(ST_AsText(geom)) as a from tube.testline where id = 1) as line;"
get_points_sql2 = "SELECT ST_X((ST_DumpPoints(geom)).geom), ST_Y((ST_DumpPoints(geom)).geom) from tube.testline where id = 1;"
cur.execute(get_points_sql2)

a1 = []
b1 = []
c1 = []
points = []

while 1:
    point = cur.fetchone()
    if not point: break
    points.append(point)

# for i in points:
a1.append(points[0])
b1.append(points[1])
c1.append(points[2])

a = np.array([0, 0])
b = np.array([0, 1])
c = np.array([1, 1])

a2 = np.array(a1[0])
b2 = np.array(b1[0])
c2 = np.array(c1[0])

ba2 = a2 - b2
bc2 = c2 - b2

cosine_angle = np.dot(ba2, bc2) / (np.linalg.norm(ba2) * np.linalg.norm(bc2))
angle = np.arccos(cosine_angle)

print(np.degrees(angle))

'''

def return_points():
    a = []
    b = []
    c = []
    points = []

    get_points_sql2 = "SELECT ST_X((ST_DumpPoints(geom)).geom), ST_Y((ST_DumpPoints(geom)).geom) from tube.testline where id = 1;"
    cur.execute(get_points_sql2)

    while 1:
        point = cur.fetchone()
        if not point: break
        points.append(point)

    a.append(points[0])
    b.append(points[1])
    c.append(points[2])

    return points[0],points[1],points[2]


def angle(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle1 = np.arccos(cosine_angle)
    angle = np.degrees(angle1)

    return angle

def calculate_angle(a,b,c):
    angle_ab = math.degrees(math.atan2(b[1] - a[1], b[0] - a[0]))
    angle_bc = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]))
    angle_ab += 360 if angle_ab < 0 else 0
    angle_bc += 360 if angle_ab < 0 else 0

    angle = angle_bc = angle_ab
    angle -= 360 if angle < 180 else 0
    angle += 360 if angle < -180 else 0

    return angle


def calculate_schematic_angle(bend):

    sign_multiplier = -1 if angle < 0 else 1

    bend = abs(bend)

    if bend > 105:
        schematic_angle = 135
    elif bend > 75:
        schematic_angle = 90
    elif bend > 20:
        schematic_angle = 45

    return schematic_angle * sign_multiplier


a,b,c = return_points()

# print(angle(a,b,c))

get_points_sql = "SELECT ST_X((ST_DumpPoints(geom)).geom), ST_Y((ST_DumpPoints(geom)).geom) from tube.routeline2 where id = 1;"
cur.execute(get_points_sql)

x_list = []
y_list = []
xy_list = []

test_xy = [(0,0),(0,0.5),(1,1),(1,2),(2,2),(2.5,1)]
test_x = [0,0,1,1,2,2.5]
test_y = [0,0.5,1,2,2,1]

# print(calculate_angle((2,2),(1,1.5),(2.5,0.5)))
# print(angle((2,2),(1,1.5),(2.5,0.5)))



'''
rows = cur.fetchall()
for row in rows:
    xy_list.append(row)
    print(row)

print(xy_list)

list_a = 0
list_b = 1
list_c = 2

waypoints = len(xy_list)
print(waypoints)
way = waypoints - 1
print(way)

for xy in xy_list[1:way]:
    a = xy_list[list_a]
    b = xy_list[list_b]
    c = xy_list[list_c]
    print(a, b, c)
    list_a += 1
    list_b += 1
    list_c += 1
    print(angle(a,b,c))
    print(calculate_angle(a,b,c))
'''

list_a = 0
list_b = 1
list_c = 2

waypoints = len(test_xy)
print(waypoints)
way = waypoints - 1
print(way)

for xy in test_xy[1:way]:
    a = test_xy[list_a]
    b = test_xy[list_b]
    c = test_xy[list_c]
    print(a, b, c)
    list_a += 1
    list_b += 1
    list_c += 1
    print(angle(a,b,c))
    print(calculate_angle(a,b,c))

plt.xlabel('x')
plt.ylabel('y')
plt.title('xy Test Plot')
plt.plot(test_x, test_y, linestyle='--',color='b')
plt.plot(test_x, test_y, 'go')
plt.axis([-0.5, 3, -0.5, 3])
plt.show()