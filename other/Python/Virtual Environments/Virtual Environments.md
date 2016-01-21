# Virtual Environments

http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/  
http://docs.python-guide.org/en/latest/dev/virtualenvs/  
https://virtualenv.readthedocs.org/en/latest/


A Virtual Environment is a tool to **keep the dependencies required by different projects in separate places**, by creating virtual Python environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.3 while also maintaining a project which requires Django 1.0

- **virtualenv**
	- Managing Environments (create, delete)
	- Using Environments (source activate, deactivate)
- **Dependencies**
	- Show Dependencies
	- Save Dependencies
	- Install Dependencies
	- toggleglobalsitepackages
- **virtualenvwrapper**
	- Managing Environments (mkvirtualenv, rmvirtualenv)
	- Using Environments (workon, deactivate)

## virtualenv

[virtualenv](https://virtualenv.readthedocs.org/en/latest/) is a tool to **create isolated Python environments**. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Install virtualenv via pip:

```
$ pip install virtualenv
```

### Managing Environments

#### 1. Create

To create a virtual environment for a project, run :

```
$ cd <path_to_directory>
$ virtualenv <envname>
```

This will create a `/envname` folder in the current directory which will contain :

- `/bin` stores the executables - noticeably a new python.
- `/lib` stores the supported libraries for a new environment.
	- `/lib/pythonX.X/site-packages/` contains packages installed in this environment (pip, setuptools and wheel packages are already installed)
- `/include` stores the development headers. 

Most importantly, Python is setup and pip is installed which you can use to install other packages.

The name of the virtual environment (in this case, it was envname) can be anything; omitting the name will place the files in the current directory instead.

##### Choose Python Version

You can specify the Python interpreter to use for the virtual environment : 

```
$ virtualenv --python=<pythonX.X> <envname>
```

This will use the Python version X.X for your virtual environment, providing that the interpreter is actually installed on your machine and the executable is accessible via the command `pythonX.X` (searching in the `PATH` directories).

#### 2. Delete

To delete a virtual environment, just delete its folder:

```
$ cd <path_to_directory>
$ rm -rf <envname>
```

### Using Environments

#### 1. Activate

To begin using the virtual environment, it needs to be activated. Simply `source` the `bin/activate` script that have been created in the envname folder :

	$ source <envpath>/bin/activate

The name of the current virtual environment will now appear on the left of the prompt :

	(envname)$ 

From now on, the `python` and `pip` versions used are the ones from the virtual environment.

```
(envname)$ which python 
<envpath>/bin/python

(envname)$ which pip
<envpath>/bin/pip
```

Any package that you install using `pip` will be placed in the following folder, isolated from the global Python installation.

```
<envpath>/lib/pythonX.X/site-packages/
``` 

### 2. Deactivate

If you are done working in the virtual environment for the moment, you can deactivate it:

	$ deactivate

This puts you back to the system’s default Python interpreter with all its installed libraries.


## Dependencies

### Show Dependencies

You can see the list of installed packages without the requirements format using :

	(envname)$ pip list

### Save Dependencies

In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages. To do this, run :

	(envname)$ pip freeze > requirements.txt

This will create a `requirements.txt` file, which contains a simple **list of all the packages in the current environment, and their respective versions**. 

### Install Dependencies

Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:

	(envname)$ pip install -r requirements.txt

This can help ensure consistency across installations, across deployments, and across developers.

### toggleglobalsitepackages

Run `toggleglobalsitepackages` in the active virtualenv to **toggle access to globally installed Python packages**. By default, global site packages are disabled. 

It is important to enable this access if you want to avoid recompiling recurrent packages such as numpy or scipy for every virtualenv.

	(envname)$ toggleglobalsitepackages
	Enabled global site-packages
	
	(envname)$ toggleglobalsitepackages
	Disabled global site-packages

## virtualenvwrapper

[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) is a set of extensions to *virtualenv* tool.
It provides a set of commands which makes working with virtual environments much more pleasant. It also places all your virtual environments in one place. It require that `virtualenv` is already installed.

- Organizes all of your virtual environments in one place.
- Use a single command (workon) to switch between environments.
- Wrappers for managing your virtual environments (create, delete, copy).
- Tab completion for commands that take a virtual environment as argument.

To install (Full virtualenvwrapper install instructions):

```
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/.virtualenvs
$ source /usr/local/bin/virtualenvwrapper.sh
```
The `WORKON_HOME` variable is the path where *virtualenvwrapper* will store all the environments. Default path is `~/.virtualenvs` which points to a hidden folder that will host your virtualenvs.

### Managing Environments

To _create a new environment_, in the `WORKON_HOME` directory :

```
$ mkvirtualenv [-r requirements_file] <envname>
```
To _remove an environment_, in the `WORKON_HOME` directory :

```
$ rmvirtualenv <envname>
```

### Using Environment

To _activate or change working virtual environments_ :

```
$ workon <envname>
```
To _deactivate the working virtual environments_ :

```
$ deactivate
```

### Other Useful Commands

`$ lsvirtualenv`  
Lists all of the environments.  
 
`$ cdvirtualenv`  
Changes the current working directory to the directory of the current virtual environment. 
 
`$ cdsitepackages`  
Changes the current working directory to the site-packages directory of the current virtual environment. 

`$ lssitepackages`  
Shows contents of `/site-packages` directory.  

`$ wipeenv`  
Removes all of the installed third-party packages in the current virtualenv.

`$ toggleglobalsitepackages`  
Controls whether the active virtualenv will access the packages in the global Python `/site-packages` directory.
