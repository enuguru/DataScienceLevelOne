# %%
import pandas as pd
from pandas import read_csv
from pandas import read_excel

# %%
# load python using pandas
filename = 'pima-indians-diabetes.data.csv'

# %%
defined_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names=defined_names)
data.shape

# %%
data

# %%
# how to read excel files using python pandas
df = pd.read_excel('pima-indians-diabetes.data.xlsx',names=defined_names)
df.shape

# %%
df

# %%
df.dtypes

# %%
# how to read excel files using python pandas
df = read_excel('file_example_XLSX_5000.xlsx')
df

# %%
# reading data from the web / cloud
data = pd.read_csv('http://winterolympicsmedals.com/medals.csv')
data

# %%
# This program shows that read_table does not read the data from a csv file if delimiter ',' is not given
import pandas as pd
filename = 'pima-indians-diabetes.data.csv'
defined_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_table(filename,names=defined_names)
data

# %%
# load python using pandas
import pandas as pd
filename = 'pima-indians-diabetes.data.csv'
defined_names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_table(filename, delimiter=',',names=defined_names)
data

# %%
data.shape

# %%
data

# %%
