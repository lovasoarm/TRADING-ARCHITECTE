---
stability: intemporel
acte: transition
---

# 99A — PONT

## Ce que tu emportes

À la sortie de **BACKTEST VS TERRAIN**, tu dois pouvoir formuler :

1. **Mécanisme** — Le backtest décrit un monde simulé ; la production révèle les frictions que la simulation a choisi de simplifier.
2. **Mesure** — quel indicateur ou quelle observation rend le mécanisme visible ?
3. **Preuve** — quel résultat peut réellement être revendiqué ?
4. **Limite** — dans quel contexte la conclusion devient-elle fragile ?
5. **Règle de révision** — quel signal te ferait changer d’avis ?

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

- White, H. (2000), *A Reality Check for Data Snooping*, Econometrica 68(5), 1097–1126. — https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), *The Probability of Backtest Overfitting*. — https://ssrn.com/abstract=2326253
