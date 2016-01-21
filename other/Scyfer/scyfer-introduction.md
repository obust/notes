# Scyfer

## Command lines: the basics

To **get acquainted with command lines**, I highly recommend to read these articles by Kirk McElhearn: [navigating files and folders](http://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html), [how to use man pages](http://www.macworld.com/article/2044790/master-the-command-line-how-to-use-man-pages.html), [copying and moving files](http://www.macworld.com/article/2080814/master-the-command-line-copying-and-moving-files.html) and [deleting files and folders](http://www.macworld.com/article/2082021/master-the-command-line-deleting-files-and-folders.html).

**Navigating files and folders**

	$ cd					# change current directory to
							# main directory (usually users/username/)
	$ cd <path/to/dir>		# change current directory to pathed dir
	$ cd ..					# change current directory to parent dir
	$ pwd					# display current directory absolute path
	$ ls					# list directories and file in current dir
	
**Copying, moving, creating files and folders**

	$ mkdir <dirname>		# creates a directory of name dirname
	$ rm <filename>			# delete file of name filename
	$ rm -r <dirname>		# delete directory (and all children, 
							# -r stands for recursive) of name dirname
	$ cp <source> <dest> 	# copy file to destination, use -r 
							# if for directory (recursive)
	$ mv <source> <dest> 	# move file to destination (-r for dir)
	$ nano <filename>		# edit file in terminal
	

## Importing modules

Both locally and on server add to the .bash_profile the following lines. The **path should be directing to the folder where you cloned the ScyferNN repo**.

    PYTHONPATH=/home/<username>/scyfer/scyfernn
    export PYTHONPATH
    
This will allow you to import the classes and functions neately, like this for example:

    from NN.layers import DenseLayer, DropoutLayer
    from NN.exceptions import LayerValueError

Reminder: to access .bash_profile do as follows

    $ cd ~
    $ nano .bash_profile
    
## Virtual Environments

Virtual environments allow you to work simultaneously with multiple versions of python packages for different projects that may require different version of say theano or numpy.

For anaconda users, they should delve into how to [use conda package]('http://conda.pydata.org/docs/using/index.html').

If you do not use anaconda, you can use the **[virtualenv]('https://virtualenv.readthedocs.org/en/latest/') package along with [virtualenvwrapping]('http://virtualenvwrapper.readthedocs.org/en/latest/index.html')**. For the latter be sure to follow the steps given in the introduction to be able to use it correctly. The following line
	
	$ source /usr/local/bin/virtualenvwrapper.sh
	
Should be modified using the path of virtualenvwrapper.sh. You can find it using command line `locate`.

	$ locate virtualenvwrapper.sh
	
To create and use a new environment, use the following command lines. `workon`allows to chosse which environment you desire to work on. Once selected, the `pip` commands will be executed in the environment folder witout messing up you global packages.

	$ mkvirtualenv new_environment
	$ workon new_environment 
	$ pip install -r new_project_requirements.txt
	
`toggleglobalsitepackages` controls whether the active virtualenv will access the packages in the global Python `site-packages`. It allows you to install only the packages that defer from your global `site-packages`on your new environment.


## Git: daily use

### Bitbucket

Bitbucket is a web-based hosting service for projects which is highly similar to GitHub, and primarly uses **Git**. The bitbucket of the team can be found [here]('https://bitbucket.org/scyferteam/'). **Creator rights** (namely developer rights) are **granted by Auke** or Tijmen.

To **use Git**, while it is highly recommended to read the whole [documentation](https://git-scm.com/docs), you can refer to this **very comprehensive [cheat-sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)**.

The **3 main rules of thumb** are:

1. Use feature branches if you work on a brand new feature.
2. Create a new repository for each project
3. Use issue tracking extensively

### Cloning repository

Let us clone scyfer core repository ScyferNN and work around just to understand a few things about git.

First let's create a folder in our main directory called scyfer, and then another folder inside this scyfer called scyfernn.

	$ cd ~
	$ mkdir scyfer
	$ mkdir scyfer/scyfernn

Now we want to clone ScyferNN repository inside our directory scyfernn. We will first want to navigate to this directory, then go on the [repository on Bitbucket](https://bitbucket.org/scyferteam/scyfernn) with your browser. On the left you should see in the `clone`button. Click and copy the command that is automatically highlighted. Paste it in your terminal, enter password as required... and DONE :) you cloned your first repository.

	$ cd scyfer/scyfernn
	$ git clone https://username@bitbucket.org/scyferteam/scyfernn.git
	$ password

To know the **status of your cloned repository** (is it up-to-date ?) you can use the git command `git status`.

	$ git status
	
As you just cloned the repo, it should be up-to-date and this should appear in your terminal:
	
	On branch master
	Your branch is up-to-date with 'origin/master'.
	nothing to commit, working directory clean


### Branches

The first line means that right now you are working on the master branch. A repository can have multiple branches, these branches are just different versions of the repository for say the needs of different projects. **To check the existing branches**, use `git branch`:

	$ git branch
	development
	* master

The asterix in front of master means you are currently working on master, but there is also this development branch. This branch is the one we are working on, where we commit everything that is useful for current projects. Only Auke works on merging development with master branch and makes sure everything in master branch remains tight and clean. We then want **to work on the development branch**. To do so, we need to `checkout` development branch. 

	$ git checkout development
	
### Commit
	
Now let's say we are getting creative and that we want to add a Layer class to our layers, we will call it ImaginaryLayer. Let's create an empty python file `imaginary_layer.py` with your favorite IDE (PyCharm) inside NN/layers directory (NN is at the root of scyfer/scyfernn if you followed this tutorial from the beginning). Now let's check the status of our repository.

	$ git status
	On branch development
	Your branch is up-to-date with 'origin/development'.
	Untracked files:
  	(use "git add <file>..." to include in what will be committed)

        NN/layers/imaginary_layer.py

	nothing added to commit but untracked files present (use "git add" 	to track)

Now we want this `imaginary_layer.py` to be available to everyone, we want to upload it to the online repository, in git term, we want to `commit` this file. A commit can be a group of file creations and modifications, that should be related. For example here, we just created an imaginary_layer.py, but we are also going to create a `test_imaginary_layer.py` in order to do some unit testing and assert our new class is working correctly. For the sake of the example, let's say we also created a script `imaginary_script.py` only useful to us (maybe to test our imaginary layer on an example just for ourselves) in NN/layers.

	$ git status
	On branch development
	Your branch is up-to-date with 'origin/development'.
	Untracked files:
  	(use "git add <file>..." to include in what will be committed)

        NN/layers/imaginary_layer.py
        NN/layers/imaginary_script.py
        tests/layers/test_imaginary_layer.py

	nothing added to commit but untracked files present (use "git add" 	to track)

Now we only want to commit our imaginary layer and its test, and not the imaginary_script.py that is only useful to us. So we want to `add` these files to the next commit.

	$ git add NN/layers/imaginary_layer.py
	$ git add tests/layers/test_imaginary_layer.py
	
Now we want to create a `commit` (that will contain only the file that we added). A **commit should always be associated with a message** through the option -m. The message must concisely explain the scope of the commit.

	$ git commit -m "Added an ImaginaryLayer that does blablabla, \
	 and its test function that covers 80% of the class output"
	 
### Stash

Now we want to `push` this commit so that it appears on Bitbucket and can be used by others. To do so, we first want to `stash` the modifications to the repository that we do not want to push (like our imaginary script). This `stash` command will put **all the local modifications that are not commited yet in a stack**. You need to stash the modifications that are not in a commit otherwise git will not know what to do with these files and will return an error when you pushing.

	$ git stash
	
To retrieve these modifications once pushed, use the command line:

	$ git stash pop


### Heuritics about pushing

**HERE PLEASE DO NOT PROCEED AND USE GIT PUSH, SCYFER DOES NOT NEED YOUR IMAGINARY LAYER.**

**Before pushing**, or whenever it has been a long time you have been working locally without checking the status of your repository, **it is highly recommened to check the status**.

**First case**, your local changes do not interfere with the current state of the repo, but you are late by N commits
	
	$ git status
	On branch development
	Your branch is behind 'origin/development' by 47 commits, and can be fast-forwarded.
  		(use "git pull" to update your local branch)
	nothing to commit, working directory clean
	
You can then safely use git pull to update your repo:

	$ git pull
	$ git push
	
**Second case**, your local changes interfere with the current state of repo, or in other words you modified a file from its past state and missed 1 or more commit that modified the same very file you have been working on. And **here is where the magic of git lies**: you can **merge your modifications with the modifications you are late on** (if of course they do not differ to much from each other, like one deletes a function you modified). **To do so safely**, use `git fetch` to fetch the modifications, and the `git rebase` that will make the file go back to its initial state, then add the modifications that you fetched, then only add the modifications you commited, while ensuring there is no conflict.

	$ git fetch
	$ git rebase

### Git workflow

1. Clone repo: `git repo <link>`
2. Check status: `git status`
3. Create and modify files
4. Add wanted files to one or multiple commit: `git add`
5. Add unwanted files to stash: `git stash`
6. Push commits: use either `git push` or `git fetch` and `git rebase`



## PyCharm

PyCharm is a professional IDE that allows remote deployment which is very useful for our server ([download PyCharm]('https://www.jetbrains.com/pycharm-edu/download/')). There is no real installation procedure, it will just unzip the package where you want to ([installation instructions]('https://www.jetbrains.com/pycharm-edu/quickstart/installation.html')). 
In order to run PyCharm for the first time you will need to access the folder where you unzipped PyCharm and launch pycharm.sh. To do so, type this in your terminal (correct the path as needed):

    $ cd ~/pycharm-5.0/bin/
    $ sh ./pycharm.sh

As you do not want to do that each time you want to run PyCharm, once it is launched go to Tools -> Create Desktop Entry. This Desktop Entry will be available through Dash, and you will be available to pin it to your launch bar.

## Unit testing



## Volume visualization

