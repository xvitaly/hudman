# Fedora installation

  1. Enable our COPR repository:
  ```
  sudo dnf copr enable xvitaly/ecrepo
  ```
  2. Install the `python3-hudman` package:
  ```
  sudo dnf install python3-hudman
  ```
  3. Run the installed application:
  ```
  hudman --huddb /path/to/hud/database.xml --outdir /tmp/hudman
  ```
