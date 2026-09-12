---
stability: intemporel
acte: comprendre
noyau: oui
route_family: core
assessment_role: instructional_checkpoint
cognitive_level: L6
perturbation_modes: [preuve_partielle, contre_exemple, contraintes_injectees]
---

> **SCÈNE CRAZYDEVS — LA SALLE DU CONSEIL :** Avant de choisir un train, regarde les rails.

> **CE MODULE RÉUTILISE :** `00-SOCLE/01-START-HERE.md`. Tu n'as pas besoin de tout relire. Réactive seulement la dépendance qui bloque réellement.

# DU CHOIX DE TRADER AU PRIX OBSERVÉ

Temps de lecture : ~8–12 min  
Temps de pratique : ~20–40 min

## 1. Pourquoi cette leçon mérite ton temps

La chaîne mécanique est décision → ordre → routage → carnet → matching → exécution → prix diffusé. Chaque maillon peut créer un écart entre ton intention et le résultat.

Cette leçon ne cherche pas à te faire mémoriser une définition. Elle construit un modèle utilisable lorsque les informations sont incomplètes, contradictoires ou coûteuses.

## 2. Le mécanisme, pas le slogan

La chaîne mécanique est décision → ordre → routage → carnet → matching → exécution → prix diffusé. Chaque maillon peut créer un écart entre ton intention et le résultat.

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

**ordre, routage, carnet, matching, exécution, spread et slippage (écart entre le prix visé et le prix effectivement obtenu)**. Ces termes sont utiles seulement lorsqu'ils permettent d'expliquer une observation.

## 3. Exemple guidé

Un market order privilégie l’exécution au contrôle exact du prix. Un limit order contrôle mieux le prix mais peut rester non exécuté. Un stop déclenché peut devenir un ordre au marché selon le lieu et le type de stop.

### Ce qu'il faut remarquer

1. Une même observation peut avoir plusieurs explications.
2. Le résultat d'un cas particulier ne suffit pas pour conclure.
3. Une règle sérieuse déclare ses conditions et ses limites.
4. Les coûts et le risque doivent être introduits dès qu'ils peuvent changer la décision.

## 4. Ce qui casse le modèle

Le piège le plus fréquent ici est de regarder d'abord la fin de l'histoire. Une fois le résultat connu, le cerveau construit une explication qui paraît plus certaine qu'elle ne l'était au moment t0.

Dans le parcours, protège-toi avec une trace datée : hypothèse avant observation, information disponible, décision, puis résultat.

## 5. Mini-atelier

Dessine un carnet de six niveaux. Envoie un ordre qui consomme plusieurs niveaux. Calcule le prix moyen exécuté et le slippage par rapport au meilleur prix initial.

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

Tu dois pouvoir expliquer le prix comme le résultat d’un mécanisme de marché, pas comme un personnage qui bouge contre toi.

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

### Références

- Hasbrouck, J. (1995), *One Security, Many Markets: Determining the Contributions to Price Discovery*, Journal of Finance 50, 1175–1199. — https://doi.org/10.2307/2329348
