Procédure d'installation
#########################

Voici la procédure d'installation de EasyTimeTable Online.

Pour résumer
~~~~~~~~~~~~

Voici les commandes que vous pouvez taper dans un terminal afin d'avoir un 
projet plainement fonctionnel::

    $ easy_install virtualenv
    $ virtualenv --no-site-packages django
    $ cd django
    $ source bin/activate
    $ easy_install django==1.1
    $ easy_install django-extensions
    $ easy_install django-uni-form
    $ git clone git@github.com:easytimetable/easytimetable.git
    $ cd easytimetable
    $ python manage.py syncdb --noinput
    $ python manage.py runserver

Et vous pouvez aller voir le site ici: http://localhost:8000

Pas à pas détaillé
~~~~~~~~~~~~~~~~~~~

Prérequis
==========

* Une station unix, linux, mac ou équivalent
* Python >= 2.5
* Git 

Virtualenv
==========

Virtualenv est un projet qui permet de séparer les dépendances système du projet
des dépendances de la machine.

Cela signifie donc qu'il est possible d'avoir plusieurs versions de modules
python d'installés sur une même machine, et qu'ils ne rentrent pas en conflit.
D'une manière générale, il est préférable d'utiliser virtualenv pour ses
projets, afin de contrôler completement l'environnement de developpement de la
même manière sur la machine de production et sur la machine de developpement.

Pour installer virtualenv, voici une procédure. Vous avez besoin d'avoir soit
pip soit easy_install sur votre machine. Voici la procédure avec easy_install::

    $ easy_install virtualenv

Une fois virtualenv installé, il faut créer un environnement de developpement::

    $ virtualenv --no-site-packages django
    New python executable in django/bin/python
    Installing setuptools............done.

Et l'activer::

    $ cd django
    $ source bin/activate
    (django)

Le `(django)` signifie que l'on utilise le virtualenv "django".

Installation de django
======================

Maintenant, installez django dans l'environnement de developpement. Nous
utilisons la version 1.1, qui est actuellement la version stable::

    $ easy_install django
    (django)

Dépendances du projet
=====================

Le projet à une dépendance aux applications `django_extensions` et `django-uniform`, voici comment les 
installer, via pip. La procédure serait la même avec easy_install::

    $ pip install django-extensions
    $ pip install django-uni-form

Dépot GIT
==========

Maintenant, sortez de votre dossier `django`::

    $ cd ..

Nous avons choisi d'utiliser le système de controle de version décentralisé GIT,
et notre dépot est disponible à l'adresse http://github.com/easytimetable/easytimetable.

Vous pouvez par exemple récupérer le projet en faisant::

    $ git clone git@github.com:easytimetable/easytimetable.git
    Initialized empty Git repository in /tmp/easytimetable/.git/
    remote: Counting objects: 78, done.
    remote: Compressing objects: 100% (74/74), done.
    remote: Total 78 (delta 36), reused 0 (delta 0)
    Receiving objects: 100% (78/78), 333.17 KiB | 183 KiB/s, done.
    Resolving deltas: 100% (36/36), done.
    (django)


   
Lancer le projet
================
 
Le projet est maintenant installé, il est possible de lancer le projet comme suit. 
Les étapes décrites ci dessous ont pour effet de créer la base de données et de lui 
fournir un jeu de données de tests. ::

    $ cd easytimetable/
    $ python manage.py syncdb --noinput
    $ python manage.py runserver 
