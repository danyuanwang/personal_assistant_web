export DBHOST="localhost"
export DBPORT="5432"
export DBUSER="personal_assistant_db_admin"
export DBNAME="personal_assistant_db"
export DBPASS="covidhub@io"

echo Please make sure the database $DBNAME has been created on $DBHOST
echo and db user $DBUSER has been set with pwd = $DBPASS
echo Please run the following SQL to do so:
if test $DBPORT == 5432
then 
echo sudo -u postgres psql 
echo CREATE DATABASE $DBNAME \;
echo CREATE ROLE $DBUSER WITH ENCRYPTED PASSWORD \'$DBPASS\'\;
echo ALTER ROLE $DBUSER WITH LOGIN SUPERUSER INHERIT CREATEDB CREATEROLE REPLICATION\;
echo GRANT ALL PRIVILEGES ON DATABASE $DBNAME TO  $DBUSER\;
echo ALTER ROLE $DBUSER SET client_encoding TO 'utf8'\;
echo ALTER ROLE $DBUSER SET default_transaction_isolation TO 'read committed'\;
echo ALTER ROLE $DBUSER SET timezone TO 'UTC'\;
else 
echo psql -h $DBHOST -p $DBPORT -d $DBNAME -U $DBUSER -W 
fi

python manage.py collectstatic

sudo rm /etc/nginx/sites-enabled/django_nginx_personal_assistant_web.conf
sudo rm /etc/nginx/sites-available/django_nginx_personal_assistant_web.conf
sudo ln -s $PWD/django_nginx.conf /etc/nginx/sites-available/django_nginx_personal_assistant_web.conf
sudo ln -s $PWD/django_nginx.conf /etc/nginx/sites-enabled/django_nginx_personal_assistant_web.conf
#sudo rm /etc/uwsgi/apps-enabled/django_uwsgi.ini
#sudo ln -s $PWD/django_uwsgi.ini /etc/uwsgi/apps-enabled/
sudo rm /etc/systemd/system/gunicorn_personal_assistant_web.socket
sudo ln -s $PWD/gunicorn_personal_assistant_web.socket /etc/systemd/system/
sudo rm /etc/systemd/system/gunicorn_personal_assistant_web.service
sudo ln -s $PWD/gunicorn_personal_assistant_web.service /etc/systemd/system/
#sudo service uwsgi restart
sudo systemctl daemon-reload
sudo systemctl restart gunicorn_personal_assistant_web.socket
sudo systemctl enable gunicorn_personal_assistant_web.socket
sudo systemctl status gunicorn_personal_assistant_web.socket
sudo systemctl restart gunicorn_personal_assistant_web.service
sudo systemctl enable gunicorn_personal_assistant_web.service
sudo systemctl status gunicorn_personal_assistant_web.service
#sudo rm /etc/supervisor/conf.d/personal_assistant_web.conf
#sudo ln -s $PWD/supervisor.conf /etc/supervisor/conf.d/personal_assistant_web.conf
#sudo supervisorctl reread
#sudo supervisorctl update
sudo service nginx restart

echo ::
echo pleas note nginx is configed to server traffic for 'askbob.test' for this website
echo consider add '127.0.0.1 askbob-test' into your /etc/hosts, 
echo and edit /etc/nsswitch.conf to 'hosts: files mdns4_minimal [NOTFOUND=return] dns' 
echo so you can use the domain name to test

