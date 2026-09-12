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
