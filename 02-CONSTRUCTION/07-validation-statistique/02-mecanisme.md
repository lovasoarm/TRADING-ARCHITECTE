---
stability: intemporel
acte: comprendre
---

# 02 : MÉCANISME : VALIDATION

Tester N variantes augmente la probabilité de trouver un gagnant par hasard.

```text
1 test → risque de faux positif
1000 tests → risque multiplié
```

Les outils comme **multiple testing (correction des essais multiples)**, White Reality Check (test de White visant à contrôler le data snooping entre stratégies), SPA, Deflated Sharpe Ratio (rendement excédentaire rapporté à une mesure de volatilité) et Probability of Backtest Overfitting (surajustement : adaptation excessive aux données connues) traitent différentes facettes du problème.

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

- White, H. (2000), _A Reality Check for Data Snooping_, Econometrica 68(5), 1097–1126. : https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), _The Probability of Backtest Overfitting_. : https://ssrn.com/abstract=2326253
