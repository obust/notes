# Cron

http://www.unixgeeks.org/security/newbie/unix/cron-1.html
https://help.ubuntu.com/community/CronHowto
http://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/

http://bencane.com/2011/11/02/did-my-cronjob-run/


Cron is the name of program that enables unix users to execute commands automatically at a specified time/date.  
It is normally used for sys admin commands, like makewhatis, which builds a search database for the man -k command, or for running a backup script, but can be used for anything. A common use for it today is connecting to the internet and downloading your email.

This file will look at Vixie Cron, a version of cron authored by Paul Vixie.

## How to start Cron

Cron is a daemon, which means that it only needs to be started once, and will lay dormant until it is required. A Web server is a daemon, it stays dormant until it gets asked for a web page. The cron daemon, or crond, **stays dormant until a time specified** in one of the config files, or crontabs.

On most Linux distributions crond is automatically installed and entered into the start up scripts. To find out if it's running do the following:
```
$ ps aux | grep crond
root       311  0.0  0.7  1284  112 ?        S    Dec24   0:00 crond
user1     8606  4.0  2.6  1148  388 tty2     S    12:47   0:00 grep crond
```
The top line shows that crond is running, the bottom line is the search we just run.

If it's not running then either you killed it since the last time you rebooted, or it wasn't started.

To start it, just add the line `crond` to one of your start up scripts. The process automatically goes into the background, so you don't have to force it with `&`. Cron will be started next time you reboot. To run it without rebooting, just type crond as root.

With lots of daemons, (e.g. httpd and syslogd) they need to be restarted after the config files have been changed so that the program has a chance to reload them. Vixie Cron will automatically reload the files after they have been edited with the crontab command. Some cron versions reload the files every minute, and some require restarting, but Vixie Cron just loads the files if they have changed.

## Using cron

There are a few different ways to use cron (surprise, surprise).

In the `/etc` directory you will probably find some sub directories called:
- `/etc/cron.hourly/`
- `/etc/cron.daily/`
- `/etc/cron.weekly/`
- `/etc/cron.monthly/`

If you place a script into one of those directories it will be run either hourly, daily, weekly or monthly, depending on the name of the directory.

### crontabs

If you want more flexibility than this, you can edit a *crontab* (the name for cron's config files). The main config file is normally /etc/crontab. On a default RedHat install, the crontab will look something like this:
```
$ cat /etc/crontab
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/

# run-parts
01 * * * * root run-parts /etc/cron.hourly
02 4 * * * root run-parts /etc/cron.daily
22 4 * * 0 root run-parts /etc/cron.weekly
42 4 1 * * root run-parts /etc/cron.monthly
```
The first part sets the variables for cron.

- `SHELL` is the 'shell' cron runs under. If unspecified, it will default to the entry in the /etc/passwd file.
- `PATH` contains the directories which will be in the search path for cron e.g if you've got a program 'foo' in the directory /usr/user1/bin, it might be worth adding /usr/user1/bin to the path, as it will stop you having to use the full path to 'foo' every time you want to call it.
- `MAILTO` is who gets mailed the output of each command. If a command cron is running has output (e.g. status reports, or errors), cron will email the output to whoever is specified in this variable. If no one if specified, then the output will be mailed to the owner of the process that produced the output.
- `HOME` is the home directory that is used for cron. If unspecified, it will default to the entry in the /etc/passwd file.

The second part defines the cron entries.  
An entry in cron is made up of a series of fields, separated by a space.
The fields specify when to run the command :


`<minute> <hour> <dom> <month> <dow> <user> <cmd>`

##### User crontabs
```
* * * * *  <command to be executed>
| | | | |
| | | | ----- day of week (0-7) (Sunday=0 or 7)
| | | ------- month (1-12) OR jan,feb,mar,apr ...
| | --------- day of month (1-31)
| ----------- hour (0-23)
------------- minute (0-59)
```
##### System wide /etc/crontab and /etc/cron.d fragments

```
* * * * *  <username> <command to be executed>
| | | | |
| | | | ----- day of week (0-7) (Sunday=0 or 7)
| | | ------- month (1-12) OR jan,feb,mar,apr ...
| | --------- day of month (1-31)
| ----------- hour (0-23)
------------- minute (0-59)
```

- `minute` : what minute of the hour the command will run on (between 0 and 59)
- `hour` : what hour the command will run on (between 0 and 23)
- `dom` : what Day of Month the command will run on (e.g. to run a command on the 19th of each month, the dom would be 19.
- `month` : what month the command will run on (between 0 and 12)
- `dow` : what Day of Week that you want a command to be run on, it can
	 also be numeric (0-7) or as the name of the day (e.g. sun).
- `user` : the user who runs the command.
- `cmd` : the command to run (may contain multiple words or spaces)

If you don't wish to specify a value for a field, just place a `*` in the field.

e.g.
```
01 * * * * root echo "This command is run at one min past every hour"
17 8 * * * root echo "This command is run daily at 8:17 am"
17 20 * * * root echo "This command is run daily at 8:17 pm"
00 4 * * 0 root echo "This command is run at 4 am every Sunday"
* 4 * * Sun root echo "So is this"
42 4 1 * * root echo "This command is run 4:42 am every 1st of the month"
01 * 19 07 * root echo "This command is run hourly on the 19th of July"
```
Notes:
- Under dow, 0 and 7 are both Sunday.
- If both the dom and dow are specified, the command will be executed when either of the events happen.
- Fields **support list** in the form, 1,2,3 (meaning 1 and 2 and 3) or 1-3 (also meaning 1 and 2 and 3).
- Fields **support steps**. A value of `*/2` in the dom field would mean the command runs every two days, and `*/5` in the hours field would mean the command runs every
5 hours.

## Multiuser cron

As Unix is a multiuser OS, some of the apps have to be able to support multiple users, cron is one of these. Each user can have their own crontab file, which can be created/edited/removed by the command `crontab`. This command creates an individual crontab file and although this is a text file, as the /etc/crontab is, it shouldn't be edited directly. The crontab file is often stored in /var/spool/cron/crontabs/<user> (Unix/Slackware/\*BSD), /var/spool/cron/<user> (RedHat) or /var/cron/tabs/<user> (SuSE), but might be kept elsewhere depending on what Un*x flavor you're running.

### Edit crontab using terminal editor

To edit (or create) your crontab file, use the command :

    $ crontab -e

This will load up the editor specified in the environment variables EDITOR or VISUAL. To change the editor invoked, run `$ export EDITOR=vi`. You can of course substitute vi for the text editor of your choice.

Your own personal crontab follows exactly the same format as the main
/etc/crontab file does, except that you need not specify the MAILTO
variable, as this entry defaults to the process owner, so you would be mailed
the output anyway, but if you so wish, this variable can be specified.
You also need not have the user field in the crontab entries. e.g.

`<minute> <hour> <dom> <month> <dow> <cmd>`

Once you have written your crontab file, and exited the editor, then it will
check the syntax of the file, and give you a chance to fix any errors.

### Edit crontab
If you want to write your crontab without using the crontab command, you can
write it in a normal text file, using your editor of choice, and then use the
crontab command to **replace your current crontab** with the file you just wrote.
e.g. if you wrote a crontab called cogs.cron.file, you would use the cmd

    $ crontab <new_crontab_file>

Use `crontab -l` to list your current crontab

Use `crontab -r` to remove your current crontab

Privileged users can also change other user's crontab with:

	$ crontab -u <username>

and then following it with either the name of a file to replace the
existing user's crontab, or one of the -e, -l or -r options.

## Controlling Access to cron

Cron has a built in feature of allowing you to specify who may, and who
may not use it. It does this by the use of /etc/cron.allow and /etc/cron.deny
files. These files work the same way as the allow/deny files for other
daemons do. To stop a user using cron, just put their name in cron.deny, to
allow a user put their name in the cron.allow. If you wanted to prevent all
users from using cron, you could add the line ALL to the cron.deny file:

root@pingu # echo ALL >>/etc/cron.deny

If you want user cog to be able to use cron, you would add the line cog
to the cron.allow file:

root@pingu # echo cog >>/etc/cron.allow

If there is neither a cron.allow nor a cron.deny file, then the use of cron
is unrestricted (i.e. every user can use it).  If you were to put the name of
some users into the cron.allow file, without creating a cron.deny file, it
would have the same effect as creating a cron.deny file with ALL in it.
This means that any subsequent users that require cron access should be
put in to the cron.allow file.  

Output from cron

As I've said before, the output from cron gets mailed to the owner of the
process, or the person specified in the MAILTO variable, but what if you
don't want that? If you want to mail the output to someone else, you can
just pipe the output to the command mail.
e.g.

cmd | mail -s "Subject of mail" user

If you wish to mail the output to someone not located on the machine, in the
above example, substitute user for the email address of the person who
wishes to receive the output.

If you have a command that is run often, and you don't want to be emailed
the output every time, you can redirect the output to a log file (or
/dev/null, if you really don't want the output).
e,g

cmd >> log.file

Notice we're using two > signs so that the output appends the log file and
doesn't clobber previous output.
The above example only redirects the standard output, not the standard error,
if you want all output stored in the log file, this should do the trick:

cmd >> logfile 2>&1

You can then set up a cron job that mails you the contents of the file at
specified time intervals, using the cmd:

mail -s "logfile for cmd" <log.file

### Contab job not running

http://askubuntu.com/questions/93313/cron-job-not-running

	cat /var/spool/mail/root
