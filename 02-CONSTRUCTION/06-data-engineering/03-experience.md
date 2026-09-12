---
stability: stable
acte: expérimenter
assessment_role: instructional_checkpoint
---

# 03 — EXPÉRIENCE : DATA BUG HUNT

## CARTE VISUELLE

```text
source → brut → contrôles → table propre
                                  ↓
                             stratégie
```

Injecte volontairement : un doublon, un trou, un timestamp décalé, une mauvaise unité et un actif disparu.

Écris pour chaque bug : symptôme, détecteur automatique, conséquence sur le backtest (simulation d’une règle sur des données historiques), correction.

### Références

- White, H. (2000), *A Reality Check for Data Snooping*, Econometrica 68(5), 1097–1126. — https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), *The Probability of Backtest Overfitting*. — https://ssrn.com/abstract=2326253

### Contrôle Python des données

```python
rows = [
    {"date": "2025-01-02", "close": "100"},
    {"date": "2025-01-03", "close": "101"},
]
assert all(float(r["close"]) > 0 for r in rows)
assert rows[0]["date"] < rows[1]["date"]
print("Contrôles minimaux : OK")
```

Refais le test avec un prix `0` ou une date inversée : l'assertion doit échouer.
