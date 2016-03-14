# Symbolic Links

Symbolic links, otherwise known as *symlinks*, are basically **advanced shortcuts**. You can create symbolic links to individual files or folders, and then these will appear like they are stored in the folder with the symbolic link even though the symbolic link only points to their real location.

There are two types of symbolic links :

- **Soft symlinks** work essentially the same as a standard shortcut.  When you open a soft link, you will be redirected to the folder where the files are stored.  
- **Hard symlinks** makes it appear as though the file or folder actually exists at the location of the symbolic link, and your applications won’t know any different. 

```
ln [-s] /path/to/original /path/to/destination
```

Use the `-s` flag option to make a *soft symlink* rather that a *hard symlink*.

## Usage

### Link executables

An example would be to offer easier access to an otherwise buried executable by linking the command to `/usr/local/bin/`

```
sudo ln -s /A/Deeply/Buried/Path/To/command /usr/local/bin/commmand
```

This would allow the user to type `command` and access the executable, without having to prefix the command execution with the entire path.

### Link folders

For example, to create a symbolic link for the user Downloads folder which links it to a directory on a separate mounted drive, syntax may look like the following:

```
ln -s /Volumes/Storage/Downloads/ ~/Downloads/
```

That will link the active users ~/Downloads/ folder to a directory named “Downloads” on the mounted drive called “Storage”. If such a directory and drive existed, this would basically allow all files that would typically appear in the user downloads folder to go to the other mounted volume instead, essentially offloading the storage burden to that separate drive, while still preserving the appearance of a ~/Downloads/ folder for the user. As mentioned before, this behaves much like an alias.