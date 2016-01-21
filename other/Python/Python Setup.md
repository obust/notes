# Python

http://youshoulddoityourself.blogspot.nl/2010/11/test.html

## OS X default Python

### Installation

Python comes pre-installed on OS X.

The native Python interpreters live under :

```
/System/Library/Frameworks/Python.framework/Versions/X.X/
```

These files **should not be modified**.

### Usage 

You can ask for the location of the python executable.

```
$ which python
/usr/bin/python
```

To check which python version is used, run:

```
$ python --version
Python 2.7.10
```

So Python 2.7.10 is the default python interpreter.



While it can be convenient to have a pre-installed Python, **you should not use it**: 

- Apple's Python runtime environment is not always up to date
- It can be a pain to play with permissions just to install third-party Python librairies
- Apple has a tendency to wipe-out your site-packages with every major OS upgrade


So I simply recommend to install Python aside the default one, with Homebrew. You’ll never have to use sudo or have permissions problem; if you have any issues, you can drop `/usr/local` and start from fresh without having messed up your OS X system.

## Homebrew Python installation

https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Homebrew-and-Python.md  
https://joernhees.de/blog/2014/02/25/scientific-python-on-mac-os-x-10-9-with-homebrew/  
http://hackercodex.com/guide/python-development-environment-on-mac-osx/  
http://blog.manbolo.com/2014/09/27/use-python-effectively-on-os-x

### Installation

Homebrew provides a formula for Python 2.7.X and one for Python 3.X. They don't conflict, so they can both be installed.

- Homebrew always has the most recent version.
- Homebrew (as a package manager) handles installation, update and deletion.
- Homebrew’s Python includes the latest versions of Pip and Setuptools (Python package management tools)

```
brew install python
```

The Python formulae install `pip` and Setuptools.

The Homebrew Python interpreters live under :

```
/usr/local/Cellar/python/2.7.X/Python.framework/Versions/X.X/   # for Python 2 interpreters
/usr/local/Cellar/python3/3.X.X/  # for Python 3 interpreters
```

```
# for Python 2.7.X
/usr/local/Cellar/python3/3.X.X/Frameworks/Python.framework/Versions/3.X/

# for Python 3.X.X
/usr/local/Cellar/python/2.7.X/Frameworks/Python.framework/Versions/2.7/
```

Pip and setuptools have been installed. To update them
  pip3 install --upgrade pip setuptools

You can install Python packages with
  pip3 install <package>

They will install into the site-package directory
  /usr/local/lib/python3.5/site-packages


.app bundles were installed.
Run `brew linkapps python3` to symlink these to /Applications.

### Usage

Homebrew will place a bunch of symlinks of executables in `/usr/local/bin` accessible by the command line :

- `pip` : symlink to pip package manager for Python 2.7 library
- `pip2` : symlink to pip package manager for Python 2.7 library
- `pip2.7` : symlink to pip package manager for Python 2.7 library
- `pip3` : symlink to pip package manager for Python 3.5 library
- `pip3.X` : symlink to pip package manager for Python 3.X library
- `python` : symlink to Homebrew's Python 2.7 executable
- `python2` : symlink to Homebrew's Python 2.7 executable
- `python2.7` : symlink to Homebrew's Python 2.7 executable
- `python3` : symlink to Homebrew's Python 3.X executable
- `python3.X` : symlink to Homebrew's Python 3.X executable

The real Python interpreters live under :

- `/usr/local/Cellar/python3/3.5.0/Frameworks/Python.framework/Versions/3.5/`
- `/usr/local/Cellar/python/2.7.10/Frameworks/Python.framework/Versions/2.7/`

The executable `python` will always point to the 2.7 and `python3` to the 3.X version.	


To create a virtual environment that will use Python 2 or Python 3, just use the -p option flag to target a specific Python. For instance:

```
mkvirtualenv -p /usr/local/bin/python3.5 myvirtualenv
```

### Removal

```
brew uninstall python
```

## Change Python Interpreter

We need to tell the system to use our new Python interpreter instead of the default one.

```
$ which python
/usr/bin/python
```

The default Python interpreter is under `/usr/bin`, and the Homebrew’s one is under `/usr/local/bin` so we’re going to edit `/etc/paths` so the `/usr/local/bin` binaries will be prioritised over `/usr/bin`.

```
$ sudo vi /etc/paths
```
Move /usr/local/bin at the beginning of the file so Homebrew binaries take priority over system binaries;

```
/usr/local/bin  
/usr/bin
/bin
/usr/sbin
/sbin
```

Finally, check everything is ok: typing python should launch the Homebrew version

```
$ source /etc/paths
$ which python
/usr/local/bin/python
```



## .pkg installation


### Installation

The Python interpreters installed live under :

`/Library/Frameworks/Python.framework/Versions/X.X/`

### Usage

The package installer will place a bunch of symlinks of executables in `/usr/local/bin` accessible by the command line :

- `pythonX.X` : symlink to Python X.X executable
- `pipX.X` : symlink to pip package manager for Python X.X library

The real Python interpreter live under :

- `/Library/Frameworks/Python.framework/Versions/X.X/`

To create a virtual environment that will use the Python version installed, just use the `-p` option flag to target a specific Python. For instance:

```
mkvirtualenv -p /usr/local/bin/pythonX.X myvirtualenv
```


### Removal

http://stackoverflow.com/questions/3819449/how-to-uninstall-python-2-7-on-a-mac-os-x-10-6-4

```
$ pkgutil --pkgs
```

or to only see the ones concerning Python:

```
$ pkgutil --pkgs | grep org.python.Python
```

This will output something like

```
org.python.Python.PythonApplications-2.7
org.python.Python.PythonDocumentation-2.7
org.python.Python.PythonFramework-2.7
org.python.Python.PythonProfileChanges-2.7
org.python.Python.PythonUnixTools-2.7
```


```
/Applications/Python3.4/IDLE.app/
/Applications/Python3.4/Python Launcher.app/
/Applications/Python3.4/Icon
/Applications/Python3.4/._Icon
/Applications/._Python 3.4
/Library/Frameworks/Python.framework/Versions/3.4/*

