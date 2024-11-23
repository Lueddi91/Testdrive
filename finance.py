import yfinance as yf 

ticker = input("Welcher Ticker soll abgerufen werden? \n")

kurs = yf.Ticker(ticker).fast_info

for k in kurs:
    print(k, ": ", kurs[k])

