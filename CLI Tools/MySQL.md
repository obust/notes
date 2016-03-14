# MySQL Commands

1. [Install MySQL](#-install-mysql)
2. [Uninstall MySQL](#-uninstall-mysql)
3. [MySQL Command-line]()

## Install MySQL  

#### Mac installation
Use Homebrew to install mysql

```
brew install mysql
```

***Potential Issue***  
A "/etc/my.cnf" from another install may interfere with a Homebrew-built server starting up correctly.

#### Linux installation

    apt-get install mysql-server mysql-client

And maybe

    apt-get install libmysqlclient-dev mysql-common

#### To launch MySQL at startup (optional)

1. add MySQL to your LaunchAgents
2. load MySQL specified configuration files

```
ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents
launchctl load ~/Library/LaunchAgents homebrew.mxcl.mysql.plist
```

#### To set the root password for MySQL
Set the root password to *root* as well. See
[here](https://www.howtoforge.com/setting-changing-resetting-mysql-root-passwords) or
[here](http://www.cyberciti.biz/faq/mysql-change-root-password/)

```
mysqladmin -u root password <newpassword>
```

#### Install mysqlclient  
[mysqlclient](https://github.com/PyMySQL/mysqlclient-python) is a Database API driver for Python : used to access databases.

```
pip install mysqlclient
```

#### Potential Issue
When running mysqlclient, might fail loading some libraries
`Library not loaded: libssl.1.0.0.dylib`  
or  
`Library not loaded: libcrypto.1.0.0.dylib`

The libraries aren't loaded because the versions aren't in the main lib directory `/usr/lib/` but in anaconda `/Applications/anaconda/lib/`

Solution from [here](http://stackoverflow.com/questions/27264574/import-psycopg2-library-not-loaded-libssl-1-0-0-dylib)  

1. Remove potential incorrect links
2. Add [simlink](https://en.wikipedia.org/wiki/Symbolic_link) (raccourci) to the versions stored in anaconda

```
sudo rm /usr/lib/libssl.1.0.0.dylib
sudo rm /usr/lib/libcrypto.1.0.0.dylib

sudo ln -s /Applications/anaconda/lib/libssl.1.0.0.dylib /usr/lib
sudo ln -s /Applications/anaconda/lib/libcrypto.1.0.0.dylib /usr/lib
```

## Uninstall MySQL
See this [post](http://stackoverflow.com/questions/4359131/brew-install-mysql-on-mac-os).

1. Remove MySQL
2. Cleanup cache
3. Remove MySQL specified configuration files from LaunchAgents
4. Remove MySQL from LaunchAgents
5. Delete old MySQL directory (otherwise future mysql installation will not be able to log in as root initially to set the password)

```
brew remove mysql
brew cleanup
launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
rm ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
sudo rm -rf ~/usr/local/var/mysql
```


## MySQL Command-line


### From the command line
**MySQL list of commands**  
`mysql help`

**Start server** (if not launched at startup)  
`mysql start` or `mysql.server start`

**Connect/Login**

* hostname: -h \<localhost> (optional)
* username: -u \<root>
* password: -p \<>

```
mysql -u <username> -p
```  
NB: To change mysql root password, see
[here](https://www.howtoforge.com/setting-changing-resetting-mysql-root-passwords) or
[here](http://www.cyberciti.biz/faq/mysql-change-root-password/).

**Disconnect**  
`>mysql QUIT` or `Ctrl+C`

**Shut down server**  
`mysql stop` or `mysql.server stop`

### From a MySQL prompt
NB: When you see `mysql>` it means from a MySQL prompt after logging into MySQL. More on [here](https://www.pantz.org/software/mysql/mysqlcommands.html).

**Create a database on the sql server** (specify all tables and columns will use UTF-8 by default)  
`mysql> CREATE DATABASE <dbname> CHARACTER SET utf8;`

**List all databases on the sql server**  
`mysql> SHOW DATABASES;`

**Switch to a database**  
`mysql> USE <dbname>;`

**To see all the tables in the db**  
`mysql> SHOW TABLES;`

**To see database's field formats**  
`mysql> DESCRIBE <tablename>;`

**To see the columns and column information of a table**  
`mysql> show columns from <tablename>;`

**To see the first entries of a table**  
`mysql> SELECT * FROM <tablename> LIMIT 5;`

**To delete a db**  
`mysql> DROP DATABASE <dbname>;`

**To delete a table**  
`mysql> DROP TABLE <tablename>;`

**To clear a table (remove all entries)**
`mysql> TRUNCATE TABLE <tablename>;`
