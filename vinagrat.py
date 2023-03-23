
from datetime import datetime
import random
def vinegret(date1,date2):
    
    dt1 = datetime.strptime(date1,"%Y-%m-%d").date()
    dt2 = datetime.strptime(date2,"%Y-%m-%d").date()
    epoch_time1 = datetime(dt1.year, dt1.month, dt1.day).timestamp()  
    epoch_time2 = datetime(dt2.year, dt2.month, dt2.day).timestamp()  
    
    epoch_rand=random.randrange(epoch_time1,epoch_time2)  
    rand_time=(datetime.fromtimestamp(epoch_rand)).date()
    print(rand_time)
    if(rand_time.weekday()==0):
        print("אין לי וינגרט");

date1=input()
date2=input()
vinegret(date1,date2)

