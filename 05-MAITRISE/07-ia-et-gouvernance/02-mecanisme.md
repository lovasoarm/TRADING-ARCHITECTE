---
stability: intemporel
acte: comprendre
---

# 02 — MÉCANISME : IA COMME SYSTÈME

Un LLM (Large Language Model — grand modèle de langage) ou un agent n'est pas « une stratégie ». Il s'insère dans une chaîne :

```text
données → perception → raisonnement → proposition → contrôle → exécution
```

L'endroit décisif est souvent le **contrôle**, pas le texte produit.

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
