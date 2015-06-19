import os
dbuser = os.environ.get('POCKET_CHANGE_DB_USER')
dbpasswd = os.environ.get('POCKET_CHANGE_DB_PASSWORD')
SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{passwd}@localhost/pocket_change'.format(user=dbuser, passwd=dbpasswd)
APP_HOST = '127.0.0.1'
APP_PORT = '5000'
SECRET_KEY = 'abcdefg1234567890'
