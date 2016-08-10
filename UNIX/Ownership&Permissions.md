# Unix File System Ownership & Permissions

http://www.tutorialspoint.com/unix/unix-file-permission.htm

https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-permissions

## Ownership

### User, Group, Other

- user (u)
- group (g)
- other (o)

### Change owner user/group

```
chown [-R] <user>:<group> <file>
```
- `-R` : applies changes recursively

### Inherit owner group

By default, a new file/directory will inherit the primary group of the user creating the file.

setuid (**s**et **u**ser **ID**) and setgid (**s**et **g**roup **ID**) are Unix access rights flags.

Setting the setgid permission on a directory (`chmod g+s <dir>`) causes new files and subdirectories created within it to **inherit its group ID**.

NB: Notice the `s` instead of `x`/`-` in the group permissions: `drwxrwsr--`. This means that setgid is set, therefore new files and subdirectories will inherit the owner group.

## Permissions

### Read, Write and Execute

There are 3 basic permissions for a file/directory:

- **Read Permission** (r) : you can see the content of the file.
- **Write Permission** (w) : you can change the content of the file.
- **Execute Permission** (x) : you can ask the operating system to run the file as if it were a program.

If the file is a shell script, then the execute attribute says you can treat it as if it were a program. To put it another way, you can create a file using your favorite editor, add the execute attribute to it, and it "becomes" a program. However, since a shell has to read the file, a shell script has to be readable and executable. A compiled program does not need to be readable.

## List Permissions

Use `ls -l <dir>` to list information about the file(s)

Each record has the following format:

```
[permissions] [number of links] [owner user] [owner group] [size] [last modification date] [file/directory name]
```

File permissions is displayed in the following format;

```
drwxrwxr--
│└┬┘└┬┘└┬┘
│ │  │  └── other permission: rwx
│ │  └───── group permission: rwx
│ └──────── user permission: rwx
└────────── directory flag: 'd' is a directory, '-' is a file
```

## Change Permissions

```
1: execute  |        x         x         x         x            
2: write    |             x    x              x    x          
4: read     |                       x    x    x    x       
======================================================
total       |   0    1    2    3    4    5    6    7         
======================================================
reference   |   ---  --x  -w-  -wx  r--  r-x  rw-  rwx                                
```

**set permissions**  
`chmod u=<rwx> <file>` or `chmod 777 <file>`

**add permissions**  
`chmod u+<rwx> <file>`

**remove permissions**  
`chmod u-<rwx> <file>`

**syntax for multiple permissions**  
`chmod u=<rwx>,g=<rwx>,o=<rwx> <file>`

## ACL (Access Control Lists)

Use ACL to provide different levels of permissions to files and folders.

NB: Notice the `+` at the end of the permissions: `drwxrwxr--+`. This means this directory has ACL applied to it.

### Set different user permissions

```
sudo setfacl -d -m user:<username>:rwx <path>
```

### Set different group permissions

```
sudo setfacl -d -m group:<groupname>:rwx <path>
```


```
$ mkdir testdir
$ ls -l
drwxrwsr-x 2 romain developers 4096 Aug 10 15:38 testdir


```
