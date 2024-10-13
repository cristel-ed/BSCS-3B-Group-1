from functions.database import setup_database
from loginform import open_loginform


setup_database()

if __name__ == '__main__':
    open_loginform()
