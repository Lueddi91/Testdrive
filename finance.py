import yfinance as yf 
import matplotlib.pyplot as plt
import pandas as pd

ticker = input("Welcher Ticker soll abgerufen werden? \n")

kurs = yf.Ticker(ticker).fast_info

#   for k in kurs:
#       print(k, ": ", kurs[k])

hist = yf.Ticker(ticker).history(period="1y")

fig1= hist["Open"].plot()
fig1.set_ylabel(kurs.currency)
fig1.set_title(ticker)
fig2= hist["Close"].plot()
plt.show()




