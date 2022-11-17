from peewee import *

db = PostgresqlDatabase('phonebook', user='llam', password='12345', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Contact(BaseModel):
  first_name = CharField()
  last_name = CharField()
  phone_number = CharField()