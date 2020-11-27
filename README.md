# HUD Manager

[![GitHub version](https://badge.fury.io/gh/xvitaly%2Fhudman.svg)](https://github.com/xvitaly/hudman/releases)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/python-hudman/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/python-hudman/)
[![GitHub issues](https://img.shields.io/github/issues/xvitaly/hudman.svg?label=issues&maxAge=60)](https://github.com/xvitaly/hudman/issues)
---

Local HUD mirror manager. Can be used with the [SRC Repair](https://github.com/xvitaly/srcrepair) project.

# License
GNU General Public License version 3. You can find it here: [LICENSE](LICENSE). External libraries can use another licenses, compatible with GNU GPLv3.

Icon for the Windows executable and installer by [Asher](https://www.deviantart.com/kyo-tux), licensed under the terms of the [CC Attribution Share-Alike](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

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
