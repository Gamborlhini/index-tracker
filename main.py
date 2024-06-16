import yfinance
import csv
import datetime
import stockclasses
import os

# Used to fetch ticker information from yfinance
def fetch_ticker_info(ticker_names):
    temp = []
    for ticker in ticker_names:
        temp.append(stockclasses.Stock(yfinance.Ticker(ticker), ticker))
    return temp


# Initialize with list of tickers you want to use
tickers = []
# Initialize with the divisor you're using for your index
# Typically you set this so the initial date returns an index value of 100
divisor = 1
# Output file name, reset if you want to change
output_file = 'index.csv'

# Populates initial stocks and index
stocks = fetch_ticker_info(tickers)
index = stockclasses.Index(stocks, divisor)


# Writes output to a csv
current_path = os.path.dirname(__file__)

with open(os.path.join(current_path, output_file), 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow([datetime.datetime.now().strftime("%d-%m-%Y"), str(index.value())])

if __name__ == '__main__':
    print("Running as main file...")
    print(index.value())
