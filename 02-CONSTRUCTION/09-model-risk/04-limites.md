---
stability: intemporel
acte: critiquer
---

# 04 : LIMITES

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

Une validation passée n'autorise pas une extrapolation infinie. Le bon niveau de maîtrise est de connaître les **conditions de validité**, pas de prétendre les avoir supprimées.

## Modes de défaillance

Pour **risque de modèle**, ne mémorise pas une liste de risques : apprends à les provoquer.

| Défaillance           | Symptôme                       | Test simple                           | Réponse attendue                 |
| --------------------- | ------------------------------ | ------------------------------------- | -------------------------------- |
| données incomplètes   | résultat anormalement propre   | supprimer une partie des observations | documenter la sensibilité        |
| changement de régime  | performance qui se retourne    | découper l'échantillon par période    | conditionner la conclusion       |
| coût sous-estimé      | edge réduit en production      | multiplier les coûts par 2            | recalculer le seuil de viabilité |
| fuite d'information   | performance irréaliste         | décaler la variable d'une période     | corriger le pipeline             |
| sélection postérieure | meilleur cas choisi après coup | rejouer l'univers complet             | conserver toutes les variantes   |

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

- Hansen, P. R. (2005), _A Test for Superior Predictive Ability_, JBES 23(4), 365–380. : https://doi.org/10.1198/073500105000000063
- White, H. (2000), _A Reality Check for Data Snooping_. : https://doi.org/10.1111/1468-0262.00152
