#!/usr/local/bin/fontforge
# Quick and dirty hack: converts a font to truetype (.ttf)
Print("Opening "+$1);
Open($1);
Print("Saving "+"/tmp/" + $2);
Generate("/tmp/" + $2);
Quit(0);
