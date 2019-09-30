####################################
Gérer des Environnements avec Conda
####################################

Gérer des environnements avec le gestionnaire de paquet :code:`conda`


Installation
=============

Suivez les instructions 
`d'ici <https://conda.io/projects/conda/en/latest/user-guide/install/index.html>`_

- Testez votre environnement avec :code:`conda --version`

Créer, Activer, Visualiser des Environnements
==============================================

Voici le commande pour la création des environnements.

- :code:`conda create --name nomEnv`
- On peut créer des environnements avec une version spécifique de
  l'interpréteur de python :code:`conda create --name nomEnv python=3.7`
- On peut activer notre environnement avec :code:`conda activate nomEnv`
- On peut désactiver notre environnement avec :code:`conda deactivate`
- On peut visualiser les environnements créés par :code:`conda info --envs` 


Partager des Environnements
============================

On peut partager des environnements par l'intermédiaire des fichiers. Il y a
deux options: :code:`spec-files` ou :code:`environnement.yml`. Le
:code:`spec-file` est spécifique au plateforme, donc il peut créer des
environnements identiques. Le :code:`environnement.yml` n'est pas spécifique
au plateforme et donc :code:`conda` peut installer les paquets adaptés à votre
plateforme, s'ils existent une version dans des canaux par défauts.

On peut créer un :code:`spec-file`:

- :code:`conda list --explicit > nom-de-spec-file.txt`

On peut installer les paquets de :code:`spec-file`:

- :code:`conda create --name monEnv --file nom-de-spec-file.txt`

Notez qu'on donne le nom d'environnement nous même lors qu'on crée
l'environnement à partir du :code:`spec-file`.

On peut créer un :code:`environnement.yml`:

- D'abord notez les environnements déjà installés
- :code:`conda activate monEnv`
- :code:`conda env export > nomEnvironnement.yml`
- :code:`conda create --name monEnv --file nomEnvironnement.yml`
- Voyez le nom de l'environnement soit par :code:`cat nomEnvironnement.yml`
  soit par :code:`conda info --envs`

Installation des Paquets
=========================

Une fois qu'on a crée l'environnement on peut installer des paquets
spécifiques comme suivant:

- :code:`conda install -c nomDeCanal nomDePaquet`

Exemple

- :code:`conda install -c conda-forge scipy`


Exercice
=========

Créez l'environnement dont le nom est :code:`simple` à partir de fichier
:code:`simpleEnv.yml`, puis installez le paquet :code:`pillow` pour lancer
l'application :code:`simple.py`
