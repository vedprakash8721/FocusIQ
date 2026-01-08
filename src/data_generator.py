import pandas as pd
# Pandas for storing the data into table form ( DataFrame)
import numpy as np
# Numpy for generating random numerical value
from datetime import datetime , timedelta
# datetime for data and time generating and timedelta to handle date time 
import random
DAYS=90
START_DATE=datetime.today() -timedelta( days=DAYS)

# Helper Function
def bounded( value,min_value,max_value):
    return max(min(value,max_value),min_value)

# Data Container
records=[]
# Baseline Behaviour 
base_focus=5.5
base_phone=3.0
base_sleep=3.5
base_mood=3.5

# Data Generation loop
for day in range(DAYS):
    current_date=START_DATE+timedelta(days=day)
    phone_hours=bounded(np.random.normal(base_phone,1.0),0.5,6.0)
    sleep_quality=bounded(np.random.normal(base_sleep-phone_hours*0.1,0.6),1,5)
    mood=bounded(np.random.normal(base_mood+(sleep_quality-3)*0.5,0.5),1,5)
    deep_work_hours=bounded(np.random.normal(base_focus+(mood-3)-phone_hours*0.4,1.0),0.5,10)
    distraction_minutes=int(bounded(phone_hours*random.randint(20,40),10,300))
    
    primary_task=random.choice(['ML Study','NLP','Practice Interview Ques','Revision','Work on Project'])
    records.append({
        "date":current_date.date(),
        "phone_hours":round(phone_hours,2),
        "sleep_quality":int(round(sleep_quality)),
        "mood":int(round(mood)),
        "deep_work_hours":round(deep_work_hours,2),
        "distraction_minutes":distraction_minutes,
        "primary_task":primary_task
    })

df=pd.DataFrame(records)
df.to_csv("data/raw/focusiq_dummy_90_days.csv",index=False)
print("Dummy Data is Generated Successfully")
from IPython.display import display
display(df.head(10))