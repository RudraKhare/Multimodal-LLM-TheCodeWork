# Multimodal-LLM-TheCodeWork
Assignment Completion: Image-to-Text and Text-to-Image Conversion
Overview
This repository contains the code and documentation for completing an assessment assignment on image-to-text and text-to-image conversion. The assignment challenged the use of Language and Vision models (LLMs) to convert images into textual descriptions and vice versa.

Approach
The assignment was approached in two stages:

Initial Attempt: Utilizing an image-to-image LLM model, which, despite efforts, did not yield satisfactory results.
Alternative Approach: Employing two LLMs in sequence:
Image-to-Text LLM: Converting images into descriptive text.
Text-to-Image LLM: Generating images based on the provided textual descriptions.
Models Used
Google Colab Model:
Utilized a pipeline for image-to-text conversion, incorporating the dreamlike-art/dreamlike-diffusion-1.0 model.
Local Models:
Model 1:
Files: predict_caption.py, predict_images.py, model.py
Utilized the vit-gpt2-image-captioning model for image-to-text conversion and the txt2img model from the Monster API for text-to-image conversion.
Model 2:
Files: imgtotext.py, texttoimg.py
Employed the Salesforce/blip-image-captioning-large model for image-to-text conversion and the runwayml/stable-diffusion-v1-5 model for text-to-image conversion.
Results
The second approach proved more effective, providing improved accuracy and precision in the output.

Learning
This assignment provided valuable learning experiences and challenges, contributing to personal and professional growth in the field of language and vision modeling.
