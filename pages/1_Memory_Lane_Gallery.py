import streamlit as st

# Title of the app
st.title("Memory Lane Gallery 💖")

# Custom CSS for aesthetics and responsiveness
st.markdown("""
    <style>
        /* Background color for the whole app */
        .main {
            background-color: #feffe9;
        }

        /* Streamlit title color */
        .stTitle {
            color: #a8d480;
        }

        /* Custom button styling */
        .stButton button {
            background-color: #b4dc87;
            color: #ffffff;
            border: none;
            padding: 0.5rem 1rem;
            font-size: 1.2rem;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }

        /* Button hover effect */
        .stButton button:hover {
            background-color: #a8d480;
            color: #ffffff;
        }

        /* Padding for mobile responsiveness */
        @media (max-width: 600px) {
            .block-container {
                padding-left: 0.5rem;
                padding-right: 0.5rem;
            }
            .stButton button {
                width: 100%;
            }
        }

        /* Image caption styling */
        .stImage > img {
            border-radius: 10px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }

        .stMarkdown {
            font-family: 'Georgia', serif;
            color: #a8d480;
        }
    </style>
    """, unsafe_allow_html=True)

# List of images (you'll need to replace these with actual file paths or URLs)
image_paths = [
    "images/l.jpg",
    "images/lv.jpg",
    "images/v.jpg"
]

# List of captions/descriptions for each image
captions = [
    "Our first date at the beach 🌊",
    "Our trip to the mountains ⛰️",
    "The day we moved into our new home 🏡"
]

# Create a session state to keep track of the current image index
if 'current_image' not in st.session_state:
    st.session_state.current_image = 0

# Function to go to the next image
def next_image():
    st.session_state.current_image = (st.session_state.current_image + 1) % len(image_paths)

# Function to go to the previous image
def prev_image():
    st.session_state.current_image = (st.session_state.current_image - 1) % len(image_paths)

# Display the current image and its caption
st.image(image_paths[st.session_state.current_image], caption=captions[st.session_state.current_image], use_column_width=True)

# Create navigation buttons with responsive columns
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous"):
        prev_image()

with col3:
    if st.button("Next ➡️"):
        next_image()

# A final message for anniversary wishes or notes
st.markdown("### Happy Anniversary! 💖 Here's to many more memories together!")
