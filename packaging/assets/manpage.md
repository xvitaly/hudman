% hudman(1) | General Commands Manual

# NAME

hudman - simple tool for creating a local HUD mirror

# SYNOPSIS

**hudman** \[-h\] --huddb HUDDB --outdir OUTDIR \[--save\]

# DESCRIPTION

HUD Manager is a simple tool for creating a local HUD mirror. Can be used together with the SRC Repair project.

# COMMAND-LINE OPTIONS

#### -h, \-\-help
Show a simple help message and exit.

#### -d, \-\-huddb
Specify full path to the HUD database file. Required.

#### -o, \-\-outdir
Specify full path to the main directory for storing downloaded files. Required.

#### -s, \-\-save
Automatically save changes to the HUD database file.

# SUPPORTED CONFIGURATIONS

HUD Manager can operate in two modes: anonymous and authorized.

This product supports of getting API credentials for the supported backends with environment variables.

# SUPPORTED BACKENDS

## Available backends

This application can use the following backends:

  * GitHub;
  * Other (only direct links are supported).

## API tokens

You can obtain API tokens from these sources:

  * **GitHub**: https://docs.github.com/en/articles/creating-a-personal-access-token-for-the-command-line

# ENVIRONMENT OPTIONS

## GitHub backend

To bypass API limits for the anonymous users, you will need to forward your API username and token:

  * **HUDMAN_LOGIN** - GitHub user login (username).
  * **HUDMAN_APIKEY** - GitHub API personal access token.

## Forwarding options

Export environment variables using `export` command:

```
export HUDMAN_LOGIN=foobar
export HUDMAN_APIKEY=ABCDEFG123
```

Start the application in authorized mode:

```
hudman --huddb /path/to/hud/database.xml --outdir /tmp/hudman
```

# AUTHORS

Copyright (c) 2021 EasyCoding Team.
