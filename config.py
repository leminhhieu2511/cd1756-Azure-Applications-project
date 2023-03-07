import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'fc48Q~WciT4dK1zuGOPYLD6sPD2fhsQKyeUP4azk'

    BLOB_ACCOUNT = 'articleblobstorage'
    BLOB_STORAGE_KEY = 'ACrwjquf5aQmN0tqN8A0P20+ccExK8G7ipQkrQ+LyjU00eByTNqhDyrODlo1m46+MdZg/VqOOgkB+ASttQLKLg=='
    BLOB_CONTAINER = 'articlecms-blob'

    SQL_SERVER = 'article-cms-server.database.windows.net'
    SQL_DATABASE = 'articledbuda'
    SQL_USER_NAME = 'udacity'
    SQL_PASSWORD = 'Hieule2511'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://udacity:Hieule@2511@article-cms-server.database.windows.net:1433?service_name=articledbuda'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://Server=tcp:article-cms-server.database.windows.net,1433;Database=articledbuda;Uid=udacity;Pwd=Hieule@2511;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "kR_8Q~QCkqzLd.55Id5b-a2v5FP0LDirIRwzmbyD"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "7dbc652d-559f-4a21-831a-7cf46bdcb0d6"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session