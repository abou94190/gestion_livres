# gestion_livres

Library Manager est une application Python simple pour gérer une collection de livres. Elle permet d'ajouter, de retirer et de rechercher des livres, ainsi que de lister tous les livres de la bibliothèque.

## Structure du Projet

library_manager/

├── library/

│ ├── init.py

│ ├── book.py

│ ├── library.py

├── tests/

│ ├── init.py

│ ├── test_book.py

│ ├── test_library.py

│ ├── test_fonctionnel.py

│ ├── test_integration.py

├── .github/

│ ├── workflows/

│ ├── python-app.yml

└── README.md


## Installation

Pour installer et utiliser ce projet, suivez ces étapes :

1. Clonez le dépôt :

   ```bash/powershell
   git clone git@github.com:abou94190/gestion_livres.git
   cd library_manager

2. Créer un environnement virtuels :
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

3. Installez les dépendances (si vous avez un fichier requirements.txt, ajoutez-le et mettez les dépendances dans ce fichier) :

bash

pip install -r requirements.txt

# Tests

Pour exécuter les tests, utilisez la commande suivante :

bash

python -m unittest discover -s tests
