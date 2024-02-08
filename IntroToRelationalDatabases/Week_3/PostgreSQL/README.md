## PgAdmin Note:
Remember to add the bin to your path inside pgadmi, you can do this in the file > preferences > path and then just add the path to the bin. 
## PSQL Notes
Psql basically is a terminal tool to interact with postgres. Remember, pgadmin is a graphical interface to interact with postgres. You can use both to interact with your databases. 

#### Psql important commands:
- Connecting to postgres
```
# Inside powershell, cmd or psql
psql -U username -d database_name -p port_number(ex. 1234) -f path to sql file (if you want to create a database or table)
```
  - The parameter -f is optional for example if your database is already populated with tables.
  - There are other letter parameters to access your database.

- Dumping/Backing up files
```
# Inside powershell, cmd or psql
pg_dump -U username -h host(localhost) - d database_name -p port(ex. 1234) > file_name.sql
```
   - In the > section, you can also type down the path to where you want the dump.
   - Also what I did here was cd to my working directoty and then just placeed the '> file_name.sql' 
