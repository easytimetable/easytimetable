Documentation utilisateur
#########################

Utilisation de la solution
==========================

Fonctionnalités Communes
------------------------

* Créer, Lister, Afficher, Modifier, Supprimer ses propres évènements.

.. image:: pictures/calendar.jpg
   :width: 33%
.. image:: pictures/eventAdd.jpg
   :width: 33%
.. image:: pictures/eventMod.jpg
   :width: 33%

* Lister et Afficher les Universités, les Campus, les Places

.. image:: pictures/locationsList.jpg
   :width: 80%
   
* Lister et Afficher les Cursuses, les Study Periods, les Subjects

.. image:: pictures/pedagogyList.jpg
   :width: 80%
   
* Lister et Afficher les Classgroups, les Students, les Campus Managers, les Teachers

.. image:: pictures/userManagementList.jpg
   :width: 80%
   
* Lister des évènements à venir (interface mobile)

.. image:: pictures/eventsList.jpg
   :width: 80%
   
* Exporter son planning au format iCal.

.. image:: pictures/iCal.jpg
   :width: 80%

* Se déconnecter.

.. image:: pictures/deauth.jpg
   :width: 80%

Autres Fonctionctionnalités
---------------------------

Lorsqu'un élément de `Locations` est affiché (Université, Campus, Place), sa localisation
géographique est affichée sur une carte.

.. image:: pictures/locationsShow.jpg
   :height: 400px

Lorsqu'une `Study Period` ou un `Subject` sont affichés, un graphique expliquant la répartition
des contenus apparait (en camembert pour `Subject`, et en barre pour `Study Period`).

.. image:: pictures/pedagogyShow.jpg
   :height: 400px

Niveaux de privilèges
---------------------

Utilisateur non authentifié
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un utilisateur non authentifié ne peut que lister :

* Les Universités

* Les Campus

* Les Places

* Les Cursuses

* Les Study Periods

* Les Subjects

Aucune des autres actions ne lui sont possibles, à part s'authentifier.

.. image:: pictures/noauth.jpg
   :width: 80%

Elève
~~~~~~

Un élève ne gère que son propre planning.

Il est associé à un classgroup.

Ses fonctionnalités sont uniquement les fonctionnalités communes.

Intervenant
~~~~~~~~~~~~

Un intervenant est chargé de dispenser des cours.

Il gère son propre planning, mais il est aussi associé à des cours.

Ses fonctionnalités sont uniquement les fonctionnalités communes.

Campus Manager
~~~~~~~~~~~~~~

Un campus manager gère un campus, les places et les classgroups associés.

Il peut donc, en plus des fonctionnalités communes :

* Créer, lister, modifier, Supprimer

	* Les Places associées à son campus.
	
	* Les Classgroups
	
	* Les Students
	
	* Les Teachers

.. image:: pictures/classgroupCRUD.jpg
   :width: 80%

Administrateur
~~~~~~~~~~~~~~

L'administrateur peut Créer, Lister, Modifier ou Supprimer tous les éléments
de l'application sauf les évènements personnels d'autres utilisateurs.

Il ne peut effectuer aucune action concernant un évènement personnel d'un
autre utilisateur.
