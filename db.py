# Move These secrets to Env Varibles
POSTGRES_URL= 'postgres.cluster-cm4hfr3bgsvb.us-east-1.rds.amazonaws.com:5432'
POSTGRES_USER= 'postgres'
POSTGRES_PW = 'aYz0PDD9bWSfAchKL44G'
POSTGRES_DB = 'postgres'
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
DEBUG = True

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)



