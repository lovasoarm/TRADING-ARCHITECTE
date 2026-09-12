"""Translate gross return into net return under different costs."""
gross=0.12
for cost in [0.01,0.03,0.05,0.08,0.10]:
    net=gross-cost
    print(f"gross={gross:.0%} cost={cost:.0%} net={net:.0%}")
