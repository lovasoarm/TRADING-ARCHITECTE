---
stability: intemporel
acte: protéger
noyau: oui
---

# 06 : LEVIER, MARGE & LIQUIDATION

**Levier (exposition / capital)** augmente les gains potentiels **et** les pertes.

**Marge (garantie immobilisée)** est un mécanisme de financement/garantie, pas un budget de perte.

**Liquidation (fermeture forcée d'une position)** peut survenir avant que ton intuition « long terme » ait le temps de se vérifier.

```text
capital
  ↓
exposition × levier
  ↓
variation du prix
  ↓
variation du P&L
  ↓
seuil de marge
  ↓
liquidation possible
```

## Exercice

Simule le même portefeuille à 1×, 2× et 5×. Mesure le drawdown et le buffer avant liquidation.

## Règle

Le sizing réel doit partir de la **perte soutenable**, pas du montant maximum autorisé.
