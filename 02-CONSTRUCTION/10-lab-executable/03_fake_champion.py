"""Show why selecting the best of many random trials is not proof."""
import random
random.seed(7)
trials=[sum(random.gauss(0,1) for _ in range(200))/200 for _ in range(500)]
best=max(trials)
print(f"Nombre d'essais: {len(trials)}")
print(f"Meilleur score simulé: {best:.4f}")
print("Le score est celui du champion choisi après 500 essais : il faut maintenant un test indépendant.")
