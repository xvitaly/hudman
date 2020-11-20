# HUD mirror script

[![GitHub version](https://badge.fury.io/gh/xvitaly%2Fhudman.svg)](https://github.com/xvitaly/hudman/releases)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/python-hudman/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/python-hudman/)
[![GitHub issues](https://img.shields.io/github/issues/xvitaly/hudman.svg?label=issues&maxAge=60)](https://github.com/xvitaly/hudman/issues)
---

Simple script to create a local HUD mirror, can be used with [SRC Repair](https://github.com/xvitaly/srcrepair) project.

# License
[GNU General Public License version 3](LICENSE). External libraries can use another compatible licenses.

# Requirements

  * Python 3.6+ with full set of standard libraries;
  * python-requests.

# Installation

  1. Clone this repository:
  ```bash
  git clone https://github.com/xvitaly/hudman.git hudman
  ```
  2. Install (in Python virtual environment):
  ```bash
  python setup.py install
  ```
  3. Run application:
  ```bash
  hudman --huddb /path/to/hud/database.xml --outdir /tmp/hudman
  ```

# Available options

```text
usage: hudman [-h] --huddb HUDDB --outdir OUTDIR [--save]
```

Optional arguments:
 * `-h` or `--help` - show this help message and exit;
 * `-d` or `--huddb` - specify full path to the HUD database file;
 * `-o` or  `--outdir` - specify full path to the main directory for storing downloaded files;
 * `-s` or `--save` - save HUD database automatically.

# Documentation

  1. Install Doxygen.
  2. Build documentation in HTML format:
  ```bash
  doxygen
  ```
