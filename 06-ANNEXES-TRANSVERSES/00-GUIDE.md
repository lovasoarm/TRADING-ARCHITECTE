---
stability: mixte - fondamentaux durables, marché et outils périssables
---

# 00-GUIDE : Tu ne sais pas quoi faire ? Commence ici.

> **Version CrazyDevs : Trading Architecte**
>
> Ce guide n'est pas un dictionnaire de trading avec une cravate.
> C'est une carte de terrain pour quelqu'un qui arrive devant un graphique,
> voit 300 indicateurs, 50 influenceurs, 20 marchés, des bougies partout,
> des mots comme _spread_, _leverage_, _alpha_, _drawdown_, _backtest_, _options_,
> et pense :
>
> **« D'accord… mais je commence par quoi ? »**
>
> Respire. On remet les pièces dans le bon ordre.

Temps de lecture : environ 100 minutes. Lis-le en plusieurs sessions.
Ce document est une boussole transversale : il t'explique **comment entrer dans le domaine**, comment choisir ton prochain pas, comment survivre aux zones de jargon et comment continuer seul.

---

## Sommaire

0. [Tu pars de zéro ? Lis ceci d’abord](#0-tu-pars-de-zéro--lis-ceci-dabord)
1. [C’est quoi, le trading ?](#1-cest-quoi-le-trading)
2. [Les grands marchés et instruments](#2-les-grands-marchés-et-instruments)
3. [Comment fonctionne un marché, vraiment ?](#3-comment-fonctionne-un-marché-vraiment)
4. [Les mots qu’on voit partout](#4-les-mots-quon-voit-partout)
5. [Débutant : par où commencer ?](#5-débutant--par-où-commencer)
6. [J’ai une idée de stratégie : que faire maintenant ?](#6-jai-une-idée-de-stratégie--que-faire-maintenant)
7. [Les vérités que l'on dit rarement au début](#7-les-vérités-que-lon-dit-rarement-au-début)
8. [Le risque, l'argent et la vraie difficulté](#8-le-risque-largent-et-la-vraie-difficulté)
9. [Le terrain : manuel, systématique, quantitatif](#9-le-terrain--manuel-systématique-quantitatif)
10. [L'IA : assistant, multiplicateur, danger](#10-lia--assistant-multiplicateur-danger)
11. [2035+ : apprendre des invariants](#11-2035--apprendre-des-invariants)
12. [Ton parcours complet](#12-ton-parcours-complet)
13. [Quand tu bloques](#13-quand-tu-bloques)
14. [Grimoire ultra-débutant](#14-grimoire-ultra-débutant)
15. [Challenge final du guide](#15-challenge-final-du-guide)
16. [Sources et entretien du guide](#16-sources-et-entretien-du-guide)

---

# 0. Tu pars de zéro ? Lis ceci d’abord

Bienvenue.

Tu n'as pas besoin d'être bon en maths au départ.
Tu n'as pas besoin d'avoir 10 000 € à trader.
Tu n'as pas besoin de connaître Python avant le jour 1.
Tu n'as pas besoin de savoir ce qu'est une bougie japonaise.
Tu n'as certainement pas besoin de mémoriser 80 indicateurs.

Tu as besoin d'un **premier pas assez petit pour être terminé**.

## 0.1 Le problème du débutant

Le débutant voit souvent ceci :

```text
                         TRADING
                            |
        +-------------------+-------------------+
        |                   |                   |
      ACTIONS             FOREX             CRYPTO
        |                   |                   |
      FUTURES            OPTIONS            DEFI
        |                   |                   |
   INDICATEURS          PRICE ACTION        NEWS
        |                   |                   |
   RSI MACD ATR          SMC FVG OB         MACRO
        |                   |                   |
      PYTHON             MT5 / TV           API
        |                   |                   |
      ML / IA            LLM / AGENTS       QUANTS
```

Son cerveau traduit :

> « Je dois tout apprendre avant de faire quoi que ce soit. »

Non.

La carte utile ressemble plutôt à ceci :

```text
                 UNE QUESTION
                      |
                      v
                 OBSERVATION
                      |
                      v
                 HYPOTHÈSE
                      |
                      v
                    TEST
                      |
               +------+------+
               |             |
             ÉCHEC          SIGNAL
               |             |
               +------+------+
                      |
                      v
                  MESURE
                      |
                      v
                   RISQUE
                      |
                      v
                  DÉCISION
                      |
                      v
                 BOUCLE SUIVANTE
```

Tu n'apprends donc pas « le trading » comme une liste infinie de chapitres.
Tu apprends une **machine de décision** qui se spécialise progressivement.

## 0.2 Le vrai premier objectif

Pas :

> « Devenir rentable en 30 jours. »

Pas :

> « Trouver LA stratégie secrète. »

Mais :

> **devenir capable d’apprendre le marché sans devenir dépendant d’un vendeur de certitude.**

Tu dois progressivement savoir faire cette boucle :

```text
Je ne sais pas
    ↓
Je précise la question
    ↓
Je trouve la définition minimale
    ↓
J'observe une donnée réelle
    ↓
Je fais un petit calcul
    ↓
Je teste une hypothèse
    ↓
Je me trompe / je découvre une limite
    ↓
Je documente ce qui a changé
    ↓
Je recommence
```

C'est déjà du travail d'ingénieur et de chercheur.

## 0.3 Ce que tu peux faire sans argent

Le premier entraînement est conçu pour fonctionner avec **zéro capital**.

```text
         APPRENDRE
             ↓
      données historiques
             ↓
       observation / papier
             ↓
        simulation simple
             ↓
     validation reproductible
             ↓
    seulement ensuite : réel
```

Le dépôt n'a pas besoin d'un dépôt chez un broker pour être utile.
Au contraire : **le débutant qui risque son argent trop tôt reçoit un feedback émotionnel beaucoup plus violent que son feedback pédagogique**.

## 0.4 Ce que le mot « trader » cache

Un trader peut être :

- quelqu'un qui prend quelques décisions discrétionnaires sur des actions ;
- un opérateur d'exécution ;
- un market maker ;
- un arbitragiste ;
- un systematic trader ;
- un quant researcher ;
- un gestionnaire de portefeuille ;
- un ingénieur qui construit l'infrastructure de décision et d'exécution.

Ces métiers partagent une même matière première : **prix, incertitude, risque, exécution, information**.
Ils n'ont pas les mêmes méthodes.

## 0.5 La règle « un noyau, plusieurs spécialisations »

Le noyau est :

```text
probabilités
    +
lecture des données
    +
mécanique des marchés
    +
gestion du risque
    +
validation
    +
décision
```

Puis tu spécialises :

```text
                 NOYAU
                   |
       +-----------+-----------+
       |           |           |
     MACRO       QUANT       EXÉCUTION
       |           |           |
      FX        FACTEURS      LOB
                 / ML       MICROSTRUCTURE
```

Ce que tu dois **éviter** : choisir une spécialité avant de savoir pourquoi elle existe.

## 0.6 Ton test d’entrée

Avant de poursuivre, réponds sans regarder les réponses dans le reste du dépôt :

1. Qu'est-ce qu'un prix ?
2. Pourquoi un trade gagnant n'est-il pas une preuve de stratégie ?
3. Que représente un spread ?
4. Qu'est-ce qu'un drawdown ?
5. Pourquoi un stop-loss ne garantit-il pas toujours la perte prévue ?
6. Qu'est-ce qu'une hypothèse falsifiable ?
7. Pourquoi un backtest parfait peut-il être suspect ?
8. Quelle différence entre risque et incertitude ?

Tu peux répondre « je ne sais pas » à huit reprises. C'est un excellent point de départ.

---

# 1. C’est quoi le trading ?

## 1.1 Une définition simple

Le trading consiste à prendre des positions sur des instruments financiers avec un horizon et des règles d'exposition donnés, en acceptant que le résultat futur soit incertain.

Cette phrase paraît banale. Elle contient déjà quatre idées essentielles :

```text
POSITION  → tu es exposé
HORIZON   → le temps compte
RÈGLE     → la décision doit être explicable
INCERTITUDE → le résultat n'est pas garanti
```

## 1.2 Trading ≠ prédiction parfaite

Une stratégie peut être utile sans prédire correctement chaque mouvement.

Exemple conceptuel :

```text
10 opérations

+2R  +2R  -1R  -1R  -1R  +3R  -1R  -1R  +2R  -1R

Résultat net = positif

mais

6 opérations perdantes / 4 gagnantes
```

Ici, compter seulement le **win rate** donne une information incomplète.

La question utile devient :

> Quelle distribution des gains et pertes, après coûts et risques, produit ce résultat ?

## 1.3 Trading, investissement, couverture, arbitrage

Ces activités peuvent utiliser les mêmes marchés mais pas le même objectif.

```text
INVESTIR   → détenir une exposition de long terme
TRADER     → gérer une exposition dans le temps
COUVRIR    → réduire un risque existant
ARBITRER   → exploiter une incohérence relative de prix
FAIRE DU MARCHÉ → fournir de la liquidité contre compensation attendue
```

Un débutant fait souvent une erreur de catégorie : il prend une technique conçue pour l'un de ces objectifs et l'utilise pour un autre.

## 1.4 Le marché n'est pas ton adversaire personnel

Un récit populaire dit :

> « Le marché a vu mon stop et est venu le chercher. »

Une lecture mécanique plus rigoureuse demande :

```text
Quels ordres étaient disponibles ?
Quelle liquidité existait ?
Quelle règle de matching ?
Quel impact de l'ordre ?
Quel événement d'information ?
Quel coût d'exécution ?
```

La recherche préparatoire du cursus distingue précisément le récit anthropomorphique du mécanisme de liquidité, d'impact et de matching.

---

# 2. Les grands marchés et instruments

## 2.1 Actions

Une action représente une part de propriété économique d'une entreprise. Pour le trader, les dimensions pratiques sont notamment : liquidité, horaires de marché, volatilité, coûts, corporate actions et risque spécifique.

Analogie :

> Une action est comme une propriété fractionnée : le marché te permet d'échanger ton droit économique, pas de commander directement l'entreprise.

## 2.2 Obligations

Une obligation est une créance. Les intuitions débutantes sont souvent trompeuses car le prix d'une obligation et son rendement évoluent de manière liée mais inverse dans le cadre simple d'une obligation classique.

## 2.3 Forex

Le FX traite des paires de monnaies. L'apprenant doit rapidement comprendre qu'une paire est **relative** : EUR/USD en hausse signifie que l'euro s'apprécie relativement au dollar selon la convention de cotation.

## 2.4 Futures

Un future est un contrat standardisé échangé sur un marché organisé. Il offre une exposition importante pour une mise de marge bien plus petite que la valeur notionnelle. C'est précisément pourquoi la gestion du levier est fondamentale.

## 2.5 Options

Une option donne un droit, pas une obligation, dans le cadre de son contrat. Le débutant doit apprendre au minimum : strike (prix d'exercice), maturité (date d'échéance), prime (prix de l'option) et volatilité implicite (niveau de volatilité reflété par le prix).

## 2.6 Crypto-actifs

Les crypto-actifs ajoutent notamment une dimension 24/7, une fragmentation des venues, des mécanismes on-chain et des risques spécifiques de plateforme et de contrat intelligent.

## 2.7 Spot vs dérivé

```text
SPOT
  → exposition à l'actif lui-même ou à son marché au comptant

DÉRIVÉ
  → contrat dont la valeur dépend d'un sous-jacent
```

Ne suppose pas que les deux ont les mêmes risques opérationnels ni le même mécanisme de prix.

## 2.8 Comment choisir ton premier terrain

Pour un débutant, préfère d'abord un environnement :

```text
liquide
+ données accessibles
+ mécanisme compréhensible
+ coûts documentables
+ possibilité de simuler
```

Tu n'as aucun besoin de commencer par l'instrument le plus exotique.

---

# 3. Comment fonctionne un marché, vraiment ?

## 3.1 L'idée la plus importante

Un graphique est une **reconstruction** d'événements de marché.

La chaîne utile à retenir est :

```text
INFORMATION
    ↓
DÉCISION
    ↓
ORDRE
    ↓
ROUTAGE
    ↓
CARNET / VENUE
    ↓
MATCHING
    ↓
EXÉCUTION
    ↓
PRIX DIFFUSÉ
    ↓
TON P&L
```

L'ordre n'est donc pas « je clique et le prix devient mon prix ».

## 3.2 Bid, ask et spread

**Bid (prix acheteur)** : meilleur prix visible auquel un acheteur est prêt à acheter.  
**Ask (prix vendeur)** : meilleur prix visible auquel un vendeur est prêt à vendre.  
**Spread** : écart entre les deux.

```text
BID        | SPREAD | ASK
  99.99     |  0.02  | 100.01
```

L'écart est une friction réelle. Dans beaucoup de stratégies rapides, il peut suffire à transformer une petite intuition positive en résultat net nul.

## 3.3 Ordre au marché vs ordre limite

**Market order (ordre au marché)** : priorité à l'exécution plutôt qu'au prix exact.

**Limit order (ordre à cours limité)** : tu spécifies le prix limite accepté. L'ordre peut ne pas être exécuté.

Analogie :

```text
MARKET → « donne-moi une place maintenant »
LIMIT  → « donne-moi une place seulement à ce prix ou mieux »
```

## 3.4 Pourquoi ton prix théorique n'est pas ton prix réel

Entre le modèle et la réalité interviennent :

- spread ;
- profondeur disponible ;
- slippage (prix exécuté différent du prix attendu) ;
- impact ;
- frais ;
- latence ;
- règles de venue ;
- gaps ;
- erreurs opérationnelles.

Le guide de risque du cursus formalise cette différence entre risque au stop et perte réellement réalisée.

## 3.5 Le carnet d'ordres n'est pas une boule de cristal

Le carnet visible montre une partie de la liquidité disponible, pas nécessairement toute la liquidité économique. Des ordres cachés, conditionnels ou d'autres venues peuvent changer le tableau.

## 3.6 Pourquoi « le prix a monté » n'est pas une explication

« Le prix a monté parce que les acheteurs étaient plus nombreux » est souvent trop vague.

La question pédagogique utile est :

> Quels ordres ont traversé quelles couches de liquidité, avec quelle information, quelle agressivité et quel déséquilibre ?

Tu passes alors du commentaire de graphique à la mécanique du marché.

---

# 4. Les mots qu’on voit partout

## 4.1 La règle du traducteur

Quand un terme nouveau apparaît :

```text
TERME
  ↓
FRANÇAIS SIMPLE
  ↓
ANALOGIE
  ↓
MÉCANISME RÉEL
  ↓
MESURE
  ↓
LIMITE
```

Une définition sans mécanisme est fragile. Une analogie sans limite devient un mythe.

## 4.2 Le premier dictionnaire

| Mot                    | Français simple                                            | Analogie                                             | Ce qu'il ne faut pas conclure                |
| ---------------------- | ---------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------- |
| actif                  | instrument exposé au marché                                | objet dans un inventaire                             | qu'il est automatiquement rentable           |
| broker (intermédiaire) | accès/acheminement vers le marché                          | guichet                                              | qu'il garantit un prix                       |
| bid                    | meilleur prix acheteur visible                             | prix proposé par le client en face                   | qu'il représente toute la demande            |
| ask                    | meilleur prix vendeur visible                              | prix demandé au guichet                              | qu'il représente toute l'offre               |
| spread                 | écart bid-ask                                              | marge entre deux guichets                            | qu'il est toujours fixe                      |
| liquidité              | facilité à transacter                                      | profondeur d'une file                                | qu'elle survit intacte en crise              |
| slippage               | écart entre attendu et exécuté                             | sol glissant                                         | qu'il est nul si tu utilises un stop         |
| levier                 | exposition amplifiée                                       | conduire une machine plus grande avec la même pédale | qu'il augmente ton edge                      |
| marge                  | garantie pour porter l'exposition                          | caution                                              | qu'elle limite toujours la perte finale      |
| rendement              | variation de valeur                                        | compteur de progression                              | qu'il mesure le risque seul                  |
| volatilité             | amplitude des variations                                   | route cahoteuse                                      | qu'elle prédit la direction                  |
| drawdown               | perte depuis un sommet                                     | descente depuis une crête                            | qu'il est identique à la volatilité          |
| backtest               | simulation historique                                      | replay d'un match                                    | qu'il prouve le futur                        |
| alpha                  | performance excédentaire relative à une référence          | bonus au-dessus d'une ligne de base                  | qu'il est permanent                          |
| beta                   | exposition à une variation de référence                    | sensibilité de la voiture à la route                 | qu'il est mauvais ou bon en soi              |
| edge                   | avantage statistique ou économique attendu                 | petit biais de la balance                            | qu'il garantit chaque trade                  |
| stop-loss              | règle de sortie prévue                                     | porte coupe-feu                                      | qu'elle fixe toujours la perte finale        |
| position sizing        | taille décidée selon le risque                             | taille du sac à dos                                  | qu'il suffit à rendre une stratégie bonne    |
| expectancy             | gain/perte moyen pondéré par les probabilités              | score moyen d'une machine de jeu                     | qu'elle reste stable                         |
| Sharpe                 | rendement excédentaire rapporté à une mesure de volatilité | vitesse par rapport aux cahots                       | qu'il suffit pour juger une stratégie        |
| regime                 | environnement de marché                                    | météo du terrain                                     | qu'il est visible à l'œil nu                 |
| overfitting            | ajustement excessif aux données passées                    | mémoriser le sujet au lieu d'apprendre la matière    | qu'il nécessite un modèle complexe           |
| look-ahead bias        | utiliser une information future                            | tricher avec la correction                           | qu'il est toujours évident                   |
| survivorship bias      | oublier les actifs disparus                                | ne regarder que les survivants                       | qu'un historique propre est forcément fidèle |
| execution              | transformation de la décision en transaction réelle        | passage du plan au terrain                           | qu'elle soit instantanée                     |

## 4.3 Les abréviations qui terrorisent les débutants

Tu verras souvent :

```text
OHLCV   → Open, High, Low, Close, Volume
ATR     → Average True Range (mesure d'amplitude de mouvement)
VWAP    → Volume Weighted Average Price (prix moyen pondéré par volume)
VWMA    → Volume Weighted Moving Average
P&L     → Profit and Loss (profit et perte)
VaR     → Value at Risk (mesure quantile de perte sous hypothèses)
ES      → Expected Shortfall (perte moyenne au-delà d'un seuil quantile)
LOB     → Limit Order Book (carnet d'ordres à cours limité)
HFT     → High-Frequency Trading (trading à très haute fréquence)
ML      → Machine Learning
LLM     → Large Language Model
RAG     → Retrieval-Augmented Generation
API     → Application Programming Interface
OOS     → Out-of-Sample (hors échantillon utilisé pour construire)
DSR     → Deflated Sharpe Ratio
PBO     → Probability of Backtest Overfitting
```

Tu n'as pas besoin de mémoriser cette liste. Tu dois apprendre à **reconnaître le mot et savoir où demander l'explication suivante**.

---

# 5. Débutant : par où commencer ?

## 5.1 Le chemin recommandé

Le meilleur chemin n'est pas « regarder 100 heures de contenu ».

C'est :

```text
0. ORIENTER
   ↓
1. COMPRENDRE LES MARCHÉS
   ↓
2. COMPRENDRE LE RISQUE
   ↓
3. OBSERVER LES DONNÉES
   ↓
4. FORMULER UNE HYPOTHÈSE
   ↓
5. CONSTRUIRE UNE RÈGLE
   ↓
6. BACKTESTER SANS SE MENTIR
   ↓
7. CASSER LE BACKTEST
   ↓
8. GÉRER L'EXPOSITION
   ↓
9. COMPRENDRE L'EXÉCUTION
   ↓
10. PORTER LE SYSTÈME SUR UN AUTRE TERRAIN
```

C'est précisément pourquoi le parcours principal est découpé en **Cadrage → Construction → Pilotage → Épreuve → Maîtrise**.

## 5.2 Pourquoi ne pas commencer par une stratégie ?

Parce que la première stratégie que tu trouves sur internet est presque toujours présentée **après coup**.

Le récit classique :

```text
voilà le setup
    ↓
voilà 7 exemples gagnants
    ↓
voilà la courbe
    ↓
achète le cours
```

Le récit ARCHITECTE-FANTOME :

```text
voilà le problème
    ↓
voilà l'hypothèse
    ↓
voilà ce qui devrait être observé si elle est vraie
    ↓
voilà comment on la teste
    ↓
voilà ce qui la réfuterait
    ↓
voilà ce qui survit
```

## 5.3 Les quatre niveaux de compréhension

Un concept est considéré comme vraiment acquis lorsque tu peux :

**Niveau 1 : reconnaître** : tu sais que le mot existe.  
**Niveau 2 : expliquer** : tu peux le dire sans copier la définition.  
**Niveau 3 : mesurer** : tu peux construire une observation ou un calcul.  
**Niveau 4 : défendre** : tu peux expliquer quand le concept échoue et quoi faire alors.

```text
RECONNAÎTRE → EXPLIQUER → MESURER → DÉFENDRE
```

Ne confonds jamais lecture fluide et compétence.

## 5.4 Les 30 premiers jours

### Jours 1–7 : vocabulaire + marché

Objectif : pouvoir expliquer vingt mots sans jargon.

### Jours 8–14 : risque + rendement

Objectif : calculer rendement, perte, gain de récupération, drawdown et taille de position simple.

### Jours 15–21 : données

Objectif : lire un petit jeu de données OHLCV, détecter les anomalies évidentes et produire des statistiques descriptives.

### Jours 22–30 : hypothèse

Objectif : écrire une hypothèse falsifiable et une première règle volontairement simple.

Tu n'as toujours pas besoin de capital réel.

## 5.5 Quand apprendre Python ?

Dès que tu atteins le point où le calcul manuel devient répétitif ou source d'erreurs.

Pas :

> « Il faut apprendre Python avant de toucher au trading. »

Mais :

> « J'ai une question que 30 lignes de calcul peuvent mesurer. »

C'est une excellente raison d'apprendre Python.

## 5.6 Quand apprendre les maths ?

Même principe.

Tu peux commencer par :

```text
pourcentages
→ fractions
→ moyenne
→ dispersion
→ probabilité
→ statistique descriptive
→ estimation
→ intervalles
→ tests
→ modèles
```

Ne saute pas directement à une équation complexe parce qu'elle semble prestigieuse.

---

# 6. J’ai une idée de stratégie : que faire maintenant ?

## 6.1 Étape 1 : transformer le slogan en hypothèse

Mauvais :

> « Quand le RSI est sous 30, il faut acheter. »

Meilleur :

> « Dans tel univers et sous telles conditions de régime, un signal de momentum extrême modifie-t-il suffisamment la distribution conditionnelle des rendements futurs pour couvrir les coûts et le risque ? »

Tu viens de passer d'un slogan à une hypothèse.

## 6.2 Étape 2 : définir ce qui te ferait perdre

Une hypothèse sérieuse contient une sortie possible :

```text
HYPOTHÈSE
   ↓
PRÉDICTION
   ↓
MESURE
   ↓
SEUIL DE SUCCÈS
   ↓
CRITÈRE D'ÉCHEC
```

Sans critère d'échec, tu peux toujours réinterpréter les résultats pour sauver l'idée.

## 6.3 Étape 3 : choisir une baseline

Une baseline est une référence simple contre laquelle comparer.

Exemples conceptuels :

```text
stratégie A vs buy-and-hold
stratégie A vs cash
stratégie A vs momentum simple
modèle ML vs règle heuristique simple
```

Si ton modèle sophistiqué ne bat qu'une baseline volontairement médiocre, tu n'as pas démontré grand-chose.

## 6.4 Étape 4 : commencer volontairement naïf

Le premier modèle doit être **suffisamment simple pour être compris ligne par ligne**.

Pourquoi ?

Parce que lorsque le résultat est étrange, tu veux pouvoir remonter la chaîne causale.

## 6.5 Étape 5 : calculer les coûts avant de célébrer

Un backtest sans coûts est une maquette.

Les coûts possibles incluent :

```text
spread
commission
slippage
impact
financement
borrow
latence
frais spécifiques
```

Une amélioration de stratégie qui disparaît après friction n'est pas une erreur de comptabilité : c'est une information sur la qualité économique de l'edge.

## 6.6 Étape 6 : tenter de casser le résultat

Pose au système les questions les plus hostiles :

```text
Et si j'avance le signal d'une barre ?
Et si je retire les 10 meilleurs trades ?
Et si les coûts doublent ?
Et si les paramètres bougent de ±20 % ?
Et si le marché change de régime ?
Et si l'univers des actifs change ?
Et si le fournisseur de données introduit un biais ?
```

Tu n'es pas en train de détruire la stratégie.
Tu cherches à mesurer **combien elle dépend de circonstances particulières**.

## 6.7 Étape 7 : seulement ensuite augmenter la sophistication

```text
règle simple
   ↓
plus de données
   ↓
validation hors échantillon
   ↓
meilleur modèle de coûts
   ↓
robustesse
   ↓
portfolio / exécution
   ↓
automation
```

Jamais :

```text
problème flou
   ↓
deep learning
   ↓
17 hyperparamètres
   ↓
beau graphique
   ↓
« alpha »
```

---

# 7. Les vérités que l'on dit rarement au début

## 7.1 Un taux de réussite élevé peut être mauvais

Exemple :

```text
19 gains de +0,2R = +3,8R
1 perte de -8R     = -8R
-----------------------------
Net                  = -4,2R
```

Le débutant voit 95 % de trades gagnants.

Le praticien voit une distribution asymétrique catastrophique.

## 7.2 Une stratégie peut être bonne et devenir mauvaise

Les marchés évoluent.
Les coûts évoluent.
La concurrence évolue.
Le comportement des autres participants évolue.

Certaines anomalies sont exploitées jusqu'à leur dégradation. Les recherches préparatoires du cursus soulignent notamment l'anomaly decay et la différence entre effet réel arbitragé et artefact de data mining. fileciteturn1file1L58-L63

Donc :

> **Une stratégie n'est jamais promue au rang de loi physique simplement parce qu'elle a bien fonctionné.**

## 7.3 Un backtest impressionnant est parfois un signal d'alarme

Un résultat trop beau pour être vrai peut révéler :

- fuite de données ;
- sélection a posteriori ;
- univers biaisé ;
- coûts sous-estimés ;
- données survivantes seulement ;
- sur-ajustement ;
- répétition massive de tests ;
- bug de code.

La question n'est pas « quelle est la performance ? » mais :

> « Combien d'hypothèses cachées ont été nécessaires pour l'obtenir ? »

## 7.4 Le marché ne te doit pas de régularité

Une stratégie peut subir 10 pertes consécutives sans être nécessairement morte.
Une stratégie peut gagner 10 fois sans être nécessairement bonne.

Le bon outil est une analyse de distribution, pas une humeur sur une petite séquence.

## 7.5 Psychologie ≠ « avoir du mental »

Une décision humaine s'améliore souvent plus facilement en réduisant le nombre de décisions dangereuses qu'en donnant à la personne un discours sur la discipline.

```text
RÈGLE CLAIRE
   +
SIZING MAÎTRISÉ
   +
LIMITES
   +
AUTOMATISATION LÀ OÙ UTILE
   +
JOURNAL
   ↓
MOINS D'ERREURS ÉVITABLES
```

Le corpus de recherche sur la psychologie insiste ainsi sur la différence entre « faiblesse morale » et architecture de décision : la charge cognitive, la perte, le regret et l'overconfidence modifient les comportements.

## 7.6 Le « secret » le plus utile est souvent ennuyeux

Des choses très peu sexy dominent souvent les résultats :

```text
données propres
+ bon timing
+ coûts réalistes
+ sizing
+ discipline de recherche
+ contrôle opérationnel
```

Le trading spectaculaire est visible sur internet. Le trading robuste est souvent invisible.

---

# 8. Le risque, l'argent et la vraie difficulté

## 8.1 Le risque avant le rendement

Le cursus traite le risque comme un système, pas comme une phrase « place un stop ».

```text
Risque statistique
Risque marché
Risque levier
Risque liquidité
Risque contrepartie
Risque modèle
Risque opérationnel
Risque comportemental
Risque de queue
```

## 8.2 Position sizing

Pour une position linéaire, une forme simple de raisonnement est :

```text
taille ≈ risque monétaire accepté
         -------------------------
         distance jusqu'à invalidation × valeur d'unité
```

Le point crucial pour un débutant :

> **Le sizing décide de combien une erreur coûte ; la stratégie décide seulement de ce qu'elle essaie de capter.**

## 8.3 Drawdown

Le drawdown est la baisse depuis un sommet antérieur.

```text
Sommet
  |
  |\
  | \
  |  \
  |   \
  |    \
  +-----Creux
        ↓
      DRAWdown
```

La récupération n'est pas symétrique :

```text
-10% → +11,1% pour revenir
-25% → +33,3%
-50% → +100%
-75% → +300%
```

C'est l'une des raisons pour lesquelles la survie n'est pas une rubrique administrative.

## 8.4 Le levier ne crée pas d'edge

Levier = amplificateur.

```text
EDGE  ×  LEVIER  → amplification du résultat
                   dans les deux directions
```

Si ton edge est nul, le levier ne le transforme pas magiquement en edge positif.

## 8.5 Stop-loss : ce qu'il fait et ce qu'il ne fait pas

Un stop est une **règle d'invalidation ou de réduction d'exposition**.

Il ne garantit pas toujours un prix de sortie exact en présence d'un gap ou d'un marché sans liquidité suffisante.

## 8.6 Le bon objectif pour un débutant

Au début, mesure plutôt :

```text
Est-ce que j'applique correctement mon protocole ?
Est-ce que je comprends mes erreurs ?
Est-ce que mon sizing respecte le budget de risque ?
Est-ce que mes résultats sont reproductibles ?
```

La « rentabilité rapide » est une métrique dangereuse comme objectif pédagogique.

---

# 9. Le terrain : manuel, systématique, quantitatif

## 9.1 Trading discrétionnaire

Décisions humaines en temps réel à partir d'un cadre.

Forces potentielles : adaptation contextuelle.

Risques : incohérence, biais, fatigue, mémoire sélective.

## 9.2 Trading systématique

Les règles sont suffisamment précises pour être appliquées de façon répétable.

```text
entrée
+ filtre
+ sizing
+ sortie
+ gestion du risque
= système
```

## 9.3 Quant research

Le chercheur quantitatif essaie de transformer une idée économique en hypothèse mesurable puis en protocole statistique.

La différence majeure n'est pas « plus de maths ». C'est souvent **plus de contrôle sur ce qui constitue une preuve**.

## 9.4 Microstructure / exécution

Ici tu cherches à comprendre la chaîne physique qui transforme la décision en transaction.

La recherche préparatoire du cursus résume cette chaîne en sept maillons : décision, ordre, routage, carnet, matching, exécution, diffusion. fileciteturn0file4L7-L20

## 9.5 Les faux clivages

Ne transforme pas :

```text
« price action » VS « quant »
« macro » VS « microstructure »
« manuel » VS « Python »
```

Ces familles répondent à des questions différentes.

Le professionnel capable de passer d'une représentation à une autre possède souvent plus de leviers :

```text
macro
  ↓
mécanisme
  ↓
données
  ↓
règle
  ↓
exécution
  ↓
risque
```

## 9.6 Comment savoir ton terrain

Tu tends vers :

**Discrétionnaire** si tu aimes l'interprétation et la décision contextuelle.  
**Systématique** si tu veux des règles explicites et reproductibles.  
**Quant** si tu veux pousser la mesure, l'inférence et la recherche.  
**Exécution** si les détails du marché, de la liquidité et du coût te passionnent.  
**Portfolio** si tu préfères raisonner en interactions d'expositions plutôt qu'en trade isolé.

Tu peux changer plus tard.

---

# 10. L'IA : assistant, multiplicateur, danger

## 10.1 Ce que l'IA peut faire

Une IA peut aider à :

```text
expliquer un concept
produire un brouillon de code
suggérer des tests
résumer une source
transformer des notes
générer des variantes d'une hypothèse
chercher des erreurs évidentes
```

## 10.2 Ce qu'elle ne doit pas recevoir sans contrôle

```text
la décision finale non auditée
la confiance sans vérification
la responsabilité du risque
la preuve du backtest
la définition de la vérité
```

## 10.3 Le piège de l'IA en trading

Un LLM est excellent pour produire de nombreuses idées.

Et c'est justement le problème.

```text
1 idée
  ↓
5 variantes
  ↓
50 variantes
  ↓
500 variantes
  ↓
« une doit forcément marcher »
```

Tu viens d'augmenter ton exposition au **data mining**.

Le document de recherche du projet souligne explicitement que la génération automatisée de nombreux candidats alpha peut reproduire le problème du factor zoo si les corrections pour tests multiples et la validation robuste sont absentes. fileciteturn1file5L203-L213

## 10.4 Le bon protocole

Quand l'IA t'aide :

```text
QUESTION
 ↓
PROPOSITION IA
 ↓
VÉRIFICATION HUMAINE
 ↓
TEST INDÉPENDANT
 ↓
MESURE
 ↓
ACCEPTATION / REJET
```

## 10.5 Les quatre usages les plus sains pour débuter

**Tuteur** : « explique-moi ce mot comme à un lycéen ».  
**Adversaire** : « donne-moi trois raisons pour lesquelles mon hypothèse peut être fausse ».  
**Débogueur** : « voici une erreur précise ; aide-moi à localiser la cause ».  
**Scribe** : « transforme mon expérience en compte rendu clair ».

Utilise moins l'IA comme **oracle**, davantage comme **multiplicateur de réflexion**.

## 10.6 Le test anti-dépendance

Demande-toi :

> « Si cet outil disparaît demain, suis-je toujours capable d'expliquer mon système ? »

Si la réponse est non, tu possèdes un workflow fragile.

---

# 11. 2035+ : apprendre des invariants

## 11.1 Pense en scénarios, pas en prédictions

Personne ne peut donner au débutant un script fiable du marché de 2035.

On peut en revanche demander :

```text
Quelles contraintes sont probablement durables ?
Quels outils sont probablement remplaçables ?
Quelles compétences sont transférables ?
Quels risques nouveaux peuvent émerger ?
```

## 11.2 Les invariants probables

Même avec plus d'automatisation, le praticien devra toujours composer avec :

```text
incertitude
liquidité
coût
régime
risque
contraintes opérationnelles
responsabilité
```

## 11.3 Ce qui peut devenir plus automatisé

```text
collecte / nettoyage standardisé
synthèse documentaire
génération de code de routine
monitoring répétitif
exécution sous contraintes
recherche de candidats
```

## 11.4 Ce qui gagne en valeur

```text
formulation du problème
choix des hypothèses
validation
architecture de contrôle
gestion de l'incertitude
compréhension du mécanisme
communication
capacité à changer de cadre
```

La recherche prospective fournie pour Trading Architecte arrive à une conclusion proche : former des architectes de systèmes plutôt que de simples utilisateurs d'outils, avec un accent sur la résilience, la gouvernance, le risk management temps réel et la capacité d'adaptation. fileciteturn1file8L325-L334

## 11.5 L'erreur 2035 classique

Mauvaise préparation :

> « J'apprends aujourd'hui le logiciel qui existera encore en 2035. »

Meilleure préparation :

> **« J'apprends les mécanismes qui me permettront d'apprendre le prochain logiciel. »**

---

# 12. Ton parcours complet

## 12.1 La carte générale

```text
00 SOCLE
│
├── orientation
├── vocabulaire
├── première observation
└── première preuve

01 CADRAGE
│
├── réalité du trading
├── marché / participants
├── prix vs signal
├── psychologie observable
└── hypothèse

02 CONSTRUCTION
│
├── strategy engineering
├── données
├── backtest
├── biais de validation
├── sizing
└── coûts

03 PILOTAGE
│
├── portefeuille
├── stress
├── exécution
├── régimes
└── contrôles

04 ÉPREUVE
│
├── validation avancée
├── recherche quantitative
├── données adversariales
├── incident
└── reconstruction

05 MAÎTRISE
│
├── allocation
├── gouvernance
├── IA
├── compétences durables
└── thèse du praticien
```

## 12.2 Comment lire un niveau

Chaque niveau doit répondre à six questions :

```text
Pourquoi ?
Quoi ?
Comment ?
Comment mesurer ?
Comment casser ?
Que faire ensuite ?
```

Si tu ne sais plus pourquoi tu lis un fichier, reviens au README du niveau.

## 12.3 Quand passer au niveau suivant

Ne te fie pas au calendrier. Utilise des preuves.

Tu es prêt à quitter le Socle lorsque tu peux expliquer le marché en termes simples et construire une première observation reproductible.

Tu es prêt pour Cadrage → Construction lorsque tu peux écrire une hypothèse et distinguer observation, interprétation et causalité supposée.

Tu es prêt pour Pilotage lorsque ta stratégie existe sous une forme suffisamment précise pour être mesurée et soumise au risque.

Tu es prêt pour Épreuve lorsque tu sais déjà chercher comment ton propre système peut se tromper.

Tu es prêt pour Maîtrise lorsque tu peux défendre tes choix, reconnaître les limites et transférer les mécanismes à un autre problème.

## 12.4 Le portefeuille de preuves

Construis progressivement :

```text
1. glossaire personnel
2. première observation
3. hypothèse falsifiable
4. mini-backtest
5. analyse de risque
6. test adversarial
7. postmortem
8. rapport de recherche
9. système de contrôle
10. thèse du praticien
```

Ton portfolio doit montrer **comment tu raisonnes**, pas seulement combien tu as gagné dans une simulation.

---

# 13. Quand tu bloques

## 13.1 Le protocole anti-panique

```text
STOP
 ↓
NOMME LE BLOCAGE
 ↓
CHERCHE LE PLUS PETIT MOT MANQUANT
 ↓
REVIENS UNE COUCHE EN ARRIÈRE
 ↓
FAIS UNE MICRO-PREUVE
 ↓
REPRENDS
```

## 13.2 « Je ne comprends pas cette équation »

Ne commence pas par chercher une autre équation.

Cherche :

```text
chaque symbole
→ son unité
→ son intuition
→ le rôle du terme
→ un exemple numérique
```

## 13.3 « Je ne comprends pas ce jargon »

Fais :

```text
mot
 ↓
phrase simple
 ↓
analogie
 ↓
contre-exemple
 ↓
retour au texte
```

Exemple : _slippage_.

> « Le prix que je pensais obtenir et le prix réellement exécuté ne sont pas identiques. »

Puis demande :

> « Pourquoi cette différence augmente-t-elle quand la liquidité se dégrade ? »

Tu viens d'apprendre le mécanisme, pas seulement le mot.

## 13.4 « Je veux regarder YouTube »

Tu peux. Mais applique le filtre :

```text
SOURCE
 ↓
AFFIRMATION
 ↓
MÉCANISME
 ↓
PREUVE
 ↓
TEST
```

Une vidéo est une source de contenu, pas un certificat de vérité.

## 13.5 « J'ai trouvé une stratégie incroyable »

Avant de l'admirer :

```text
Quel univers ?
Quelle période ?
Quels coûts ?
Quel benchmark ?
Combien de variantes testées ?
Quel hors-échantillon ?
Quel drawdown ?
Quelle capacité ?
Quel mécanisme ?
```

Si la personne répond « peu importe, ça marche », tu n'as pas encore de stratégie démontrée.

## 13.6 « Je suis mauvais en maths »

Tu n'as pas besoin de résoudre des équations de niveau recherche le premier jour.

Tu dois être capable de manipuler :

```text
pourcentage
ratio
variation
moyenne
écart
probabilité intuitive
ordre de grandeur
```

Puis tu montes progressivement.

---

# 14. Grimoire ultra-débutant

## 14.1 Vingt analogies de survie

**Marché** → un immense système d'enchères.  
**Prix** → le résultat d'échanges appariés et diffusés.  
**Bid** → meilleur acheteur visible.  
**Ask** → meilleur vendeur visible.  
**Spread** → coût implicite entre les deux côtés.  
**Liquidité** → profondeur disponible sans trop déplacer le prix.  
**Volatilité** → amplitude des mouvements.  
**Drawdown** → descente depuis ton dernier sommet.  
**Levier** → multiplicateur d'exposition.  
**Marge** → garantie pour maintenir l'exposition.  
**Stop** → règle qui dit « au-delà de là, mon hypothèse est invalidée ou mon exposition doit changer ».  
**Backtest** → replay historique d'une règle.  
**Out-of-sample** → terrain que tu n'as pas utilisé pour fabriquer la règle.  
**Overfitting** → apprendre par cœur le passé.  
**Baseline** → adversaire simple de référence.  
**Edge** → petite asymétrie statistique ou économique exploitable.  
**Regime** → climat de marché.  
**Portfolio** → combinaison d'expositions, pas simple collection de trades.  
**Execution** → passage du plan au terrain réel.  
**Governance** → règles qui encadrent la décision et ses exceptions.

## 14.2 Le tableau « ne confonds pas »

| Ne pas confondre | Avec           | Pourquoi                                                                   |
| ---------------- | -------------- | -------------------------------------------------------------------------- |
| corrélation      | causalité      | deux séries peuvent bouger ensemble sans mécanisme causal                  |
| gain             | edge           | une opération réussie peut être due au hasard                              |
| backtest         | preuve         | le passé est utilisé pour tester une hypothèse, pas pour garantir le futur |
| volatilité       | direction      | l'amplitude ne dit pas à elle seule où va le prix                          |
| levier           | avantage       | amplifier n'améliore pas la qualité du signal                              |
| indicateur       | mécanisme      | un indicateur est une transformation de données, pas une loi physique      |
| complexité       | sophistication | plus de paramètres augmentent aussi les occasions de sur-ajuster           |
| IA               | vérité         | un modèle peut être utile et faux simultanément                            |
| intuition        | validation     | l'intuition génère une hypothèse ; le test la confronte au réel            |
| win rate         | rentabilité    | la taille relative des gains/pertes et les coûts comptent                  |

## 14.3 Les cinq phrases que tu peux utiliser partout

Quand tu es perdu, demande :

> **« Quelle quantité mesure-t-on exactement ? »**

> **« À quel moment cette information était-elle disponible ? »**

> **« Qu'est-ce qui pourrait produire le même résultat sans que mon mécanisme soit vrai ? »**

> **« Quels coûts et quelles contraintes rendent cette idée non rentable ? »**

> **« Qu'est-ce qui me ferait changer d'avis ? »**

Ces cinq questions ont une valeur transversale énorme.

## 14.4 Première fiche de décision

```text
PROBLÈME :

ACTIF / UNIVERS :

HORIZON :

OBSERVATION :

HYPOTHÈSE :

MÉCANISME IMAGINÉ :

MESURE :

BASELINE :

COÛTS :

RISQUE PRINCIPAL :

CRITÈRE D'ÉCHEC :

PROCHAINE ACTION :
```

Imprime-la. Utilise-la jusqu'à ce qu'elle devienne une seconde nature.

---

# 15. Challenge final du guide

## Mission

Explique à quelqu'un qui n'a jamais tradé ce qu'est une décision de trading **sans utiliser plus de dix mots techniques non expliqués**.

La personne doit ensuite pouvoir répondre à cinq questions :

1. Pourquoi un trade gagnant ne prouve-t-il pas une stratégie ?
2. Pourquoi le levier peut-il accélérer la ruine ?
3. Pourquoi un backtest peut-il tromper ?
4. Pourquoi un graphique ne montre-t-il pas tout le marché ?
5. Pourquoi l'IA doit-elle être contrôlée ?

## Niveau 1 : Construire

Dessine une carte :

```text
information → décision → ordre → marché → exécution → résultat
```

## Niveau 2 : Expliquer

Explique dix mots du grimoire sans copier leurs définitions.

## Niveau 3 : Mesurer

Prends vingt observations de rendement et calcule au minimum moyenne, dispersion et drawdown d'une courbe cumulée.

## Niveau 4 : Casser

Trouve trois raisons pour lesquelles ton expérience pourrait donner un faux signal.

## Niveau 5 : Défendre

Réponds à :

> « Mais cette stratégie a 90 % de trades gagnants ! »

sans dire « parce qu'un expert l'a dit ».

## Boss

Un faux expert montre trois captures d'écran gagnantes et affirme :

> « J'ai compris le marché. »

Tu dois :

```text
1. séparer observation et narration
2. demander les données manquantes
3. demander les coûts
4. demander l'univers et la période
5. demander le hors-échantillon
6. chercher une baseline
7. définir un test qui pourrait contredire l'affirmation
```

## Test de maîtrise

Tu passes ce guide lorsque tu peux faire les quatre choses suivantes sans aide :

```text
SE REPÉRER
EXPLIQUER
MESURER
SE CONTRADIRE
```

---

# 16. Sources et entretien du guide

## Comment utiliser les sources

Le but d'une source n'est pas de remplacer ton raisonnement.

Utilise-la pour :

```text
1. identifier une affirmation
2. comprendre son mécanisme
3. retrouver la méthode
4. vérifier les limites
5. transférer l'idée au terrain
```

Le corpus de recherche de Trading Architecte sert notamment à documenter : microstructure, risque, biais cognitifs, validation, trading quantitatif et prospective 2035+.

Parmi les principes particulièrement importants : la validation doit tenir compte du data snooping et des tests multiples ; le travail de recherche préparatoire propose notamment une progression qui commence par données brutes, statistiques descriptives, hypothèse falsifiable et premier backtest, avant les étapes adversariales. fileciteturn1file0L15-L29

Les fondations académiques du projet utilisent également une hiérarchie explicite de la preuve, avec distinction entre effets robustes, effets conditionnels, artefacts et folklore. fileciteturn0file6L1-L2

## Règle d'entretien pédagogique

Ce guide doit rester le point où un débutant peut venir lorsque le reste du dépôt lui paraît trop dense.

La règle est donc :

```text
MOT INCOMPRIS
   ↓
GUIDE
   ↓
GRIMOIRE
   ↓
LEÇON CORE
   ↓
EXPÉRIENCE
   ↓
PREUVE
```

## Dernière règle

> **Ne cherche pas à devenir quelqu'un qui sait tout sur les marchés.**
>
> Cherche à devenir quelqu'un qui sait :
> **où il est, ce qu'il ne sait pas, comment le mesurer, comment le tester, comment gérer l'erreur, et comment apprendre la couche suivante.**

C'est cela, l'esprit de Trading Architecte.

## Carnet transversal unique : 7 micro-pratiques

Ce carnet est le rituel commun. Les 7 exercices sont à refaire au besoin ; les **44 missions spécialisées** ci-dessous sont différentes et ancrées dans leur domaine.

1. **Observation sans histoire** : écrire 10 faits observables sans causalité.
2. **Deux mécanismes concurrents** : proposer 2 explications incompatibles et la donnée qui les départagerait.
3. **Coût caché** : ajouter spread, commission, slippage et impact à un résultat théorique.
4. **Le miroir** : écrire la meilleure objection à sa propre hypothèse.
5. **Traduction pédagogique** : définir 5 termes avec définition simple, analogie, exemple, limite.
6. **Transfert** : déplacer un mécanisme vers un autre actif, horizon ou contexte.
7. **Preuve en une page** : résumer uniquement ce qui peut être mesuré, testé ou marqué comme hypothèse.

## 44 missions spécialisées

### Mission 01 : L’entrée dans le métier

**Ancrage :** `00-SOCLE/02-PROLOGUE`

Écrire en 120 mots la différence entre « observer un prix » et « expliquer un marché ». Puis donner un exemple où l’on confond les deux.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 02 : Repères et vocabulaire

**Ancrage :** `00-SOCLE/03-REFERENTIEL`

Choisir 6 termes du référentiel et construire une chaîne : terme → définition simple → unité ou objet mesurable → erreur typique.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 03 : Rendement et hasard

**Ancrage :** `00-SOCLE/04-FUNDAMENTALS`

Prendre 5 prix 100, 102, 101, 105, 103. Calculer les 4 rendements simples, puis comparer leur moyenne et leur médiane.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 04 : Question → test

**Ancrage :** `00-SOCLE/05-PROBLEM-SOLVING`

Transformer une question vague en hypothèse falsifiable avec seuil numérique d’échec, fenêtre de 20 observations et décision finale.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 05 : Biais sous pression

**Ancrage :** `00-SOCLE/06-MINDSET`

Après 3 pertes de 0,5 % chacune, calculer le capital restant à partir de 10 000 €. Écrire ensuite la règle qui interdit l’escalade de taille.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 06 : Macro sans récit

**Ancrage :** `01-CADRAGE/06-fondamentaux-macro`

Comparer une hausse de taux de 50 pb à une baisse de 25 pb : calculer l’écart absolu en points de base et décrire deux canaux économiques opposés.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 07 : Changement de régime

**Ancrage :** `01-CADRAGE/07-regimes`

Sur une série imaginaire où la volatilité passe de 1 % à 3 %, calculer le multiplicateur de volatilité et expliquer pourquoi un même sizing change de risque.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 08 : Familles d’edge

**Ancrage :** `01-CADRAGE/08-familles-de-strategies`

Comparer un signal à espérance 0,20 € avec 55 % de gains et un autre à 0,20 € avec 35 % de gains. Démontrer pourquoi le win rate seul ne suffit pas.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 09 : Échelle temporelle

**Ancrage :** `01-CADRAGE/09-timeframes`

Un signal journalier vise 2 % avec un stop de 1 %. Un signal horaire vise 0,5 % avec un stop de 0,25 %. Calculer le RR brut des deux et identifier ce que le RR ne dit pas.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 10 : Données sales

**Ancrage :** `02-CONSTRUCTION/06-data-engineering`

Introduire un split 2:1 dans une série à 100 €. Montrer le rendement artificiel obtenu sans ajustement, puis écrire la correction attendue.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 11 : Tests multiples

**Ancrage :** `02-CONSTRUCTION/07-validation-statistique`

Simuler mentalement 100 tests indépendants au seuil 5 %. Calculer le nombre moyen de faux positifs attendus sous l’hypothèse nulle.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 12 : Feature leakage

**Ancrage :** `02-CONSTRUCTION/08-feature-design`

Une variable utilise le rendement de T+1 pour expliquer T. Numéroter la séquence temporelle correcte et indiquer exactement où se trouve la fuite.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 13 : Risque de modèle

**Ancrage :** `02-CONSTRUCTION/09-model-risk`

Un modèle estime 1 % de risque quotidien mais réalise 4 % une fois sur 50 jours. Calculer la moyenne du choc observé dans ce cas et expliquer pourquoi une moyenne masque le tail risk.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 14 : Laboratoire

**Ancrage :** `02-CONSTRUCTION/10-lab-executable`

Lancer le sizing sur 10 000 € avec 0,5 % de risque et 2 € de distance au stop. Vérifier à la main la taille obtenue et écrire une assertion qui la protège.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 15 : Greeks

**Ancrage :** `03-PILOTAGE/06-derives-et-greques`

Une option a delta 0,45 et le sous-jacent gagne 3 €. Estimer la variation delta-hedgée de premier ordre, puis expliquer pourquoi l’approximation n’est pas une garantie.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 16 : Corrélation

**Ancrage :** `03-PILOTAGE/07-portfolio-construction`

Deux actifs ont volatilité 10 % et 15 %, corrélation 0,2, poids 60/40. Calculer la volatilité de portefeuille à partir de la covariance.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 17 : Opérationnel

**Ancrage :** `03-PILOTAGE/08-operations-et-compliance`

Un ordre est envoyé deux fois sur 100 titres à 50 €. Quantifier l’exposition additionnelle et définir le contrôle qui aurait dû empêcher l’incident.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 18 : Runbook

**Ancrage :** `03-PILOTAGE/09-runbooks`

Construire une alerte avec seuil : drawdown intraday 2 %, latence 500 ms, ou perte cumulative 1 %. Indiquer le premier déclencheur et l’action associée.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 19 : Réplication

**Ancrage :** `04-EPREUVE/06-replication-lab`

Une étude annonce Sharpe 1,2. Recalculer le Sharpe après division par 2 de l’excès de rendement mais volatilité inchangée, puis discuter la robustesse.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 20 : Backtest vs réel

**Ancrage :** `04-EPREUVE/07-live-vs-backtest`

Backtest : 12 % brut, coûts 2 %. Réel : 12 % brut, coûts 5 %. Calculer les rendements nets et le différentiel de 3 points.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 21 : Red team

**Ancrage :** `04-EPREUVE/08-red-team-research`

Prendre une affirmation « robuste » et proposer 3 attaques quantitatives : période, coûts, univers. Pour chacune, fixer un seuil de falsification.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 22 : Lire un papier

**Ancrage :** `05-MAITRISE/06-lecture-de-recherche`

Extraire d’un résultat annoncé n=500 observations : variable expliquée, estimateur, intervalle de confiance et taille d’effet. Refuser toute conclusion sans ces 4 éléments.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 23 : Gouvernance

**Ancrage :** `05-MAITRISE/07-ia-et-gouvernance`

Un agent propose 40 ordres dont 6 dépassent la limite. Calculer le taux d’ordres rejetés et définir un garde-fou automatique.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 24 : Défense orale

**Ancrage :** `05-MAITRISE/08-communication-praticien`

Présenter en 90 secondes un système avec 52 % de trades gagnants et gain moyen 1,4R contre perte moyenne 1R. Calculer l’espérance par trade.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 25 : Horizon 2035

**Ancrage :** `05-MAITRISE/09-feuille-de-route-2035`

Classer 4 compétences selon leur durée de vie : microstructure, syntaxe d’un outil, gestion du risque, nom d’un fournisseur. Justifier le classement avec une fenêtre 2026→2035.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 26 : Sensibilité au spread

**Ancrage :** `CROSS/01`

Avec 60 trades/mois, spread 2 € par trade : calculer le coût mensuel. Refaire à 3 € et mesurer l’écart.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 27 : Drawdown

**Ancrage :** `CROSS/02`

Une equity passe 10 000 → 9 200 → 10 580. Calculer le drawdown maximal puis le gain nécessaire pour revenir au sommet.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 28 : Position sizing

**Ancrage :** `CROSS/03`

Capital 25 000 €, risque 0,4 %, distance 1,25 €. Calculer le budget de risque et la quantité théorique.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 29 : Slippage

**Ancrage :** `CROSS/04`

Prix prévu 100 €, exécution moyenne 100,08 € pour 400 unités. Calculer le slippage en euros et en points de base.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 30 : Espérance

**Ancrage :** `CROSS/05`

40 gains à +1,5R et 60 pertes à −1R sur 100 trades. Calculer l’espérance en R/trade.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 31 : Profit factor

**Ancrage :** `CROSS/06`

Gross wins 7 500 €, gross losses 5 000 €. Calculer le profit factor et préciser ce qu’il ignore.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 32 : Sharpe

**Ancrage :** `CROSS/07`

Rendement moyen 0,06 %/jour, écart-type 0,9 %. Calculer le Sharpe journalier simplifié et rappeler qu’une annualisation suppose une convention.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 33 : VaR vs perte

**Ancrage :** `CROSS/08`

VaR 95 % = 1,2 %. Une journée réalise −3,5 %. Mesurer l’écart et expliquer pourquoi la VaR ne borne pas la perte.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 34 : Corrélation

**Ancrage :** `CROSS/09`

Deux positions ont ρ=0,9. Comparer qualitativement le gain de diversification à ρ=0,1 et donner un exemple de risque commun.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 35 : Turnover

**Ancrage :** `CROSS/10`

Un portefeuille de 100 000 € tourne 80 % par semaine à 15 pb de coût aller-retour. Estimer un coût hebdomadaire simplifié.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 36 : Regime filter

**Ancrage :** `CROSS/11`

Régime calme : vol 0,8 %. Régime stress : 2,4 %. Calculer le ratio 3:1 et la réduction de taille nécessaire pour garder un risque absolu comparable.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 37 : Walk-forward

**Ancrage :** `CROSS/12`

4 fenêtres train/test de 120/30 jours. Calculer le nombre total d’observations de test et expliquer pourquoi le futur n’est jamais mélangé au passé.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 38 : Overfitting

**Ancrage :** `CROSS/13`

10 000 configurations sont testées à seuil 5 %. Donner l’espérance naïve de faux positifs sous indépendance et expliquer pourquoi ce n’est qu’un ordre de grandeur.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 39 : Break-even costs

**Ancrage :** `CROSS/14`

Edge brut 0,18R/trade, coût 0,11R. Calculer l’edge net et le coût maximal avant passage à zéro.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 40 : Options

**Ancrage :** `CROSS/15`

Premium 4 €, delta 0,5, move de 2 €. Approximation de premier ordre : variation du premium. Puis citer ce qui manque (gamma, theta, vol implicite).

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 41 : Execution latency

**Ancrage :** `CROSS/16`

100 ordres, 8 au-delà de 500 ms. Calculer le taux de dépassement et proposer une alerte à 10 %.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 42 : Data quality

**Ancrage :** `CROSS/17`

1 000 lignes, 12 timestamps dupliqués, 5 prix manquants. Calculer les pourcentages de doublons et de valeurs manquantes.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 43 : Scenario stress

**Ancrage :** `CROSS/18`

Perte −6 % du portefeuille, corrélation qui passe de 0,2 à 0,8. Calculer la hausse en points de corrélation et expliquer le risque de convergence.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 44 : Research decay

**Ancrage :** `CROSS/19`

Une anomalie annonce 8 % ; post-publication 4,8 %. Calculer la baisse relative de rendement.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.

### Mission 45 : Capital recovery

**Ancrage :** `CROSS/20`

Après −30 %, calculer le gain requis pour revenir au capital initial et expliquer l’asymétrie.

**Critère de sortie :** une réponse chiffrée, une hypothèse explicite et une phrase sur la limite principale.
