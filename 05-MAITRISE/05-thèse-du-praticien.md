---
stability: evolutif
acte: comprendre
noyau: oui
route_family: core
assessment_role: instructional_checkpoint
cognitive_level: L5
perturbation_modes: [preuve_partielle, contre_exemple, contraintes_injectees]
---

> **SCÈNE CRAZYDEVS — LA SALLE DU CONSEIL :** À ce niveau, tu décides aussi ce qui mérite d’être arrêté.

> **CE MODULE RÉUTILISE :** `04-EPREUVE/README.md`. Tu n'as pas besoin de tout relire. Réactive seulement la dépendance qui bloque réellement.

# CONSTRUIRE ET DÉFENDRE UNE POSITION DE RECHERCHE

Temps de lecture : ~8–12 min  
Temps de pratique : ~20–40 min

## 1. Pourquoi cette leçon mérite ton temps

Une position professionnelle dit ce qu’elle soutient, ce qui l’affaiblit et ce qui provoquerait une révision.

Cette leçon ne cherche pas à te faire mémoriser une définition. Elle construit un modèle utilisable lorsque les informations sont incomplètes, contradictoires ou coûteuses.

## 2. Le mécanisme, pas le slogan

Une position professionnelle dit ce qu’elle soutient, ce qui l’affaiblit et ce qui provoquerait une révision.

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

**thèse, preuves, contre-preuves, incertitude et règle de décision**. Ces termes sont utiles seulement lorsqu'ils permettent d'expliquer une observation.

## 3. Exemple guidé

Une thèse solide peut rester conditionnelle. Dire « je ne sais pas encore » devient une compétence si tu sais quelle expérience réduira l’incertitude.

### Ce qu'il faut remarquer

1. Une même observation peut avoir plusieurs explications.
2. Le résultat d'un cas particulier ne suffit pas pour conclure.
3. Une règle sérieuse déclare ses conditions et ses limites.
4. Les coûts et le risque doivent être introduits dès qu'ils peuvent changer la décision.

## 4. Ce qui casse le modèle

Le piège le plus fréquent ici est de regarder d'abord la fin de l'histoire. Une fois le résultat connu, le cerveau construit une explication qui paraît plus certaine qu'elle ne l'était au moment t0.

Dans le parcours, protège-toi avec une trace datée : hypothèse avant observation, information disponible, décision, puis résultat.

## 5. Mini-atelier

Rédige une note de 2 à 4 pages et défends-la contre trois objections. Chaque réponse doit revenir à une preuve ou proposer un test.

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

Tu termines avec un raisonnement défendable, pas avec une promesse de rentabilité.

Tu n'as pas démontré une rentabilité future. Tu as démontré une capacité de raisonnement sur ce problème.

## 8. CHECKPOINT DE PROFONDEUR — rappel à livre fermé

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

## Architecture de la thèse

La thèse n'est pas un « meilleur setup ». C'est une **affirmation limitée, falsifiable et reproductible** sur un mécanisme de marché.

### Question

Formule une phrase dont l'issue peut être : **supportée, infirmée ou indécidable**.

### Preuve minimale

```text
hypothèse
   ↓
pré-enregistrement de la règle
   ↓
données point-in-time
   ↓
test in-sample
   ↓
hors échantillon
   ↓
coûts réalistes
   ↓
résultats + incertitude
   ↓
réplication
```

### Cas chiffré miniature

Un backtest affiche 12 % annuel brut, 7 % après coûts, avec un drawdown maximal de 18 %. La conclusion n'est pas « 7 % est bon ». La vraie question est : l'incertitude de l'estimation, le nombre d'essais, la stabilité des périodes et la plausibilité du coût permettent-ils encore d'attribuer une partie du résultat au mécanisme proposé ?

### Chapitre de réfutation

Une thèse forte contient sa propre attaque : variation des fenêtres, univers élargi, coûts ×2, retard d'exécution, sous-périodes, permutation ou bootstrap, et réplication par un protocole indépendant.

### Grille de soutenance

- 3 pts — problème et mécanisme
- 3 pts — protocole reproductible
- 2 pts — preuve quantitative + incertitude
- 1 pt — limites et contre-exemple
- 1 pt — décision de suite

**Une thèse qui ne dit pas clairement ce qui la ferait échouer n'est pas terminée.**

### Références

- White, H. (2000), *A Reality Check for Data Snooping*, Econometrica 68(5), 1097–1126. — https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), *The Probability of Backtest Overfitting*. — https://ssrn.com/abstract=2326253
