---
title: Creating Assets for Substance painter
description: 
date: 2022-05-26
tags:
	- Substance Painter
    - Pipeline
layout: layouts/post.njk
---

There are two workflows I use.

## Method1: Baking decal with blender

[GrabDoc](https://razed.gumroad.com/l/grabdoc) is a free addon that simplifies the baking process.

The addon utilized blender's baker so the same limitation applies here.

Bring out the Addon panel by pressing `N` and click on new scene

{% image "/img/painter_decal/grabdoc_new.png" %}

When you set up a new scene with grabdoc you get:

{% image "/img/painter_decal/grabdoc_scene.png" %}
{% image "/img/painter_decal/grabdoc_outliner.png" %}

1. A square backplate
2. A orthographic camera above the plane pointing at it. 
3. The render resolution is set to 2048x2048 pixels  

For basic usage you only need to konw three settings.

{% image "/img/painter_decal/grabdoc_menu_annotate.png" %}

1. The backplate control. Selectibility, viewport visibility, render visibility (toggle this off for transparent background)
2. Export path. Where the texture will be saved.
3. Three columns 
    - Checkbox: Check the map you want to be exported
    - Long button: Preview bake within viewport
    - Short button: Preview in a pop up window. 

#### Example 1: Screw

Here I modeled a very simple screw like object. There is a round plane underneath the plane with a groove. They are not connected. Since normal map doesn't store height information, the edge where the two plane join will be seamless as long as they are facing the same direction.

{% sidebyside %}
{% image "/img/painter_decal/floater_decal_wire_crop.png" %}
{% image "/img/painter_decal/floater_decal_solid_crop.png" %}
{% endsidebyside %}

In this case I only needed the normal map.

{% sidebyside %}
{% image "/img/painter_decal/flathead_normal.png" %}
{% image "/img/painter_decal/flathead_applied.png" %}
{% endsidebyside %}


#### Example 2: Ornamental Curve

{% sidebyside %}
{% image "/img/painter_decal/ornamental_curve_normal.png" %} 
{% image "/img/painter_decal/ornamental_curve_applied.png" %}
{% endsidebyside %} 

A bunch of curves with a bevel profile on them. I also baked an alpha for masking. 

## Method2: Alpha map -> Normal map with Materialize

[Materialize](http://boundingboxsoftware.com/materialize/) is a standalone software that generates various textures with just a diffuse map. 


Several alpha texture is created in affinity designer.

{% image "/img/painter_decal/affinity_decal.png" %}

They are then imported into materialize.

Import your diffuse map into the software by clicking on the `O` under the Diffuse Map.

{% image "/img/painter_decal/materialize_diffuse.png" %}

Create a Height Map using the `Create` button under the height Map.

Using the sliders to adjust the height map look. Area in white will appear indented. If embossed look is desired, adjust the contrast so the height map is inverted. 

{% sidebyside %}
{% image "/img/painter_decal/materialize_diffuse_adjust.png" %}
{% image "/img/painter_decal/materialize_diffuse_adjust2.png" %}
{% endsidebyside %}

If the alpha map is aliased at the edge it is a good idea to make the heightmap slightly blurry so the final normal map wouldn't be as pixelated when applied.

This is the normal map, created from heightmap. Click on the `S` to save the map.

{% image "/img/painter_decal/materialize_normal.png" %}

Now let's import the map into substance. Create a new paint layer, turn off all the channels except the normal channel.

Unfortunately there are a couple of problems. 

1. The edge is blurry
2. The stamp is stretched

The solutions are quite simple:
1. Change to a hard edge brush
2. Modify the texture to a square texture

The normal map produced by Materilize follows the DirectX convention and will work in Substance Painter wihtout changes. 

Although substance painter can export either OpenGL or DirectX normal map, the ones imported into substance painter must not be in opengl otherwise the output will be mangled. If you need to convert one to the other, invert the green channel of the normal map, either through photoshop or via shaders. 

The reason why I square the image afterwards and not before feeding it into Materialize is so that the area outside the decal isn't painted over, which also happens to be affinity designer's default behavior.

{% sidebyside %}
{% image "/img/painter_decal/stamp_substance.png" %}
{% image "/img/painter_decal/stamp_directx.png" %}
{% endsidebyside %}

{% sidebyside %}
{% image "/img/painter_decal/Hammer%20Diameter%20Normal_blur_square.png" %}
{% image "/img/painter_decal/Hammer%20Diameter%20Normal_blur_square_directX.png" %}
{% endsidebyside %}

Here is two screenshots of the viewport of substance painter and the viewport of blender. The lights are coming from the north. Top row opengl maps, bottom row directx maps. 

Recall the flathead decal I have shown earlier. If you paid attention you might have realized something isn't quite right. 

{% sidebyside %}
{% image "/img/painter_decal/flathead_applied.png" %}
{% image "/img/painter_decal/flathead_invert_applied.png" %}
{% endsidebyside %}

