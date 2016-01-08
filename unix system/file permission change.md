# Unix File System Permissions

http://www.tutorialspoint.com/unix/unix-file-permission.htm


### File Permissions - Read, Write and Execute

There are 3 basic permissions for a file/directory:

- **Read Permission** (r) : you can see the content of the file.
- **Write Permission** (w) : you can change the content of the file.
- **Execute Permission** (x) : you can ask the operating system to run the file as if it were a program.

If the file is a shell script, then the execute attribute says you can treat it as if it were a program. To put it another way, you can create a file using your favorite editor, add the execute attribute to it, and it "becomes" a program. However, since a shell has to read the file, a shell script has to be readable and executable. A compiled program does not need to be readable.


### Permission Assignment

- user (u)
- group (g)
- other (o)

### List Permissions

Use `ls -al` to

    $ ls -al



For drwxrwxr-x it's:

### Change Permissions

r - read
w - write
x - execute

### Change Permissions (bis)

```
1: execute  |        x         x         x         x            
2: write    |             x    x              x    x          
4: read     |                       x    x    x    x       
======================================================
total       |   0    1    2    3    4    5    6    7         
======================================================
reference   |   ---  --x  -w-  -wx  r--  r-x  rw-  rwx                                       
```


```
$ touch myfile.sh
$ ls -al

$ chmod 777 <filename>
```
