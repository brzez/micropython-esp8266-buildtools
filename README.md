# micropython-esp8266-buildtools
Build micropython for esp8266 using docker


You can set it up via docker-compose.yml

`MICROPYTHON_LIB` - contains a list of micropython-lib libraries (space delimited)  
volumes:  
`./my_module` - path for code which will be built into the result .bin  

To build image - just run `docker-compose up`. It will build the Dockerfile (this will take some time).  
Then it will run the `build.sh` script.
The resulting `firmware-combined.bin` should be located in `./build` directory.

## deploy.py

This is a standalone tool for quickly precompiling and deploying files to the board.
It uses ampy & mpy-cross (`requirements.txt`). 

Setup:
- `PORT` - port which the board is on
- `OUT_DIR` - temporary output directory
- `FILES` - list of files, `("input file", "output file")` Where, if output file ends with .mpy - it will get compiled using mpy-cross
