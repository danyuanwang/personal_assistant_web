import sqlite3
import psycopg2
from django.conf import settings
import os
from datetime import date
import time
import sys
import csv
import re
import traceback

def parser_log_data(drop_table):
#    print("parse us data in file:", fname)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_assistant_web.settings')
    # conn = sqlite3.connect('WC.db.sqlite')]
    dbsettings = settings.DATABASES['default']
    print(dbsettings)
    conn = psycopg2.connect(host=dbsettings["HOST"],port=dbsettings["PORT"], database=dbsettings["NAME"],
                            user=dbsettings["USER"], password=dbsettings["PASSWORD"])
    cur = conn.cursor()
    if(drop_table == 'yes') :
        cur.execute('''
        DROP TABLE IF EXISTS conversation_log
        ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS conversation_log (
        id SERIAL PRIMARY KEY,
        from_user  TEXT,
        timestamp timestamp default current_timestamp
        )
    ''')
    
    conn.commit()
 
    cur.close()

if_drop_table = input("Drop all tables?: [No/yes]")
start_time = time.time()
parser_log_data(if_drop_table)
elapsed_time = time.time() - start_time
print("elapsed_time:", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
