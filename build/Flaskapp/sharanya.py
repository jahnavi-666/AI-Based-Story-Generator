import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import cohere
from gtts import gTTS
import os

# Initialize Cohere API
API_KEY = "9F511xzR9nAv5pBOn4OBtZzmsup8QgJLZlS8e8LA"  # Replace with your Cohere API key
co = cohere.Client(API_KEY)

# Function to generate a caption for an image
def generate_caption(image):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

# Function to generate a story using Cohere
def generate_story(prompt, max_tokens=300, temperature=0.7):
    try:
        response = co.generate(
            model='command-xlarge',
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            k=0,
            p=0.75,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

# Custom CSS for styling the app
st.markdown("""
    <style>
        body {
            background-color: #FFFAE5;
            color: #1F1F1F;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .stButton>button {
            background-color: #FF5733;
            color: white;
            font-size: 16px;
            padding: 15px 25px;
            border-radius: 10px;
        }
        .stSlider>div {
            background-color: #FFD700;
        }
        .stTextInput>div>input {
            background-color: #FFEB3B;
        }
        .stSelectbox>div>div>input {
            background-color: #FFEB3B;
        }
        .stImage {
            padding: 10px;  /* Adds space inside the image for better visual separation */
            margin-bottom: 20px; /* Adds space below the image */
        }
        h1 {
            text-align: center;
            color: #FF5733;
            font-size: 3em;
        }
        h2 {
            color: #FF5733;
        }
        .stAudio {
            margin-top: 20px;
            background-color: #FFD700;
            padding: 10px;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app UI
st.title("✨ Image-to-Story Generator ✨")
st.write("Upload a sequence of images to generate a fun, creative story based on the captions! 🌟")

# Initialize session state for audio
if "audio_ready" not in st.session_state:
    st.session_state.audio_ready = False

# File uploader for multiple images
uploaded_files = st.file_uploader("Choose some images to create your story...", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Age range selection with colorful options
age_range = st.selectbox(
    "👶 Select the target age range for the story:",
    ["6-8 years", "8-10 years", "10-12 years", "12+ years"],
    help="Choose the age range for which the story will be customized."
)

# Map age range to specific prompt adjustments
age_prompts = {
    "6-8 years": "Write a very simple and short story for kids aged 6 to 8 with easy words and basic grammar. Story prompt: ",
    "8-10 years": "Write a story with some adventurous elements and moderately complex words for kids aged 8 to 10. Story prompt: ",
    "10-12 years": "Write an engaging and detailed story with advanced grammar for kids aged 10 to 12. Story prompt: ",
    "12+ years": "Write a compelling and imaginative story for teenagers and above. Story prompt: "
}

if uploaded_files:
    captions = []
    st.subheader("🖼️ Uploaded Images and Captions")
    
    # Process each uploaded image
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)  # Adjusts to fit within container width
        caption = generate_caption(image)
        captions.append(caption)
        st.write(f"📝 Caption: {caption}")

    combined_prompt = "Here is a story based on these events: " + " ".join(captions)
    st.write(f"📜 Combined Prompt: {combined_prompt}")

    # Combine the age-based prompt adjustment with the story prompt
    adjusted_prompt = age_prompts[age_range] + combined_prompt

    # Adjust max_tokens and temperature sliders with color
    max_tokens = st.slider("📝 Story Length (max tokens):", min_value=50, max_value=500, value=300, step=50)
    temperature = st.slider("🎨 Creativity Level (temperature):", min_value=0.0, max_value=1.0, value=0.7, step=0.1)

    # Generate story section
    if st.button("Generate Story ✨"):
        with st.spinner("Generating your magical story... 🌟"):
            try:
                # Generate story
                story = generate_story(adjusted_prompt, max_tokens=max_tokens, temperature=temperature)
                st.subheader("🎉 Your Generated Story:")
                st.write(story)

                # Convert text to speech and save
                tts = gTTS(story, lang='en')
                tts.save("story_audio.mp3")
                st.session_state.audio_ready = True  # Update session state
                st.success("Story audio is ready to play! 🎧")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Check if audio is ready in session state
if st.session_state.audio_ready:
    st.audio("story_audio.mp3", format="audio/mp3", start_time=0)
