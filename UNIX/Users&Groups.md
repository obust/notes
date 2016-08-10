# Unix Users & Groups

https://www.linode.com/docs/tools-reference/linux-users-and-groups  
http://www.tecmint.com/manage-users-and-groups-in-linux/

<!-- TOC depthFrom:2 depthTo:6 withLinks:1 updateOnSave:1 orderedList:1 -->

1. [Manage Users](#manage-users)
2. [Manage Groups](#manage-groups)
3. [Manage Group Users](#manage-group-users)
4. [Grant sudo rights](#grant-sudo-rights)

<!-- /TOC -->

## Manage Users

**Create user (interface)**  
`adduser <username>`

- `--home <dir>`: home directory of the new account.
- `--group <groupname>`: name of the primary group of the new account.

**Delete user**  
`deluser <username>`

- `--remove-home`: remove the users home directory and mail spool.
- `--remove-all-files`: remove all files owned by user.

**List users**  

The full account information is stored in the `/etc/passwd` file. This file contains a record per system user account and has the following format (fields are delimited by a colon).
```
[username]:[x]:[UID]:[GID]:[Comment]:[Home directory]:[Default shell]
```

- Fields `[username]` and `[Comment]` are self explanatory.
- The `x` in the second field indicates that the account is protected by a shadowed password (in /etc/shadow), which is needed to logon as `[username]`.
- The `[UID]` and `[GID]` fields are integers that represent the User IDentification and the primary Group IDentification to which `[username]` belongs, respectively.
- The `[Home directory]` indicates the absolute path to `[username]`’s home directory, and
- The `[Default shell]` is the shell that will be made available to this user when he or she logins the system.

**Change user password**  
`passwd <username>`

**Change user name**  
`usermod -l <new_username> <old_username>`

**Change user home directory**  
`usermod [-m] -d <new_home_dir> <username>`
- `-m` (`--move-home`) : move the content of the current home dir to the new home dir.

## Manage Groups

**Create group**  
`addgroup <groupname>`

- `--gid <ID>`: use ID for the new group.
- `--system`: create a system group.

**Delete group**  
`delgroup <groupname>`

**List groups**  
Group information is stored in the `/etc/group` file. Each record has the following format.

```
[Group name]:[Group password]:[GID]:[Group members]
```
- `[Group name]` is the name of group.
- An x in `[Group password]` indicates group passwords are not being used.
- `[GID]`: same as in `/etc/passwd`.
- `[Group members]`: a comma separated list of users who are members of `[Group name]`.

## Manage Group Users

**Set user primary group**  
`usermod -g <groupname> <username>`

**Set user supplementary groups**  
`usermod -G <group1>,<group2> <username>`

**Append supplementary group**  
`usermod -a -G <group1>,<group2> <username>`

**List user groups**  
`groups <username>`

**Remove user from group**  
`deluser <username> <groupname>`

## Grant sudo rights

Use the `visudo` command as a sudo user to change sudoers.

Before:
```
# User privilege specification
root       ALL=(ALL:ALL) ALL
```
After:
```
# User privilege specification
root       ALL=(ALL:ALL) ALL
<username> ALL=(ALL:ALL) ALL
```
