Description
-----------

Content falls under `/portfolio` and `/posts`

Add portfolio file
------------------

- place file under `/img/portfolio/`
- run `image_preproc.py`
  - used to generate image metadata as photoswipe needs img dimension to work. The generated json is placed under `/_data` and named same as the md template. 

beside the extension the two files need to have the same filename. The variable inside the json is then made available to the md template for use.

Add new post
------------
- Add .md files to `/posts`

Add new Image
-------------
Place image under `/img`

use nunjuck tag `{% img400 "./path/to/image/", "annotation %}` path relative to `_site`

thumbnail will be automatically generated on build. 


Code Snippet
------------

Photoswipe 
 
	```{% gallery %}
{% for img in THE_NAME_OF_THE_POST %}
<a href="{{img.fullres_path}}" data-pswp-width={{img.width}} data-pswp-height={{img.height}} target="_blank"><img src="{{img.thumbnail_path}}" alt="{{img.alt}}" loading="lazy"></a>
{% endfor %}
{% endgallery %}```

