========================================
image         css      .article-image
title         css      .article-title
excerpt       css      .article-excerpt
button        css      .article-button
========================================

@ *
--------------------

button 
    centered horizontally inside: parent

@@ if
image
    visible
@@ do

title
    above: image 10 to 20 px
@@ end    

excerpt
    above: title 10 to 20 px

button
    above: excerpt 200px