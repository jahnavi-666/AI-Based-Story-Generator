## AI BASED STORY GENERATOR BY INPUTING IMAGES TO KIDS

Image-to-Story Generator

This repository contains the code for an Image-to-Story Generator web application. The app allows users to upload a sequence of images, generates captions for them using a pre-trained image captioning model, and creates a story based on the captions using the Cohere API. Additionally, the generated story is converted to audio for an immersive experience.

Features

Image Upload: Users can upload multiple images in jpg, jpeg, or png format.

Caption Generation: Captions are generated for each uploaded image using the Salesforce BLIP image captioning model.

Story Generation: A creative story is generated based on the captions using Cohere's text generation API.

Text-to-Speech Conversion: The generated story is converted to an audio file using Google Text-to-Speech (gTTS).

Streamlit UI: A user-friendly web interface built with Streamlit.

Demo

Screenshot or GIF of the application in use

Installation

Clone this repository:

git clone https://github.com/yourusername/image-to-story-generator.git
cd image-to-story-generator

Install the required dependencies:

pip install -r requirements.txt

Replace the placeholder Cohere API key in the code with your own:

API_KEY = "your_cohere_api_key"

Run the Streamlit application:

streamlit run app.py

Usage

Launch the web application by running the command above.

Upload one or more images using the file uploader.

Adjust the story length and creativity level using the provided sliders.

Click the Generate Story button to create a story based on the captions.

If desired, listen to the generated story audio by clicking the play button.

Technologies Used

Python: Backend logic and integration.

Streamlit: Web application framework for building the UI.

Salesforce BLIP: Pre-trained image captioning model.

Cohere API: Text generation API for story creation.

gTTS: Text-to-speech conversion.

Pillow: Image processing library.

Folder Structure

image-to-story-generator/
├── app.py                 # Main application code
├── requirements.txt       # Python dependencies
├── story_audio.mp3        # Generated story audio (temporary file)
└── README.md              # Project documentation

Requirements

Python 3.8 or above

Streamlit 1.0.0 or above

Cohere API key

Dependencies

streamlit

Pillow

transformers

cohere

gTTS

Install all dependencies using the provided requirements.txt file:

pip install -r requirements.txt

License

This project is licensed under the MIT License.

Contributing

Contributions are welcome! Feel free to fork this repository, submit issues, or create pull requests.

Author

Your NameLinkedIn | GitHub

Acknowledgements

Salesforce BLIP

Cohere AI

Streamlit

Google Text-to-Speech
