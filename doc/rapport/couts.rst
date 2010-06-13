Couts de la solution
#####################

Pour étudier le coût de notre application, nous avons pris en compte
à la fois l'investissement humain et l'investissement logiciel (cout des
licences etc.)

Investissement Humain :
-----------------------

Coût en jour homme:

======================  ===================================================
Cout (en jours homme)   Taches
======================  ===================================================
4                       Analyse(modélisation, mokups)
4                       Développement de l'interface administrateur
2                       Authentification, gestion des droits utilisateur
1/2                     Affichage des graphiques, geolocalisation
4                       Ergonomie du logiciel
20                      Gestion du calendrier
5                       Phase de tests, correction de bugs
1/2                     Mise en production de la solution
4                       Redaction de la documentation
1/2                     Application mobile
1/2                     Export iCal
======================  ===================================================

Total: **43 jours homme**


L'équipe étant constitué de quatre personnes, nous nous sommes réparti le
travail sur un total de 15 jours.

Vosu pouvez vous referrer au diagramme de GANTT pour plus d'informations

.. image:: pictures/Diagram_gantt.png

Pour évaluer les couts, nous evaluons à 100 euros/jour le cout d'un developpeur
en entreprise.

Le developpement de TIMETABLEEASY à donc eu un coût de "main d'oeuvre", de 40
(jours) * 100 (€) = 4300€.


Investissement Logiciel :
-------------------------

Nous nous sommes appuyé uniquement sur des outils open source pour la *
réalisation de TIMETABLEEASY, ce qui fixe le coût des licences à 0.

Par contre, il est necessaire de prendre en compte le coût des serveurs utilisés
pour deployer la solution.


Etude de la concurence et fixation d'un prix pour TIMETABLEEASY:
-----------------------------------------------------------------

Le premier concurent à notre logiciel est hyperplanning.
Bien implenté dans le monde de l'éducation francaise ils fixent les tarifs
via un forfait annuel ou en vendant la licence de son logiciel.

Trois types d'offre sont disponibles :

    - Monoposte avec un seul poste possédant la capacité d'administrer
      le systeme de planning à 1140 euro HT annuel ou 3406 euro HT pour une
      licence "à vie".
    - Reseaux local à 2376 euro HT à l'année, 7114 euro HT à vie
    - Reseau local et internet à 3406 euros à l'année et 10204 euro HT à vie.

Pour pouvoir mettre en ligne les plannings, le client devra s'offrir un hebergement
non compris dans l'offre elle même.

Au niveau des fonctionalités, hyperplanning possède une fonction pour comptabiliser
l'absence et la présence des élèves que nous ne possédont pas.

En revanche nous possédons une capacité à gérer plusieurs universités, la géolocation
des différentes universités et autres lieux, la représentation graphique de nos informations
(hors calendrier), et un plus large panel de types d'utilisateurs.

Etant donnée le faible demande, hyperplanning et ses concurent répondant déjà à une bonne
part du marché, et nous devons nous aligner sur les prix du marché.

Un prix de 2000 euro HT me parait correct aux vues des fonctionnalités proposées et nous
permettrai au bout de 2 ventes de rembourser l'investissement que nous avons fait.

Chaque client sera libre de demander une personnalisation, ou l'ajout de modules complémentaires
à un pris forfaitaire permettant au différents développeurs de maintenir et d'enrichir
l'application.

L'hebergement n'est pas inclus dans le prix du logiciel. Nous proposons des forfaits qui 
permettent d'essayer le logiciel sur des courtes durées, pour ensuite s'engager.
