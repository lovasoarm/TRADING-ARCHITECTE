---
stability: intemporel
acte: transition
---

# 99A : PONT

## Ce que tu emportes

À la sortie de **RUNBOOKS & MONITORING**, tu dois pouvoir formuler :

1. **Mécanisme** : Un système professionnel prévoit son comportement quand quelque chose devient anormal.
2. **Mesure** : quel indicateur ou quelle observation rend le mécanisme visible ?
3. **Preuve** : quel résultat peut réellement être revendiqué ?
4. **Limite** : dans quel contexte la conclusion devient-elle fragile ?
5. **Règle de révision** : quel signal te ferait changer d’avis ?

## Test de portage

```text
concept appris
     ↓
contexte nouveau
     ↓
qu'est-ce qui reste invariant ?
     ↓
qu'est-ce qui doit être recalibré ?
     ↓
décision documentée
```

### Exemple

Ne porte pas « le RSI fonctionne ». Porte plutôt : « une mesure de momentum peut avoir un comportement différent selon le régime ; je dois définir le régime, mesurer les coûts et tester hors échantillon ».

### Validation

- [ ] je peux l'expliquer à un débutant ;
- [ ] je peux donner un nombre ;
- [ ] je peux montrer un contre-exemple ;
- [ ] je sais quel fichier ouvrir ensuite.

**NEXT ACTION →** retourne au README du niveau parent et poursuis vers le prochain acte.

### Références

- Hansen, P. R. (2005), _A Test for Superior Predictive Ability_, JBES 23(4), 365–380. : https://doi.org/10.1198/073500105000000063
- White, H. (2000), _A Reality Check for Data Snooping_. : https://doi.org/10.1111/1468-0262.00152
