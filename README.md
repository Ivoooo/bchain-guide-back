# blockchain-guide-back

How to get started:

1. Install python if needed, try python3 --verison to make sure

2. Go to the directory you downloaded this repo into ( cd .. )

3. To install all needed libraries run the following command:

pip install -r requirements.txt

4. Before running the website you need to initialize the database:

python3 manage.py makemigrations
python3 manage.py migrate

5. Now you can run the server:

python manage.py runserver
