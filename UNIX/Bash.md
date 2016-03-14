# Bash Shell

http://www.linfo.org/path\_env_var.html  
http://superuser.com/questions/426114/understanding-bashrc-and-bash-profile

## Shell Configuration

`.bashrc` and `.bashrc` are configuration files for the bash shells. Generally speaking, there are two things you do with these scripts: 

- Run startup programs
- Set specific environment variables


`.bash_profile` is executed for login bash shells only (e.g. when you open a terminal).  
`.bashrc` is executed for every OTHER bash shells.

Anything you want to run when you log in, you put in `.bash_profile`.  
Anything you want to set on every other shell, you put in `.bashrc`.

See the difference between [login, non-login, interactive, non-interactive bash shells](http://unix.stackexchange.com/questions/38175/difference-between-login-shell-and-non-login-shell).

Therefore, `.bash_profile` will typically source `.bashrc` if it exists so you don't have to duplicate any commands you want to run for every shell whether it was a login shell or not.

Examples for `.bashrc`:

- Set `$PS1` (prompt bash look)
- Enable special tab completion rules
- Set shell options by running shopt
- Set up command aliases

Examples for `.bash_profile`:

- Source `.bashrc`
- Add directories to `$PATH` (executable files directory list)
- Run ssh-agent

## Edit Hidden Files

`.bashrc` and `.bash_profile` are a hidden files located in each user's home directory `~/`.

To see a hidden file, use the `ls -a` command (ie. list with *all* option).  
To edit a hidden file, use the `vi <filename>` command (ie. [visual editor](https://www.cs.colostate.edu/helpdocs/vi.html)).

```
vim .bash_profile
nano .bash_profile
open -a "TextEdit" .bash_profile
```
After you've edited the file, make sure to source the .bash_profile again. Otherwise, bash won't recognize the changes:

```
source .bash_profile
```