import os 

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True 

SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="notificationsuser", DB_PASS="1234", DB_ADDR="127.0.0.1", DB_NAME="notificationsdb") 
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
