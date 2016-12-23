import psycopg2
import matplotlib.pyplot as plt

DSN = "dbname='paul' user='postgres' host='localhost' password='postgres'"
con = psycopg2.connect(DSN)
cur = con.cursor()

origin_x = -792989
origin_y = 2342199  # need to change this to match the grid already made -
# TODO make a grid that is from an origin for an area

max_x = -773906
max_y = 2362413

col = (abs(origin_x - max_x)//1000)+1
row = (abs(origin_y - max_y)//1000)+1

print(abs(origin_x - max_x))
print(col)
print(row)

x_coordinates = []
x_coordinates.append(origin_x)
x = origin_x
for i in range(col):
    x += 1000
    x_coordinates.append(x)

y_coordinates = []
y_coordinates.append(origin_y)
y = origin_y
for i in range(row):
    y += 1000
    y_coordinates.append(y)

print(x_coordinates)
print(y_coordinates)

xy_coordinates = []
xx = []
yy = []
for i in x_coordinates:
    for ii in y_coordinates:
        xy = (i,ii)
        xy_coordinates.append(xy)
        xx.append(i)
        yy.append(ii)

print(len(xy_coordinates))
print(xy_coordinates)

for xy in xy_coordinates:
    X = xy[0]
    Y = xy[1]
    sql = "INSERT INTO tube.grid_soton_e(id, geom) VALUES(NEXTVAL('tube.soton_grid_id'), " \
          "ST_GeomFromText('POINT({X} {Y})', 102013));".format(X=X, Y=Y)
    cur.execute(sql)

con.commit()

# get_points_sql = "SELECT ST_X((ST_DumpPoints(geom)).geom), ST_Y((ST_DumpPoints(geom)).geom) from tube.routeline2 where id = 1;"
# cur.execute(get_points_sql)
#
# x_list = []
# y_list = []
# xy_list = []
#
# while 1:
#     point = cur.fetchone()
#     if not point:
#         break
#
#     print(point)
#     x_list.append(point[0])
#     y_list.append(point[1])
#
# xy_list.append(x_list)
# xy_list.append(y_list)
# print(xy_list)
#
# x = [x_list[0], x_list[-1]]
# y = [y_list[0], y_list[-1]]
#
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('xy Grid Test Plot')
# plt.plot(x_list, y_list, linestyle='--',color='b')
# plt.plot(x_list, y_list, 'ro')
# plt.plot(x, y, linestyle='-.',color='y')
# plt.plot(xx, yy, 'go')
# plt.show()

