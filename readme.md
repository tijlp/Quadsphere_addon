# Quadsphere Addon

Really simple Blender addon to make a cube into a sphere with all quad topology.
Adds the item to the shift+A menu so you can use it like any mesh primitive.

How the addon works:
A subdivison modifier gets added to give the cube enough topo to deform.
Then all you need is a cast modifier set to factor 1 and some smooth shading. 

I usually do this with hardOps/spherecast but it's an extra step,
and this shape should really be inside Blender by default!  

EDIT: You add a quadsphere with 'Extra Objects" addon that comes with Blender.
Use the "Round Cube" and set the radius to 1.00 (mine was set wrong).


<3  
v0.3.0:  
Added menu that let's you quickly set a viewport material  
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
## Known Issues:
v0.3.0:  
Calling the viewport color picker menu blocks acces to the original menu, Not even F9 brings it back :(    
I'll try to solve it soon.. if you know how let me know! :)  
For now realize you can't change size/subdivs/apply modifiers anymore after opening the color menu.