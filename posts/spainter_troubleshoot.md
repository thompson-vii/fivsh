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

{% image400 "./img/spainter_troubleshoot/spt_ngon.png", "" %}

{% image400 "./img/spainter_troubleshoot/spt_world_normal.png", "" %}

Solution: Triangulate any ngons before exporting to substance painter.

## UV coordinate overflow

By default, unwrapped uv islands will fill up the entire uv space in blender. UV islands with vertex touching the UV border wraps around to the other side. Seems to be a bug. 

{% sidebyside %}
{% image400 "./img/spainter_troubleshoot/spt_blender_uv.png", "" %}
{% image400 "./img/spainter_troubleshoot/spt_substance_uv.png", "" %}
{% endsidebyside %}

{% image400 "./img/spainter_troubleshoot/spt_substance_uv2.png", "" %}

Solution: Scale the uv islands so the edge doesn't touch the border.

## World Space Normal Bakes Checker Pattern

Specifically for stacked UV islands.

{% image400 "./img/spainter_troubleshoot/spt_checker.png", ""%}

Solution: I don't know wtf is happening, why is it happening but stacking outward facing faces together solves it.



