#### Requirements
- Python >= 3.4
- Python virtualenv (pyvenv)

#### Dev Setup
Create a virtual env
```
pyvenv ve
```

Activate the virtual env
```
source ve/bin/activate
```

> You can deactivate the virtual env using the `deactivate` command

Install requirements
```
pip install -r requirements.txt
```

Run
```
./bright_bytes.py
```

Test
```
py.test test_bright_bytes.py
```
