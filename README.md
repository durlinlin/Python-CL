# Contacts
 Python built contacts list, using a SQL database with PeeWee models
 ## To Start
 Run <b>psql postgress</b> in your terminal and create the database 'phonebook'
 ```
 CREATE DATABASE phonebook
```
Next run <b>pipenv shell</b> for the root directory and then run
```
python3 app.py
```
This would then prompt 
```
Hello! What would you like to do today?

To continue please enter
View (to view contacts)
Find (to find a contact)
Add (to add a new contact)
Exit (to exit the application)

Input here: 
```
Insert your desired input to obtain your desired outcomes.
| Input | Endpoint    |
| ------ | ----------- |
| View    | Lists all contacts      |
| Find    | Help search a contact based on their first name |
| Add     | Prompts to add a new contact |
| Exit    | Exits the session |
