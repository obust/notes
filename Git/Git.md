# Git

To **use Git**, while it is highly recommended to read the whole [documentation](https://git-scm.com/docs), you can refer to this **very comprehensive [cheat-sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)**.

Git Official Documentation : [https://git-scm.com/docs](https://git-scm.com/docs)  
Atlassian (aka BitBucket) Git Tutorial : [https://www.atlassian.com/git/tutorials/](https://www.atlassian.com/git/tutorials/)  
Github Git Interactive Tutorial : [https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)  
Github Git Cheatsheet : [https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)

- Setting up repository
	1. BitBucket 
	2. Create a repo
	3. Clone a repo 
	4. Branch
- Making changes
	2. Edit
	3. Add (Stage)
	4. Status
	5. Commit
- Syncing
	1. Pull
	2. Push
	3. Rebase 

## Git workflow



	
1. Clone repo: `git repo <link>`
3. Create and modify files
4. Add wanted files to one or multiple commit: `git add`
5. Add unwanted files to stash: `git stash`
6. Push commits: use either `git push` or `git fetch` and `git rebase`


## Setting up a repository

### Bitbucket

Bitbucket is a web-based version control service that primarly uses **Git**.  
It is highly similar to GitHub, but allow private repositories for free. 

The bitbucket of the team can be found at [https://bitbucket.org/scyferteam/](https://bitbucket.org/scyferteam/). Creator rights (namely developer rights) are granted by Auke or Tijmen.

The **main rules of thumb** are:

1. Never use master branch. It is restricted to the framework administrator.
2. Use development branch if you work on feature that might be of use on other projects.
3. Create feature branches if you work on a brand new or project specific features.
4. Create a new repository for each project.
5. Use issue tracking extensively.


### Clone

Use `git clone <repo>` to **copy an existing Git repository** onto the local machine.  

The created Git repository has its own history, manages its own files, and is a completely isolated environment from the original repository.

When you clone a repository, it automatically creates a remote connection called `origin` pointing back to the original repository. This makes it very easy to interact with the original repository when synchronizing branches.

##### *Example*

Let us clone scyfer core repository ScyferNN.

First let's create a folder called `scyfer/`, that will host the Scyfer different Git repositories.

	$ cd ~
	$ mkdir scyfer

Now we clone the ScyferNN remote repository inside our directory `scyfer/`.

	$ cd scyfer
	$ git clone https://<username>@bitbucket.org/scyferteam/scyfernn.git
	$ password

You can obtain the link to the [ScyferNN Git repository](https://bitbucket.org/scyferteam/scyfernn) on the repo's page.

## Making changes

Developing a project revolves around the basic **edit/stage/commit** pattern. 

1. First, you **edit your files** in the *working directory*. 
2. When you’re ready to save a copy of the current state of the project (*snapshot*), you **stage changes** with `git add`. 
3. After you’re happy with the staged snapshot, **commit the snapshot** to the project history with `git commit`.

### Branch

A *branch* represents an **independent line of development**. Branches serve as an abstraction for the edit/stage/commit process.

Create a separate branch to **develop a feature** (or work on a bug) without disturbing the *master branch*. 

You can think of them as a way to request a brand new working directory, staging area, and project history. This makes sure that unstable code is never committed to the main code base, and it gives you the chance to clean up your feature’s history before merging it into the main branch.

<img src="https://www.atlassian.com/git/images/tutorials/collaborating/using-branches/01.svg" />

Use `git branch` to **list all _local_ branch**, and show the current branch.  
Use `git branch <branchname>` to **create a local branch**.  
Use `git branch -d <branchname>` to **delete a local branch**.  
Use `git branch -m <newbranchname>` to **rename the current local branch**.

Use `git checkout <branchname` to **select a branch to work on**.

You can work on multiple features in a single repository with `git branch` by switching between them with `git checkout`.

### Example

A repository can have multiple branches, these branches are just different versions of the repository for say the needs of different projects. 

	$ git branch
	* master

The first line means that right now you are working on the master branch. 

The * in front of "master" means we are currently working on the branch *master*.  
There is also a "development" branch. This branch is the one we are working on, where we commit everything that is useful for current projects. We want **to work on the development branch**. Only Auke works on merging development with master branch and makes sure everything in master branch remains tight and clean. 

	$ git checkout development
	Branch development set up to track remote branch development from origin.
	Switched to a new branch 'development'

First, this will update files locally to match the remote branch version.  
Then, it switches to this new branch, as we can now check:

	git branch
	* development
	  master

## Add

Use `git add <file>` to **add modified files to the staging area**.  

The *staging area* is like a buffer before commit. It tells Git which updates you want to include in the next commit, instead of committing all the changes. However, changes are not actually recorded until you run `git commit`.

Use `git add -a` to add all modified files to the staging area.  
Use `git add -p` to add portions of files to the staging area. This will present you with a chunk of changes and prompt you for a command :

- y to stage the chunk, 
- n to ignore the chunk, 
- s to split it into smaller chunks, 
- e to manually edit the chunk,
- q to exit.

### Example

Let's say we want to add a Layer class to our layers. We create an empty python file `my_awesome_layer.py` inside the `scyfernn/NN/layers/` directory. 


## Status

Use `git status` to **display the state between the *working directory* and the *staging area*.**

- files modified that are staged (changes to be committed)
- files modified that are not staged (changes not staged for commit)
- files that are not tracked (new files of the project that have never been committed)
	
## Commit

Use `git commit -m "<message>"` to **commit the staged snapshot to the project history**. Committed snapshots can be thought of as “safe” versions of a project—Git will never change them unless you explicity ask it to. Along with git add, this is one of the most important Git commands.

The message should summarize the entire commit in less than 50 characters. For instance :

- Update the sayHello() function to output the user's name
- Change the sayGoodbye() function to a friendlier message

### Example
	
Now let's check the status of our repository.

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
	 
## Stash

Now we want to `push` this commit so that it appears on Bitbucket and can be used by others. To do so, we first want to `stash` the modifications to the repository that we do not want to push (like our imaginary script). This `stash` command will put **all the local modifications that are not commited yet in a stack**. You need to stash the modifications that are not in a commit otherwise git will not know what to do with these files and will return an error when you pushing.

	$ git stash
	
To retrieve these modifications once pushed, use the command line:

	$ git stash pop


## Syncing

In Git’s collaboration model, every developer has their own copy of the repository, with its own local history and branch structure.

Git lets you **share entire branches between repositories**.

- "push" branches to other repositories to _publish local history_
- "pull" branches into your local repository to _see what others have contributed_

### Fetch

The git fetch command imports commits from a remote repository into your local repo.

### Creating connection wit

### Heuritics about pushing

**HERE PLEASE DO NOT PROCEED AND USE GIT PUSH, SCYFER DOES NOT NEED YOUR IMAGINARY LAYER.**

**Before pushing**, or whenever it has been a long time you have been working locally without checking the status of your repository, **it is highly recommened to check the status**.

#### Fast-forward merge

A *fast-forward merge* can occur when there is a linear path from the current branch tip to the target branch. 

Instead of “actually” merging the branches, all Git has to do is move the current branch tip up to the target branch tip.

For example:

<img src="https://www.atlassian.com/git/images/tutorials/collaborating/using-branches/07.svg" width="500" />

```
      A---B---C  development(local)
     /
D---E            origin/development(remote)

```

```
D---E---A---B---C  origin/development(remote)

```

#### 3-way merge

A *3-way merge* can occur when the branches have diverged.

To merge the branches, Git use a dedicated commit to tie together the two histories.  
The name comes from the fact that Git uses three commits to generate the merge commit: 

- the tip of the current branch.
- the tip of the target branch.
- the common ancestor commit of the two branches.

<img src="https://www.atlassian.com/git/images/tutorials/collaborating/using-branches/08.svg" width="500" />


Your local changes do not interfere with the current state of the repo, but you are late by N commits
	
	$ git status
	On branch development
	Your branch is behind 'origin/development' by X commits, and can be fast-forwarded.
  		(use "git pull" to update your local branch)
	nothing to commit, working directory clean

A *fast-forward* is done when you are behind the remote branch, with no local changes. Since you have a local change, you can't fast-forward.
	
You can then safely use `git pull` to update your repo:

	$ git pull
	$ git push

#### 3-way merge

	
#### Rebase

Your local changes interfere with the current state of repo, or in other words you modified a file from its past state and missed 1 or more commit that modified the same very file you have been working on. 

	$ git status
	On branch development
	Your branch is behind 'origin/development' by X commits, and can be fast-forwarded.
  		(use "git pull" to update your local branch)
	nothing to commit, working directory clean
	
For example:

```
      A---B---C  development(local)
     /
D---E---F---G    origin/development(remote)

```

And here is where the magic of git lies: you can **rebase your modifications on the commits you are late on** (if of course they do not differ to much from each other, like one deletes a function you modified). **To do so safely**, 

Use `git fetch` to **fetch the commits you missed**.  
Use `git rebase` to **rebase/reapply your local changes on the commits you are late on** :

1. temporarily undo your local commits (E) 
2. fast-forward to the tip of the remote branch (G)
3. reapply your local commits as the last commits (A', B', C')



```
              A'--B'--C'  development(local)
             /
D---E---F---G             origin/development(remote)
```

```
$ git fetch
$ git rebase
```
## Config

### Default Pull config

	$ git config --global branch.autosetuprebase always

All `git pull` commands will integrate commits via `git rebase` instead of `git merge`. This ensure a linear history by preventing unnecessary merge commits.

It is like saying, “I want to put my changes on top of what everybody else has done.”

### Default Push Config

	$ git config --global push.default simple

### Undo Last Commit Command

Let's create a git command to undo the last submitted commit. This may be useful when : 

- your commit is incomplete
- you mispelled your message.

```
$ git config --global alias.undo-commit 'reset --soft HEAD^'
```

Then just run the following command when needed

	$ git undo-commit

## Git Workflow

### Setup local repository

- clone _origin/master_ branch
- create _development_ branch
- synchronize _development_ branch to _origin/development_ branch, using pull

```
$ git clone https://<username>@bitbucket.org/scyferteam/scyfernn.git
$ git branch development
$ git checkout development
$ git pull origin/development
```

### Work on a new feature

##### Setup feature branches

- create _feature_ branch
- create _origin/feature_ branch and synchronize to _feature_ branch, using push 

```
$ git checkout development
$ git branch feature_x
$ git push --set-upstream origin/feature
```

##### Make changes

- edit
- stage
- commit

- make changes
	- edit
	- stage
	- commit
- synchronize changes

```
$ git checkout feature

```

##### Merge

```
$ git checkout development
$ git fetch
$ git rebase
$ git pull origin/feature_x
$ git add ...
$ git commit
($ git status)
$ git push
```

##### Delete feature branches

```
$ git push origin :feature_x
- [deleted]		feature_x

$ git branch -D feature_x
Deleted branch feature_x
```


