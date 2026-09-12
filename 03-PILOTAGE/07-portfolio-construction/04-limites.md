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

Les matrices de covariance sont estimées, donc bruitées. Les corrélations peuvent converger en stress. La diversification historique n'est pas un contrat pour la prochaine crise.

## Modes de défaillance

Pour **construction de portefeuille**, ne mémorise pas une liste de risques : apprends à les provoquer.

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
