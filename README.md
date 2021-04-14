# oc_p5_openfoodfacts
   **Purbeurre**

Program that request data from the OpenFoodFacts API. Sort it out and insert 
it in differents tables. 
The user thanks to command-line interface could select and save the better
 nutriscores' products. 

**About that Readme**  

Those Readme will explain step by step how to copy the project and running him 
on your local machine for testing. 

**Clone the repo** 

git clone https://github.com/SergueiNK/oc_p5_openfoodfacts.git

**Virtual environment creation:**

python3 -m venv .venv

**Dependencies installation**

LINUX

.venv/bin/pip install -r requirements.txt

WINDOBS

cd .venv/Scripts/

pip install -r ../../requirements.txt

**Activation virtual env**

LINUX

source env/bin/activate

WINDOWS

env\Scripts\activate.bat

##** Purbeurre software - Launch**

For connexion et creation of database you need 
to open on your local terminal : python constants.py

In constants.py you need to add your mysql login et password : 

""Creating data base"""
infos_db = {
    'user': 'your-root',
    'password': 'your-password',
    'host': '127.0.0.1'
}

"""Connexion to database"""
infos_db_purbeurre = {
    'user': 'your-root',
    'password': 'your-password',
    'host': '127.0.0.1',
    'database': 'purbeurre'

For launch the creation of database on your local terminal : 
python create_bdd.py

For launch the program on your local terminal : python main.py
