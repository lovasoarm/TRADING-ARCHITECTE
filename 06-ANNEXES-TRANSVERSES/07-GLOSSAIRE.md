---
stability: stable
---

# GLOSSAIRE — OPÉRATIONNEL

- **Ask** : meilleur prix vendeur disponible.
- **Bid** : meilleur prix acheteur disponible.
- **Spread** : écart bid/ask.
- **Slippage** : différence entre prix prévu et prix exécuté.
- **Liquidité** : capacité à négocier sans déplacer excessivement le prix.
- **Volatilité** : dispersion des variations ; ce n’est pas tout le risque.
- **Drawdown** : baisse depuis un sommet de capital.
- **Edge** : avantage statistique ou économique sous conditions.
- **Espérance** : résultat moyen théorique sous un modèle.
- **Out-of-sample** : données non utilisées pour ajuster le modèle.
- **Overfitting** : ajustement excessif au bruit des données d’apprentissage.
- **Look-ahead bias** : utilisation d’une information indisponible à t0.
- **Survivorship bias** : exclusion des actifs/acteurs disparus.
- **Market impact** : déplacement de prix causé par l’exécution.
- **Levier** : exposition supérieure au capital engagé.
- **Marge** : garantie de position ; pas plafond universel de perte.
- **Kelly** : cadre de sizing ; très sensible à l’erreur d’estimation en pratique.
- **CPCV** : validation combinatoire purgée adaptée à certaines données temporelles.
- **DSR** : correction de l’optimisme du Sharpe sous multiplicité des essais.
- **SPA** : comparaison de capacité prédictive face à des alternatives sous sélection multiple.
- **Régime** : état de marché décrit par des propriétés observables.
- **Reverse stress test** : recherche des conditions minimales de non-viabilité.

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

- White, H. (2000), *A Reality Check for Data Snooping*, Econometrica 68(5), 1097–1126. — https://doi.org/10.1111/1468-0262.00152
- Bailey, D. H. et al. (2015), *The Probability of Backtest Overfitting*. — https://ssrn.com/abstract=2326253
