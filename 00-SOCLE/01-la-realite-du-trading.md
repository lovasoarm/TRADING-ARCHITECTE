---
stability: intemporel
acte: comprendre
noyau: oui
route_family: core
assessment_role: instructional_checkpoint
cognitive_level: L8
perturbation_modes: [preuve_partielle, contre_exemple, contraintes_injectees]
---

> **SCÈNE CRAZYDEVS : LA SALLE DU CONSEIL :** Avant de choisir un train, regarde les rails.

> **CE MODULE RÉUTILISE :** `00-SOCLE/01-START-HERE.md`. Tu n'as pas besoin de tout relire. Réactive seulement la dépendance qui bloque réellement.

# POURQUOI LE TRADING EST UN PROBLÈME DE DÉCISION SOUS INCERTITUDE

Temps de lecture : ~8–12 min  
Temps de pratique : ~20–40 min

## 1. Pourquoi cette leçon mérite ton temps

Une décision de trading se prend avant le résultat. Il faut donc séparer la qualité de la décision, le résultat d’un cas particulier et la performance d’une règle sur une population. Le taux de réussite décrit seulement la fréquence des résultats gagnants ; il ne décrit ni leur taille ni la taille des pertes.

Cette leçon ne cherche pas à te faire mémoriser une définition. Elle construit un modèle utilisable lorsque les informations sont incomplètes, contradictoires ou coûteuses.

## 2. Le mécanisme, pas le slogan

Une décision de trading se prend avant le résultat. Il faut donc séparer la qualité de la décision, le résultat d’un cas particulier et la performance d’une règle sur une population. Le taux de réussite décrit seulement la fréquence des résultats gagnants ; il ne décrit ni leur taille ni la taille des pertes.

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

**espérance, variance, edge, distribution et drawdown (baisse du capital depuis un précédent sommet)**. Ces termes sont utiles seulement lorsqu'ils permettent d'expliquer une observation.

## 3. Exemple guidé

Imagine deux règles. La première gagne souvent mais perd énormément lorsqu’elle perd. La seconde gagne moins souvent mais les gains sont trois fois plus grands que les pertes. Calcule l’espérance avant de regarder le graphique : ce simple exercice force le cerveau à abandonner l’illusion du win rate.

### Ce qu'il faut remarquer

1. Une même observation peut avoir plusieurs explications.
2. Le résultat d'un cas particulier ne suffit pas pour conclure.
3. Une règle sérieuse déclare ses conditions et ses limites.
4. Les coûts et le risque doivent être introduits dès qu'ils peuvent changer la décision.

## 4. Ce qui casse le modèle

Le piège le plus fréquent ici est de regarder d'abord la fin de l'histoire. Une fois le résultat connu, le cerveau construit une explication qui paraît plus certaine qu'elle ne l'était au moment t0.

Dans le parcours, protège-toi avec une trace datée : hypothèse avant observation, information disponible, décision, puis résultat.

## 5. Mini-atelier

Construis deux distributions de 100 trades. Calcule moyenne, médiane, dispersion, pire série et drawdown. Puis écris ce que tu aurais cru en ne regardant que le nombre de trades gagnants.

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

Tu viens de démontrer qu’un résultat individuel n’est pas une preuve suffisante sur une règle. Le trading commence par une décision sous incertitude, pas par une prédiction parfaite.

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
