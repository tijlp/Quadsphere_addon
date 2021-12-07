# Quadsphere Addon

Really simple Blender addon to make a cube into a sphere with all quad topology.
Adds the item to the shift+A menu so you can use it like any mesh primitive.

Subdivision are needed to give the cube enough topo to deform.
Then all you need is a cast modifier set to factor 1  

I usually do this with hardOps/spherecast but it's an extra step,
and this shape should really be inside Blender by default!  
EDIT: You can do the same with 'Extra Objects" addon that comes with Blender,
use the Round Cube and set the radius to 1.00. Doesn't come shaded smooth though
so it's still an extra step but with Round Cube you can change the subdiv levels
on the fly. 

<3

v0.1.0:  
Currently the only options after adding the mesh are to change the size and apply the modifiers.

## Download the addon:

```

Go to the green button that says "Code" and download the zip

```
## Install the addon:

```
Install like any other addon: F4 > Preferences > Addons > Install the zip file

```
