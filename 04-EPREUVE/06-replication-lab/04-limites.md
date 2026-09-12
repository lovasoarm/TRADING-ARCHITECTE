---
stability: intemporel
acte: critiquer
---

# 04 : LIMITES

## CARTE VISUELLE

```text
papier → protocole → données
                     ↓
                 résultat
                     ↓
                réplication
                     ↓
              accord / écart
```

Une non-réplication n'implique pas automatiquement que l'idée est fausse : univers, période, qualité de données et coûts peuvent différer. La conclusion correcte peut être « non répliqué dans ces conditions ».

## Modes de défaillance

Pour **réplication indépendante**, ne mémorise pas une liste de risques : apprends à les provoquer.

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
