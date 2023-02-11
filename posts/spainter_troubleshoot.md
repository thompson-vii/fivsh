---
title: Troubleshooting Substance Painter Problems
description: 
date: 2022-12-21
tags:
	- Pipeline
    - Substance Painter
layout: layouts/post.njk
---

## Ngons bad

Ngons are problematic due to the way different DCCs triangulates them. It doesn't always cause problems, but in this case it appears that substance painter decided to not give a fuck. 

{% image400 "./img/spainter_troubleshoot/spt_ngon.png", "The ngon on the right has edges connected to a single vertex" %}

{% image400 "./img/spainter_troubleshoot/spt_world_normal.png", "Ngon with world space bake" %}

Solution: Triangulate any ngons before exporting to substance painter.

## UV coordinate overflow

By default, unwrapped uv islands will fill up the entire uv space in blender. UV islands with vertex touching the UV border wraps around to the other side. Seems to be a bug. 

{% sidebyside %}
{% image400 "./img/spainter_troubleshoot/spt_blender_uv.png", "UV map viewed inside blender" %}
{% image400 "./img/spainter_troubleshoot/spt_substance_uv.png", "UV map viewed inside Substance Painter. Notice the center island stretching across the entire tile" %}
{% endsidebyside %}

{% image400 "./img/spainter_troubleshoot/spt_substance_uv2.png", "UV map viewed inside Substance Painter. Notice the slim uv island going from top to bottom" %}

Solution: Scale the uv islands so the edge doesn't touch the border.

## World Space Normal Bakes Checker Pattern

Specifically for stacked UV islands.

{% image400 "./img/spainter_troubleshoot/spt_checker.png", ""%}

Solution: Reason of why this is happening is not exactly known. Stacking outward facing faces together solves it. 



