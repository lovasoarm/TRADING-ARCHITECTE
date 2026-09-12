---
stability: stable
---

# CORE MINI-PROJECT MAP

| Niveau | Projet                                                                  | Preuve                         |
| ------ | ----------------------------------------------------------------------- | ------------------------------ |
| 00     | Carnet d’ordre + distributions                                          | carte + mesures                |
| 01     | Dossier d’hypothèse + journal                                           | 30 décisions                   |
| 02     | Moteur de backtest (simulation d’une règle sur des données historiques) | reproductibilité + OOS + coûts |
| 03     | Portefeuille + stress pack                                              | dossier de risque              |
| 04     | Capstone adversarial                                                    | postmortem                     |
| 05     | Thèse du praticien                                                      | soutenance                     |

## Utilisation détaillée

Chaque mini-projet transforme un concept en artefact inspectable et prépare le projet suivant.

### Séquence

```text
question
  ↓
vocabulaire simple
  ↓
mécanisme
  ↓
exemple chiffré
  ↓
expérience
  ↓
contre-exemple
  ↓
preuve
  ↓
portage
```

### Règle d'auto-apprentissage

Ne valide pas une section parce que tu peux la relire. Valide-la lorsque tu peux **reconstruire le raisonnement sans regarder**, produire un exemple et expliquer au moins une limite.

### Références

- White, H. (2000), _A Reality Check for Data Snooping_, Econometrica 68(5), 1097–1126. : https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), _The Probability of Backtest Overfitting_. : https://ssrn.com/abstract=2326253
