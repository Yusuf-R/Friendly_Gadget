import urllib
from os import getenv

from models.base import Base
from models.model import Model
from models.brand import Brand
from models.features import Features
from models.secondary_features import Secondary

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


usr = "root"
pswd = "Remisql@91"
db = "fg_db"
host = "localhost"

pd_encd = urllib.parse.quote_plus(pswd)
engine = create_engine(
    "mysql+mysqldb://{}:{}@{}/{}".format(usr, pd_encd, host, db),
    pool_pre_ping=False,
    echo=False,
)
engine.connect()

clx = {
    "Model": Model,
    "Brand": Brand,
    "Features": Features,
    "Secondary": Secondary,
}

Session = sessionmaker(bind=engine)


class DBStorage:
    """interaacts with the MySQL database"""

    __engine = None

    __session = Session()
    obj_inst = {}

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB
            ),
            pool_pre_ping=False,
            echo=False,
        )

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in clx:
            if cls is None or cls is clx[clss] or cls is clss:
                objs = self.__session.query(clx[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def get(self, cls, id):
        """returns the object based on the class name and id"""
        if cls and id:
            key_name = "{}.{}".format(cls.__name__, id)
            return self.all(cls).get(key_name)
        return None

    def count(self, cls=None):
        """counts the number of objects in fle storage"""
        if cls:
            return len(self.all(cls))
        else:
            return len(self.all())
