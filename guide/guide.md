# Tanglebots for beginners

Scratch is a drag-drop programming language we can use to control
tanglebots. It works by dragging blocks from the library of commands on
the left of the window into the scripts window in the middle to build
programs up. There should be a cat in the window in the right, but lets
try controlling a motor first.  

## Controlling a motor 

Motors are controlled using variables – you'll need to add a new
variable called 'motor1' in the window on the left.

[](https://.github.com/images/variables.png)

Wire a motor to the Explorer Hat's motor 1 '+' and '–' connections (it
doesn't matter which way round).

You can now set your variable to different numbers to turn the motor at
different speeds in each direction:

[](https://github.com/Kairotic/tanglebots/guide/motor1.png)

[](./motor2.png)

Click on these blocks you've made to control the motor. 

## Reading sensors from the outside world

Let's use a microswitch to spin the cat in the right window. The the
blocks are organised in the library by colour, which should help you
find them. Click on the green flag to test it works.

[](rotate.png)

In order to sense a microswitch being pressed you'll need to find these
3 new blocks below. Use the arrow on the 'sensor value' to select
'Input1' from the menu.

[](rotate2.png)

Then put the sensor value block inside the left bit of the “=” block,
and type “1” into the right so it looks like this:

[](rotate3.png)

Then finish it so it looks like this:

[](rotate4.png)

Wire up the microswitch so one wire goes into 5V on the Explorer Hat,
and the other goes to Input 1. Try spinning the cat with the switch!
Putting it all together Now you can use scratch to read sensors and
control motors:

[](final.png)



















