# VirtualEnv installation

  1. Clone this repository:
  ```
  git clone https://github.com/xvitaly/hudman.git hudman
  ```
  2. Create a new Python Virtual Environment:
  ```
  python3 -m venv hudman
  ```
  3. Activate Virtual Environment:
  ```
  source hudman/bin/activate
  ```
  4. Install bot using Python 3 in VENV:
  ```
  cd hudman
  python3 setup.py install
  ```
  5. Run the installed application:
  ```
  /bin/hudman --huddb /path/to/hud/database.xml --outdir /tmp/hudman
  ```
