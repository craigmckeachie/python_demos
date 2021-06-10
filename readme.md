## Installing

https://opensource.com/article/19/5/python-3-default-mac
https://github.com/pyenv/pyenv#how-it-works

### Mac

```
which python
which python3
python -V
python3 -V
echo "alias python=/usr/local/bin/python3" >> ~/.zshrc
echo "alias python=/usr/local/bin/python3" >> ~/.bashrc
```

```
which pip
pip -V
```

## Linting

https://code.visualstudio.com/docs/python/linting

## String Formatting

https://realpython.com/python-string-formatting/

## Collections

https://www.geeksforgeeks.org/python-list-vs-array-vs-tuple/

## Virtual Environment

### POSIX

```
python -V
python3 -m venv venv # or just python if 3 is default
source ./venv/bin/activate
python -V
```

### Windows

```
python -V
python -m venv venv
.\venv\Scripts\Activate.ps1
# OR
.\venv\Scripts\activate.bat
```

### VS Code

Check to make sure VS Code status bar is using venv version as well as terminal
If prompted to install autopep8 or other linter go ahead and install
