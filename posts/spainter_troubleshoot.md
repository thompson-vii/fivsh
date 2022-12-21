---
title: Troubleshooting Substance Painter Mesh Problems
description: 
date: 2022-12-21
tags:
	- Pipeline
    - Substance Painter
layout: layouts/post.njk
---

## Ngons are bad

Ngons are problematic due to the way different DCCs triangulates them. 

{% image "/img/spainter_troubleshoot/spt_ngon.png" %}

{% image "/img/spainter_troubleshoot/spt_world_normal.png" %}

Solution: Triangulate any ngons before exporting to substance painter.

## UV coordinate overflow

By default, unwrapped uv islands will fill up the entire uv space in blender, however Substance Painter does not support free floating uv islands outside the avaliable uv tiles so they are wrapped around. 

{% sidebyside %}
{% image "/img/spainter_troubleshoot/spt_blender_uv.png" %}
{% image "/img/spainter_troubleshoot/spt_substance_uv.png" %}
{% endsidebyside %}

{% image "/img/spainter_troubleshoot/spt_substance_uv2.png" %}

Solution: Scale the uv islands so the edge doesn't touch the border.



