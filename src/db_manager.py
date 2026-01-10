# Using sqlite3 for database . it is built in lightweight and serverless database 
import sqlite3
import pandas as pd
from pathlib import Path
DB_PATH=Path("database/focusiq.db") # for path and if file not exist then it will create a file

# Connection Function
def get_connection():
    return sqlite3.connect(DB_PATH)
# Creating Table
def create_table():
    conn=get_connection() # conncection open 
    cursor=conn.cursor() # tool for running sql commands
    cursor.execute("""
                   create table if not exists daily_logs(
                   date TEXT PRIMARY KEY,
                   phone_hours REAL,
                   sleep_quality INTEGER,
                   mood INTEGER,
                   deep_work_hours REAL,
                   distraction_minutes INTEGER,
                   primary_task TEXT
                   )
    """)
    conn.commit() # save all changes to database
    conn.close() # close database connection
# Insert data from csv
def insert_from_csv(csv_path):
    df=pd.read_csv(csv_path)
    conn=get_connection()
    df.to_sql("daily_logs",conn,if_exists="replace",index=False)
    conn.close()
    print("Data successfully inserted into database ")

# Fetch Sample Data 
def fetch_sample(limit=5):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute(
        " select * from daily_logs order by date limit ?",
        (limit,)
    )
    rows=cursor.fetchall()
    conn.close()
    return rows

# Run Phase 2
if __name__=="__main__":
    create_table()
    insert_from_csv("data/raw/focusiq_dummy_90_days.csv")
    print("sample rows from database")
    for row in fetch_sample():
        print(row)