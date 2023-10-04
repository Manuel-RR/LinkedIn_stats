import os
import pandas as pd
from os.path import join

import warnings
warnings.filterwarnings(action='ignore')

try:
  file_folder = join(os.getcwd(),'profile_data')

except:
  print('Google colab enviroment detected!')
  file_folder = join(os.getcwd(),'LinkedIn_stats','profile_data')

file_name = os.listdir(file_folder)[0]
FILE = pd.ExcelFile(join(file_folder,file_name))
print(f'Succesfully loaded: {file_name}')


def stats_by_month(data:pd.DataFrame) -> pd.DataFrame:
  return data.groupby(data.index.month_name()).describe()

def stats_by_day(data:pd.DataFrame) -> pd.DataFrame:
  return data.groupby(data.index.day_name()).describe()