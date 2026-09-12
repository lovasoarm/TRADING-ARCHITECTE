---
stability: intemporel
acte: critiquer
---

# 04 — LIMITES

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

Une famille de stratégie n'est pas un système de trading. Deux implémentations de « momentum (persistance statistique de la direction récente des rendements) » peuvent avoir des turnover, univers, coûts et risques radicalement différents.

Le niveau suivant consiste à rendre la règle précise et testable.

## Modes de défaillance

Pour **familles de stratégies**, ne mémorise pas une liste de risques : apprends à les provoquer.

| Défaillance | Symptôme | Test simple | Réponse attendue |
|---|---|---|---|
| données incomplètes | résultat anormalement propre | supprimer une partie des observations | documenter la sensibilité |
| changement de régime | performance qui se retourne | découper l'échantillon par période | conditionner la conclusion |
| coût sous-estimé | edge réduit en production | multiplier les coûts par 2 | recalculer le seuil de viabilité |
| fuite d'information | performance irréaliste | décaler la variable d'une période | corriger le pipeline |
| sélection postérieure | meilleur cas choisi après coup | rejouer l'univers complet | conserver toutes les variantes |

### Ce que la limite ne signifie pas

Une limite n'implique pas que le concept est inutile. Elle indique **quand** il devient dangereux de le généraliser.

### Test de robustesse

```text
version nominale
      ↓
une contrainte adverse
      ↓
résultat avant / après
      ↓
la conclusion change-t-elle ?
```

### Phrase obligatoire

> « La conclusion est conditionnelle à **[hypothèse]** ; elle devient fragile si **[scénario]** ; le prochain test est **[test]**. »

### Références

- Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H. (2012), *Time Series Momentum*. — https://doi.org/10.1016/j.jfineco.2011.11.003
- Harvey, C. R., Liu, Y., & Zhu, H. (2016), *... and the Cross-Section of Expected Returns*, Review of Financial Studies 29, 5–68. — https://doi.org/10.1093/rfs/hhv059
