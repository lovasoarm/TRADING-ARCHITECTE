---
stability: intemporel
acte: dépanner
---

# 06 : DEBUGGING DE BACKTEST (simulation d’une règle sur des données historiques)

Quand une stratégie « devient miraculeusement » rentable, suspecte d'abord :

1. look-ahead (information future involontairement disponible) ;
2. survivorship ;
3. data snooping ;
4. coûts irréalistes ;
5. index temporel incorrect ;
6. règle de remplissage impossible ;
7. bug de taille de position.

```text
performance anormale
   ↓
chercher d'abord une erreur simple
   ↓
puis seulement une explication sophistiquée
```

### Références

- White, H. (2000), _A Reality Check for Data Snooping_, Econometrica 68(5), 1097–1126. : https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), _The Probability of Backtest Overfitting_. : https://ssrn.com/abstract=2326253
