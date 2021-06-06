```
python -V
python3 -m venv venv
source ./venv/bin/activate
python -V
```

```
python -m pip install pyyaml
python -m freeze > requirements.txt
```

## DI

```
python -m pip install dependency-injector
python -m freeze > requirements.txt
```

? Virtual Environment seems to be picking up dependencies globally installed on the machine
