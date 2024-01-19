import json
import csv
import numpy as np

#data on TSLA stock stored in csv:
with open("TeslaStockData.csv", "r") as f:
    reader = csv.reader(f, delimiter=",")
    data = []
    for row in reader:
        data.append(row)

json_data = json.dumps(data)

with open("data.json", "w") as f:
    json.dump(json_data, f)

# Get the current stock price
    current_price = data[-1][4]
    current_price = current_price.replace('$', '')
    try:
        current_price = float(current_price)
    except ValueError:
        current_price = None
    print(current_price)
    
    # Get the day's high and low prices
    high = float(data[-1][2])
    low = data[-1][3]

    # Remove the dollar sign from the string.
    low = low.replace('$', '')

    # Try to convert the string to a float.
    try:
        low = float(low)
    except ValueError:
        low = None
    
    # Get the volume of shares traded
    volume = data[-1][5]

    # Remove the dollar sign from the string.
    volume = volume.replace('$', '')

    # Try to convert the string to an integer.
    try:
        volume = int(volume)
    except ValueError:
        volume = None

    # Calculate the percentage change in the stock price from yesterday
    yesterday_price = data[-2][4]

    # Remove the dollar sign from the string.
    yesterday_price = yesterday_price.replace('$', '')

    # Try to convert the string to a float.
    try:
        yesterday_price = float(yesterday_price)
    except ValueError:
        yesterday_price = None

    percentage_change = (current_price - yesterday_price) / yesterday_price * 100

    # Calculate the moving average of the stock price over the past 5, 10, and 20 days
    # moving_average_5 = sum([float(row[4]) for row in data[-5:]]) / 5
    moving_average_5 = []

# Get the last 5 prices of the stock.
    for row in data[-5:]:
        price = row[4]

  # Remove the dollar sign from the string.
    price = price.replace('$', '')

  # Try to convert the string to a float.
    try:
        price = float(price)
        moving_average_5.append(price)
    except ValueError:
    # If the conversion fails, skip the row.
        pass

# Calculate the moving average.
    if len(moving_average_5) > 0:
        moving_average_5 = sum(moving_average_5) / len(moving_average_5)
    else:
        moving_average_5 = None

    # moving_average_10 = sum([float(row[4]) for row in data[-10:]]) / 10
    moving_average_10 = []
    #Get last 10 prices of stock:
    for row in data[-10:]:
        price = row[4]

    #Remove $ from string:
    price = price.replace('$', '')

    #Try to convert the string to a float:
    try:
        price = float(price)
        moving_average_10.append(price)
    except ValueError:
        pass

    if len(moving_average_10) > 0:
        moving_average_10 = sum(moving_average_10) / len(moving_average_10)
    else:
        moving_average_10 = None


    # moving_average_20 = sum([float(row[4]) for row in data[-20:]]) / 20
    moving_average_20 = []
    #Get last 10 prices of stock:
    for row in data[-20:]:
        price = row[4]

    #Remove $ from string:
    price = price.replace('$', '')

    #Try to convert the string to a float:
    try:
        price = float(price)
        moving_average_20.append(price)
    except ValueError:
        pass

    if len(moving_average_20) > 0:
        moving_average_20 = sum(moving_average_20) / len(moving_average_20)
    else:
        moving_average_20 = None

    # Calculate the buy and sell signals based on the stock trends
    if current_price > moving_average_5 and current_price > moving_average_10 and current_price > moving_average_20:
        buy_signal = 1
        sell_signal = 0
    elif current_price < moving_average_5 and current_price < moving_average_10 and current_price < moving_average_20:
        buy_signal = 0
        sell_signal = 1
    else:
        buy_signal = 0
        sell_signal = 0

    print("Current price:", current_price)
    print("High:", high)
    print("Low:", low)
    print("Volume:", volume)
    print("Percentage change:", percentage_change, "%")
    print("Moving average 5:", moving_average_5)
    print("Moving average 10:", moving_average_10)
    print("Moving average 20:", moving_average_20)
    print("Buy signal:", buy_signal)
    print("Sell signal:", sell_signal)

    # Next steps: 1.) Employ multiple technical indicators for tech analysis
    # 2.) Use trading strategy to make program carry out buy/selling decisions
    # based on strategy

    #Indicators to implement:
    # Bollinger bands
    # Relative strength index
    # Stochastic oscillator

    # BOLLINGER BANDS:

    def bollinger_bands(data, period, std):

        close = data["Close"]
        n = len(close)
        rolling_mean = []
        rolling_std = []

        for i in range(n - period + 1):
            start = i
            end = i + period
            sub_array = close[start:end]
            rolling_mean.append(sum(sub_array) / len(sub_array))
            rolling_std.append(np.std(sub_array))

        upper_band = []
        lower_band = []

        for i in range(n):
            upper_band.append(rolling_mean[i] + std * rolling_std[i])
            lower_band.append(rolling_mean[i] - std * rolling_std[i])

        return upper_band, rolling_mean, lower_band

    def main():
  # Get the stock data
        data = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]

  # Calculate the Bollinger Bands
        upper_band, middle_band, lower_band = bollinger_bands(data, 20, 2)

  # Print the Bollinger Bands
        print(upper_band)
        print(middle_band)
        print(lower_band)


if __name__ == "__main__":
  main()

    # Initial trading strategy:
    # Buy when price crosses above moving average
    # Sell when price crosses below moving average
    # Use stop-loss
    

