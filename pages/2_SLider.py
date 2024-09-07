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

# Create a slider to select the image index
image_index = st.slider("Slide to select an image", 0, len(image_paths) - 1, 0)

# Display the selected image
st.image(image_paths[image_index], caption=captions[image_index], use_column_width=True)
