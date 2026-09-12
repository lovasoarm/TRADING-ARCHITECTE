---
stability: stable
---

<div align="center">

# TRADING ARCHITECTE

**Comprendre · Mesurer · Tester · Casser · Gérer · Construire · Adapter**

*Un curriculum de trading orienté terrain pour apprendre à raisonner sous incertitude — du zéro-prérequis à la conception, validation et défense d’un système.*

[**Commencer**](00-SOCLE/00-GUIDE/README.md) · [**Voir le parcours**](PROGRESSION.md) · [**Préparer l’environnement**](SETUP.md)

</div>

<div align="center">

<svg width="120" height="18" viewBox="0 0 120 18" role="img" aria-label="Trading Architecte">
  <path d="M8 9h30" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
  <circle cx="60" cy="9" r="4" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <path d="M82 9h30" fill="none" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>
</svg>

</div>

---

## L’idée en une page

Trading Architecte ne part pas de la question « quelle stratégie gagne ? ».

Il part de celle-ci :

> **Que dois-tu comprendre, mesurer, tester et contrôler pour qu’une décision reste défendable lorsque le marché, les données ou tes propres hypothèses deviennent hostiles ?**

Le dépôt traite le trading comme une **chaîne de décision** :

```text
MARCHÉ
  ↓
INFORMATION
  ↓
HYPOTHÈSE
  ↓
STRATÉGIE
  ↓
EXÉCUTION
  ↓
RISQUE
  ↓
VALIDATION
  ↓
SURVEILLANCE
  ↓
RÉVISION
```

Pas de promesse de revenu. Pas de « stratégie secrète ». Pas de validation par lecture seule.

---

## Pour qui ?

### Tu débutes complètement

Tu peux commencer sans connaître le trading, Python ou les statistiques.

Le [**Guide transversal — START HERE**](06-ANNEXES-TRANSVERSES/00-GUIDE.md) répond d’abord aux questions fondamentales :

- qu’est-ce qu’un actif, un marché, un ordre, une position ou un spread ;
- pourquoi un prix bouge ;
- différence entre investir, spéculer, couvrir et arbitrer ;
- ce que signifient levier, volatilité, drawdown, risque et perte ;
- comment observer et pratiquer **sans engager de capital** ;
- comment apprendre le vocabulaire sans devoir tout connaître d’un coup ;
- comment savoir quoi faire quand tu bloques.

Le principe est simple : **la technicité ne disparaît pas ; elle devient franchissable.**

### Tu as déjà un niveau intermédiaire

Le parcours peut aussi servir de laboratoire : hypothèses falsifiables, données, backtests, validation hors échantillon, coûts, exécution, stress tests, risques et réplication.

### Tu veux aller vers le quant / systématique

Le curriculum mène progressivement vers la programmation, l’ingénierie de données, la statistique appliquée, la recherche systématique, le portfolio, le monitoring et la gouvernance.

---

## Le fil canonique

```text
00  SOCLE
    Comprendre le terrain
        ↓
01  CADRAGE
    Transformer une idée en hypothèse
        ↓
02  CONSTRUCTION
    Construire quelque chose de testable
        ↓
03  PILOTAGE
    Gérer risque, exécution et opérations
        ↓
04  ÉPREUVE
    Chercher activement ce qui casse
        ↓
05  MAÎTRISE
    Défendre, transférer et adapter
```

Chaque niveau ajoute une capacité **observable**.

| Niveau | Question centrale | Sortie attendue |
|---|---|---|
| **00 — Socle** | De quoi parle-t-on ? | vocabulaire, terrain, premières expériences |
| **01 — Cadrage** | Que prétends-je exactement ? | hypothèse, protocole, critères d’échec |
| **02 — Construction** | Comment le rendre testable ? | données, règles, code, backtests |
| **03 — Pilotage** | Comment survivre à l’exécution ? | sizing, coûts, exposition, contrôle |
| **04 — Épreuve** | Qu’est-ce qui le fait casser ? | stress tests, red team, ruptures, postmortems |
| **05 — Maîtrise** | Puis-je le défendre et le transférer ? | réplication, gouvernance, capstone |

---

<div align="center">
<svg width="160" height="14" viewBox="0 0 160 14" aria-hidden="true">
  <path d="M4 7h44m8 0h44m8 0h48" stroke="currentColor" stroke-width="1" stroke-linecap="round"/>
  <circle cx="52" cy="7" r="2.5" fill="none" stroke="currentColor" stroke-width="1"/>
  <circle cx="104" cy="7" r="2.5" fill="none" stroke="currentColor" stroke-width="1"/>
</svg>
</div>

## La règle d’or : la preuve gagne progressivement le droit d’exister

Une idée séduisante n’est pas encore une stratégie crédible.

```text
PHÉNOMÈNE
   ↓
POUVOIR PRÉDICTIF
   ↓
HORS ÉCHANTILLON
   ↓
APRÈS COÛTS
   ↓
SOUS STRESS
   ↓
EN TERRAIN
```

Le curriculum traite explicitement les pièges qui font passer un résultat de « joli » à « fragile » :

`data snooping` · `overfitting` · sélection ex post · biais de survivance · non-stationnarité · coûts · slippage · liquidité · risque opérationnel · corrélations · comportement humain.

**Une courbe d’equity n’est pas une preuve. C’est le début de l’enquête.**

---

## Une pédagogie qui oblige à faire

Chaque concept important suit autant que possible une boucle de travail :

```text
EXPLIQUER
   ↓
OBSERVER
   ↓
FAIRE
   ↓
MESURER
   ↓
CASSER
   ↓
COMPRENDRE L'ÉCHEC
   ↓
RÉVISER
```

Le dépôt utilise donc des :

**cartes** · **expériences** · **mini-projets** · **challenges** · **Boss** · **postmortems** · **ponts de transfert** · **grimoire**

L’objectif n’est pas de réciter une méthode. L’objectif est de produire quelque chose que tu peux **inspecter, tester, critiquer et défendre**.

---

## Le langage : technique, mais lisible

Un débutant ne devrait pas être arrêté par un acronyme qu’il n’a jamais rencontré.

Le principe de lecture du dépôt est donc :

```text
TERME TECHNIQUE
      ↓
explication simple
      ↓
analogie
      ↓
mécanisme réel
      ↓
expérience
      ↓
preuve
```

Les termes spécialisés sont accompagnés d’une explication lorsque nécessaire, sans retirer la précision du vocabulaire professionnel.

---

## Ce que tu vas réellement apprendre

### Marchés & microstructure

Actifs, places de marché, acteurs, carnet d’ordres, matching, liquidité, découverte des prix, ordres, exécution et coûts.

### Probabilités & risque

Rendements, distributions, espérance, variance, volatilité, drawdown, corrélation, risque de ruine, position sizing, scénarios et incertitude de modèle.

### Recherche & stratégies

Hypothèses falsifiables, momentum, trend following, mean reversion, pairs trading, facteurs, stratégies systématiques et lecture critique de l’analyse technique.

### Données & code

Données brutes, qualité, timestamps, biais de données, pipelines, règles reproductibles, backtests, validation et automatisation progressive.

### Validation

Hors-échantillon, walk-forward, tests multiples, data snooping, robustesse, coûts de transaction, stress tests, réplication et red team.

### Exécution & opérations

Sizing, exposition, slippage, liquidité, contrepartie, monitoring, contrôles, kill switch, incidents et procédures de survie.

### Psychologie observable

Loss aversion, overconfidence, disposition effect, FOMO, revenge trading, charge cognitive et conception de process qui réduit les décisions fragiles.

### Horizon 2035+

Automatisation, exécution algorithmique, données alternatives, IA, agents, gouvernance, résilience et compétences durables — en distinguant clairement **fait, tendance, scénario plausible et spéculation**.

---

## Ce que le dépôt refuse

```text
SETUP MAGIQUE              ✕
PROMESSE DE RENDEMENT      ✕
SECRET DE MARCHÉ           ✕
GRAPHIQUE = PREUVE        ✕
BACKTEST = FUTUR           ✕
IA = ORACLE                ✕
```

Une idée populaire peut être étudiée.
Une idée controversée peut être testée.
Une idée séduisante peut être mise à l’épreuve.

Mais **la popularité ne remplace jamais la preuve**.

---

## Commencer sans se perdre

### Itinéraire recommandé

```text
1. Ouvre le START HERE
        ↓
2. Comprends le terrain et le vocabulaire
        ↓
3. Suis le SOCLE
        ↓
4. Passe au CADRAGE
        ↓
5. Construis une première hypothèse
        ↓
6. Teste-la avant d'ajouter de la complexité
        ↓
7. Apprends à chercher ce qui pourrait l'invalider
        ↓
8. Monte progressivement vers l'automatisation
```

**Ne saute pas directement à une stratégie complexe parce qu’elle est plus impressionnante.**

Une bonne progression donne d’abord les moyens de comprendre pourquoi une méthode fonctionne, pourquoi elle échoue et dans quelles conditions elle cesse d’être crédible.

---

<div align="center">
<svg width="150" height="16" viewBox="0 0 150 16" aria-hidden="true">
  <path d="M8 8h32m12 0h32m12 0h38" stroke="currentColor" stroke-width="1" stroke-linecap="round"/>
  <path d="M40 5v6m52-6v6" stroke="currentColor" stroke-width="1" stroke-linecap="round"/>
</svg>
</div>

## Une architecture faite pour durer

Les outils changent vite. Les contraintes fondamentales changent moins vite.

```text
OUTILS                     → changent
PLATEFORMES                → changent
LIBRAIRIES                 → changent
MODÈLES                    → changent

MÉCANIQUE DU MARCHÉ        → beaucoup plus stable
PROBABILITÉ                → stable
GESTION DU RISQUE          → stable
RIGUEUR EXPÉRIMENTALE      → stable
DISCIPLINE DES DONNÉES     → stable
CAPACITÉ À DÉTECTER L'ERREUR → indispensable
```

C’est pourquoi le curriculum vise davantage les **invariants** que la mémorisation d’un stack logiciel particulier.

---

## Navigation

| Besoin | Entrée |
|---|---|
| **Je pars de zéro** | [`06-ANNEXES-TRANSVERSES/00-GUIDE.md`](06-ANNEXES-TRANSVERSES/00-GUIDE.md) |
| **Je veux le parcours complet** | [`PROGRESSION.md`](PROGRESSION.md) |
| **Je veux installer l’environnement** | [`SETUP.md`](SETUP.md) |
| **Je veux comprendre le Socle** | [`00-SOCLE/`](00-SOCLE/) |
| **Je veux commencer la progression** | [`01-CADRAGE/`](01-CADRAGE/) |
| **Je veux construire et tester** | [`02-CONSTRUCTION/`](02-CONSTRUCTION/) |
| **Je veux apprendre le pilotage** | [`03-PILOTAGE/`](03-PILOTAGE/) |
| **Je veux éprouver un système** | [`04-EPREUVE/`](04-EPREUVE/) |
| **Je veux aller vers la maîtrise** | [`05-MAITRISE/`](05-MAITRISE/) |
| **Je veux utiliser les annexes transverses** | [`06-ANNEXES-TRANSVERSES/`](06-ANNEXES-TRANSVERSES/) |

---

## La question à garder pendant tout le parcours

> **« Qu’est-ce qui me ferait changer d’avis ? »**

C’est une meilleure protection contre les illusions de maîtrise que n’importe quel indicateur supplémentaire.

<div align="center">

**Trading Architecte**

*Pas apprendre à prédire. Apprendre à construire des décisions qui restent défendables quand la prédiction échoue.*

</div>
