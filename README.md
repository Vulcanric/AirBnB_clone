# AirBnB Clone
This project series attempts to create a website similar to the [AirBnB website](https://www.airbnb.com) for the purpose of covering the fundamentals of Higher level development track. And to deploy this web application through a server.
## The project series
Development of the project follows a series of steps to acheive a fully responsive web application. This follows the process:
1. **The Console** - The backend utility tool used for debugging and development.
2. **HTML/CSS templating** - The frontend (static and dynamic).
3. **Database storage** - For persistency.
4. **API** - Provides a communication interface between the front-end and the data
5. **Front-end integration**
**First step: The Console**
### The Console
A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
It's a shell-like command interpreter, but restricted in commands; Its commands are mainly for data manipulation within the program.
#### How to start it
To start the console, first clone the project through its link and change directory to that of the project:
```bash
$ git clone https://github.com/Vulcanric/AirBnB_clone.git
...
$ cd AirBnB_clone
```
Once in, run the `console.py` executable file, you will see a prompt, `(hbnb) `. Now you can use it:
```bash
$ ./console.py
(hbnb) 
```
#### How to use it
To use it, start by typing the `help` command to see all the commands available to the console:
**The Console in interactive mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF	help	quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

**Non-interactive mode:**
```bash
$ echo "help" | ./console.py
(hbnb) 

Documented commands (type help <topic>):
========================================
EOF	help	quit
(hbnb) 
$
```

Please note that the commands available are more than the `EOF`, `help` and `quit` commands seen above.
Type `help <command>` to know more about a command.

#### Examples
```bash
$ ./connsole.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF	help	quit	create	show
destroy	all	update	count

(hbnb) help create

Create an instance of a class and prints out the id of the instance
SYNOPSIS: create <object class>

(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) show BaseModel 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) update BaseModel 2dd6ef5c-467c-4f82-9521-a772ea7d84e9 first_name "Betty"
(hbnb) show BaseModel 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'first_name': 'Betty', 'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb)
(hbnb) destroy BaseModel 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) show BaseModel 2dd6ef5c-467c-4f82-9521-a772ea7d84e9
** no instance found **
(hbnb)
(hbnb) quit
$
```
