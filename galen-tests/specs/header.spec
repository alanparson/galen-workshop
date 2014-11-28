=========================================
header             css    .header
header-content     css    .header-content

brand-logo         css    .brand-logo
brand-name         css    .brand-name

nav                css    .main-nav
nav-item-*         css    .main-nav > ul > li

toggle             css    .main-nav-toggle
=========================================


@ *
--------------------
header
    width: 100% of screen/width
    height: 60px

header-content
    centered horizontally inside: header


brand-logo 
    inside: header-content 0px left
    centered vertically inside: header-content


@ desktop
------------------

brand-name 
    near: brand-logo 5 to 20px left
    text is: Galen Framework

toggle
    absent

nav 
    inside: header-content 0px right


@ mobile 
------------------

brand-name
    absent



