from project import mongo


class Products(mongo.Document):
    meta = {'collection': 'products'}

    id = mongo.IntField(null=True, primary_key=True)
    brand = mongo.StringField(required=True)
    description = mongo.StringField(required=True)
    image = mongo.StringField(required=True)
    price = mongo.IntField(required=True)


class CountryRepository:
    def __init__(self):
        self.model = Products
