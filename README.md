# Tanglebots

Tanglebots are prototype weaving robots -
[for more info see here](http://fo.am/tanglebots). This workshop was funded by [AHRC Digital Transformations](http://www.ahrc.ac.uk/research/fundedthemesandprogrammes/themes/digitaltransformations/) and the [British Science Association](http://www.britishscienceassociation.org/)

![](figures/tanglebot.jpg)

## Parts list

  * [Raspberry Pi 2 Model B](https://www.raspberrypi.org/products/raspberry-pi-2-model-b/)
  * [Pimoroni Explorer Hat](https://shop.pimoroni.com/products/explorer-hat)
  * [Raspberry Pi Touch Display](https://www.raspberrypi.org/products/raspberry-pi-touch-display/)
  * Small USB keyboard/mouse (although we're using a touchscreen a mouse is easier to use)
  * [Microswitches](http://uk.rs-online.com/web/p/microswitches/0515690/) (other suppliers exist)
  * [Small motors](http://uk.rs-online.com/web/p/dc-motors/2389692/) (other suppliers exist)
  * Second hand lego
  * Second hand/broken electronic toys (e-waste)
  * Lots of yarn
  * A box of materials from the [Cornwall Scrap Store](http://www.cornwallscrapstore.co.uk/)

Some colour printed [tanglebots for beginners](guide/guide.md) guides.

This repository includes Scratch API code for access to
[Pimoroni Explorer Hat](https://shop.pimoroni.com/products/explorer-hat)
capacitive touch buttons as sensor inputs.

## Installing

- Get the pimoroni explorer hat [python api](https://github.com/pimoroni/explorer-hat): `curl get.pimoroni.com/explorerhat | bash`

Copy tanglebots scratch stuff (I should write a script for this, but this is a bit safer):
- `sudo mkdir /opt/scratch_tanglebots`
- `sudo cp scratch/* /opt/scratch_tanglebots/`
- `cp scratch/tanglebots.sb  /home/pi/Documents/Scratch\ Projects/`
- `cp scratch_tanglebots.desktop /home/pi/Desktop`

## Debugging

- Test the example script it loads automatically, which should flash the LED's
- Run /opt/scratch_tanglebots/scratch_tanglebots.sh in a console to see output from python
