"""Simple, reproducible moving-average backtest on real daily CSV data."""
from __future__ import annotations
import argparse, csv, math
from pathlib import Path

def load_prices(path: Path) -> list[float]:
    with path.open(newline="", encoding="utf-8") as f:
        return [float(r["Close"]) for r in csv.DictReader(f) if r.get("Close") not in (None, "", "nan")]

def sma(xs: list[float], n: int) -> float:
    return sum(xs[-n:]) / n

def run(prices: list[float], short: int, long: int, cost_bps: float) -> dict[str, float]:
    if len(prices) <= long + 2: raise ValueError("Pas assez de données")
    cost = cost_bps / 10_000
    equity = 1.0; peak = 1.0; mdd = 0.0; position = 0
    daily = []
    for i in range(long, len(prices)-1):
        signal = 1 if sma(prices[:i+1], short) > sma(prices[:i+1], long) else 0
        turnover = abs(signal - position)
        r = prices[i+1] / prices[i] - 1
        net = signal * r - turnover * cost
        equity *= 1 + net
        peak = max(peak, equity)
        mdd = min(mdd, equity / peak - 1)
        daily.append(net)
        position = signal
    mean = sum(daily) / len(daily)
    vol = math.sqrt(sum((x-mean)**2 for x in daily) / max(1, len(daily)-1))
    sharpe = mean / vol * math.sqrt(252) if vol else 0.0
    return {"equity": equity, "mdd": mdd, "sharpe": sharpe, "observations": len(daily)}

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--short",type=int,default=20); p.add_argument("--long",type=int,default=50); p.add_argument("--cost-bps",type=float,default=5.0); a=p.parse_args()
    result=run(load_prices(Path(a.input)),a.short,a.long,a.cost_bps)
    for k,v in result.items(): print(f"{k}: {v:.4f}" if isinstance(v,float) else f"{k}: {v}")

if __name__ == "__main__": main()
