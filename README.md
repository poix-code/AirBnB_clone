<h1>0x00. AirBnB clone - The console<h1>
<hr>

<h2>Description</h2>
<p>This is the first step towards building our first full web application: the AirBnB clone.</p>

<p>A command interpreter to manage our Airbnb clone objects:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc…</li>
<li>Do operations on objects (count, compute stats, etc…)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>
<h5>Example 1 | help command in interactive mode</h5>

<pre>
<code>
"emacs:AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all
Prints a string representation of all instances, can include class
        name to specify only instances of that class
        Usage: all <class name>

(hbnb)


"
</code>
</pre>

<h5>Example 2 | help command non-interactive mode</h5>

<pre>
<code>
"emacs:AirBnB_clone$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) emacs:AirBnB_cat test_helpsole.py
help
emacs:AirBnB_clone$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

"
</code>
</pre>


</h3>List of allowed functions and system calls</h3>
<h2>Requirements for Python Scripts</h2>
<ul>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly #!/usr/bin/python3</li>
<li>A README.md file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the PEP 8 style (version 1.7 or more)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using wc</li>
<li>All your modules should have a documentation (python3 -c 'print(import("my_module").doc)')</li>
<li>All your classes should have a documentation (python3 -c 'print(import("my_module").MyClass.doc)')</li>
<li>All your functions (inside and outside a class) should have a documentation (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')</li>
</ul>
<h2>Requirements for Python unit tests</h2>
<ul>
<li>Allowed editors: vi, vim, emacs</li>
<li>All your files should end with a new line</li>
<li>All your test files should be inside a folder tests</li>
<li>You have to use the unittest module</li>
<li>All your test files should be python files (extension: .py)</li>
<li>All your test files and folders should start by test_</li>
<li>Your file organization in the tests folder should be the same as your project: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py for models/user.py, unit tests must be in: tests/test_models/test_user.py</li>
<li>All your tests should be executed by using this command: python3 -m unittest discover tests</li>
<li>You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py</li>
<li>All your modules should have a documentation (python3 -c 'print(import("my_module").doc)')</li>
<li>All your classes should have a documentation (python3 -c 'print(import("my_module").MyClass.doc)')</li>
<li>All your functions (inside and outside a class) should have a documentation (python3 -c 'print(import("my_module").my_function.doc)' and python3 -c 'print(import("my_module").MyClass.my_function.doc)')</li>
</ul>
<hr>
<table>
<thead>
<tr>
<th>File</th>
<th>Task</th>
</tr>
</thead>
<tbody>
<tr>
<td>AUTHORS</td>
<td>The authors page</td>
</tr>
<tr>
<td>README.md</td>
<td>Read me file</td>
</tr>
<tr>
<td>tests</td>
<td>Unit Test</td>
</tr>
<tr>
<td>base_model.py</td>
<td>a parent class for initialization, serialization and deserialization for new instances</td>
</tr>
<tr>
<td>file_storage.py</td>
<td>abstract storage engine</td>
</tr>
<tr>
<td>console.py</td>
<td>program to handles a command interpreter</td>
</tr>
<tr>
<td>user.py</td>
<td>class user that inherits from BaseModel</td>
</tr>
<tr>
<td>state.py</td>
<td>class state that inherits from BaseModel</td>
</tr>
<tr>
<td>city.py</td>
<td>class city that inherits from BaseModel</td>
</tr>
<tr>
<td>amenity.py</td>
<td>class amenity that inherits from BaseModel</td>
</tr>
<tr>
<td>place.py</td>
<td>class place that inherits form BaseModel</td>
</tr>
<tr>
<td>review.py</td>
<td>class review that inherits from BaseModel</td>
</tr>
</body>
</table>
<hr>
<h3>AUTHORS</h3>
<p>Juan Uribe 1996@holbertonschool.com</p>
<p>Hector Orozco 2066@holbertonschool.com</p>
<br>
<hr>