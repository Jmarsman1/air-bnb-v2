#!/usr/bin/python3
"""Class of database storage"""


class DBStorage:
    import os
    from sqlalchemy import MetaData
    from sqlalchemy.orm import Session
    meta = MetaData()
    database_url = os.environ.get('HBNB_MYSQL_DB', )
    sql_pwd = os.environ.get('HBNB_MYSQL_PWD', )
    sql_usr = os.environ.get('HBNB_MYSQL_USER', )
    sql_host = os.environ.get('HBNB_MYSQL_HOST', 'localhost')
    env = os.environ.get('HBNB_ENV')
    
    """Database storage class"""
    __engine = None
    __session = None
    def __init__(self):
        """Instatntiates db storage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
        if env == "test":
            for tbl in reversed(meta.sorted_tables):
                engine.execute(tbl.delete())

    def all(self, cls=None):
        """query on the current database session"""
        session = Session(self.__engine)
        some_dict = {}
        key = obj.__class__.__name__ + "." + obj.id
        some_dict[key]=obj

    def new(self, obj):
        """add obj to current db"""
    
    def save(self):
        """commit all changes"""

    def delete(self, obj=None):
        """del obj if exists"""
        if obj is not None:
            # create key to check if it exists
            key = obj.__class__.__name__ + "." + obj.id
            # if key in the dictionary then we use the key to delete the obj
            if key in self.__objects:
                self.__objects.pop(key)
        else:
            return

    def reload(self):
        """Reload it"""        