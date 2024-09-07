import streamlit as st
import streamlit.components.v1 as components

# List of image paths
image_paths = [
    "images/l.jpg",  # Replace with actual image URLs
    "images/lv.jpg",
    "images/v.jpg"
]

# HTML for a simple carousel using Slick
carousel_html = """
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css"/>
<div class="slider">
    <div><img src='{}' style="width:100%'></div>
    <div><img src='{}' style="width:100%'></div>
    <div><img src='{}' style="width:100%'></div>
</div>
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js"></script>
<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>
<script type="text/javascript">
    $(document).ready(function(){
        $('.slider').slick({
            dots: true,
            infinite: true,
            speed: 300,
            slidesToShow: 1,
            adaptiveHeight: true
        });
    });
</script>
""".format(image_paths[0], image_paths[1], image_paths[2])

# Embed the carousel
components.html(carousel_html, height=500)
