# Fedora installation

Enable our COPR repository:
```
sudo dnf copr enable xvitaly/ecrepo
```

Install the `python3-hudman` package:
```
sudo dnf install python3-hudman
```

Run the installed application:
```
hudman update --huddb /path/to/hud/database.xml --outdir /tmp/hudman
```
