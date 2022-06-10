# VirtualEnv installation

Clone this repository:
```
git clone https://github.com/xvitaly/hudman.git hudman
```

Create a new Python Virtual Environment:
```
python3 -m venv hudman
```

Activate Virtual Environment:
```
source hudman/bin/activate
```

Install bot using Python 3 in VENV:
```
cd hudman
python3 setup.py install
```

Run the installed application:
```
/bin/hudman update --huddb /path/to/hud/database.xml --outdir /tmp/hudman
```
