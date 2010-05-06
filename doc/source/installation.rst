Procédure d'installation
#########################

Voici la procédure d'installation de EasyTimeTable Online.

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

Le (django) signifie que l'on utilise le virtualenv "django".

Installation de django
======================

Maintenant, installez django dans l'environnement de developpement. Nous
utilisons la version 1.1, qui est actuellement la version stable::

    $ easy_install django
    (django)

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


Dépendances du projet
=====================

Le projet à une dépendance vers l'application `django_extensions`, voici comment l'installer::

    $ cd ..
    $ git clone http://github.com/django-extensions/django-extensions.git
    $ cd django-extensions
    $ python setup.py install
    $ cd ..
   
Lancer le projet
================
 
Le projet est maintenant installé, il est possible de lancer le projet comme suit::

    $ cd easytimetable/
    (django)
    $ python manage.py syncdb
    $ python runserver 
