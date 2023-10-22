# Gestion de location : digikazAPI

## Présentation

Cette API est construite en utilisant Django Rest Framework (DRF) et intègre une base de données SQLite. Elle permet la gestion des locations de biens immobiliers, y compris la création, la mise à jour, la suppression, 
et la recherche de locations.

## Configuration

Assurez-vous d'avoir Python 3.x et pip installé sur votre système.

## Installation

  1) Créez un dossier (par exemple, "digikazAPI").

  2) Ouvrez un terminal dans le dossier que vous venez de créer.

  3) Créez un environnement Python en utilisant la commande suivante :

         python3 -m venv nomEnv

  4) Activez l'environnement Python :

         Sous Windows :  nomEnv\Scripts\activate

         Sous MacOS/Linux :  source nomEnv/bin/activate

  5) Installez Django en utilisant la commande :
     
         pip install Django

  6) Installez Django Rest Framework avec la commande :
     
          pip install djangorestframework

  7) Créez un projet Django en utilisant la commande :

          django-admin startproject nomProjet .

       Ouvrez le dossier de votre projet dans le terminal.

  8) Créez une application Django en utilisant la commande :
    
          django-admin startapp nomApplication

  9) Synchronisez la base de données SQLite en exécutant la commande :
     
          python manage.py migrate

## Exécution

Pour lancer le serveur de développement, utilisez la commande suivante :

          python manage.py runserver

Le serveur sera disponible à l'adresse http://127.0.0.1:8000/ .

## Authentification

Cette API utilise l'authentification JWT (JSON Web Tokens) pour sécuriser les endpoints. Vous devez vous authentifier pour effectuer certaines opérations.

## Documentation API

La documentation de l'API est automatiquement générée par DRF. Vous pouvez y accéder à http://127.0.0.1:8000/docs/.


## Tests unitaires

Ce projet comprend des tests unitaires pour assurer le bon fonctionnement de l'API. Vous pouvez les exécuter avec la commande suivante :

        python manage.py test nomApplication.tests

## Versioning avec Git

Ce projet utilise Git pour le contrôle de version. Assurez-vous de créer des branches de fonctionnalités et de fusionner vos modifications de manière ordonnée.

## Liens Utiles

- [Documentation Django]  (https://docs.djangoproject.com/en/stable/)
- [Documentation Django Rest Framework] (https://www.django-rest-framework.org/)


## Contributeurs

    Salamata Nourou MBAYE (salambaye2001@gmail.com)
    Souleymane SALL (souleymanesall@esp.sn)
