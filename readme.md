# Quadsphere Addon

Really simple Blender addon to make a cube into a sphere with all quad topology.
Adds the item to the shift+A menu so you can use it like any mesh primitive.

How the addon works:
A subdivison modifier gets added to give the cube enough topo to deform.
Then all you need is a cast modifier set to factor 1 and some smooth shading. 

I usually do this with hardOps/spherecast but it's an extra step,
and this shape should really be inside Blender by default!  

EDIT: You can do the same with 'Extra Objects" addon that comes with Blender.
Use the Round Cube and set the radius to 1.00 (mine was set wrong).
Doesn't come shaded smooth though so it's still an extra step!

<3  
v0.2.0:
Added option to change subdivision levels  
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
