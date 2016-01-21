
# Gulp

## Introduction

Gulp is a build system. A build system is a collection of tasks (called "task runners") that automate repetitive work.

#### What a build system does
- Repetitive tasks
	- concatenating Javascript
	- prefixing CSS
- Utilities
	- JSHint
	- Uglify (compress+minify)	Javascript
- Local server
- Live reload

#### How it affect you
Page Speed:

- Less file requests for page load
- Faster file requests

Development Worflow:

- You can use cool technologies (SASS)
- You can break your code into multiple files
- Easier to avoid conflicts with multiple files (collaborative work)
- You can avoid annoying, repetitive tasks

#### Gulp vs. Grunt

Gulp's force is in the use of streams (data streams in memory) which limits reading/writing in files (slower operations).

For each task, Grunt reads a file and writes the solution which affects performance
This also forces repetition in tasks configurations because they are configured independently instead of in relation with eachother.


Since streams are asynchronous, we can use different system resources simultaneously. 

- Write to Disc does not require a lot of CPU or memory 
- Operate on the data does not solicit discs (except extreme cases). 

With GruntJS these steps take place sequentially which creates bottlenecks. With Gulp these are simultaneous, leading to a more intelligent use of the system.

## Install Gulp
Using npm, install Gulp (in node_modules/) and add it as a dependency (in package.json). Gulp needs to be installed globally to have `gulp` available on the command line.

```
[sudo] npm install -g gulp
npm install gulp --save-dev
```

## Structure of a Gulp file

A typical Gulp file will have 4 different sections:

1. Required Modules
2. Defined Tasks
3. Watch Task
4. Default Task

### Required Modules

In this section, declare any modules that you need for your build.

```
var gulp = require('gulp');
var uglify = require('gulp-uglify');
```

### Defined Tasks

In this section, define and name task  

Ex:

- task for compressing static images
- task for concatenating files
- task for deployment build

```
gulp.task('task-name', function(){
	// instructions
});
```
To run a defined task, just run : `gulp <task-name>`

### Watch Task

The purpose of the "watch task" is to watch for changes in certain files. When changes occur, then run certain tasks.

Ex: Watch folder js for all .js files, then on change run 'scripts' task.

```
gulp.task('watch', function(){
	gulp.watch('app/js/**/*.js', ['scripts']);
});
```

### Default Task

The purpose of the "default task" is to kick off certain tasks when running the `gulp` command. It will run the given tasks asynchronously (ie at the same time).

Define the default task:

```
gulp.task('default', ['scripts', 'watch']);
```

Run the default task from the CLI:

```
gulp
```

## Structure of a Gulp Task

The physiognomy of a Gulp task is:

1. `gulp.src(glob)`: match globs or array of globs and returns a stream of objects that can be piped to plugins.
2. `pluginname()`: branch the stream on one or more tasks.
3. `gulp.dest(path)`: write to the given folder.

```
gulp.task('sass', function(){
	return gulp.src('source-files')
	.pipe(sass()) // Using gulp-sass
	.pipe(gulp.dest('destination-folder'))
});
```

## Globs in Node

Globs are matching patterns for files that allow you to add more than one file into gulp.src. It's like regular expressions, but specifically for file paths.

Most workflows with Gulp tend to only require 4 different globbing patterns:

- `*.scss`: The `*` pattern is a wildcard that matches any pattern in the current directory. In this case, we’re matching any files ending with .scss in the root folder (project).
- `**/*.scss`: This is a more extreme version of the * pattern that matches any file ending with .scss in the root folder and any child directories.
- `!not-me.scss`: The `!` indicates that Gulp should exclude the pattern from its matches, which is useful if you had to exclude a file from a matched pattern. In this case, not-me.scss would be excluded from the match.
- `*.+(scss|sass)`: The plus `+` and parentheses `()` allows Gulp to match multiple patterns, with different patterns separated by the pipe `|` character. In this case, Gulp will match any file ending with .scss or .sass in the root folder.

```
gulp.task('sass', function() {
	return gulp.src('app/scss/**/*.scss') // all .scss files in app/scss and children dirs
		.pipe(sass())
		.pipe(gulp.dest('app/css'))
})
```

## Main Gulp Plugins
http://blog.nodejitsu.com/npmawesome-9-gulp-plugins/

- gulp-util : 
- gulp-concat : concatenate files
- gulp-uglify : minify js files with UglifyJS
- gulp-rename : rename file
- gulp-watch : watch changes in files
- gulp-sass : compile Sass to CSS with libsass (faster than ruby sass)
- gulp-changed : only pass through changed files
- gulp-minify-css : minify css with clean-css
- gulp-markdown : Markdown to HTML
- gulp-pleeease : CSS preprocessors with PostCSS plugins
- gulp-imagemin : compress images
- gulp-cache : caching of images so only changed images are compressed
- browser-sync : synchronised browser testing (works with Gulp)

More [Gulp Plugins](http://gulpjs.com/plugins/)

## Gulp Recipes

[Gulp Recipes](https://github.com/gulpjs/gulp/tree/master/docs/recipes)

## References

[Gulp.js Build System Tutorial](https://www.youtube.com/watch?v=LmdT2zhFmn4&list=PLv1YUP7gO_viROuRcGsDCNM-FUVgMYb_G)  
https://markgoodyear.com/2014/01/getting-started-with-gulp/
https://css-tricks.com/gulp-for-beginners/
https://blog.simpleblend.net/gulp-organization-structure/


