---
stability: stable
acte: construire
---

# Laboratoire exécutable : données réelles

Ici, on quitte le jouet : le laboratoire télécharge une série **réelle** depuis Stooq, la conserve localement, puis exécute un mini backtest reproductible. Le code utilise uniquement la bibliothèque standard Python.

```text
DONNÉES RÉELLES
     ↓
QUALITÉ / TIMESTAMPS
     ↓
SIGNAL SMA 20/50
     ↓
COÛTS PARAMÉTRÉS
     ↓
WALK-FORWARD 4×
     ↓
TESTS + RAPPORT
```

## Prérequis

Python 3.10+ et une connexion Internet uniquement pour le téléchargement initial. Aucune clé API n'est nécessaire.

## Parcours

1. `01_position_sizing.py` : taille et budget de risque.
2. `02_drawdown.py` : drawdown et récupération.
3. `03_fake_champion.py` : sélection après plusieurs essais.
4. `04_download_data.py` : téléchargement d'une série réelle.
5. `05_backtest_real.py` : backtest SMA avec coûts.
6. `06_walk_forward_real.py` : walk-forward multi-fenêtres.
7. `07_lab_tests.py` : tests avec `assert`.

### Commande minimale

```bash
python 04_download_data.py --symbol spy.us --start 2018-01-01 --end 2025-12-31
python 05_backtest_real.py --input data/spy.us.csv --short 20 --long 50 --cost-bps 5
python 06_walk_forward_real.py --input data/spy.us.csv --cost-bps 5
python 07_lab_tests.py
```

## Pourquoi Stooq ?

Le laboratoire télécharge un CSV de marché public à la demande. **Le dépôt ne prétend pas embarquer une base historique propriétaire** : la donnée est récupérée au moment de la séance et sa provenance est enregistrée dans le fichier de données.

## Exercices

### Exercice A : refaire le sizing

Capital `10 000 €`, risque `0,5 %`, distance au stop `2 €`. Calculer le budget et la taille avant d'exécuter le script.

### Exercice B : changer le coût

Rejouer le backtest avec `0`, `5`, `10` et `20 bps` (points de base, 1 bp = 0,01 %). Noter le point où l'edge net change de signe.

### Exercice C : falsifier le signal

Tester `10/30`, `20/50` et `50/100`. **Ne choisir aucun champion sur le seul résultat d'entraînement** : comparer les fenêtres walk-forward.

### Exercice D : vérifier les tests

Casser volontairement une assertion dans `07_lab_tests.py`, observer l'échec, puis restaurer le comportement attendu.

### Exercice E : changer l'actif

Télécharger un autre symbole Stooq et vérifier si les mêmes conclusions tiennent. Un changement d'actif qui détruit le résultat est une information, pas un échec pédagogique.

## Références

- Stooq : données historiques CSV : https://stooq.com/q/d/l/
- White, H. (2000), _A Reality Check for Data Snooping_, Econometrica 68(5), 1097–1126. DOI : https://doi.org/10.1111/1468-0262.00152
- Hansen, P. R. (2005), _A Test for Superior Predictive Ability_, Journal of Business & Economic Statistics 23(4), 365–380. DOI : https://doi.org/10.1198/073500105000000063
- Bailey, D. H. et al. (2015), _The Probability of Backtest Overfitting_. SSRN : https://ssrn.com/abstract=2326253
