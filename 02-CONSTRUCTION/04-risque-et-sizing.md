---
stability: evolutif
acte: pratiquer
noyau: oui
route_family: core
assessment_role: instructional_checkpoint
cognitive_level: L4
perturbation_modes: [preuve_partielle, contre_exemple, contraintes_injectees]
---

> **SCÈNE CRAZYDEVS : LA SALLE DU CONSEIL :** Une idée brillante n’est pas encore une lame : il faut la forger puis la casser.

> **CE MODULE RÉUTILISE :** `01-CADRAGE/README.md`. Tu n'as pas besoin de tout relire. Réactive seulement la dépendance qui bloque réellement.

# LE RISQUE COMMENCE AVANT LE TRADE

Temps de lecture : ~8–12 min  
Temps de pratique : ~20–40 min

## 1. Pourquoi cette leçon mérite ton temps

Le sizing détermine la vitesse à laquelle une bonne ou mauvaise stratégie modifie ton capital. Le risque au stop est seulement un composant du risque réel.

Cette leçon ne cherche pas à te faire mémoriser une définition. Elle construit un modèle utilisable lorsque les informations sont incomplètes, contradictoires ou coûteuses.

## 2. Le mécanisme, pas le slogan

Le sizing détermine la vitesse à laquelle une bonne ou mauvaise stratégie modifie ton capital. Le risque au stop est seulement un composant du risque réel.

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

**risk budget, sizing, leverage, drawdown (baisse du capital depuis un précédent sommet), margin (marge : garantie mobilisée pour soutenir une position) et risk of ruin**. Ces termes sont utiles seulement lorsqu'ils permettent d'expliquer une observation.

## 3. Exemple guidé

Une formule de quantité peut être correcte et pourtant insuffisante si elle ignore gap, slippage (écart entre le prix visé et le prix effectivement obtenu), frais, financement ou dépendance avec d’autres positions.

### Ce qu'il faut remarquer

1. Une même observation peut avoir plusieurs explications.
2. Le résultat d'un cas particulier ne suffit pas pour conclure.
3. Une règle sérieuse déclare ses conditions et ses limites.
4. Les coûts et le risque doivent être introduits dès qu'ils peuvent changer la décision.

## 4. Ce qui casse le modèle

Le piège le plus fréquent ici est de regarder d'abord la fin de l'histoire. Une fois le résultat connu, le cerveau construit une explication qui paraît plus certaine qu'elle ne l'était au moment t0.

Dans le parcours, protège-toi avec une trace datée : hypothèse avant observation, information disponible, décision, puis résultat.

## 5. Mini-atelier

Compare sizing fixe, fraction de capital et sizing fractionnel sous erreur d’estimation. Observe drawdown, récupération et ruine avant de regarder le rendement moyen.

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

Le capital devient une ressource à protéger plutôt qu’un compteur de points.

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

## Exemple chiffré : risque au stop ≠ perte garantie

Capital = **10 000 €**. Risque budgété = **0,5 %**, donc **50 €**. Entrée = 100 €, invalidation = 98 €, valeur par unité = 1 €.

Taille théorique :

**q = 50 / (2 × 1) = 25 unités.**

Si un gap de 3 % survient entre deux cotations, la perte réelle peut dépasser le budget prévu. La taille protège contre le scénario modélisé ; elle ne supprime pas le risque de discontinuité.

## Référence

Le cadre de risque reprend les notions de sizing, drawdown, liquidité, slippage et tail risk documentées dans le dossier de risk management du projet.

### Références

- Hansen, P. R. (2005), _A Test for Superior Predictive Ability_, JBES 23(4), 365–380. : https://doi.org/10.1198/073500105000000063
- White, H. (2000), _A Reality Check for Data Snooping_. : https://doi.org/10.1111/1468-0262.00152
