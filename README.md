kingpick-cli
==============================================================================

Requirements
------------
- Python3
- Pip
- Virtualenv

Development
------------

Inside `cli` directory:

```bash
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

python setup.py develop

kpick -h
```

Installation
------------

Inside `cli` directory:

```bash
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

python setup.py install

kpick -h
```

Docker
------------

Inside `cli` directory:

```bash

docker build -t kpick .

docker run --rm kpick

```