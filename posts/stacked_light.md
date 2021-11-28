---
title: Creating light falloff with stacked light and varied radius
description: 
date: 2021-11-25
tags:
	- Lighting
layout: layouts/post.njk
---

![Stacked light example](/img/stacked_lights/stacked_lights_render.png)

This mimics a sun near dusk lighting an interior with a highly compressed light falloff. The scene has two lights in the same location, but with different radius, different color temperatures and different max bounces. 

The technique isn't "photographical realistic" realistic but is quite commonly deployed by 2d artists. 

https://www.youtube.com/watch?v=UnxLy71xuPk

# Setup (srgb view transform)

This simple scene is a simple blockout of an interior scene with two sun lamps.

The first lamp is a 1000k, strength 2 sun lamp with a high radius to make the edge slightly blurry.
![First lamp](/img/stacked_lights/low_temp_isolated.png)

This light has a limited bounce to avoid red light spilling all over the scene. This is the result with the default 1024 bounces, it might or might not be desirable.
![High bounce on the red lamp will tint the shadow red](/img/stacked_lights/too_high_bounces.png)

The second lamp is a 3500k, strength 8 with a low radius for a sharper edge.
![Second lamp](/img/stacked_lights/high_temp_isolated.png)

The scene uses standard srgb view transform. The default filmic transform compresses highlight area, making it less pronounced. 

# Setup (filmic view transform)
![Filmic render](/img/stacked_lights/no_filmic.png)

You can still achieve the blown out highlight look with filmic transform but not without some tweaking. The scene will be overall more illuminated and less saturated. 

![Filmic render adjusted](/img/stacked_lights/yes_filmic.png)
- Color management:
	- Filmic
	- Very High Contrast
	- Exposure -2
- Lights:
	- High temperature light: Strength 120, Angle 2, Max Bounces 1024, 3500 Kelvin
	- Low temperature light: Strength 50, Angle 4, Max Bounces 2, 1200 Kelvin


## Example blend file

[stacked_lights.blend](/asset/stacked_lights.blend)