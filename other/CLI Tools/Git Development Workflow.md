# Git Development Workflow

To **use Git**, while it is highly recommended to read the whole [documentation](https://git-scm.com/docs), you can refer to this **very comprehensive [cheat-sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)**.

Official Git Documentation : [https://git-scm.com/docs](https://git-scm.com/docs)  
Github Git Cheatsheet : [https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
Atlassian (aka BitBucket) Git Tutorial : [https://www.atlassian.com/git/tutorials/](https://www.atlassian.com/git/tutorials/)  

- Setting up repository
	3. Clone repo 
	4. Create branch
- Make and record changes
	1. Edit
	2. Stage (Add)
	3. *Status*
	4. Commit

- Update code base
	1. Fetch
	2. *Status*
	1. Pull (when fast-forward) / Rebase (when
	1.
- Sync Branches
	1. Fetch
	2. *Status*
	1. Pull
	2. Push
	3. Rebase 



## Config

### Default Push Config

	$ git config --global push.default simple

### Undo Last Commit

Let's create a git command to undo the last submitted commit. This may be useful when your commit is incomplete, or you mispelled your message.

	$ git config --global alias.undo-commit 'reset --soft HEAD^'

Then just run the following command when needed

	$ git undo-commit

## Git Workflow

### Setup local repository

- clone _origin/master_ branch
- create _development_ branch
- synchronize _development_ branch to _origin/development_ branch, using pull

```
# Clone repository
$ git clone https://<username>@bitbucket.org/scyferteam/scyfernn.git

# Sync local development branch with remote development branch
$ git checkout development
```
Since your local repo knows that origin has a development branch, it automatically understands that you want to checkout to that branch. Therefore Git automatically creates a local development branch with origin/development as upstream branch.

### Develop new feature

##### Setup feature branches

```
# Check out development to fork from it
$ git checkout development

# Start new feature branch
$ git branch new_feature
$ git checkout new_feature

# Create upstream connection
$ git push --set-upstream origin/new_feature

($ git push -u new_feature origin/new_feature)
```

##### Make changes (loop)

```
$ git checkout new_feature

# Edit some files
git add <file>
git commit -m "Start a new feature"

# Edit some files
git add <file>
git commit -m "Continue improving new feature"

# Publish changes
git push
```

### Finish new feature

##### Publish new feature

```
$ git checkout development

# Update development branch to latest version
$ git fetch
$ git rebase

# Merge new feature
$ git pull origin/new_feature
$ git add <files>
$ git commit -m "Added new feature"

# Publish development branch with new feature
$ git push
```

##### Delete feature branches

```
# Delete remote feature branch
$ git push origin :feature_x
- [deleted]		feature_x

# Delete local feature branch
$ git branch -d feature_x
Deleted branch feature_x
```


