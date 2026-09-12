"""Tiny walk-forward example using price changes only."""
import csv
from pathlib import Path
prices=[]
with open(Path(__file__).with_name("sample_prices.csv"), newline="") as f:
    for row in csv.DictReader(f): prices.append(float(row["close"]))
returns=[prices[i]/prices[i-1]-1 for i in range(1,len(prices))]
cut=len(returns)//2
train=returns[:cut]
test=returns[cut:]
print(f"Train observations: {len(train)}")
print(f"Test observations: {len(test)}")
print(f"Train mean return: {sum(train)/len(train):.3%}")
print(f"Test mean return: {sum(test)/len(test):.3%}")
