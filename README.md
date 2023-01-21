# Presentation from a logo

This is a template for a latex beamer presentation using a custom logo. Theme colors are modified according to prevailing color of the logo.

Created with logo of the Department of Fluid Mechanics and Thermodynamics, FME CTU kept in mind.

To create `main.tex` run `preprocess.py`. This script takes following arguments:

* `-i`: path to logo, defaults in `imgs/logo.png`
* `-l`: RGB code of a light color to blend the main color with, defaults in white (`255, 255, 255`)
* `-d`: RGB code of a dark color to blend the main color with, defaults in black (`0, 0, 0`)

Try running e.g. with these arguments:

```bash
python3 preprocess.py -i "imgs/logo.png" -l "220,255,255"
```

With a main created one can continue creating a beamer presentation as usually.
