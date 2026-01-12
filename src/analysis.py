import sqlite3
import pandas as pd
from pathlib import Path

# DATABASE PATH 
DB_PATH=Path("database/focusiq.db")
# DATABASE CONNECTION
def get_connection():
    return sqlite3.connect(DB_PATH)
# LOAD DATA FROM DATABSE
def load_data():
    conn=get_connection()
    query=" select * from daily_logs order by date"
    df=pd.read_sql(query,conn)
    conn.close()
    return df

# BASIC METRICS
def basic_metrics(df):
    return {
        "avg_focus_hours": round(df['deep_work_hours'].mean(),2),
        "avg_phone_hours": round(df['phone_hours'].mean(),2),
        "avg_sleep_quality": round(df['sleep_quality'].mean(),2),
        "avg_mood_quality": round(df['mood'].mean(),2)
    }

# LAST 7 DAYS TREND
def last_7_days_trend(df):
    last_7_days=df.tail(7)
    return { 
        "focus_trend": round(last_7_days['deep_work_hours'].mean(),2),
        "phone_usage_trend": round(last_7_days['phone_hours'].mean(),2),
        "sleep_quality_trend": round(last_7_days['sleep_quality'].mean(),2),
        "mood_quality_trend": round(last_7_days['mood'].mean(),2)
    }
# RUNNING PHASE
if __name__=="__main__":
    df=load_data()
    print("\n -----------------Basic Metrics----------------")
    for k,v in basic_metrics(df).items():
        print(f" {k}:{v}")
    
    for k,v in last_7_days_trend(df).items():
        print(f"{k}:{v}")
    