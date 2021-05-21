import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import seaborn as sns
import datetime as dt
import tkinter as tk

from tkinter import simpledialog

# Creating the UI
canvas = tk.Tk()

canvas.withdraw() # removes from the window from the screen

# the input dialog
userinput = simpledialog.askstring(title="Cryptocurrency Analyzer", prompt="Input Cryptocurrency Ticker Symbol seperated with a space:") # take the strings entered
userinput = userinput.split()

currency = "USD"
metric = "Close"

start = dt.datetime(2018 , 1, 1)
end = dt.datetime.now()

crypto = userinput
colnames = []

first = True

for ticker in crypto:
    data = web.DataReader(f'{ticker}-{currency}', "yahoo", start, end)
    if first:
        combined = data[[metric]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[metric])
        colnames.append(ticker)
        combined.columns = colnames

'''
plt.yscale('log')

for ticker in crypto:
    plt.plot(combined[ticker], label = ticker)

plt.legend(loc = "upper right")
'''

combined = combined.pct_change().corr(method = "pearson")
sns.heatmap(combined, annot = True, cmap = "coolwarm")

plt.show()


