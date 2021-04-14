# VirtualEnv installation

  1. Clone this repository:
  ```bash
  git clone https://github.com/xvitaly/hudman.git hudman
  ```
  2. Create a new Python Virtual Environment:
  ```bash
  python3 -m venv hudman
  ```
  3. Activate Virtual Environment:
  ```bash
  source hudman/bin/activate
  ```
  4. Install bot using Python 3 in VENV:
  ```bash
  cd hudman
  python3 setup.py install
  ```
  5. Run the installed application:
  ```bash
  /bin/hudman --huddb /path/to/hud/database.xml --outdir /tmp/hudman
  ```
