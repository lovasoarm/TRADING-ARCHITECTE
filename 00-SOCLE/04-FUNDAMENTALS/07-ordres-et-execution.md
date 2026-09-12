---
stability: intemporel
acte: comprendre
noyau: oui
---

# 07 : ORDRES & EXÉCUTION

Un **market order (ordre priorisant l'exécution)** n'offre pas le prix exact. Un **limit order (ordre limitant le prix accepté)** peut ne pas être exécuté.

```text
intention
 ↓
ordre
 ↓
routage
 ↓
carnet
 ↓
matching
 ↓
exécution
```

## Exercice

Construis un carnet à six niveaux. Fais traverser trois tailles d'ordres et mesure le prix moyen d'exécution.

## Piège

Le graphique ne montre pas toute la mécanique qui vient d'avoir lieu.

### Références

- Almgren, R. & Chriss, N. (2001), _Optimal Execution of Portfolio Transactions_. : https://doi.org/10.21314/JOR.2001.041
- Hasbrouck, J. (1995), _One Security, Many Markets_. : https://doi.org/10.2307/2329348
