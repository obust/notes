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
<program -v>
```


Find Broken Symlinks

http://unix.stackexchange.com/questions/34248/how-can-i-find-broken-symlinks

    $ find . -type l -exec sh -c "file -b {} | grep -q ^broken" \; -print
