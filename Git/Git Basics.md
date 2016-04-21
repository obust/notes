# Git Basics

To **use Git**, while it is highly recommended to read the whole [documentation](https://git-scm.com/docs), you can refer to this **very comprehensive [cheat-sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)**.

Official Git Documentation : [https://git-scm.com/docs](https://git-scm.com/docs)  
Github Git Cheatsheet : [https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
Atlassian (aka BitBucket) Git Tutorial : [https://www.atlassian.com/git/tutorials/](https://www.atlassian.com/git/tutorials/)  
Git Flow :
[http://nvie.com/posts/a-successful-git-branching-model/](http://nvie.com/posts/a-successful-git-branching-model/)

- Setting up repository
	3. Clone repo
	4. Create branch
- Record changes
	1. Edit
	2. Add (Stage)
	3. Status
	4. Commit
- Sync Branches
	1. Fetch
	1. Pull
	2. Push
	3. Rebase

## Setting up a repository

### Clone

Use `git clone <repo>` to **copy an existing Git repository** onto the local machine.  

The created Git repository has its own history, manages its own files, and is a completely isolated environment from the original repository.

When you clone a repository, it automatically creates a remote connection called `origin` pointing back to the original repository. This makes it very easy to interact with the original repository when synchronizing branches.

### Branch

A *branch* represents an **independent line of development**.

Create a separate branch to **develop a feature** (or work on a bug). The created branch has its own working directory, staging area, and history. It is a completely isolated environment from the master branch.

![](https://www.atlassian.com/git/images/tutorials/collaborating/using-branches/01.svg)

Use `git branch` to **list all _local_ branches**, and show the current branch.  
Use `git branch <branchname>` to **create a local branch**.  
Use `git branch -d <branchname>` to **delete a local branch**.  
Use `git branch -m <newbranchname>` to **rename the current local branch**.

Use `git checkout <branchname>` to **select a branch to work on**.

You can work on multiple features in a single repository using branches by switching between them with `git checkout`.

## Record changes

Developing a feature revolves around the basic **edit/stage/commit** pattern.

1. **Make changes** by editing the local branch files.
2. **Stage changed files** with `git add` to select the changed files you want to include in the next *snapshot* of the local branch.
3. **Record changed files** with `git commit` to save the *snapshot* of the local branch state to the history.

### Add

Use `git add <file>` to **add changed files to the *staging area*.**  

The *staging area* is like a buffer before commit. It tells Git which modification you want to include in the next commit, instead of committing all the changes.

Commits should tackle

However, changes are not actually recorded until you run `git commit`.



### Status

Use `git status` to **display the difference between the last commit and the staging area.**

- files modified that are staged (changed files to be committed)
- files modified that are not staged (changed files not staged for commit)
- untracked/unknown files (files that have never been committed: e.g. new files)

### Commit

Use `git commit -m "<message>"` to **commit the staged snapshot to the project history**. Committed snapshots can be thought of as “safe” versions of the local branch. will never change them unless you explicity ask it to.

Commited snapshots should answer one
The message should summarize the entire commit in less than 50 characters. For instance :

- Update the sayHello() function to output the user's name
- Change the sayGoodbye() function to a friendlier message

Make sure to commit regularly.

## Syncing

In Git’s collaboration model, every developer has their own copy of the repository, with its own local history and branch structure.

Git lets you **share entire branches between local and remote repositories**.

- "fetch" upstream commits into your local repo to _see upstream branch file changes_.
- "merge" upstream commits to _incorporate upstream branch file changes_ into the local branch.
- "rebase" local commits to _reapply local history of commits on the current version of the upstream branch files_.
- "push" local commits to the upstream branch to _publish local file changes_.

### Upstream branch

When a branch is forked, their is a connection created between the local branch and the upstream branch

- upstream branch : original/forked branch (usually on the remote repo).
- local branch : local copy of the original branch (we can work on it independently).

### Fetch
Fetching enables to **update the info we have (local repo) about the upstream branch files (remote repo)**.

Use `git fetch` to **retrieve commits from other people to the upstream branch files** into your local repo.

```
# Before fetching

  A---B---C---D---E--       origin/<branchname> (remote)

  A---B---?---              origin/<branchname> (local)
       \         
	    X---Y---Z----     * <branchname> (local)

# After fetching

  A---B---C---D---E--       origin/<branchname> (remote)

  A---B---C---D---E--       origin/<branchname> (local)
       \          
	    X---Y---Z----     * <branchname> (local)
```

### Status

Use `git status` to **display the state between the *local branch* and the *upstream branch*.**

- changed files that are staged (changes to be committed)
- changed files that are not staged (changes that will NOT be committed)
- untracked/unknown files that are not staged (files that have never been committed : e.g. new files)


### Merge

When working on a branch, it's important to be able to get it back into the main code base.
Once you’ve finished developing a feature in an isolated branch, it's important to be able to get it back into the main code base. *Merging*

NB1: ALWAYS `fetch` before merging. Otherwise the synchronization with the upstream branch.
NB2: prefer `rebase` over `merge`

1. Use `git fetch` to **fetch the commits you missed**.
2. Use `git merge <branchname>` to **incorporate a branch's history into the current branch**.



#### a) fast forward merge

A *fast-forward merge* can occur when there is a linear commit path from the local branch to the upstream branch.

```
$ git status
	On branch <branchname>
	Your branch is behind 'origin/<branchname>' by <?> commits,
and can be fast-forwarded.
```


Instead of “actually” merging the branches, all Git has to do is move the branch fork up to the upstream branch tip.

```
# Before merging (fast-forward)

A---B---C---D---E----      origin/<branchname>
     \
      \--                * <branchname>

# After merging (fast-forward)

A---B---C---D---E----      origin/<branchname>
                 \
                  \--    * <branchname>

```

NB: `git rebase`, `git merge` are equivalent in this case.

#### b) rebase merge

Your local changes interfere with the current state of repo, or in other words you modified a file from its past state and missed 1 or more commit that modified the same very file you have been working on.

Rebasing enables to **rebase your modifications on the commits you are late on**.


Use `git rebase` to **reapply local history of commits on the current version of the upstream branch files**.

1. Use `git fetch` to fetch the commits you missed.  
2. Use `git rebase` to **rebase/reapply your local changes on the tip of the upstream branch** :

This will replay the changes made (X, Y, Z) on the local branch since it diverged (B), and record the result in a new commit (H):


1. temporarily undo your local commits (B)
2. fast-forward to the tip of the remote branch (D)
3. reapply your local commits as the last commits (X', Y', Z')


```
# Before rebasing

  A---B---C---D             origin/<branchname>
       \
        X---Y---Z           <branchname>

# After rebasing

  A---B---C---D             origin/<branchname>
               \
                X'--Y'--Z'  <branchname>

```

#### c) 3-way merge

A *3-way merge* is also an option when the branches have diverged.

NB: Using rebasing is safer than merging;)


```
$ status
On branch <branchname>
	Your branch and branch 'origin/<branchname>' have diverged by respectively <?> and <#> commits.
```

To merge the branch, Git use a dedicated commit (K) to tie together the two histories.  

```
# Before merging

  A---B---C---D---E--       origin/branchname
       \         
	    X---Y---Z----     * branchname

# After merging

  A---B---C---D---E--       origin/branchname
       \           \
	    X---Y---Z---K--   * branchname
```

The name comes from the fact that Git uses three commits to generate the merge commit:

- the tip of the current branch.
- the tip of the target branch.
- the common ancestor commit of the two branches.

#### c) merge conflicts




### Push

Pushing enables to **publish your local changes to a central repository**.

Use `git push <remotename> <branchname>` to **export commits to the upstream branch in the remote repository** from your local repo.  

Note that `git push` is the counterpart of `git fetch` and fast-forward `git merge`.

```
# Before pushing

  A---B                origin/master
       \
        X---Y---Z      master


# After pushing

  A---B---X---Y---Z    origin/master
                   \
                       master

```

Git prevents you from overwriting the central repository’s history by refusing push requests when they result in a non-fast-forward merge. So, if the remote history has diverged from your history, you need to :

1. `git fetch` to retrieve the latest commits to the upstream branch
2. `git rebase` to apply your local commit history on top of the latest version
3. `git push` to publish your local changes to the upstream branch


## Stash

Dealing with uncommitted changes

The stash area is like the desktop bin. It's a buffer area for the deletion.

- Use `git stash` to put changed in the stashing area.
- Use `git stash pop` to **retrieve changes** from the stashing area.
- Use `git stash drop` to **discard changes** in the stashing area.

### When discarding changes

Use the stashing area to **discard changes** that have not been committed yet. Git will then bring the file back to its state of the last commit.

```
$ git stash [<filenames>]
$ git stash drop
```

### When pushing

If you try to push your local commits to the upstream branch, Git will complain because it doesn't know what to do with the uncommitted files.


all changes not committed will be discarded

```
$ git stash [<filenames>]
$ git push
$ git stash pop
```

### When switching branch

If you switch branch, all changes not committed will be discarded

```
### Move changes to another branch

$ git stash [<filename>]
$ git checkout <otherbranch>
$ git stash pop

###

$ git stash [<filename>]
$ git checkout <otherbranch>
$ git checkout <firstbranch>
$ git stash pop

```


## Config

### Default Push Config

	$ git config --global push.default simple

### Undo Last Commit

Let's create a git command to undo the last submitted commit. This may be useful when your commit is incomplete, or you mispelled your message.

	$ git config --global alias.undo-commit 'reset --soft HEAD^'

Then just run the following command when needed

	$ git undo-commit
