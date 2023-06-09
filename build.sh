echo "Build Start"
python3.9 -m pip install -r requirements.txt
echo "Moving Static"
python3.9 manage.py collectstatic --noinput --clear
echo "making migrations"
python3.9 manage.py makemigrations
echo "migrating"
python3.9 manage.py migrate
echo "End"