---
title: Things Substance Painter's Normal Map Format Actually Does
description: 
date: 2022-06-01
tags:
	- Substance Painter
    - Pipeline
layout: layouts/post.njk
---

{% image "/img/painter_project_setting/painter_project_setting.png" %}

I was a bit confused as what exactly happens when changing the normal map format under project setting do.


I can change them live but the viewport shading stay the same. After a big of digging I figured it out, the answer is actually quite simple.


On the export template there are the `Input maps - Normal` and two converted maps one of `DirectX` the other `OpenGL`.


The Normal follows whatever setting the project setting is under. The Converted map, as expected, are not affected.

{% image "/img/painter_project_setting/painter_export_template.png" %}
{% image "/img/painter_project_setting/painter_project_setting_map_compare.png" %}