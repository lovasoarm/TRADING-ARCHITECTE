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

# CHERCHER ACTIVEMENT POURQUOI LE RÉSULTAT EST FAUX

Temps de lecture : ~8–12 min  
Temps de pratique : ~20–40 min

## 1. Pourquoi cette leçon mérite ton temps

Chaque essai supplémentaire crée une occasion de trouver un résultat impressionnant par hasard. Le chercheur doit donc compter son histoire de recherche.

Cette leçon ne cherche pas à te faire mémoriser une définition. Elle construit un modèle utilisable lorsque les informations sont incomplètes, contradictoires ou coûteuses.

## 2. Le mécanisme, pas le slogan

Chaque essai supplémentaire crée une occasion de trouver un résultat impressionnant par hasard. Le chercheur doit donc compter son histoire de recherche.

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

**overfitting (surajustement : adaptation excessive aux données connues), look-ahead, survivorship, data snooping et multiple testing**. Ces termes sont utiles seulement lorsqu'ils permettent d'expliquer une observation.

## 3. Exemple guidé

Un excellent résultat peut être le champion d’une compétition de modèles médiocres. Hors échantillon, le champion peut revenir à la moyenne ou disparaître.

### Ce qu'il faut remarquer

1. Une même observation peut avoir plusieurs explications.
2. Le résultat d'un cas particulier ne suffit pas pour conclure.
3. Une règle sérieuse déclare ses conditions et ses limites.
4. Les coûts et le risque doivent être introduits dès qu'ils peuvent changer la décision.

## 4. Ce qui casse le modèle

Le piège le plus fréquent ici est de regarder d'abord la fin de l'histoire. Une fois le résultat connu, le cerveau construit une explication qui paraît plus certaine qu'elle ne l'était au moment t0.

Dans le parcours, protège-toi avec une trace datée : hypothèse avant observation, information disponible, décision, puis résultat.

## 5. Mini-atelier

Teste dix variantes documentées, gèle ton choix et compare la meilleure variante in-sample à toutes les variantes hors échantillon. Conserve aussi les variantes rejetées.

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

Tu apprends à rechercher les raisons pour lesquelles un résultat pourrait être faux.

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

## Cas numérique : le meilleur des 100 n'est pas automatiquement bon

Suppose 100 variantes indépendantes avec une probabilité théorique de 5 % de produire un résultat « positif » par hasard. La probabilité d'avoir au moins un positif parmi 100 essais est : **1 − 0,95^100 ≈ 99,4 %**.

Les marchés ne satisfont évidemment pas toutes les hypothèses d'indépendance ; l'exemple sert à construire l'intuition. C'est pourquoi White Reality Check, SPA, DSR et validation hors échantillon jouent des rôles distincts.

## Références

White (2000), Hansen (2005), Bailey et al. (PBO/DSR selon les extensions étudiées), Harvey, Liu & Zhu (2016).

### Références

- Hansen, P. R. (2005), _A Test for Superior Predictive Ability_, JBES 23(4), 365–380. : https://doi.org/10.1198/073500105000000063
- White, H. (2000), _A Reality Check for Data Snooping_. : https://doi.org/10.1111/1468-0262.00152

### Mini-expérience Python

```python
scores = [0.01, -0.02, 0.03, 0.015, 0.08]
best = max(scores)
assert best == 0.08
print("Champion in-sample :", best)
print("Question suivante : le champion survit-il sur des données non utilisées pour le choisir ?")
```

Le but est de rendre visible la différence entre **sélectionner** un meilleur score et **démontrer** qu'il est robuste.
