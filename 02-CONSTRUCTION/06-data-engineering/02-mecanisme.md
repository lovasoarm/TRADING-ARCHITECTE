---
stability: intemporel
acte: comprendre
---

# 02 : MÉCANISME : LA CHAÎNE DE DONNÉES

Une stratégie voit ce que le pipeline lui donne.

```text
source
 ↓
ingestion
 ↓
normalisation
 ↓
validation
 ↓
version
 ↓
feature
 ↓
backtest
```

Chaque flèche est un endroit où peut apparaître une donnée future, un décalage d'horodatage ou une unité erronée.

### Références

- White, H. (2000), _A Reality Check for Data Snooping_, Econometrica 68(5), 1097–1126. : https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), _The Probability of Backtest Overfitting_. : https://ssrn.com/abstract=2326253
