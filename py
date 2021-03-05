
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
import arrow 
import pandas as pd
import datetime as dt
from datetime import timedelta

def get_start_end_day(start="202001"):
    start_day = dt.datetime(int(start[:-2]), int(start[-2:]), 1)
    
    end_year = int(start[:-2])
    end_month = int(start[-2:]) + 1
    if end_month > 12:
        end_month = 1
        end_year += 1
    
    end_day = dt.datetime(end_year, end_month, 1) - timedelta(days=1)
    e_list = pd.bdate_range(start_day, end_day)
    three_month= [temp.strftime('%Y-%m-%d') for temp in e_list.date]
    return three_month
