#!/Users/JLee/anaconda/envs/NLP/bin/python
PATH = "/Users/JLee/Google Drive/Data Science/Projects/Chinese Vocab Manager/Known_words/"
CSVFILE = "knownwords.csv"

import psycopg2
import psycopg2.extras
#from psycopg2.extras import RealDictCursor

#connect to db server
def connectServer():
    conn = psycopg2.connect("host=localhost dbname=HanziVocabManager user=postgres password=qwerty")
    return conn

#create table
def createTable(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE knownwords(
        word text PRIMARY KEY
    )
    """)
    conn.commit()
    cur.execute("""CREATE TABLE tocfl_list(
        tocfl_word text PRIMARY KEY,
        level text
    )
    """)
    conn.commit()

#insert table
def insertTable(conn, target_tb, source_tb):
    cur = conn.cursor()
    with open(PATH + source_tb, 'r') as f:
        next(f) # Skip the header row.
        cur.copy_from(f, target_tb, sep=',')
    conn.commit()

#return table as list
def getTableAsList(conn, tb, col):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT " + col + " FROM " + tb)
    tbList = cur.fetchall()
    return [w for rowList in tbList for w in rowList]

if __name__ == "__main__":
    conn = connectServer()
    #createTable(conn)
    #insertTable(conn, 'knownwords', 'knownwords.csv')
    #insertTable(conn, 'tocfl_list', 'tocflwords.csv')
    l = getTableAsList(conn, 'knownwords', 'word')
    print("word list length: %d" % len(l))
    print(l)