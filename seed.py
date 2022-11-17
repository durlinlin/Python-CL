from models import *

db.connect()
db.drop_tables([Contact])
db.create_tables([Contact])

Contact(first_name='Keanu', last_name='Reeves', phone_number='234-233-6780').save()
Contact(first_name='Anne', last_name='Hathaway', phone_number='983-283-2199').save()
