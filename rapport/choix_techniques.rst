Choix techniques
##################

Pour la réalisation de ce projet, nous nous appuyons sur la stabilité et 
les possibilités offertes par les logiciels libres.

"TimeTableEasy" étant particulièrement spécifique, afin d'accroître notre 
vitesse de développement, nous avons choisi de nous appuyer sur des composants 
déjà existants, ainsi que sur des frameworks.

Après une analyse du besoin et la modélisation des données, nous avons jugé que 
l'utilisation du langage Python nous permettrait d'aller à l'essentiel, et de 
gagner en efficacité. 
Associé au framework web Django, nous avons pu nous appuyer sur l'expérience 
accumulée de milliers de développeurs et d'utilisateurs à travers le monde, 
mais aussi de l'appui d'une communauté extrêmement active.

Afin de bien pouvoir comprendre nos choix techniques, nous allons vous présenter nos choix par rapport à la liste des fonctionnalités que nous proposons dans
TIMETABLEEASY:

- Dans le cas de la gestion des utilisateurs nous avons utilisé 
  django.contrib.auth (module du framework Django s'occupant de 
  l'authentification) associé à un système personnalisé d'ACL 
  (Access Control List).

- Pour l'interface d'administration permettant la gestion des cursus, 
  des campus, des classes et des étudiants nous avons créé une application
  Django réutilisable, factorisant les fonctionnalités de création, 
  modification, liste et suppression (CRUD) d'éléments.

- Pour la gestion des lieux et des campus nous avons utilisé l'API Google 
  maps afin d'en offrir une représentation géographique.

- Pour les cursus, les périodes d'étude et les matières nous avons utilisé 
  la bibliothèque graphique Javascript "HighCharts", permettant ainsi de mettre
  en valeur les informations qui nous semblaient pertinentes.

- Pour les gestion du planning, nous avons choisi de nous appuyer sur une extension au framework javascript jQuery nommée FullCalendar. 

- Pour l'export au format iCal, nous utilisons une bibliothèque Python, vobject.

Il est possible d'héberger notre solution sur des machines dédiées, 
sur des Systèmes d'exploitations tels que Microsoft Windows, des Unixs 
(nous utilisons FreeBSD pour notre serveur de test) et GNU/Linux.

Nous préconisons l'utilisation de solutions BSD ou Linux pour le gain en coût
que cela implique, et pour le cout de maintenance à venir. Il est également
possible d'héberger notre solution sur le Cloud de Google ou sur Amazon EC2, si
l'on souhaite pouvoir prévoir les futures montées en charge des serveurs.


Nous avons également utilisé, pour faciliter notre travail collaboratif, le 
système de gestionnaire de versions git.

GIT
===

Git est un gestionnaire de versions décentralisé, dont le principal
avantage est de bien savoir "merger". Cela signifie qu'il est possible de
travailler en même temps à plusieurs sur le même fichier, sans que cela pose
énormément de problèmes.

Python
======

Python est un langage simple, concis et précis, qui permet d'aller à l'essentiel.

C'est un langage de script qui est notamment utilisé pour des sites à
fortes charges, tels que Google et YouTube par exemple. Un des gros avantages de
python est qu'il est facile à prendre en main, et dispose d'une communauté très
active, proposant très souvent des bibliothèques, en accès libre et gratuit, via
le Python Package Index (PyPI).

Python est un language orienté objet qui favorise la programmation impérative
structurée.

Python est un language qui permet de travailler plus efficacement, et d'intégrer
des solutions de manière rapide. Quiconque peut apprendre à utiliser Python et
ressentir des gains de productivité immédiats et de réduire ses coûts de
maintenance.

Un autre avantage lié à l'utilisation de Python est qu'il fonctionne sur la
plupart des plateformes informatiques, de Windows à Unix, en passant par Linux,
MacOS ou même le JRE de Java ou le CLR de .NET.

Django
======

Il existe plusieurs frameworks Web écrits en python, et qui profitent des atouts
de ce langage, nous avons avons choisi de nous baser sur Django, pour plusieurs
raisons: 


 * Django est un framework *full stack*, ce qui signifie que l'ensemble des
   composants qui le composent interagissent de manière efficace.

 * Au niveau des membres de l'équipe que nous avons choisi de constituer, 3
   membres sur quatre avaient une expérience de Python, et souhaitaient utiliser
   cette opportunité pour découvrir Django et Python plus en profondeur

 * De plus, il s'agit d'un outil qui à dores et déjà fait ses preuves, puisque
   de nombreux sites à forte charge l'utilisent.

Django est connu pour être un outil qui facilite la productivité des
développeurs, et qui apporte énormément de solutions aux problèmes rencontrés de
manière récurrente lors de la mise en place de sites web.

De plus, Django à son propre écosystème, et de nouvelles applications (au sens
de modules que l'on peut ajouter ou enlever) voient le jour ou sont mises à jour
toutes les heures.
 
HTML 
====

Le HTML est sûrement la manière incontournable de présenter du contenu dans des
pages web. Alors que nous aurions pu utiliser des technologies qui ajoutent une
sur-couche à HTML (Flash, Silverlight), nous avons choisi d'utiliser le plein
potentiel de HTML. Cela permet entres autres d'avoir un contenu accessible
facilement, et de manière sémantique. Il nous est ainsi possible de changer la
représentation de ces données uniquement en modifiant les feuilles de styles qui
s'occupent du design de l'application.

Javascript / jQuery
===================

Pour ce qui est de l'affichage des données, nous avons choisi d'utiliser le
couple désormais connu HTML + Javascript. jQuery est un framework javascript
qui permet de simplifier l'utilisation de javascript. jQuery propose également
une API qui permet de factoriser certaines utilisations courantes en
javascript, par exemple pour ce qui concerne les requêtes dites "Ajax", ou la
manipulation du DOM.

Outre le fait que Javascript soit plus facile d'accès grâce à jQuery, celui ci
est grandement enrichi par le fait qu'il s'agisse d'un logiciel libre,
bénéficiant ainsi d'une communauté grandissante et active, qui propose chaque
jour de nouveaux plugins, pour tous les usages que l'on peut imaginer, un peu à
la manière de Django.

Blueprint CSS
=============

CSS est un langage qui sert à décrire la présentation des documents HTML et
XML. Un des principal défaut de CSS est relatif aux logiciels que l'on
utilise pour naviguer sur internet. Chacun à ses spécificités, et cela rends
difficile de créer des feuilles de style qui sont compatibles avec l'ensemble de
ces navigateurs.

Blueprint CSS propose entres autres de résoudre ce problème, et apporte
également un système de représentation des pages web en grilles. Il devient
alors possible de s'abstraire des problématiques bas niveau et de travailler
directement avec une représentation en grille.

JSON
====

JSON signifie "Javascript Object Notation", et il s'agit d'un format de données
textuel, qui est implémenté dans énormément de langages, et notamment Python et
javascript sont capable de transformer des objets JSON en objets javascript ou
python, et inversement.


FullCalendar
============

FullCalendar est un plugin jQuery qui permet d'afficher de manière simple des
évènements au sein d'un calendrier. Il possède plusieurs vues (mois, semaine et
jour), et permet la communication avec le format JSON. 


Les APIs Google Maps
====================

Afin de représenter les adresses dans notre logiciel, nous nous appuyons sur la
très simple API Google Maps, qui nous permet d'afficher des images avec les
adresses que nous souhaitons.
