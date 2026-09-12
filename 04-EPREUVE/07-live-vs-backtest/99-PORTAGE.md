---
stability: intemporel
acte: transférer
---

# 99 — PORTAGE

## CARTE VISUELLE

```text
question
  ↓
mécanisme
  ↓
mesure
  ↓
expérience
  ↓
contre-exemple
  ↓
décision
```

Transfère le mécanisme de **BACKTEST (simulation d’une règle sur des données historiques) VS TERRAIN** à un autre actif, un autre horizon et un problème non financier.

Pour chaque cas : invariant, changement, mesure, risque.

## Cas de transfert

Prends le concept **écart entre modèle et marché réel** et applique-le à un objet différent de celui de l'exercice principal.

### Protocole

1. définis le même mécanisme en langage simple ;
2. change l'actif, la période ou la granularité ;
3. garde la même question ;
4. mesure ce qui change ;
5. explique pourquoi le résultat est différent ou similaire.

### Exemple

Un raisonnement appris sur des actions quotidiennes ne peut pas être copié mot à mot sur des futures intraday (contrats standardisés négociés en continu sur une place donnée). Tu dois réévaluer les coûts, la liquidité, le calendrier et la granularité des données.

### Critère de réussite

Le portage est réussi si tu peux dire **deux invariants** du mécanisme et **deux paramètres** qui doivent changer dans le nouveau contexte.

### Preuve

Conserve : contexte initial → contexte nouveau → tableau comparatif → décision.

### Références

- White, H. (2000), *A Reality Check for Data Snooping*, Econometrica 68(5), 1097–1126. — https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), *The Probability of Backtest Overfitting*. — https://ssrn.com/abstract=2326253
