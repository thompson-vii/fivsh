Description
-----------

Content falls under `/portfolio` and `/posts`

image_preproc.py
 - used to generate image metadata as photoswipe needs img dimension to work. The generated json is placed under `/_data` and named same as the md template. 

beside the extension the two files need to have the same filename. The variable inside the json is then made available to the md template for use.

thumbnail_gen.py
 - take all image under /img and generate a smaller thumbnail of the same names and place them under /img200

Add new post
------------

- Write the post text first. 
- Put image under the associated directory under `/img`
- generate 200 wide thumbnail with imagemagick and place them under `/img200`
	- alternatively delete img200, duplicate img and rename the copy to img200, mogrify the whole image `find . -name '*.jpg' | parallel -j8 mogrify -resize x200` 
- add another line in image_preproc `PROC_DIC`
- add nunjuck template

Code Snippet
------------

Photoswipe 
 
	```{% gallery %}
{% for img in THE_NAME_OF_THE_POST %}
<a href="{{img.fullres_path}}" data-pswp-width={{img.width}} data-pswp-height={{img.height}} target="_blank"><img src="{{img.thumbnail_path}}" alt="{{img.alt}}" loading="lazy"></a>
{% endfor %}
{% endgallery %}```

