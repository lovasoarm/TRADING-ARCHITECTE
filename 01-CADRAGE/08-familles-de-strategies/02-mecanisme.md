---
stability: intemporel
acte: comprendre
---

# 02 — MÉCANISME : FAMILLES

```text
Trend → exploiter une persistance de direction
Momentum → comparer des performances relatives
Mean reversion → exploiter un retour conditionnel
Carry → rémunération liée au portage
Arbitrage → relation relative entre prix
Market making → fournir de la liquidité contre compensation
Volatility → traiter la variance / convexité plutôt que le seul sens
```

Chaque famille possède un mécanisme, une source de risque et une façon différente de mourir.

## Exemple chiffré

Supposons 100 essais indépendants et un faux positif théorique de 5 % par test. Le risque de voir au moins un « gagnant » par hasard devient **1 − 0,95^100 ≈ 99,4 %**. Le calcul n'est pas un modèle complet des marchés, mais il montre pourquoi tester beaucoup de variantes réclame une correction du protocole.

## Lecture opérationnelle

```text
plus de variantes testées
          ↓
plus de chances de trouver un champion accidentel
          ↓
validation hors échantillon
          ↓
stress des coûts + réplication
```

## Référence

Pour ce mécanisme, le parcours s'appuie notamment sur White (2000, Reality Check), Hansen (2005, SPA) et les travaux de McLean & Pontiff sur la décroissance post-publication, déjà recensés dans le corpus de recherche.

### Références

- Hansen, P. R. (2005), *A Test for Superior Predictive Ability*, JBES 23(4), 365–380. — https://doi.org/10.1198/073500105000000063
- White, H. (2000), *A Reality Check for Data Snooping*. — https://doi.org/10.1111/1468-0262.00152
