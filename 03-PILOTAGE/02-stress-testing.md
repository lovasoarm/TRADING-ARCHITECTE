---
stability: evolutif
acte: pratiquer
noyau: oui
route_family: core
assessment_role: instructional_checkpoint
cognitive_level: L4
perturbation_modes: [preuve_partielle, contre_exemple, contraintes_injectees]
---

> **SCÈNE CRAZYDEVS : LA SALLE DU CONSEIL :** Un cockpit sérieux surveille aussi les alarmes et les procédures de sortie.

> **CE MODULE RÉUTILISE :** `02-CONSTRUCTION/README.md`. Tu n'as pas besoin de tout relire. Réactive seulement la dépendance qui bloque réellement.

# TESTER LA SURVIE PLUTÔT QUE LE SCÉNARIO MOYEN

Temps de lecture : ~8–12 min  
Temps de pratique : ~20–40 min

## 1. Pourquoi cette leçon mérite ton temps

Un stress test ne prédit pas le prochain crash. Il mesure les conséquences d’un monde volontairement défavorable.

Cette leçon ne cherche pas à te faire mémoriser une définition. Elle construit un modèle utilisable lorsque les informations sont incomplètes, contradictoires ou coûteuses.

## 2. Le mécanisme, pas le slogan

Un stress test ne prédit pas le prochain crash. Il mesure les conséquences d’un monde volontairement défavorable.

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

**stress, scénarios, tail risk, liquidité et reverse stress**. Ces termes sont utiles seulement lorsqu'ils permettent d'expliquer une observation.

## 3. Exemple guidé

Une baisse de prix seule est trop pauvre. Un vrai scénario peut combiner gap, spread élargi, marge plus forte, corrélation croissante et liquidité réduite.

### Ce qu'il faut remarquer

1. Une même observation peut avoir plusieurs explications.
2. Le résultat d'un cas particulier ne suffit pas pour conclure.
3. Une règle sérieuse déclare ses conditions et ses limites.
4. Les coûts et le risque doivent être introduits dès qu'ils peuvent changer la décision.

## 4. Ce qui casse le modèle

Le piège le plus fréquent ici est de regarder d'abord la fin de l'histoire. Une fois le résultat connu, le cerveau construit une explication qui paraît plus certaine qu'elle ne l'était au moment t0.

Dans le parcours, protège-toi avec une trace datée : hypothèse avant observation, information disponible, décision, puis résultat.

## 5. Mini-atelier

Construis cinq scénarios et recherche, par reverse stress, la plus petite combinaison qui rend le système non viable.

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

Tu apprends à penser en modes de défaillance et seuils de survie.

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
