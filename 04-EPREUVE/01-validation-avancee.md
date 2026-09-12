---
stability: evolutif
acte: pratiquer
noyau: oui
route_family: core
assessment_role: instructional_checkpoint
cognitive_level: L8
perturbation_modes: [preuve_partielle, contre_exemple, contraintes_injectees]
---

> **SCÈNE CRAZYDEVS : LA SALLE DU CONSEIL :** L’épreuve commence quand quelqu’un change les conditions.

> **CE MODULE RÉUTILISE :** `03-PILOTAGE/README.md`. Tu n'as pas besoin de tout relire. Réactive seulement la dépendance qui bloque réellement.

# CPCV, DSR (Deflated Sharpe Ratio : Sharpe corrigé notamment pour les essais multiples et la non-normalité) ET COMPARAISON CONTRE DES ALTERNATIVES

Temps de lecture : ~8–12 min  
Temps de pratique : ~20–40 min

## 1. Pourquoi cette leçon mérite ton temps

Un seul split ne raconte pas toute l’incertitude de la recherche. Les méthodes avancées tentent de tenir compte de la dépendance temporelle ou du nombre d’essais.

Cette leçon ne cherche pas à te faire mémoriser une définition. Elle construit un modèle utilisable lorsque les informations sont incomplètes, contradictoires ou coûteuses.

## 2. Le mécanisme, pas le slogan

Un seul split ne raconte pas toute l’incertitude de la recherche. Les méthodes avancées tentent de tenir compte de la dépendance temporelle ou du nombre d’essais.

```text
QUESTION
   ↓
INFORMATION DISPONIBLE À t0
   ↓
MODÈLE / HYPOTHÈSE
   ↓
DÉCISION
   ↓
RÉSULTAT
   ↓
MESURE
   ↓
CONTRE-EXEMPLE
   ↓
RÉVISION
```

**CPCV, Deflated Sharpe (ratio comparant un rendement excédentaire à une mesure de volatilité) Ratio, SPA, Reality Check (test de White visant à contrôler le data snooping entre stratégies) et multiplicité**. Ces termes sont utiles seulement lorsqu'ils permettent d'expliquer une observation.

## 3. Exemple guidé

Un acronyme n’est pas une garantie. Chaque test possède des hypothèses et des limites.

### Ce qu'il faut remarquer

1. Une même observation peut avoir plusieurs explications.
2. Le résultat d'un cas particulier ne suffit pas pour conclure.
3. Une règle sérieuse déclare ses conditions et ses limites.
4. Les coûts et le risque doivent être introduits dès qu'ils peuvent changer la décision.

## 4. Ce qui casse le modèle

Le piège le plus fréquent ici est de regarder d'abord la fin de l'histoire. Une fois le résultat connu, le cerveau construit une explication qui paraît plus certaine qu'elle ne l'était au moment t0.

Dans le parcours, protège-toi avec une trace datée : hypothèse avant observation, information disponible, décision, puis résultat.

## 5. Mini-atelier

Compare un split simple avec plusieurs découpages combinatoires et note le nombre total de variantes testées avant le modèle final.

### Format de preuve

Conserve :

```text
Hypothèse initiale : __________
Données utilisées : ____________
Mesure : ______________________
Résultat : _____________________
Contre-exemple : _______________
Limite : _______________________
Décision suivante : ____________
```

## 6. Expérience de transfert

Prends le mécanisme de cette leçon et change un seul paramètre : instrument, horizon ou environnement. Qu'est-ce qui reste invariant ? Qu'est-ce qui devient faux ? Quelle nouvelle mesure devient nécessaire ?

## 7. Ce que tu viens de démontrer

La validation avancée doit réduire l’excès de confiance, pas fabriquer un nouveau talisman statistique.

Tu n'as pas démontré une rentabilité future. Tu as démontré une capacité de raisonnement sur ce problème.

## 8. CHECKPOINT DE PROFONDEUR : rappel à livre fermé

Ferme le fichier.

- Explique le mécanisme en cinq lignes sans jargon.
- Donne un exemple qui n'était pas dans la leçon.
- Donne un contre-exemple.
- Nomme une hypothèse encore fragile.
- Donne une observation qui te ferait changer d'avis.

Une réponse récitée ferme le vocabulaire. Une réponse transférée ferme la compétence.

## 9. ANTI-HINDSIGHT

Avant la prochaine observation, écris :

```text
Ce que je pense avant de voir la suite : ________
Ce que je sais réellement à t0 : _______________
Ce qui pourrait réfuter mon interprétation : _____
```

### Références

- Hansen, P. R. (2005), _A Test for Superior Predictive Ability_, JBES 23(4), 365–380. : https://doi.org/10.1198/073500105000000063
- White, H. (2000), _A Reality Check for Data Snooping_. : https://doi.org/10.1111/1468-0262.00152
