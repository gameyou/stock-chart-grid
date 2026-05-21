import yfinance as yf
import pandas as pd
import json

with open("codes.txt", "r", encoding="utf-8") as f:
    codes = [line.strip() for line in f if line.strip()]

result = {}

for code in codes:
    symbol = code + ".T"

    try:
        df = yf.download(symbol, period="2y", interval="1d", progress=False)

        if df.empty:
            print(f"skip {symbol}")
            continue

        df = df.reset_index()

        result[code] = [
            {
                "date": row["Date"].strftime("%Y-%m-%d"),
                "close": float(row["Close"])
            }
            for _, row in df.iterrows()
        ]

        print(f"ok {symbol}")

    except Exception as e:
        print(symbol, e)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(result, f)
