import matplotlib.pyplot as plt
import numpy as np
import psycopg2
from shapely.geometry import Point, LineString
from shapely import wkb

# plt.plot([1,2,3,4], [1,4,9,16], linestyle='--',color='b')
# plt.plot([1,2,3,4], [1,4,9,16], 'go')
# plt.axis([0, 6, 0, 20])
# plt.show()

DSN = "dbname='paul' user='postgres' host='localhost' password='postgres'"
con = psycopg2.connect(DSN)
cur = con.cursor()


get_points_sql = "SELECT ST_X((ST_DumpPoints(geom)).geom), ST_Y((ST_DumpPoints(geom)).geom) from tube.routeline2 where id = 1;"
cur.execute(get_points_sql)

x_list = []
y_list = []
xy_list = []

while 1:
    point = cur.fetchone()
    if not point:
        break

    print(point)
    x_list.append(point[0])
    y_list.append(point[1])

xy_list.append(x_list)
xy_list.append(y_list)
print(xy_list)

x = [x_list[0], x_list[-1]]
y = [y_list[0], y_list[-1]]

print(x)
print(y)

bounding_box = "SELECT St_AsText(ST_Envelope(geom)) from tube.routeline2 where id = 1;"
cur.execute(bounding_box)

bbox = cur.fetchone()
print(bbox[0])

make_fishnet = "create table tube.fishnet as select * from st_createfishnet(360,720,0.5,0.5,-180,-90);"


plt.plot(x_list, y_list, linestyle='--',color='b')
plt.plot(x_list, y_list, 'go')
plt.plot(x, y, linestyle='-.',color='y')
# plt.axis([0, 6, 0, 20])
plt.show()


# get_line = "SELECT ST_AsText(ST_StartPoint(geom)), ST_AsText(ST_EndPoint(geom)) from tube.routeline2 where id = 1;"
# make_line = "SELECT ST_AsText(ST_MakeLine(ST_StartPoint(geom),ST_EndPoint(geom))) from tube.routeline2 where id = 1;"
# get_start = "SELECT ST_X(ST_StartPoint(geom)), ST_Y(ST_StartPoint(geom))from tube.routeline2 where id = 1;"
# get_end = "SELECT ST_X(ST_EndPoint(geom)), ST_Y(ST_EndPoint(geom)) from tube.routeline2 where id = 1;"
# cur.execute(get_start)
#
# while 1:
#     point = cur.fetchone()
#     if not point:
#         break
#
#     start_x = point[0]
#     start_y = point[1]
#     end_x = point[2]
#     end_y = point[3]
#
#     print()

