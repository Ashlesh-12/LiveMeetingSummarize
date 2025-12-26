# big photo gallery by adding more image URLs and displaying them in a grid layout.

import streamlit as st

st.title("Big Photo Gallery from the Internet")

# List of image URLs (12+ images)
image_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/640px-PNG_transparency_demonstration_1.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Koala_climbing_tree.jpg/640px-Koala_climbing_tree.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/House_sparrow04.jpg/640px-House_sparrow04.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Red_Panda_in_River.jpg/640px-Red_Panda_in_River.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/17/Golden_Retriever_standing_Tucker.jpg/640px-Golden_Retriever_standing_Tucker.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Sunset_in_Florida.jpg/640px-Sunset_in_Florida.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/6/63/Earth_Eastern_Hemisphere.jpg/640px-Earth_Eastern_Hemisphere.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Beach_summer.jpg/640px-Beach_summer.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Tulip_fields_in_Holland.jpg/640px-Tulip_fields_in_Holland.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Mountain_landscape.jpg/640px-Mountain_landscape.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Sunflower_field.jpg/640px-Sunflower_field.jpg",
]

# Number of columns per row
cols_per_row = 4

# Display images in a gallery grid
for i in range(0, len(image_urls), cols_per_row):
    cols = st.columns(cols_per_row)
    for col, img_url in zip(cols, image_urls[i:i + cols_per_row]):
        col.image(img_url, use_container_width=True)



#  Display single image

import streamlit as st

st.title("Display Image from the Internet")

# Display image from URL
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg",
    caption="Image from Internet",
    use_container_width=True
)


# 3 images

import streamlit as st
from PIL import Image

st.title("Display Images in Columns")

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Load your image
img = Image.open(r"C:\Users\nikhi\OneDrive\Pictures\Screenshots 1\sample.png")  # Make sure "sample.jpg" is in the same folder

# Display the image in each column
with col1:
    st.image(img, caption="Image 1", use_container_width=True)

with col2:
    st.image(img, caption="Image 2", use_container_width=True)

with col3:
    st.image(img, caption="Image 3", use_container_width=True) 