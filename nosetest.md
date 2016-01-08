# Nosetests

http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137


To test coverage, execute 

	THEANO_FLAGS="device=cpu" theano-nose tests/  --with-doctest --with-coverage --cover-package=NN --cover-html

standard unittest

	nosetest

also perform doctests

	nosetest --with-doctest 

perform coverage tests

	nosetest --with-coverage

Only perform coverage test for this package

	nosetest --with--coverage --cover-package=NN

write coverage results to html

	nosetest --with-coverage --cover-html

- `--with-doctest` : also perform doctests
- `--with-coverage` : also perform a coverage report
- `--with-coverage --cover-package=<package>` : restrict coverage report to selected package
- `--with-coverage --cover-html` : produces 

### Example

	theano-nose tests/  --with-doctest --with-coverage --cover-package=NN --cover-html