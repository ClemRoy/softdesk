# Softdesk

 L'objectif de ce projet est de mettre en place une API REST permettant de servir les données pour une application de suivi des problèmes permettant de créer des projets,d'assigner les utilisateurs a des projets particulier, de créer des problèmes liés a ces projets ainsi que des commentaires pour chaque problèmes.



## Table of Contents
- [Softdesk](#Softdesk)
  - [Table of Contents](#table-of-contents)
  - [Installation](#Installation)
  - [Informations générales](#Informations-générales)
  - [Project Status](#project-status)


## Installation
 
 Vous pouvez télécharger l'archive zip et l'extraire dans le dossier ou vous desirez installer le projet.
 Alternativement,vous pouvez installer le projet dans le dossier désiré avec la commande:
 ```
 git clone https://github.com/ClemRoy/softdesk
 ```
   Une fois cette étape accompli,déplacez vous dans le dossier litreview a l'aide de :
 ```
 cd softdesk-master
 ```
   Vous pouvez désormais créer un environement virtuel avec:
 ```
 python -m venv env
 ```
 puis l'activer avec:
 ```
 env/scripts/activate
 ```
 La prochaine étape consiste a installer les dépéndance a l'aide de:
 ```
 pip install -r requirements.txt
 ```
 enfin vous pouvez lancer le serveur de développement avec:
 ```
 python manage.py runserver
 ```

## Informations générales

 Une fois le projet installé et le serveur de developpement lancé,vous pouvez accéder a l'API via:
 ```
 http://127.0.0.1:8000/
 ```

 Une fois cette étape franchie vous accederez aux différentes fonctionalitées du site permettant d'accomplir les differentes actions relative au suivi des problèmes via les différentes requêtes détaillée dans cette documentation postman: 

  ```
 https://documenter.getpostman.com/view/19443765/2s8ZDSdR8H
 ```
 
  La base de donnée contient un jeu de donnée factice pour vous permettre de tester l'API.Vous pouvez y accéder en utilisant les identifiants suivants:
  email : user1@demo.com password: user1
  email : user2@demo.com password: user2
  email : user3@demo.com password: user3
  email : user4@demo.com password: user4

## Project Status

 Project is: _completed_