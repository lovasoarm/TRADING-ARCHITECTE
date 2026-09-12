---
stability: evolutif
---

# EXPERIMENT LIBRARY

## E01 — Win rate contre espérance
Créer plusieurs distributions de trades et comparer taux de réussite, espérance et drawdown (baisse du capital depuis un précédent sommet).

## E02 — Carnet et slippage (écart entre le prix visé et le prix effectivement obtenu)
Faire consommer plusieurs niveaux d’un carnet synthétique et calculer le prix moyen.

## E03 — Hindsight
Décider avec données masquées puis révéler la suite.

## E04 — Overfitting (surajustement : adaptation excessive aux données connues)
Tester plusieurs variantes, geler la meilleure et observer l’out-of-sample (hors échantillon : données gardées à l’écart de la construction).

## E05 — Coûts adverses
Multiplier spread (écart entre le meilleur prix vendeur et le meilleur prix acheteur), slippage et frais.

## E06 — Gap stress
Remplacer le prix de sortie théorique par des gaps croissants.

## E07 — Corrélation de crise
Faire converger des corrélations vers un régime élevé.

## E08 — Kelly (critère de taille de mise fondé sur l’avantage estimé et le risque de ruine) sous erreur
Perturber volontairement les paramètres de sizing.

## E09 — Données dégradées
Injecter retard, trous, doublons et unités erronées.

## E10 — Psychologie instrumentée
Comparer trades planifiés, impulsifs et revenge-like.

## E11 — Incident d’exécution
Perdre une confirmation et tester réconciliation/idempotence.

## E12 — Attribution
Séparer marché, signal, allocation, timing et coûts.

### Références

- Almgren, R. & Chriss, N. (2001), *Optimal Execution of Portfolio Transactions*. — https://doi.org/10.21314/JOR.2001.041
