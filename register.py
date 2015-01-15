import sqlite3
import argparse
from series import Series

database_name = "dcwikia.db"

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-r', '--register', help='Register a new series in '
        'the database. You must provide the url from dcwikia')
    parser.add_argument('-d', '--download', help='Download all new covers')

def create_tables():
    conn = sqlite3.Connection(database_name)
    cur = conn.cursor()

    queries = ["""CREATE TABLE series(
        serieid INTEGER PRIMARY KEY,
        serieurl TEXT UNIQUE);
        """, """CREATE TABLE comics(
        comicid INTEGER PRIMARY KEY,
        comicurl TEXT,
        serieid INTEGER,
        FOREIGN KEY(serieid) REFERENCES series(serieid));
        """, """CREATE TABLE covers(
        coverid INTEGER PRIMARY KEY,
        coverurl TEXT,
        comicid INTEGER,
        FOREIGN KEY (comicid) REFERENCES comics(comicid));
        """]

    for query in queries:
        cur.execute(query)

def add_series(url):
    query = """INSERT INTO series VALUES(?)"""
    conn = sqlite3.Connection(database_name)
    cur = conn.cursor()

    cur.execute(query, url)

def download():
    query = """SELECT serieurl FROM series"""
    conn = sqlite3.Connection(database_name)
    cur = conn.cursor()
    cur.execute(query)
    urls = cur.fetchall()
    for url in urls:
        series = Series(url[0])
        for comic in series.comics:
            comic.download_covers()

