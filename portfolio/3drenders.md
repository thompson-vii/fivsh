---
title: 3D Renders
description: 
date: 2022-05-23
tags:
	- portfolio
layout: layouts/gallery.njk
---

<h1>{{title}}</h1>

{% gallery %}
{%- for img in 3drenders -%}

<a href="{{img.fullres_path}}" data-pswp-width={{img.width}} data-pswp-height={{img.height}} target="_blank"><img src="{{img.thumbnail_path}}" alt="{{img.alt}}" loading="lazy"></a>

{%- endfor -%}
{% endgallery %}
