
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

```
# Start a new feature
git checkout -b new-feature master

# Edit some files
git add <file>
git commit -m "Start a feature"

# Edit some files
git add <file>
git commit -m "Finish a feature"

# Merge in the new-feature branch
git checkout master
git merge new-feature
git branch -d new-feature
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
	
```	
# Start a new feature
git branch new-feature

# Develop the feature branch
git checkout new-feature

# Edit some files
git add <file>
git commit -m "Start a feature"

# Edit some files
git add <file>
git commit -m "Finish a feature"

# Develop the master branch
git checkout master

# Edit some files
git add <file>
git commit -m "Make some super-stable changes to master"

# Merge in the new-feature branch
git merge new-feature
git branch -d new-feature
```

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
