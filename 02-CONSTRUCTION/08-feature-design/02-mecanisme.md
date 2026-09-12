---
stability: intemporel
acte: comprendre
---

# 02 — MÉCANISME : VARIABLES

Une **feature (variable construite pour fournir de l'information à un modèle ou une règle)** doit être disponible au moment de la décision.

```text
données disponibles à t
       ↓
transformation autorisée
       ↓
feature_t
       ↓
décision_t
```

Toute information de t+1 injectée dans feature_t est une fuite.
