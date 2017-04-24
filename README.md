kingpick-cli
==============================================================================

Development
------------

```bash
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

python setup.py develop

kpick -h
```

Installation
------------

```bash
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

python setup.py install

kpick -h
```

Docker
------------

```bash

docker build -t kpick .

docker run --rm kpick

```