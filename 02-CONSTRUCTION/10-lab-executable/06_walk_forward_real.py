"""Real rolling walk-forward: choose parameters on train, evaluate only on next test."""
from __future__ import annotations
import argparse
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location("bt", Path(__file__).with_name("05_backtest_real.py"))
bt = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(bt)

CANDIDATES = [(10, 30), (20, 50), (50, 100)]

def simple_score(prices: list[float], short: int, long: int, cost_bps: float) -> float:
    """Use training equity as selection score; parameters never see test data."""
    return bt.run(prices, short, long, cost_bps)["equity"]

def windows(n: int, train: int, test: int, step: int):
    start = 0
    while start + train + test <= n:
        yield start, start + train, start + train + test
        start += step

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--train", type=int, default=252)
    p.add_argument("--test", type=int, default=63)
    p.add_argument("--step", type=int, default=63)
    p.add_argument("--cost-bps", type=float, default=5.0)
    a=p.parse_args()
    prices=bt.load_prices(Path(a.input))
    results=[]
    for j,(s,m,e) in enumerate(windows(len(prices),a.train,a.test,a.step),1):
        train=prices[s:m]
        test=prices[m:e]
        viable=[(short,long) for short,long in CANDIDATES if long < len(train)]
        assert viable, "Fenêtre train trop courte pour les paramètres candidats."
        best=max(viable, key=lambda pair: simple_score(train,*pair,a.cost_bps))
        test_result=bt.run(test,best[0],best[1],a.cost_bps)
        results.append(test_result)
        print(f"window={j} train={len(train)} test={len(test)} chosen={best[0]}/{best[1]} test_equity={test_result['equity']:.4f} test_mdd={test_result['mdd']:.2%}")
    assert len(results) >= 2, "Augmenter la période ou réduire les fenêtres pour obtenir au moins 2 tests."
    print(f"windows: {len(results)}")

if __name__ == "__main__":
    main()
