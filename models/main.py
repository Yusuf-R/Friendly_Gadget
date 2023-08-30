import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.brand import Brand
from models.model import Model, Base
from models.features import Features
from models.data import apple_data, samsung_data, spec_iphone_14
from models.secondary_features import Secondary
from models import storage


usr = "root"
pswd = "Remisql@91"
db = "fg_db"
host = "localhost"

pd_encd = urllib.parse.quote_plus(pswd)
engine = create_engine(
    "mysql+mysqldb://{}:{}@{}/{}".format(usr, pd_encd, host, db),
    pool_pre_ping=True,
    echo=False,
)
engine.connect()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables
Base.metadata.create_all(engine)


clx = {
    "Model": Model,
    "Brand": Brand,
    "Features": Features,
    "Secondary": Secondary,
}


def create_brands(data):
    """Create a new brands"""
    if data == "" or data is None or data == []:
        print("data cannot be empty")
        return
    try:
        if type(data) is str:
            obj = Brand()
            obj.brand_name = data
            session.add(obj)
            session.commit()
            session.close()
            return
        elif type(data) is list:
            for brand in data:
                obj = Brand()
                obj.brand_name = brand
                session.add(obj)
                session.commit()
                session.close()
            return
    except TypeError:
        print("data must be a string or a list of strings")
        return


def create_models(brand_id, data):
    """Create a new model for a particular brand"""
    for brand in data:
        for value in brand.values():
            obj = Model()
            obj.model_name = value
            obj.brand_id = brand_id
            session.add(obj)
            session.commit()
    session.close()


def create_features(model_id, data=None):
    """Populate features for a given model based on it's id"""

    feat = [
        "PhoneDetails",
        "LaunchDetails",
        "NetworkDetails",
        "DisplayDetails",
        "BodyDetails",
        "PlatformDetails",
        "Processor",
        "ChipSet",
        "MemoryDetails",
        "MainCamera",
        "SelfieCamera",
        "Battery" "Purpose",
    ]

    if data is None:
        obj = Features()
        obj.model_id = model_id
        session.add(obj)
        session.commit()
        session.close()

    if data is not None:
        obj = Features()
        obj.model_id = model_id
        session.add(obj)
        session.commit()
        for column_data in feat:
            if column_data in data:
                setattr(obj, column_data, data[column_data])
                if isinstance(data[column_data], dict):
                    for key, value in data[column_data].items():
                        secondary_entry = Secondary()
                        secondary_entry.feature_id = obj.id
                        secondary_entry.inner_key = key
                        secondary_entry.inner_value = value
                        session.add(secondary_entry)
        session.commit()
    session.close()


# brands = ["Apple", "Huawei", "Samsung", "Tecno", "Nokia"]
# create_brands(brands)

# apple_id = session.query(Brand).filter_by(brand_name="Apple").first().id
# samsung_id = session.query(Brand).filter_by(brand_name="Samsung").first().id


# create_models(apple_id, apple_data)
# create_models(samsung_id, samsung_data)

# # get the id of iphone 14

iphone_14_id = (
    session.query(Model).filter(Model.model_name == "iPhone 14").first().id
)

create_features(iphone_14_id, spec_iphone_14)

l = []
brands = storage.all(Model).values()
for data in brands:
    if data.features:
        b = data.features
        for c in b:
            l.append(c.to_dict())
    else:
        continue
print(l)

x = storage.count(Brand)
print(x)


# #create_brands("Infinix")
# # y = storage.all(Brand).values()
# # for x in y:
# #   print(x.to_dict())

# v = storage.get(Brand, "1208902f-b221-42b5-901f-45d02243bdf9")
# print(v.id)
