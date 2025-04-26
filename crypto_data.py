# crypto_data.py
import requests 
import pandas as pd
import matplotlib as plt

from pycoingecko import CoinGeckoAPI

# Initialize CoinGecko API
cg = CoinGeckoAPI()

# Function to get the current price from CoinGecko
def get_crypto_price(coin_name):
    try:
        coin_data = cg.get_price(ids=coin_name, vs_currencies='usd')
        if coin_name in coin_data:
            return coin_data[coin_name]['usd']
        else:
            return None  # If the coin is not found
    except Exception as e:
        return f"Error: {e}"

    
def plot_crypto_price_history(coin_id="ethereum", days=10):
    data = get_historical_price(coin_id, days=days)
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['price'], marker='o', linestyle='-', color='cyan')
    plt.title(f'{coin_id.capitalize()} Price - Last {days} Days')
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("price_chart.png")
    return "price_chart.png"

# Function to get historical price (you can customize this as needed)
def get_historical_price(coin_name, days=10):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_name.lower()}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days,
        "interval": "daily"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = data.get("prices", [])
        df = pd.DataFrame(prices, columns=["Timestamp", "Price"])
        df["Date"] = pd.to_datetime(df["Timestamp"], unit='ms').dt.date
        return df[["Date", "Price"]]
    else:
        return pd.DataFrame()
