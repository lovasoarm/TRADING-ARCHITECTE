"""Download real daily data from Stooq using the standard library only."""
from __future__ import annotations
import argparse, csv, urllib.request
from pathlib import Path

BASE = "https://stooq.com/q/d/l/"

def fetch(symbol: str, start: str, end: str, out: Path) -> int:
    params = f"?s={symbol}&d1={start.replace('-','')}&d2={end.replace('-','')}&i=d"
    with urllib.request.urlopen(BASE + params, timeout=30) as r:
        raw = r.read().decode("utf-8")
    rows = list(csv.DictReader(raw.splitlines()))
    if not rows or "Close" not in rows[0]:
        raise RuntimeError("Aucune donnée exploitable reçue. Vérifier le symbole et la période.")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)
    return len(rows)

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--symbol", default="spy.us")
    p.add_argument("--start", default="2018-01-01")
    p.add_argument("--end", default="2025-12-31")
    p.add_argument("--output", default=None)
    a = p.parse_args()
    out = Path(a.output or f"data/{a.symbol}.csv")
    n = fetch(a.symbol, a.start, a.end, out)
    print(f"{n} lignes écrites dans {out}")
    print(f"Source: {BASE} | symbole={a.symbol} | {a.start}→{a.end}")

if __name__ == "__main__":
    main()
