from peewee import *


db = MySQLDatabase('estates_db', user='root', password='',
                host='localhost', port=3306)
RENT_STATUS = (
    (1,'محلات'),
    (2,'شقق'),
)

class login(Model):
    user_name = CharField()
    password = CharField()
    admin = BooleanField()
    class Meta:
        database = db

class aroud(Model):
    name = CharField()
    phone = CharField()
    date = DateField()
    category = CharField()
    contract = CharField()
    region = CharField()
    address = TextField()
    amount_required = CharField()
    discription = TextField()    
    class Meta:
        database = db

class talabat(Model):
    name = CharField()
    phone = CharField()
    date = DateField()
    category = CharField()
    contract = CharField()
    region = CharField()
    rental_limit = CharField()
    discription = TextField()

    class Meta:
        database = db

class rents(Model):
    owner = CharField()
    owner_id = CharField()
    tenant = CharField()
    tenant_id = CharField()
    date = DateField()
    category = CharField(choices=RENT_STATUS)
    discription = TextField()
    address = TextField()
    cont_term = CharField()
    start = DateField()
    end = DateField()
    rental_value = CharField()
    insurance = CharField()
    purpose = CharField()

    class Meta:
        database = db

class ownership(Model):
    seller = CharField()
    seller_id = CharField()
    buyer = CharField()
    buyer_id = CharField()
    date = DateField()
    category = CharField()
    discription = TextField()
    address = TextField()
    title_deed = CharField() # سند الملكية
    price = CharField()
    advance = CharField() # المقدم
    remain = CharField()  # الباقي
    installments = CharField() # عدد الأقساط
    install_value = CharField() # قيمة القسط
    penalty = CharField() # الشرط الجزائي

    class Meta:
        database = db

db.connect()
db.create_tables([login, aroud, talabat, rents, ownership])
