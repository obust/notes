# Aptitude

https://www.digitalocean.com/community/tutorials/package-management-basics-apt-yum-dnf-pkg

```
sudo apt-get autoclean
sudo apt-get autoremove
sudo apt-get update
sudo apt-get dist-upgrade
```


```
which <program>
```

```
<program> -v
```


Find Broken Symlinks

http://unix.stackexchange.com/questions/34248/how-can-i-find-broken-symlinks

    $ find . -type l -exec sh -c "file -b {} | grep -q ^broken" \; -print


## Upgrade

#### update

`update` updates the list of packages.

```
sudo apt-get update
```

#### upgrade

`upgrade` is used to install the newest versions of all packages currently installed on the system from the sources enumerated in /etc/apt/sources.list. Packages currently installed with new versions available are retrieved and upgraded; under no circumstances are currently installed packages removed, or packages not already installed retrieved and installed. New versions of currently installed packages that cannot be upgraded without changing the install status of another package will be left at their current version. An update must be performed first so that apt-get knows that new versions of packages are available.

```
sudo apt-get upgrade
```

#### dist-upgrade

`dist-upgrade` in addition to performing the function of upgrade, also intelligently handles changing dependencies with new versions of packages; apt-get has a "smart" conflict resolution system, and it will attempt to upgrade the most important packages at the expense of less important ones if necessary. So, dist-upgrade command may remove some packages. The /etc/apt/sources.list file contains a list of locations from which to retrieve desired package files. See also apt_preferences(5) for a mechanism for overriding the general settings for individual packages.

```
sudo apt-get dist-upgrade
```

#### full-upgrade

`full-upgrade` performs the function of upgrade but may also remove installed packages if that is required in order to resolve a package conflict.

```
sudo apt full-upgrade
```
