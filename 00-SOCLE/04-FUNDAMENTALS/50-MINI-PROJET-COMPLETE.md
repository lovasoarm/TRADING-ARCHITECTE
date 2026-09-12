---
stability: stable
acte: construire
noyau: oui
assessment_role: project_gate
---

# 50 — MINI-PROJET FOUNDATIONS

## CARTE VISUELLE

```text
DÉCISION
   ↓
ORDRE
   ↓
ROUTAGE
   ↓
CARNET
   ↓
MATCHING
   ↓
EXÉCUTION
   ↓
PRIX DIFFUSÉ
```

Construis un **marché miniature** local : données de rendements, distributions, carnet, sizing et liquidation (fermeture d’une position, parfois forcée).

## Livrables

- [ ] 100 rendements synthétiques
- [ ] statistiques descriptives
- [ ] max drawdown (baisse du capital depuis un précédent sommet)
- [ ] carnet 6 niveaux
- [ ] exécution de 3 tailles
- [ ] position sizing avec unité explicite
- [ ] scénario de levier 1×/2×/5×
- [ ] un dérivé expliqué en langage simple

## Critère CrazyDevs

Chaque artefact possède :

`hypothèse → procédure → résultat → limite → prochaine décision`.

### Références

- Almgren, R. & Chriss, N. (2001), *Optimal Execution of Portfolio Transactions*. — https://doi.org/10.21314/JOR.2001.041
