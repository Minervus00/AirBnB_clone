# HolbertonBnB
## Description of the project
A minified clone of `AirBnB` web site.

## The console
It's command line interface to manage (create, modify or delete) AirBnB objects
The HolbertonBnB console can be run both interactively and non-interactively.

###### How to run and close it
To run the console in non-interactive mode, pipe any command(s) into an execution of the file `./console.py` at the command line. Ex: `$ echo "help" | ./console.py`.
To quit the console, enter the command `quit`, or input an EOF signal (`ctrl-D`/`ctrl-Z` for `ubuntu`/`windows`).

```
$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```

or

```
$ ./console.py
(hbnb) 
(hbnb) quit
$ ./console.py
(hbnb) 
(hbnb) ^D (or ^Z for windows or EOF)
$
```
###### Availabe Commands
- **create** : `create <class>` -> Creates a new instance of the specified class. The class' ID is printed and the instance is saved to the file `file.json`.
- **show**: `show <class> <id>` or `<class>.show(<id>)` -> Prints the string representation of a class instance based on a given id
- **destroy**: `destroy <class> <id>` or `<class>.destroy(<id>)` -> Deletes a class instance based on a given id
- **all**: `all` or `al <class> <id>` or `<class>.all(<id>)` -> Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.
- **update**: `update <class> <id> <attribute name> "<attribute value>"` or `<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(<id>, <attribute dictionary>)` -> Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs.
- **count**: Retrieves the number of instances of a given class

###### Examples
```
$ ./console.py
(hbnb) create BaseModel
119be863-6fe5-437e-a180-b9892e8746b8
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2022-10-31T21:30:42.215277", "created_at": "2022-10-31T21:30:42.215277", "__class__": "BaseModel", "id": "119be863-6fe5-437e-a180-b9892e8746b8"}}
$ ./console.py
(hbnb) create User
1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb)
(hbnb) show User 1e32232d-5a63-4d92-8092-ac3240b29f46
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-ac3240b29f46', 'created_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828), 'updated_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828)}
(hbnb) 
(hbnb) User.show(1e32232d-5a63-4d92-8092-ac3240b29f46)
[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-ac3240b29f46', 'created_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828), 'updated_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828)}
(hbnb) all
["[BaseModel] (119be863-6fe5-437e-a180-b9892e8746b8) {'id': '119be863-6fe5-437e-a180-b9892e8746b8', 'created_at': datetime.datetime(2022, 10, 31, 21, 30, 42, 215277), 'updated_at': datetime.datetime(2022, 10, 31, 21, 30, 42, 215277)}", "[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-ac3240b29f46', 'created_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828), 
'updated_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828)}"]
(hbnb) all User or User.all()
["[User] (1e32232d-5a63-4d92-8092-ac3240b29f46) {'id': '1e32232d-5a63-4d92-8092-ac3240b29f46', 'created_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828), 'updated_at': datetime.datetime(2022, 10, 31, 21, 34, 3, 635828)}"]
(hbnb) destroy User 1e32232d-5a63-4d92-8092-ac3240b29f46
(hbnb) all User or User.all()
(hbnb) 
(hbnb) count User or User.count()
0
(hbnb) count BaseModel or BaseModel.count()
1
(hbnb) update BaseModel 119be863-6fe5-437e-a180-b9892e8746b8 first_name "Bond"
["[BaseModel] (119be863-6fe5-437e-a180-b9892e8746b8) {'id': '119be863-6fe5-437e-a180-b9892e8746b8', 'created_at': datetime.datetime(2022, 10, 31, 21, 30, 42, 215277), 'updated_at': datetime.datetime(2022, 10, 31, 21, 30, 42, 215277), 'first_name': 'Bond'}"]
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.119be863-6fe5-437e-a180-b9892e8746b8": {"updated_at": "2022-10-31T21:30:42.215277", "created_at": "2022-10-31T21:30:42.215277", "__class__": "BaseModel", "id": "119be863-6fe5-437e-a180-b9892e8746b8", "first_name": "Bond"}}
$ 
```
