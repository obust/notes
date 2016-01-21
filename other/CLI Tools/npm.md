# npm

[npm](https://www.npmjs.com/) is a **package manager** for **node development utilities** dependencies. (aka the utility tool package manager)

ex: Grunt, Gulp, Browser-Sync, Plumber, etc.

## Install npm

### Requirements
npm requires Node to run. 

To install Node, simply use an installer from [nodejs.org](http://nodejs.org/).

### Install npm

Node comes with npm installed so you should have a version of npm. However, npm gets updated more frequently than Node does, so you'll want to make sure it's the latest version `npm -v`.

```
[sudo] npm install -g npm
```

## package.json
package.json is the manifest file used to manage npm packages locally.


##### Create a package.json file:

```
npm init
```

##### Add a package as dependency in package.json with `--save-dev` option:

```
npm install <package-name> --save-dev
```
##### Synchronize packages with a package.json:

```
npm install
```
npm will look through package.json and download all dependencies for you. This makes any build **reproducible** and allows team members to quickly get their project up to speed with the correct dependencies.

## Install packages

##### To install a package, run:

```
cd path/to/project
npm install <package-name> --save-dev
```
- npm installs the package (or module) to "**node_modules/**"
- npm adds the package as a dependency in package.json (`--save-dev` option)

##### To uninstall a package, run:

```
cd path/to/project
npm uninstall <package-name> --save-dev
```
- npm removes the package (or module) from "node_modules/"
- npm removes the package dependency in package.json (`--save-dev` option)

## To go further


