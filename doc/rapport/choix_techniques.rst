Choix techniques
##################


Pour la réalisation de ce projet, nous nous appuyons sur la "force de frappe" des logiciels libres.

"TimeTableEasy" étant particulièrement spécifique, afin d'accroitre notre vitesse de production nous avons choisi de nous 
appuyer sur des composants déjà écrits, ainsi que des frameworks.
Après une analyse du besoin et la modélisation des données, nous avons jugé que le plus productif serai l'utilisation du lanaguage python 
associé au framework web django 1.1 nous permettent de nous appuyer sur l'expérience accumulée de milions
developpeurs et utilisateurs à travers le monde, mais aussi de l'appui d'une communoté extrement active.


Afin de bien pouvoir comprendre nos choix technique, nous allons vous presenter nos choix par rapport à la liste des fonctionnalité:

- Dans le cas de la gestion des utilisateurs nous avons utilisé django.contrib.auth (module du framework django* s'occupant de l'authentification) associé à un système personalisé d'ACL(Access Control List).

- Pour l'interface d'administration permettant la gestion des cursus, des campus, des classes et des étudiants nous avons créer une classe 
python factorisant les fonctionnalités Create Read Update Delete et donc un maximum de traitements nous faisant ainsi gagner en maintenabilité, vitesse de developpement, et propreté.
    * Pour la gestion des lieux et des campus nous avons utilisé l'API google map afin d'avoir une représentation géographique
    * Pour les cursus, les periodes d'étude et les sujets nous avons utilisé la bibliothèque graphique javascript "HighCharts"
      permettant ainsi une représentation graphique afin de bien voir la place de chaque chose.
- Pour les gestion de vue du planning, nous avons implémenté Fullcalendar*, un calendrier opensource nourrit par du JSON, auquel nous avons rajouté des intéractions en utilisant AJAX via le framework javascript JQuery 1.4.2 .
- Pour l'exportation ical nous avons utilisé une classe qui existait déjà et l'avons implémenté à notre projet.
- Pour l'application mobile, nous avons crée une interface web spéciale au format smartphone afin de garder un maxium de compatibilé sur tous les portables.


Pour la présentation nous avons utiliser HTML5 et CSS3 avec des bibliotèque CSS "superfish" (menu), "awesome buttons", et le framework css blueprint.

Nous avons également utilisé les frameworks on bibliothèques suivantes:


Pour ce qui est de la solution d'hebergement, il est possible d'heberger notre
solution sur des machines dédiées, sur des Systèmes d'exploitations tels que 
Microsoft Windows, des Unixs (la famille des BSD) et des Linux.

Nous préconnisons l'utilisation de solutions BSD ou Linux pour le gain en cout
que cela implique, et pour le cout de maintenance à venir. Il est également
possible d'heberger notre solution sur le Cloud de Google ou sur Amazon EC2, si
l'on souhaite pouvoir prévoir les futures montées en charge des serveurs.


Nous avons également utilisé, pour faciliter notre travail collaboratif, le 
système de gestionnaire de versions git.

GIT
===

Git est un gestionnaire de versions décentralisé, dont la principale
fonctionalité est de bien savoir "merger". Cela signifie qu'il est possible de
travailler en même temps à plusieurs sur le même fichier, sans que cela pose
énormement de problèmes.

Python
======

Python est un langage simple, concis et précis, qui permet d'aller à l'essentiel.

C'est un language de scripts qui est notemment utilisé pour des sites à
fortes charges, tels que Google et YouTube par exemple. Un des gros avantages de
python est qu'il est facile à prendre en main, et dispose d'une communautée très
active, proposant très souvent des bibliothèques, en accès libre et gratuit, via
le Python Package Index (PyPI).

Python est un language orienté objet qui favorise la programmation impérative
structurée.

Python est un language qui permet de travailler plus efficacement, et d'intégrer
des solutions de manière rapide. Quiconque peut apprendre à utiliser python et
ressentir des gains de productivité immediats et réduire ses couts de
maintenance.

Un autre avantage lié à l'utilisation de python est qu'il fonctionne sur la
plupart des plateformes informatiques, de Windows à Unix, en passant par Linux,
MacOS ou même le JRE de Java ou le CLR de .NET.

Django
======

Il existe plusieurs frameworks Web écrits en python, et qui profitent des atouts
de ce langage, nous avons avons choisi de nous baser sur django, pour plusieurs
raisons: 


 * Django est un framework *full stack*, ce qui signifie que l'ensemble des
   composants qui le composent interagissent de manière efficace.

 * Au niveau des membres de l'équipe que nous avons choisi de constituer, 3
   membres sur quatre avaient une experience de python, et souhaitaient utiliser
   cette opportunité pour découvrir django et python plus en profondeur

 * De plus, il s'agit d'un outil qui à dores et déjà fait ses preuves, puisque
   de nombreux sites à forte charge l'utilisent.

Django est connu pour être un outil qui facilite la productivité des
developpeurs, et qui apporte énormement de solutions aux problèmes rencontrés de
manière récurrente lors de la mise en place de sites web.

Egalement, Django à son propre écosystème, et de nouvelles applications (au sens
de modules que l'on peut ajouter ou enlever) voient le jour ou sont mises à jour
toutes les heures.
 
HTML 
====

Le HTML est surement la manière incontournable de présenter du contenu dans des
pages webs. Alors que nous aurions pu utiliser des technologies qui ajoutent une
surcouche à HTML (Flash, Silverlight), nous avons choisi d'utiliser le plein
potentiel de HTML. Cela permet entres autres d'avoir un contenu accessible
facilement, et de manière sémentique. Il nous est ainsi possible de changer la
representation de ces données uniquement en modifiant les feuilles de styles qui
s'occuppent du design de l'application.

Javascript / jQuery
===================

Pour ce qui est du coté affichage des données, nous avons choisi d'utiliser le
couple désormais connu HTML + Javascript. jQuery est un framework javascript
qui permet de simplifier l'utilisation de javascript. jQuery poropose également
une API qui permet de factoriser certaines utilisations courantes en
javascript, par exemple pour ce qui concerne les requêtes dites "Ajax", ou la
manipulation du DOM.

Outre le fait que Javascript soit plus facile d'accès grace à jQuery, celui ci
est grandement enrichi par le fait qu'il s'agisse d'un logiciel libre,
bénéficiant ainsi d'une communauté grandissante et active, qui propose chaque
jour de nouveaux plugins, pour tous les usages que l'on peut imaginer, un peu à
la manière de django.

Blueprint CSS
=============

CSS est un language qui sert à decrire la présentation des documents HTML et
XML. Un des principal défault de CSS est relatif aux navigateurs que l'on
utilise pour naviguer sur internet. Chacun à ses specificités, et cela rends
difficle de créer des feuilles de style qui sont compatibles avec l'ensemble de
ces navigateurs.

Blueprint CSS propose entres autres de résoudre ce problème, et apporte
également un système de représentation des pages web en grilles. Il devient
alors possible de s'abstraire des problématiques bas niveau et de travailler
directement avec une representation en grille.

JSON
====

JSON signigie "Javascript Object Notation", et il s'agit d'un format de données
textuel, qui est implémenté dans énormement de languages, et nottement python et
javascript sont capable de transformer des objets JSON en objets javascript ou
python, et inversement.


FullCalendar
============

FullCalendar est un plugin jQuery qui permet d'afficher de manière simple des
evenements au sein d'un calendrier. Il possède plusieurs vues (mois, semaine et
jour), et permet la communication avec le format JSON. 


Les APIs Google Maps
====================

Afin de représenter les adresses dans notre logiciel, nous nous appuyons sur la
très simple API Google Maps, qui nous permet d'afficher des images avec les
adresses que nous souhaitons.
