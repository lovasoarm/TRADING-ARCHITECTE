"""Toy sizing lab: no broker/API, deterministic inputs."""
capital=10_000
risk_fraction=0.005
entry=100.0
invalidation=98.0
value_per_unit=1.0
risk_budget=capital*risk_fraction
distance=abs(entry-invalidation)
qty=risk_budget/(distance*value_per_unit)
print(f"Capital: {capital:,.0f} €")
print(f"Budget de risque: {risk_budget:.2f} €")
print(f"Distance: {distance:.2f}")
print(f"Taille théorique: {qty:.2f} unités")
# Ajout volontaire : 1% de gap adverse
gap_loss=qty*entry*0.01
print(f"Perte supplémentaire simplifiée avec gap 1%: {gap_loss:.2f} €")
