This extension defines a directive 'sagecell' which allows to embedd sage cell inside sphinx doc. To learn more about sage cell server visit: http://aleph.sagemath.org/static/about.html


Installation
=========
   1. Install this extension: 
        'python(3) setup.py build'
        'sudo python(3) setup.py install'
   2. Move 'layout.html' to your '_templates' directory. Change sagecell paths if necessary.
   3. Add 'sagecell.sagecell' to your extensions in 'conf.py'


How to use it
===========

Example of usage::

	.. sagecell::

        L = [factor(n) for n in range(1, 20)]
        L[4:9]

Options
======
The r option is used if the code is to be interpreted as R code, otherwise the code is interpreted as Sage.

Example:

.. sagecell::
    :r: 

    a <- 3
    a+5

The codefile option is used to read the code from a file instead of writing it directly in the sphinx rst file.

Example:

.. sagecell::
    :codefile: example.sage

During latex generation, the code is displayed verbatim if the showcode option is chosen. If the img option is set to an image file the image will be displayed (beneath the code if the showcode option is also chosen). The width of the image is set with the imgwidth option, if no width is set the default width is 8cm.

.. sagecell::
    :codefile: example.sage
    :img: example.jpg
    :imgwidth: 4cm

.. sagecell::
    :r: 
    :showcode:  
    :img: ex.png 

    a <- 3
    a+5

.. sagecell::
    :showcode:

    2+3


