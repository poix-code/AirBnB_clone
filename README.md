<h1>0x00. AirBnB clone - The console</h1>
<br>
<hr>
<h3>Description</h3>
<h4>This is the first step towards building our first full web application: the AirBnB clone.</h4>

<h4>A command interpreter to manage our Airbnb clone objects:</h4>

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
Example 1 | help command in interactive mode
emacs:AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all
Prints a string representation of all instances, can include class
        name to specify only instances of that class
        Usage: all <class name>

(hbnb)

Example 2 | help command non-interactive mode

emacs:AirBnB_clone$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) vagrant:AirBnB_cat test_helpsole.py
help
emacs:AirBnB_clone$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update


List of allowed functions and system calls
Requirements for Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7 or more)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(import("my_module").doc)')
All your classes should have a documentation (python3 -c 'print(import("my_module").MyClass.doc)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')
Requirements for Python unit tests
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
You have to use the unittest module
All your test files should be python files (extension: .py)
All your test files and folders should start by test_
Your file organization in the tests folder should be the same as your project: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py for models/user.py, unit tests must be in: tests/test_models/test_user.py
All your tests should be executed by using this command: python3 -m unittest discover tests
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
All your modules should have a documentation (python3 -c 'print(import("my_module").doc)')
All your classes should have a documentation (python3 -c 'print(import("my_module").MyClass.doc)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')

File	Task

AUTHORS Juan Uribe <1996@holbertonschool.com>
        Hector Orozco <2066@holbertonschool.com>
	the authors page

README.md read me file

TESTS unittest.
<br>
<hr>
