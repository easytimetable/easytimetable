Documentation d'administration
#########################

Installation de la solution
===========================

Prérequis
---------

Ci-dessous, les composants logiciels nécessaires au fonctionnement de
l'application

    * Une station unix, linux, mac ou équivalent
    * Python >= 2.5
    * nginx
    * easy_install ou pip
    * Un compte de service pour lancer l'application (ci-après "srveasy")

Pour une installation en ligne
    
    * Git

Pour une installation hors ligne
    
    * Le paquet easytimetable.tar.gz
    * tar
    * gunzip

Les procédures suivantes ont été conçues pour une installation sous
Debian GNU/Linux. Elles sont toutefois théoriquement appliquables à
tous les systèmes sur base unix, sous réserve de quelques modifications
(notamment au niveau des chemins) et de disponibilités des dépendances.

Procédure d'installation rapide
-------------------------------

Les commandes présentées dans ce paragraphe sont à taper dans un terminal.
Le bon déroulement des procédures permettra d'obtenir une application
pleinement fonctionnelle.

Installation hors ligne
~~~~~~~~~~~~~~~~~~~~~~~

En tant que srveasy::

	$ easy_install virtualenv
	$ virtualenv --no-site-packages django
	$ cd django
	$ source bin/activate
	$ easy_install django==1.1
	$ easy_install django-extensions
	$ easy_install django-uni-form
	$ easy_install vobject
	$ cd ..
	$ tar -xzf easytimetable.tar.gz
	$ cd easytimetable
	$ python manage.py syncdb --noinput
	$ easy_install gunicorn
	$ gunicorn_django -D -w 5

En tant que root::

	# cd /home/srveasy/easytimetable
	# cp config/gunicorn_app_srv /etc/nginx/conf.d/
	# rm /etc/nginx/sites-enabled/default
	# cp config/gunicorn_srv /etc/nginx/sites-enabled/
	# /etc/init.d/nginx restart
	
L'applicaton est maintenant accessible sur le port http du serveur.

Installation pour tests
~~~~~~~~~~~~~~~~~~~~~~~~

Un installation à des fins de tests ne nécessite pas gunicorn ni nginx : le serveur
d'applications intégré à django est largement suffisant pour une mise en tests, ce qui
est d'ailleurs sa raison d'être.

Pour effectuer une installation de test, suivre la procédure précédente en remplaçant les lignes
suivantes::

	$ easy_install gunicorn
	$ gunicorn_django -D -w 5
	
par::

	$ python manage.py runserver

La partie en tant que root n'a alors plus lieu d'être.

Le serveur d'application écoute par défaut sur la boucle locale, port 8000.
Pour que l'application soit accessible depuis une autre machine, la dernière ligne doit
être la suivante::

	$ python manage.py runserver 0.0.0.0:8000
	
L'application sera alors accessibleà l'adresse : http://<serveur>:8000/

Installation en ligne
~~~~~~~~~~~~~~~~~~~~~

La procédure est la même sauf pour la ligne::
	
	$ tar -xzf easytimetable.tar.gz

qu'il suffit de remplacer par::

	$ git clone git://github.com/easytimetable/easytimetable.git

Procédure détaillé
------------------

Virtualenv
~~~~~~~~~~~

Virtualenv est un projet qui permet de séparer les dépendances système du projet
des dépendances de la machine.

Cela signifie donc qu'il est possible d'avoir plusieurs versions de modules
python d'installés sur une même machine, et qu'elles n'entrent pas en conflit.
D'une manière générale, il est préférable d'utiliser virtualenv pour les
projets, afin de contrôler complètement l'environnement de de production et
ainsi d'obtenir le même environnement d'exécution sur la machine de developpement
et sur la machine de production.

Ci-dessous, la commande easy_install pour installer virtualenv::

    $ easy_install virtualenv

Easy_install et pip ayant la même syntaxe, les commandes easy_install peuvent
être effectuée en utilisant pip au lieu d'easy_install.

L'étape suivante est la création un environnement d'exécution::

    $ virtualenv --no-site-packages django
    New python executable in django/bin/python
    Installing setuptools............done.

Puis son activation::

    $ cd django
    $ source bin/activate
    (django)

Le `(django)` signifie que l'on utilise le virtualenv "django".

Installation de django
~~~~~~~~~~~~~~~~~~~~~~

L'application est basée sur le framework django, ella a donc besoin que
celui-ci soit installé pour fonctionner::

    $ easy_install django==1.1
    (django)

La version 1.1 de django étant l'actuelle version stable, c'est celle
utilisée pour ce projet.

Dépendances du projet
~~~~~~~~~~~~~~~~~~~~~~

Le projet dépend des applications `django_extensions` et `django-uniform`, leur
installation dans l'environnement est donc obligatoire::

    $ easy_install django-extensions
    $ easy_install django-uni-form

Le projet dépend également de `vobject`, qui permet de fournir des données au format
iCal::

	$ easy_install vobject

La préparation de l'environnement est maintenant terminée.
Pour la suite de la procédure, il est nécessaire de sortir du dossier django::

    $ cd ..

Dépot GIT
~~~~~~~~~~

Il a été choisi d'utiliser le système de controle de version décentralisé GIT.
Le dépôt est disponible à l'adresse http://github.com/easytimetable/easytimetable.

Voici la commande à utiliser pour installer le projet en utilisant ce dépôt::

    $ git clone git://github.com/easytimetable/easytimetable.git
    Initialized empty Git repository in /tmp/easytimetable/.git/
    remote: Counting objects: 78, done.
    remote: Compressing objects: 100% (74/74), done.
    remote: Total 78 (delta 36), reused 0 (delta 0)
    Receiving objects: 100% (78/78), 333.17 KiB | 183 KiB/s, done.
    Resolving deltas: 100% (36/36), done.
    (django)

Initialisation du projet
~~~~~~~~~~~~~~~~~~~~~~~~~

Le projet est maintenant installé, il est maintenant nécessaire de l'initialiser.
Les étapes décrites ci dessous ont pour effet de créer la base de données et de lui
fournir un jeu de données de tests. ::

    $ cd easytimetable/
    $ python manage.py syncdb --noinput

Lancer le projet
~~~~~~~~~~~~~~~~~

Le framework django embarquant un serveur web, il est possible de lancer le projet
comme suit::

	$ python manage.py runserver

Cependant cette fonctionnalité existe surtout à des fins de développement et ses
performances risquent de ne pas être suffisantes en cas de forte charge.

Il est donc recommandé d'utiliser gunicorn, qui est un serveur d'application
python, en association avec nginx qui lui est un serveur http très léger.
Ce dernier servira de proxy afin que les utilisateurs n'aient pas directement
accès au serveur d'application. Ce fonctionnement est recommandé afin d'accroître
la sécurite.

* Toujours dans l'environnement virtuel::

	$ easy_install gunicorn
	$ gunicorn_django -D -w 5

Le paramètre -w dépend du nombre de coeurs de processeur qui sont alloués à la machine :
-w = (nbr coeurs x 2) + 1
Le paramètre -D sert quant à lui à indiquer que le serveur gunicorn va fonctionner en
arrière plan (daemon).

Puis, en tant que root (super utilisateur):

* Copier le fichier config/gunicorn_app_srv dans le dossier /etc/nginx/conf.d/::
	
	# cp config/gunicorn_app_srv /etc/nginx/conf.d/
	
Ce fichier sert à déclarer le serveur gunicorn dans nginx.

* Supprimer le fichier de configuration par défaut de nginx::

	# rm /etc/nginx/sites-enabled/default

Le fait de supprimer ce fichier n'est pas nécessaire, cependant il ne permet pas en l'état
d'utiliser l'application. La modification de ce fichier pouvant être ardue, la suppression
est l'option choisie dans un soucis de facilité d'installation.

* Copier le fichier /config/gunicorn dans le dossier /etc/nginx/sites-enabled::

	# cp /config/gunicorn /etc/nginx/sites-enabled/
	
Ce fichier contient les paramêtres permettant à nginx de servir des applications proposées par
gunicorn.

* Redémarrer nginx::

	# /etc/init.d/nginx restart

Le redémarrage de nginx n'est pas obligatoire (un reload peut être suffisant), cependant le
redémarrage est le moyen le plus sûr pour que le serveur prenne bien en compte les
nouveaux paramètres, ainsi que leur bonne configuration

L'applicaton est maintenant accessible sur le port http (80) du serveur.

Administration de la solution
==============================

Démarrage automatique
~~~~~~~~~~~~~~~~~~~~~~

Pour que le serveur gunicorn démarre automatiquement au démarrage du serveur, le script `gunicornd`
est fourni::

	# cp config/gunicornd /etc/init.d/
	# chmod +x /etc/init.d/gunicornd
	# update-rc.d gunicornd defaults

N.B. Cette procédure n'est applicables qu'à des systèmes à base de distribution Debian GNU/Linux.