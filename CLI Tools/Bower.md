
# Bower

[Bower](http://bower.io/) is a **package manager** for **front-end/client-side** dependencies (aka the brower package manager).

ex: Foundation, jQuery, Angular.js, Backbone, etc.


## Install Bower

### Requirements

Bower requires [Node](https://nodejs.org/), [npm](https://www.npmjs.com/) and [Git](https://git-scm.com/).

To check your current requirements versions, run `node -v`, `npm -v` and `git -v` in the CLI.

### Install Bower

```
[sudo] npm install -g bower
```

## bower.json
bower.json is the manifest file used to manage bower packages locally.


##### Create a bower.json file:

```
bower init
```

##### Add a package as dependency in bower.json with `--save` option:

```
bower install <package-name> --save
```
##### Synchronise packages with a bower.json file:

```
bower install
```
Bower will look through bower.json and download all dependencies for you. This makes any build **reproducible** and allows team members to quickly get their project up to speed with the correct dependencies.

## Install packages

##### To install a package, run:

```
cd path/to/project
bower install <package-name> --save
```

- Bower installs the package to "**bower_components/**"
- Bower adds the package as a dependency in bower.json (`--save` option)

##### To uninstall a package, run:

```
cd path/to/project
Bower uninstall <package-name> --save
```
- Bower removes the package (or module) from "bower_components/"
- Bower removes the package dependency in bower.json (`--save` option)

## To go further

- [Bower Tools: Grunt/Gulp tools to use with Bower](http://bower.io/docs/tools/)
- [Blog article: How to manage your frontend dependencies with Bower](http://www.zell-weekeat.com/bower/)