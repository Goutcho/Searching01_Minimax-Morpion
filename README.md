# Projet Tic Tac Toe avec Algorithme Minimax

## Vue d'ensemble
Ce projet est une implémentation du jeu classique Tic Tac Toe (aussi connu sous le nom de Morpion) en Python. L'objectif principal est de démontrer l'efficacité de l'algorithme Minimax dans la prise de décision. Cet algorithme permet au programme de choisir le coup optimal à chaque tour, en simulant toutes les possibilités jusqu'à la fin de la partie.

## Fonctionnement de l'Algorithme Minimax
L'algorithme Minimax est utilisé dans les jeux à deux joueurs de type somme nulle comme le Tic Tac Toe. Voici les principes de base de son fonctionnement :

- **Exploration de l'Arbre de Jeu :** Chaque nœud représente un état du jeu. Minimax explore récursivement ces nœuds pour évaluer les mouvements possibles.
- **Joueurs Minimisant et Maximisant :** L'algorithme considère deux joueurs - un qui cherche à maximiser le score (Maximisant) et l'autre qui cherche à minimiser le score (Minimisant).
- **Évaluation des Nœuds :** Les nœuds terminaux (états de jeu où quelqu'un a gagné ou le jeu est nul) sont évalués et reçoivent une valeur. Les états intermédiaires sont évalués en fonction du meilleur coup possible pour le joueur concerné.
- **Choix du Meilleur Coup :** L'algorithme remonte l'arbre de jeu, choisissant le coup optimal pour le joueur Maximisant tout en supposant que le joueur Minimisant joue également de manière optimale.

## Structure du Projet
Le projet se compose de deux fichiers principaux :
- `tictactoe.py` : Contient la logique du jeu et l'implémentation de l'algorithme Minimax.
- `runner.py` : Un script pour lancer le jeu, gérer les interactions avec l'utilisateur, et afficher l'état du jeu.

## Comment Exécuter
Pour lancer le jeu, exécutez la commande suivante dans votre terminal :
```bash
python runner.py
