import psycopg2

DSN = "dbname='paul' user='postgres' host='localhost' password='postgres'"
con = psycopg2.connect(DSN)
cur = con.cursor()

get_azi = "SELECT gid, azimuth from tube.segments_soton_e;"
cur.execute(get_azi)

segments = []
points_to_keep = []

while 1:
    segment = cur.fetchone()
    if not segment: break
    segments.append(segment)

list_a = 0
list_b = 1
end = len(segments)-1

first_pnt = segments[0]
pnt1 = first_pnt[0]
points_to_keep.append(pnt1)
print(points_to_keep)

print(len(points_to_keep))

for xy in segments[:end]:
    a = segments[list_a]
    b = segments[list_b]
    list_a += 1
    list_b += 1
    print(a[1], b[1], abs(a[1] - b[1]))
    if abs(a[1] - b[1]) > 22.5:
        points_to_keep.append(b[0])
        print("Keep")
    else:
        print("Not Needed")

print(len(points_to_keep))

last_pnt = segments[end]
pnt_last = last_pnt[0]
points_to_keep.append(pnt_last)

print(points_to_keep)
print(len(points_to_keep))


def remove_duplicate(alist):
    return list(set(alist))

final_points = remove_duplicate(points_to_keep)

print(final_points)

sort_list = sorted(final_points, key=int)

print(sort_list)

for pnt in sort_list:
    get_start_pnts = "INSERT INTO tube.route_soton_e_segment_pnts VALUES ({0}, (SELECT ST_StartPoint(geom) from tube.segments_soton_e where gid = {0}));".format(pnt)
    cur.execute(get_start_pnts)
con.commit()

end_pnt_idx = len(final_points)-1
end_pnt = final_points[end_pnt_idx]

insert_end_pnt = "INSERT INTO tube.route_soton_e_segment_pnts VALUES ({0}, (SELECT ST_EndPoint(geom) from tube.segments_soton_e where gid = {0}));".format(end_pnt)
cur.execute(insert_end_pnt)
con.commit()


