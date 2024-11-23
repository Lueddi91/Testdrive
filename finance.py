import yfinance as yf 

ticker = input("Welcher Ticker soll abgerufen werden? \n")

kurs = yf.Ticker(ticker).fast_info

print(kurs.last_price, kurs.currency)

