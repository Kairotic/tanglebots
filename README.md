# Setup for tanglebots workshop

Tanglebots are failed weaving robots -
[for more info see here](http://fo.am/tanglebots).

Includes Scratch code for access to Pimoroni Explorer Hat capacitive
touch buttons from scratch (as sensors).

Install: 

- Get the pimoroni explorer hat python api: `curl get.pimoroni.com/explorerhat | bash`

Really it only now depends on the python capxxx lib for the buttons that this installs, but the rest is good to have anyway.
Link to the github for that: https://github.com/pimoroni/explorer-hat

Copy tanglebots scratch stuff:
- sudo mkdir /opt/scratch_tanglebots
- sudo cp scratch/* /opt/scratch_tanglebots/ 
- cp scratch/tanglebots.sb  /home/pi/Documents/Scratch\ Projects/
- cp `scratch_tanglebots.desktop` /home/pi/Desktop

Debugging 
- test the example script it loads automatically
- run /opt/scratch_tanglebots/scratch_tanglebots.sh in a console to see output from python
