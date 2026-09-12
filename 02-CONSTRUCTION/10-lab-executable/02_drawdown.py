"""Compute running peak and drawdown from a tiny equity curve."""
equity=[10_000,10_500,10_200,9_800,10_100,9_200,9_700,10_300]
peak=equity[0]
max_dd=0.0
for e in equity:
    peak=max(peak,e)
    dd=(e/peak)-1
    max_dd=min(max_dd,dd)
    print(f"equity={e:,.0f} peak={peak:,.0f} drawdown={dd:.2%}")
print(f"Maximum drawdown: {max_dd:.2%}")
