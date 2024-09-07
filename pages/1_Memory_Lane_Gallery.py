import streamlit as st

# List of image paths
image_paths = [
    "images/l.jpg",
    "images/lv.jpg",
    "images/v.jpg"
]

# List of captions
captions = [
    "Our first date at the beach 🌊",
    "Our trip to the mountains ⛰️",
    "The day we moved into our new home 🏡"
]

# Display images in a gallery using columns
cols = st.columns(3)

for idx, col in enumerate(cols):
    col.image(image_paths[idx], caption=captions[idx], use_column_width=True)
