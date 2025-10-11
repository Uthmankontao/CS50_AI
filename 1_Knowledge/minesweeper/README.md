# 🧩 Minesweeper AI

Un démineur classique en **Python**, avec une **intelligence artificielle logique** qui apprend à jouer au jeu.  
Projet inspiré du cours **CS50’s Introduction to Artificial Intelligence with Python**.

---

## 🚀 Fonctionnalités
- Plateau de démineur généré aléatoirement (`Minesweeper`).  
- Joueur humain via interface graphique (clic gauche pour révéler, clic droit pour marquer une mine).  
- Agent intelligent (`MinesweeperAI`) qui déduit logiquement quelles cases sont sûres ou dangereuses.  
- Bouton **AI Move** : laisse l’IA jouer automatiquement.  
- Bouton **Reset** : recommence une partie.  


## 🎮 Utilisation

Lancer le jeu :
```bash
python runner.py
```

- **Mode manuel** :  
  - Clic gauche → révéler une case  
  - Clic droit → marquer/démarquer une mine  

- **Mode IA** :  
  - Clique sur le bouton **AI Move** : l’IA joue un coup  
  - Elle choisit toujours un coup sûr si possible, sinon elle prend un risque calculé.  

- **Victoire** 🏆 : toutes les mines sont correctement marquées.  
- **Défaite** 💥 : une mine est révélée.  



## 🤖 Aperçu IA
L’IA repose sur un **moteur de règles logiques** :  
- Chaque indice (nombre de mines autour d’une case) est ajouté comme **Sentence**.  
- Si tous les voisins restants sont sûrs → ils sont marqués comme **safe**.  
- Si tous les voisins restants sont des mines → ils sont marqués comme **mines**.  
- De nouvelles règles peuvent être déduites par **subsets** entre phrases.  

