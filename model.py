import sys
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image
from monsterapi import client

sys.path.append(r'C:\Users\rudra\Desktop\ITI\predict_caption.py') # Add the directory containing the first script to the system path
import predict_caption as fs # Import the content of the first script as a separate module

# Initialize the client with your API key
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjM4MTM0YWE3YzcyNzhmMGZlZTU4YjMxNDlhMjc3M2IyIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDQtMTBUMTc6NTQ6MzEuOTE1NjQyIn0.anl_7S6cdKuDQhDc93jdoRpcPIO8irbavGMzA4UXK8k'
monster_client = client(api_key)

model = 'txt2img'  # Replace with the desired model name

# Load the models and tokenizers
fs_model = fs.VisionEncoderDecoderModel.from_pretrained('vit-gpt2-image-captioning')
fs_feature_extractor = fs.ViTImageProcessor.from_pretrained(
    'vit-gpt2-image-captioning')
fs_tokenizer = fs.AutoTokenizer.from_pretrained('vit-gpt2-image-captioning')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
fs_model.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {'max_length': max_length, 'num_beams': num_beams}

def predict_step(image):
    pixel_values = fs_feature_extractor(
        images=[image], return_tensors='pt').pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = fs_model.generate(pixel_values, **gen_kwargs)

    preds = fs_tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds[0]

# Read the image
image = Image.open(r'C:\Users\rudra\Desktop\ITI\image (1).jpg')

# Generate the description
description = predict_step(image)

# Prepare the input data for image generation
input_data = {
    'prompt': description,
    'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn face',
    'samples': 2,
    'steps': 50,
    'aspect_ratio': 'square',
    'guidance_scale': 7.5,
    'seed': 2414,
}

# Call the image generation endpoint
result = monster_client.generate(model, input_data)

# Print the output
print(result['output'])