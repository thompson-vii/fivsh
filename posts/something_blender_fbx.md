---
title: Blender just can't handle FBX animation 
description: 
date: 
tags:
	- Animation
layout: layouts/post.njk
---

FBX is pretty much the industry standard for file exchange. Game engines use them, asset packs use them, DCC uses them. FBX is an all in one file format that can carry mesh, texture, rig, animation data and bunch others. 

Autodesk provides an sdk for reading and writing FBX, but due to the way blender is licensed, the foundation cannot incorporate sdk code into blender. Autodesk doesn't publish the file format specification either so no there was no alternative implementation. Blender didn't have FBX import support [until 2013](https://www.blender.org/download/releases/2-69/). [They reverse engineered the file format](https://code.blender.org/2013/08/fbx-binary-file-format-specification/)

It was a formidable accomplishment, but it was not perfect, the amount of notes in [documentation](https://docs.blender.org/manual/en/latest/addons/import_export/scene_fbx.html) would hint at that. 

I have used blender for authoring FBX files. The mesh and texture works fine without much issues provided you adherent to the most basic PBR workflow. The animation exports are... not good. 

Recently a friendly of mine was exploring blender to unreal workflow. He was trying to modify one of the FBX viewport model from unreal first person shooter demo, to add a sword swing animation in blender. He exported the animation back to unreal just to find a a messed up arm. I tried to do the same but without modifying the FBX whatsoever to see what would happen. 

The blender export failed the unreal import. "mesh contains root bone as root but animation doesn't contain the root track". I don't really understand what this means exactly but I do have a planB.

{% image "/img/something_blender_fbx/unreal_mismatched_bone.png" %}

BetterFBX is a paid addon that uses FBX sdk and supports several version of FBX files. I had use it a couple time and it is suppose to work better. 

And it did exported a FBX that imported into unreal but again, the mesh is messed up. 

Compare the outliner of the imported s the reason becomes obvious.

{% image "/img/something_blender_fbx/bone_outliner.png" %}
{% image "/img/something_blender_fbx/blender_fbx_bad.png" %}

This isn't new, [bug report1](https://developer.blender.org/T60111) and [bug report2](https://developer.blender.org/T63807) from 2019 still remain unfixed today. 

The fire animation does not have any mesh in it, there is a rig and associated associated animating. 

I imported the fbx 4 times with different settings: native fbx import, native fbx import auto bone orientation, betterfbx import, betterfbx import auto bone orientation.


{% image "/img/something_blender_fbx/rig_bone_anno.png" %}

I then tried import them into unreal, targeting the original SK_Mannequin_Arms. The built-in fails import with the same error message as before, due to incorrect bone hierarchy. The betterfex works but only one of the import has correct animation, or rather, the orientation of the bone, while being correct in blender, diverges from the original skeleton. 

{% sidebyside %}
{% image "/img/something_blender_fbx/betterfbx_anim.png" %}
{% image "/img/something_blender_fbx/betterfbx_anim_auto_bone.png" %}
{% endsidebyside %}

but I can't really modify the animation with this rig. 

{% image "/img/something_blender_fbx/how_tf_do_i_anim_this_shit.png" %}

Editing maya fbx in blender is just asking for trouble. [Blender to Unreal just has a lot of caveats](https://unrealcommunity.wiki/blender-fbx-pipeline-qw16qyxh).

Guess I will be reaching for my maya LT copy. 

Here is a list of currently known [fbx bugs in blender](https://developer.blender.org/T68575), not much is happening though.