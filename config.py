import os


class BaseConfig:
    """Base configuration."""

    '''
    os.getenv() method in Python returns the value of the environment variable key if it exists 
    otherwise returns the default value.

    Syntax: os.getenv(key, default = None)
    Parameters:
        key: string denoting the name of environment variable
        default (optional) : string denoting the default value in case key does not exists. 
                             If omitted default is set to ‘None’.

    Return Type: This method returns a string that denotes the value of the environment variable key. In case key does not exists it returns the value of default paramete
    '''

    SECRET_KEY = os.getenv('SECRET_KEY', 'asdfghjkl123456')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SESSION_TYPE = 'filesystem'