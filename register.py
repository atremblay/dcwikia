import sqlite3
import argparse

"""
CREATE TABLE series(
serieid INTEGER PRIMARY KEY,
seriename TEXT,
serieurl TEXT);

CREATE TABLE comics(
comicid INTEGER PRIMARY KEY,
comicurl TEXT,
serieid INTEGER,
FOREIGN KEY(serieid) REFERENCES series(serieid));

CREATE TABLE covers(
coverid INTEGER PRIMARY KEY,
coverurl TEXT,
comicid INTEGER,
FOREIGN KEY (comicid) REFERENCES comics(comicid));
"""