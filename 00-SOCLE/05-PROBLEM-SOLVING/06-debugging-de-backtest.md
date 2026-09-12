---
stability: intemporel
acte: dépanner
---

# 06 : DEBUGGING DE BACKTEST

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
