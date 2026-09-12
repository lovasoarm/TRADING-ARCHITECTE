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

Un shadow mode n'est pas encore du capital réel. Mais il expose déjà des erreurs que le backtest (simulation d’une règle sur des données historiques) ne voit pas.

## Modes de défaillance

Pour **écart entre modèle et marché réel**, ne mémorise pas une liste de risques : apprends à les provoquer.

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

- White, H. (2000), *A Reality Check for Data Snooping*, Econometrica 68(5), 1097–1126. — https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), *The Probability of Backtest Overfitting*. — https://ssrn.com/abstract=2326253
