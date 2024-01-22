## PSQL Notes
Psql basically is a terminal tool to interact with postgres. Remember, pgadmin is a graphical interface to interact with postgres. You can use both to interact with your databases. 

#### Psql important commands:
- Connecting to postgres
```
# Inside powershell or cmd:
psql -U username -d database_name -p port_number(ex. 1234) -f path to sql file (if you want to create a database or table)
```
The parameter -f is optional for example if your database is already populated with tables. 
