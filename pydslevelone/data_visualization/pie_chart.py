
import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('medal.csv')
#country_data = df["country"]
#medal_data = df["gold_medal"]
#colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
#explode = (0.1, 0, 0, 0, 0)  
df.plot(subplots=True,kind='pie')#medal_data, labels=country_data, explode=explode, colors=colors,
#autopct='%1.1f%%', shadow=True, startangle=140)
#plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show()
