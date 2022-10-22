# sss site generator (Super Simple Static site generator)

**Note** that this a Work in Progress and the information 
below is just a wishlist of how the project is supposed to
work.

sss site generator generates minimal and simple sites using
templates that are as minimal as possible.

## How to use

Create markdown files in ./site/ and they will be converted
to html with the same folder structure and placed in ./output/.

Any other files (images, stylesheets, etc) need to be placed in ./res
and can be referenced from there. For example `/res/stylesheets/main.css`.

Create a template in the templates folder. Add {CONTENT} somwhere in the
html template this is where the content from markdown files will be placed.
Specify which template to use with markdown meta tags with no enclosing \---
Add {title} in places where you want to add the title of a document.

Files that aren't markdown files will be left alone.
