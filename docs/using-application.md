# Using application

## Running application

Forward [API tokens](api-tokens.md) as an environment variables, then run the application:

```bash
export HUDMAN_LOGIN=SAMPLE
export HUDMAN_APIKEY=SAMPLE_API_KEY
hudman update --huddb /path/to/hud/database.xml --outdir /tmp/hudman
```

## Command-line options

```text
usage: hudman [-h] (download | update) --huddb HUDDB --outdir OUTDIR
```

Actions (required, mutually exclusive):

  * `download` - download all HUDs without updating them;
  * `update` - update all HUDs and download only new files.

Options:

  * `-h` or `--help` - show help message and exit;
  * `-d` or `--huddb` - path to the local HUDs database file;
  * `-o` or  `--outdir` - path to the output directory for storing downloaded files.
