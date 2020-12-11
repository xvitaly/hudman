# HUD Manager

[![GitHub version](https://img.shields.io/github/v/release/xvitaly/hudman?sort=semver&color=brightgreen&logo=git&logoColor=white)](https://github.com/xvitaly/hudman/releases)
[![PyPi Version](https://img.shields.io/pypi/v/hudman.svg?logo=pypi&logoColor=white)](https://pypi.org/project/hudman/)
[![GitHub CI status](https://github.com/xvitaly/hudman/workflows/Python%20CI/badge.svg?branch=master)](https://github.com/xvitaly/hudman/actions)
[![AppVeyor CI status](https://ci.appveyor.com/api/projects/status/35yrms4i0thaw9vx?svg=true)](https://ci.appveyor.com/project/xvitaly/hudman)
[![LGTM grade](https://img.shields.io/lgtm/grade/python/g/xvitaly/hudman.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/xvitaly/hudman/context:python)
[![LGTM alerts](https://img.shields.io/lgtm/alerts/g/xvitaly/hudman.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/xvitaly/hudman/alerts/)
[![CodeFactor](https://www.codefactor.io/repository/github/xvitaly/hudman/badge/master)](https://www.codefactor.io/repository/github/xvitaly/hudman/overview/master)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/python-hudman/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xvitaly/ecrepo/package/python-hudman/)
[![GitHub issues](https://img.shields.io/github/issues/xvitaly/hudman.svg?label=issues)](https://github.com/xvitaly/hudman/issues)

---

Local HUD mirror manager. Can be used with the [SRC Repair](https://github.com/xvitaly/srcrepair) project.

# License
GNU General Public License version 3. You can find it here: [LICENSE](LICENSE). External libraries can use another licenses, compatible with GNU GPLv3.

Icon for the Windows executable and installer by [Asher](https://www.masteriantart.com/kyo-tux), licensed under the terms of the [CC Attribution Share-Alike](https://creativecommons.org/licenses/by-sa/4.0/legalcode).

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
