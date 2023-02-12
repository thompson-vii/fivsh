---
title: Working with FBX animation in blender is still a pain
description: 
date: 2022-08-03
tags:
    - Unreal Engine
    - Animation
    - Pipeline
layout: layouts/post.njk
---

FBX is the standard format for file exchange. Game engines use them, asset packs use them, DCC uses them. FBX is an all in one file format that can carry mesh, texture, rig, animation data and bunch others. 

Autodesk provides a sdk for reading and writing FBX, but due to license issues, the blender foundation cannot incorporate sdk code into blender itself. Autodesk doesn't publish the file format specification so no one can make a clean room implementation aside from the sdk. Blender didn't have FBX import support [until 2013](https://www.blender.org/download/releases/2-69/). [They reverse engineered the file format](https://code.blender.org/2013/08/fbx-binary-file-format-specification/)

It was a formidable accomplishment, but it was not perfect, the amount of notes in [documentation](https://docs.blender.org/manual/en/latest/addons/import_export/scene_fbx.html) would hint at that. 

I have used blender for authoring models with PBR workflow. The mesh and texture works fine without much issues when exported to FBX, provided you adherent to the standard PBR workflow. The animation exports are... not good. 

# FBX animations

Recently a friendly of mine was exploring blender to unreal workflow. He was trying to modify one of the arm model from Unreal Engine's first person shooter demo, to add a sword swing animation in blender. He exported the animation back to unreal just to find a completely messed up arm. I tried to do the same but without modifying the FBX whatsoever to see what would happen. 

I exprted the FBX with blender and drop it onto Unreal. It fails: "mesh contains root bone as root but animation doesn't contain the root track". I don't really understand what this means exactly but I do have a backup plan.

{% image400 "./img/something_blender_fbx/unreal_mismatched_bone.png", "Error on FBX import in Unreal Engine" %}

BetterFBX is a paid addon that incorporates the FBX sdk and supports several version of the FBX versions. I had use it a couple time and it is suppose to work better. 

The addon did export a FBX artifact that Unreal accepted, but the animation is still messed up.  

Compare the outliner of the imported s the reason becomes obvious.

{% image400 "./img/something_blender_fbx/bone_outliner.png", ""%}
{% image400 "./img/something_blender_fbx/blender_fbx_bad.png", "" %}

This isn't new, [bug report1](https://developer.blender.org/T60111) and [bug report2](https://developer.blender.org/T63807) from 2019 still remain unfixed today. 

The fire animation does not have any mesh in it, there is a rig and associated associated animating. 

I imported the fbx 4 times with different settings: native fbx import, native fbx import auto bone orientation, betterfbx import, betterfbx import auto bone orientation.


{% image400 "./img/something_blender_fbx/rig_bone_anno.png", "" %}

I then tried import them into unreal, targeting the original SK_Mannequin_Arms. The built-in fails import with the same error message as before, due to incorrect bone hierarchy. The betterfex works but only one of the import has correct animation, or rather, the orientation of the bone, while being shown correctly in blender, diverges from the original skeleton. 

{% sidebyside %}
{% image400 "./img/something_blender_fbx/betterfbx_anim.png", "Unmodified rig with animation imported into Unreal Engine" %}
{% image400 "./img/something_blender_fbx/betterfbx_anim_auto_bone.png", "Modified rig with Automatic Bone Orientation checked" %}
{% endsidebyside %}

{% image400 "./img/something_blender_fbx/how_tf_do_i_anim_this_shit.png", "The unmodified rig shown in blender. Animating it is difficult" %}

Editing maya fbx in blender is just asking for trouble. [Blender to Unreal workflow just has a lot of caveats](https://unrealcommunity.wiki/blender-fbx-pipeline-qw16qyxh). Beside blender mangling the rig's hierarchy on import, Unreal Engine has specific convention on how the bones are named. 

I do not know if this is problematic for Unity or other engines.

Here is a list of currently known [fbx bugs in blender](https://developer.blender.org/T68575), the list is long. I do not expect them to be sorted out anytime soon due to the nature of reverse engineering. 