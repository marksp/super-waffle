﻿Create table tube.route_soton_e (
  waypoint integer,
  lat double precision,
  lon double precision,
  prev_bearing double precision,
  next_bearing double precision,
  prev_dist double precision,
  next_dist double precision,
  line text,
  routename text
)

COPY tube.route_soton_e FROM 'c:/Paul/MyProjects/AutoTubeMap/route2.csv' DELIMITER ',' HEADER CSV;

ALTER TABLE tube.route_soton_e ADD COLUMN geom geometry(POINT,4326);

UPDATE tube.route_soton_e SET geom = ST_SetSRID(ST_MakePoint(lon,lat),4326);

create table tube.route_soton_e_equal_area (
  waypoint integer,
  lat double precision,
  lon double precision,
  prev_bearing double precision,
  next_bearing double precision,
  prev_dist double precision,
  next_dist double precision,
  line text,
  geom geometry(Point,102013),
  routename text
)

INSERT INTO tube.route_soton_e_equal_area select waypoint, lat, lon, prev_bearing, next_bearing, prev_dist, next_dist, line, ST_Transform(geom, 102013), routename from tube.route_soton_e;

create table tube.route_soton_e_equal_area_snapped (
  waypoint integer,
  lat double precision,
  lon double precision,
  prev_bearing double precision,
  next_bearing double precision,
  prev_dist double precision,
  next_dist double precision,
  line text,
  geom geometry(Point,102013),
  routename text
)

INSERT INTO tube.route_soton_e_equal_area_snapped select waypoint, lat, lon, prev_bearing, next_bearing, prev_dist, next_dist, line, ST_SnapToGrid(geom, -792989, 2342199, 1000, 1000), routename from tube.route_soton_e_equal_area;

CREATE TABLE tube.grid_soton_e
(
  id integer,
  geom geometry
);

CREATE SEQUENCE tube.soton_grid_id;

Create table tube.snappedroute_soton_e (id int, routename text, geom geometry(Linestring, 102013));

insert into tube.snappedroute_soton_e values (2, 'Soton Pilotage E', (SELECT ST_SetSRID(ST_MakeLine(geom),102013) As newgeom
    FROM tube.route_soton_e_equal_area_snapped));


create table tube.simplesnappedroute_soton_e (id, routename, geom) as select id, routename, ST_removerepeatedpoints(geom) from tube.snappedroute_soton_e;

create table tube.segments_soton_e as WITH
    dumps AS (
      SELECT id, ST_DumpPoints(geom) AS pt FROM tube.simplesnappedroute_soton_e
    ),
    pts AS (
      SELECT id, (pt).geom, (pt).path[1] AS vert FROM dumps
    )
    SELECT a.id, ST_AsText(ST_MakeLine(ARRAY[a.geom, b.geom])) AS geom
    FROM pts a, pts b
    WHERE a.id = b.id AND a.vert = b.vert-1 AND b.vert > 1;

alter table tube.segments_soton_e rename geom to geomtext;

alter table tube.segments_soton_e add column geom geometry(Linestring, 102013);

update tube.segments_soton_e set geom = ST_SetSRID(ST_GeomFromText(geomtext),102013);

alter table tube.segments_soton_e add column azimuth float;

update tube.segments_soton_e set azimuth = degrees(ST_Azimuth(ST_StartPoint(geom), ST_EndPoint(geom)));

create sequence segments_soton_e_id_seq;
alter table tube.segments_soton_e add column gid integer unique default nextval('segments_soton_e_id_seq');

CREATE TABLE tube.route_soton_e_segment_pnts
(
  id integer,
  geom geometry(Point,102013)
);

Create table tube.soton_e_tubeline (id int, routename text, geom geometry(Linestring, 102013));

insert into tube.soton_e_tubeline values (2, 'Soton Pilotage E', (SELECT ST_SetSRID(ST_MakeLine(geom),102013) As newgeom
    FROM tube.route_soton_e_segment_pnts));