import pandas as pd
from datetime import date

start_date = date(2020,4,1)
end_date = date(2020,4,30)
date_range = pd.date_range(start_date,end_date)

for d in date_range:
    print(d)
