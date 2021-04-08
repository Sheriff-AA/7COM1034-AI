import heroes_and_sk_2
import dfs_function
# import sys
# sys.setrecursionlimit(1000)

hero = heroes_and_sk_2.HeroSidekicks()
print(dfs_function.dfs_heroes(hero, hero.start()))
