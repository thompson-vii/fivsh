---
title: Create and Use Normals inside Substance Painter
description: 
date: 2022-05-26
tags:
	- Substance Painter
    - Pipeline
layout: layouts/post.njk
---

<i> Updated 2023-02-10: Add captions; Clarify which normals are which</i>
<br>
There are two workflows I use.

## Method1: Baking decal with blender

[GrabDoc](https://razed.gumroad.com/l/grabdoc) is a free addon that simplifies the baking process.

The addon utilized blender's baker so the same limitation applies here.

Bring out the Addon panel by pressing `N` and click on new scene

{% image400 "./img/painter_decal/grabdoc_new.png", "Addon toolbar"%}

When you set up a new scene with grabdoc you get:

{% image400 "./img/painter_decal/grabdoc_scene.png", "An orthographic camera above the backing plane, the camera is pointing at the plane" %}
{% image400 "./img/painter_decal/grabdoc_outliner.png", "Objects created when New Scene is created."%}

Three things happen when you add a New Scene.
1. A square backplate
2. A orthographic camera above the plane pointing at it. 
3. The render resolution is set to 2048x2048 pixels  

For basic usage you only need to know three settings.

{% image400 "./img/painter_decal/grabdoc_menu_annotate.png", "" %}

1. The backplate control. Selectibility, viewport visibility, render visibility (toggle this off for transparent background)
2. Export path. Where the texture will be saved.
3. Three columns 
    - Checkbox: Check the map you want to be exported
    - Long button with text: Preview bake within viewport
    - Short button: Preview in a pop up window. 

#### Example 1: Screw

Here I modeled a very simple screw like object. There is a round plane underneath the plane with a groove. They are not connected. Since normal map doesn't store height information, the edge where the two plane join will be seamless as long as they are facing the same direction.

{% sidebyside %}
{% image400 "./img/painter_decal/floater_decal_wire_crop.png", "Wireframe View" %}
{% image400 "./img/painter_decal/floater_decal_solid_crop.png", "Solid View" %}
{% endsidebyside %}

In this case I only needed the normal map. So I unckecked all the other maps and hit Export Map. Remember to uncheck render under ❶

{% sidebyside %}
{% image400 "./img/painter_decal/flathead_normal.png", "Exported Normal map" %}
{% image400 "./img/painter_decal/flathead_applied.png", "Normal map being used as a stamp inside Substance Painter" %}
{% endsidebyside %}

Remember blender uses and bakes OpenGL normal maps. This will be important later. 
#### Example 2: Ornamental Curve

Just a bunch of curves with a bevel profile on them. I also baked an alpha for masking.

{% sidebyside %}
{% image400 "./img/painter_decal/ornamental_curve_normal.png", "An ornamental Normal Map" %} 
{% image400 "./img/painter_decal/ornamental_curve_applied.png", "The above map being painted onto the side of a wood table" %}
{% endsidebyside %} 

## Method2: Alpha map -> Normal map with Materialize

[Materialize](http://boundingboxsoftware.com/materialize/) is a standalone software that can generate various texture maps with just a color image.

{% image400 "./img/painter_decal/affinity_decal.png", "Several alpha textures are created in affinity designer" %}

The maps are then imported into materialize.

Import your diffuse map into the software by clicking on the `O` under the Diffuse Map.

{% image400 "./img/painter_decal/materialize_diffuse.png", "One of the alpha inside materialize" %}

Create a Height Map using the `Create` button under the height Map.

Using the sliders to adjust the height map look. Area in white will appear indented. If embossed look is desired, adjust the contrast so the height map is inverted. 

{% sidebyside %}
{% image400 "./img/painter_decal/materialize_diffuse_adjust.png", "Side by side preview is provided" %}
{% image400 "./img/painter_decal/materialize_diffuse_adjust2.png", "Messing with the slider to get a desired look" %}
{% endsidebyside %}

If the alpha map is aliased at the edge it is a good idea to make the heightmap slightly blurry so the final normal map wouldn't be as pixelated on the edge when applied.


Click on the `S` to save the map.

{% image400 "./img/painter_decal/materialize_normal.png", "A normal map created from the heightmap" %}

Now let's import the map into substance. Create a new paint layer, turn off all the channels except the normal channel.

Unfortunately there are a couple of problems. 

1. The edge is blurry
2. The stamp is stretched

The solutions are quite simple:
1. Change to a hard edge brush
2. Modify the texture to a square texture

The normal map produced by Materilize follows the DirectX convention and will work in Substance Painter without any changes. 

Although substance painter can export either OpenGL or DirectX normal maps, the incoming normal maps still need to be in DirectX format otherwise the viewport won't show the shading correctly when you texturing. If you need to convert one format to the other, invert the green channel of the normal map. 

After exporting normals from Materilize, be sure to pad the map with transparency until the image is square. In Substance Painter, Rectangular normal maps will be distorted to fit a square. When painting the normal, use a brush with hard edge.

{% sidebyside %}
{% image400 "./img/painter_decal/stamp_substance.png", "Substance Painter Viewport, light coming from the top, the bottom DirectX normal has correct lighting" %}
{% image400 "./img/painter_decal/stamp_directx.png", "Blender viewport, light coming from the right, the top OpenGL normal has the correct Lighitng" %}
{% endsidebyside %}

{% sidebyside %}
{% image400 "./img/painter_decal/Hammer_Diameter_Normal_blur_square.png", "OpenGL normal" %}
{% image400 "./img/painter_decal/Hammer_Diameter_Normal_blur_square_directX.png", "DirectX normal" %}
{% endsidebyside %}

Here is two screenshots of the viewport of substance painter and the viewport of blender. The lights are coming from the north. Top row opengl maps, bottom row directx maps. 

Recall the flathead decal I have shown earlier. If you paid attention you might have realized something isn't quite right. 

{% sidebyside %}
{% image400 "./img/painter_decal/flathead_applied.png", "Incorrect Lighting, using OpenGL normal" %}
{% image400 "./img/painter_decal/flathead_invert_applied.png", "Correct Lighting, using DirectX normal" %}
{% endsidebyside %}

Here is two screenshots of the viewport of substance