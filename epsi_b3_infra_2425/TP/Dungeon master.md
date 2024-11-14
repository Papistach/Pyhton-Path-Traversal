# Dungeon master

## Partie 1

- Implémenter une fonction ``generer_niveau()`` qui :
  - Créé une liste vide
  - Remplis 20 fois cette liste avec un nombre aléatoire ``1`` ``(équivalent de → ennemi)`` ou ``0`` `(équivalent de salle vide)`
  - Retourne la liste
- Tester 3 fois le système en affichant 3 niveaux aléatoires différents

## Partie 2

- Définir une fonction ``traverse_niveau(niveau)`` qui :
  - Prend un niveau en paramètre
  - Définit une variable `vie` égale à 1
  - Itère les emplacements du niveau
  - A chaque ``ennemi``
    - Jette un dés à 6 faces
      - Si il fait 1, 2 ou 3 → perd une vie
      - Si il fait 4, 5 ou 6 → rien ne se passe
  - Rien ne se passe dans une ``salle vide``
  - Retourne `False` si la vie est inférieure ou égale à ``0`` après la traversée
  - Autrement retourne `True` (la traversée du niveau a été réussie)

## Partie 3

- Dans une fonction `main()`
- Tant qu'une traversée n'a pas été réussie
  - Exécute les deux fonctions `generer_niveau()` & `traverse_niveau(niveau)` 
- Affiche "Jeu terminé ! X niveaux traversés avant de réussir !"

```python
# ...
[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0]
[1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0]
[1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1]
[0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]
"Jeu terminé ! 90 niveaux traversés avant de réussir !"
```