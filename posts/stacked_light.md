---
title: Creating light falloff with stacked light and varied radius
description: 
date: 2021-11-25
tags:
	- Lighting
layout: layouts/post.njk
---

![Stacked light example](/img/stacked_lights/stacked_lights_render.png)

This simple scene is a simple blockin of an interior scene with two sun lamps shining through a small gap in an otherwise enclosed box. 

This setup mimics a sun near dusk lighting an interior with a highly compressed light falloff. The scene has two lights in the same location, but with different radius, different color temperatures and different max bounces. 

The technique isn't "photographical realistic" realistic but is commonly deployed by 2d artists. 

https://www.youtube.com/watch?v=UnxLy71xuPk

# Setup (srgb)

- First lamp
	- 1000 kelvin
	- Strength 2
	- Angle 6deg (Soft edge)
	- Max Bounces 1 

![First lamp](/img/stacked_lights/low_temp_isolated.png)

This light has a limited bounce to avoid tinting the indirects red. Below is with the default 1024 bounces.
![High bounce on the red lamp will tint the shadow red](/img/stacked_lights/too_high_bounces.png)

- Second lamp
	- 3500 kelvin
	- Strength 8
	- Angle 2deg (Sharper edge)
	- Max Bounces 1024
	
![Second lamp](/img/stacked_lights/high_temp_isolated.png)

# Setup (filmic)

This is with the same parameters as the srgb set up. 
![Filmic render](/img/stacked_lights/no_filmic.png)

You can still achieve the blown out highlight look with filmic transform but not without some tweaking. Filmic compresses highlight and reduces color saturation, increasing the strength of the sun lamp is a necessity. The scene will be overall more illuminated and less saturated. The color falloff is also less pronounced. 

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