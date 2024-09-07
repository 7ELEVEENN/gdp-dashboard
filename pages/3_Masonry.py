import streamlit as st
import streamlit.components.v1 as components

# List of image paths
image_paths = [
    "images/l.jpg",
    "images/lv.jpg",
    "images/v.jpg"
]

# HTML for Masonry Layout
masonry_html = """
<style>
.masonry {
    column-count: 3;
    column-gap: 1em;
}
.masonry-item {
    margin-bottom: 1em;
}
.masonry-item img {
    width: 100%;
    display: block;
}
</style>
<div class="masonry">
    <div class="masonry-item"><img src='{}'></div>
    <div class="masonry-item"><img src='{}'></div>
    <div class="masonry-item"><img src='{}'></div>
</div>
""".format(image_paths[0], image_paths[1], image_paths[2])

# Embed the masonry layout
components.html(masonry_html, height=500)
