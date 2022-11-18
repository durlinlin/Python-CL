from models import *
from playhouse.shortcuts import dict_to_model, model_to_dict

contactsList = []
for people in Contact.select():
  contactsList.append(model_to_dict(people))

def greeting():
  print('Hello! What would you like to do today?')
  selections()

def selections():
  choice = input('\nTo continue please enter\nView (to view contacts)\nFind (to find a contact)\nAdd (to add a new contact)\nExit (to exit the application)\n\nInput here: ')
  print('')
  if choice.lower() == 'View'.lower():
    print('Your Contacts List:')
    view()
    selections()
  elif choice.lower() == 'Find'.lower():
    find()
    selections()
  elif choice.lower() == 'Add'.lower():
    add()
    selections()
  else:
    print('Session ended')
  
def view():
  for people in contactsList:
    print(f"{contactsList.index(people)+1}. First Name: {people['first_name']}  Last Name: {people['last_name']} Phone #: {people['phone_number']}")

def find():
  search = input('Enter to search by First Name: ')
  for people in contactsList:
    if search.lower() == people['first_name'].lower():
      print(f"{contactsList.index(people)+1}. First Name: {people['first_name']}  Last Name: {people['last_name']} Phone #: {people['phone_number']}")
  else:
    print('Could not find contact')

def add():
  print('Please enter the information for the new Contact')
  new_Contact = Contact(
    first_name = input('First name: '),
    last_name= input('Last name: '),
    phone_number = input('Phone number: ')
  )
  new_Contact.save()
  print(f'New contact {new_Contact.first_name} {new_Contact.last_name} has been saved')

greeting()