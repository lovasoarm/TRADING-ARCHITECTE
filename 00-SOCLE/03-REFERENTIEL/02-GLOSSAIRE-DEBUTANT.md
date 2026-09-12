---
stability: évolutif
acte: restituer
---

# 02 : GLOSSAIRE DÉBUTANT

> Le vocabulaire n'est pas une porte fermée. Chaque terme doit être traduisible en langage normal.

| Terme         | Explication immédiate                                               | Ce que ce terme ne garantit pas           |
| ------------- | ------------------------------------------------------------------- | ----------------------------------------- |
| broker        | intermédiaire qui donne accès au marché                             | qu'il améliore ton edge                   |
| exchange      | place organisée où des ordres sont appariés                         | toute la liquidité du monde               |
| bid           | meilleur prix acheteur visible                                      | le prix auquel tu seras forcément exécuté |
| ask           | meilleur prix vendeur visible                                       | un prix stable                            |
| spread        | différence ask-bid                                                  | une commission totale universelle         |
| order book    | file d'ordres d'achat/vente à certains prix                         | toute la liquidité cachée                 |
| market order  | priorité donnée à l'exécution                                       | prix exact garanti                        |
| limit order   | prix maximal/minimal accepté                                        | exécution garantie                        |
| slippage      | écart entre prix visé et obtenu                                     | erreur de stratégie                       |
| notional      | valeur faciale exposée                                              | argent réellement perdu                   |
| marge         | garantie mobilisée pour une position                                | limite de perte suffisante                |
| leverage      | exposition / capital                                                | rentabilité supplémentaire                |
| long          | exposition gagnante si le prix monte                                | forte conviction                          |
| short         | exposition gagnante si le prix baisse                               | risque illimité dans tous les instruments |
| rendement     | variation relative de valeur                                        | qualité de décision                       |
| alpha         | performance attribuable à un avantage après définition du benchmark | résultat certain                          |
| beta          | sensibilité à un facteur de marché                                  | risque complet                            |
| volatilité    | dispersion/amplitude des rendements                                 | probabilité exacte d'une perte            |
| drawdown      | baisse depuis un sommet de la courbe                                | volatilité pure                           |
| Sharpe        | rendement excédentaire rapporté à une mesure de volatilité          | robustesse future                         |
| backtest      | simulation historique                                               | preuve causale                            |
| overfitting   | adaptation excessive aux données connues                            | simple « erreur de débutant »             |
| out-of-sample | données non utilisées pour construire la règle                      | futur garanti                             |
| regime        | environnement où les propriétés du marché diffèrent                 | une étiquette parfaite                    |
| tail risk     | événement rare à fort impact                                        | événement nécessairement prévisible       |
| hedging       | réduction d'une exposition par une autre position                   | disparition du risque                     |
| margin call   | demande de garantie supplémentaire                                  | mécanisme de marché à lui seul            |
| liquidation   | fermeture forcée ou volontaire d'une position                       | prix favorable                            |

## Termes techniques essentiels

| ATR | amplitude récente des mouvements de prix | ne prédit pas la direction |
| OHLCV | ouverture, plus haut, plus bas, clôture et volume | ne montre pas toute la microstructure |
| P&L | gain ou perte d’une position | ne mesure pas la qualité de la décision à lui seul |
| VWAP | prix moyen pondéré par les volumes | n’est pas un prix juste garanti |
| HFT | trading automatisé à très haute fréquence | ne signifie pas automatiquement avantage rentable |
| VaR | seuil de perte estimé à un niveau de confiance | ne décrit pas parfaitement les queues extrêmes |
| Expected Shortfall | perte moyenne au-delà du seuil de VaR | dépend du modèle et des données |
| PBO | probabilité estimée de surajustement du backtest | ne garantit pas la robustesse |
| DSR | Sharpe corrigé notamment pour les essais multiples | ne transforme pas un signal faible en vérité |
| Greeks | sensibilités d’une option à ses facteurs de risque | ne prédisent pas seuls la trajectoire |
| RAG | génération de texte assistée par récupération de sources | ne garantit pas la qualité des sources |
| LLM | grand modèle de langage | ne garantit pas la véracité de sa réponse |

### Références

- White, H. (2000), _A Reality Check for Data Snooping_, Econometrica 68(5), 1097–1126. : https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), _The Probability of Backtest Overfitting_. : https://ssrn.com/abstract=2326253
