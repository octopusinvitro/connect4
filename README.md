# Connect four

A CLI game made just for fun.

## Install

Install `pyenv`:
https://github.com/pyenv/pyenv

Install the `pyenv-virtualenvwrapper` plugin:
https://github.com/pyenv/pyenv-virtualenvwrapper

Add an alias to your `.bash_aliases` file:

```sh
alias python="$HOME/.pyenv/shims/python"
alias pipenv="python -m pipenv"
```

Use `pyenv` to install the python version:

```sh
pyenv install 3.10.0
pyenv local 3.10.0
```

Upgrade `pip` and Install `pipenv` for that version of python:

```sh
python3 -m pip install --upgrade pip
python3 -m pip install pipenv
```

Use `pyenv-virtualenvwrapper` to  create a python environment for the project:

```sh
mkvirtualenv -a . connect-four
```

Check that the environment was created and that the `.project` file points to the right place:

```sh
ls $WORKON_HOME/
more $WORKON_HOME/connect-four/.project
```

Activate the environment adn install dependencies:

```sh
workon connect-four
pipenv install
```

## To run

```sh
. bin/run
```

Tests:

```sh
. bin/test
```

Lint:

```sh
. bin/lint
```
