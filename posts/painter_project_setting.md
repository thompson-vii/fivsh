---
title: Substance Painter's Normal map format
description: 
date: 2022-06-01
tags:
	- Substance Painter
    - Pipeline
layout: layouts/post.njk
---

{% image400 "./img/painter_project_setting/painter_project_setting.png", "Project Setting dialog" %}

I was a bit confused as what exactly happens when changing the normal map format under project setting do.


I can change them live but the viewport shading stay the same. After a big of digging I figured it out, the answer is actually quite simple.


On the export template there are the `Input maps - Normal` and two converted maps one of `DirectX` the other `OpenGL`.


The Normal follows whatever setting the project setting is under. The Converted map, as expected, are not affected.

{% image400 "./img/painter_project_setting/painter_export_template.png", "Output Template" %}
{% image400 "./img/painter_project_setting/painter_project_setting_map_compare.png", "" %}