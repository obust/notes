# PATH environment variable

https://kb.iu.edu/d/acar  
http://www.linfo.org/path\_env_var.html

## Understand PATH

When you run a command like `python` or `pip`, your operating system searches through a list of directories to find an executable file with that name. This list of directories lives in an *environment variable* called `PATH`, with **each directory in the list separated by a colon**.

To find out what your `PATH` is, at the Unix shell prompt, run :

```
echo $PATH
```
This should output something like :

```
/usr/local/bin:/usr/bin:/bin
```

Directories in `PATH` are searched from left to right, so a matching executable in a directory at the beginning of the list takes precedence over another one at the end. 

In this example, the directories are searched in the following order :

1. `/usr/local/bin directory`
2. `/usr/bin`
3. `/bin`

## Change PATH

### Temporary changes (for the current Shell session)

A la déconnexion PATH reprendra sa valeur par défaut, donc /home/user/mes_prog n'existera plus dans PATH. 

To add a directory path of executables _to the front_ of the list :

```
export PATH=<new_path>:$PATH
```


To add a directory path of executables _to the end_ of the list :

```
export PATH=$PATH:<new_path>
```

To set a totally new list of directory paths of executables :

```
export PATH=<new_colon_separated_list_of_paths>
```

### Permanent changes

Si vous voulez configurer PATH de façon permanente, vous devez éditer le fichier de configuration de votre shell de connexion. 
Comme le plus souvent c'est le shell BASH qui est utilisé, vous devez éditer votre fichier /home/user/.bashrc. 

To configure `PATH` permanently, you need to edit the `.bash_profile` file which is the user's configuration file for Shell sessions.

This file can be . and should be edited with a Text Editor

==To make these changes permanent, add the commands described above to the end of your .cshrc file (for csh and tcsh), .profile file (for sh and ksh), or .bash_profile file (for bash).==

```
echo 'export PATH=$PATH:/home/user/mes_prog' >> /home/user/.bashrc
```
Ainsi à chaque connexion votre PATH contiendra votre répertoire /home/user/prog 

Cette opération peut être exécutée par l'utilisateur *user* vu qu'il s'agit de son environnement. 
