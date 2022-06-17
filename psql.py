from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from server_settings import postgresql as settings

import logging

log = logging.getLogger(__name__)

def get_engine_from_settings():
    """
    Sets up database connection from local settings.
    Input:
        Dictionary containing pghost, pguser, pgpassword, pgdatabase and pgport.
    Returns:
        Call to get_database returning engine
    """
    keys = ['pguser','pgpasswd','pghost','pgport','pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')

    return get_engine(settings['pguser'],
                      settings['pgpasswd'],
                      settings['pghost'],
                      settings['pgport'],
                      settings['pgdb'])

def get_engine(user, passwd, host, port, db):
    """
    Get SQLalchemy engine using server_settings.py
    Input:        
        user: Username
        passwd: Password for the database
        host: Hostname of the database server
        port: Port number
        db: database name
    Returns:
        Database engine
    """

    url = f'postgresql://{user}:{passwd}@{host}:{port}/{db}'
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

def get_database():
    """
    Connects to database.
    Returns:
        engine
    """
    try:
        engine = get_engine_from_settings()
        log.info("Connected to PostgreSQL database!")
    except IOError:
        log.exception("Failed to get database connection!")
        return None, 'fail'

    return engine

def get_session():
    """
    Return an SQLAlchemy session
    Input:
        engine: an SQLAlchemy engine
    """
    engine = get_database()
    Session = sessionmaker(bind=engine)
    session = Session()
    return session 

db = get_database()
session = get_session()
Base = declarative_base()
