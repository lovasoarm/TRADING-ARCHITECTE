"""Regression tests for the teaching lab."""
from pathlib import Path
import importlib.util
spec=importlib.util.spec_from_file_location("bt",Path(__file__).with_name("05_backtest_real.py")); bt=importlib.util.module_from_spec(spec); assert spec and spec.loader; spec.loader.exec_module(bt)

assert abs(bt.sma([1,2,3],3)-2.0) < 1e-12
assert abs(bt.sma([10,20,40],2)-30.0) < 1e-12
r=bt.run([100,101,102,103,104,105,106],2,3,5)
assert r["observations"] > 0
assert r["equity"] > 0
print("OK : 4 assertions de base passent.")
