# Command-line arguments

```text
usage: hudman [-h] (download | update) --huddb HUDDB --outdir OUTDIR
```

Actions (required, mutually exclusive):
  * `download` - download all HUDs without updating them;
  * `update` - update all HUDs and download only new files.

Options:
  * `-h` or `--help` - show help message and exit;
  * `-a` or `--huddb` - path to the local HUDs database file;
  * `-o` or  `--outdir` - path to the output directory for storing downloaded files.
