# Homebrew

## Uninstall
	
	# Uninstall - uninstalls
	$ brew uninstall <app>
	
	# Cleanup - cleans up old homebrew files
	$ brew cleanup

	# Prune - removes dead symlinks in homebrew
	$ brew prune

### Force uninstalls failed python

	$ brew uninstall -f python



### Cleanup - cleans up old homebrew files
	
	$ brew cleanup

### Reinstall python

	$ brew install python

## Cache

### Clear the brew cache

	$ rm -rf `brew --cache`

### Recreate the brew cache

	$ mkdir `brew --cache`
	
	

## Symlinks

### Add symlinks

Use `brew link [--overwrite] <command>` to **make symlinks in `/usr/local/bin` that point to Homebrew's installed executables**.
	
	brew link --overwrite python	

### Remove symlinks

Use `brew prune` to **remove dead symlinks** in homebrew.

## Doctor

Use `brew doctor` to **check for common errors causing issues** in homebrew.