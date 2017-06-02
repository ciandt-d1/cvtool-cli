cvtool-cli
==========

Requirements
------------
- Python3
- Pip
- Virtualenv

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

Development with Docker
------------

```bash
 
# build local docker image
docker build --build-arg setup_mode=develop -t cvtool/cli:local .

# open bash
docker run -it --rm --entrypoint bash -v ${PWD}/kpick:/usr/src/app/kpick cvtool/cli:local
```

![](https://raw.githubusercontent.com/ciandt-d1/cvtool-cli/master/kpick%20command%20line.png)