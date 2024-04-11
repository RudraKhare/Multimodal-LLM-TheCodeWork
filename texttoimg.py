import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "The image has a user interface for mobile applications in which the nike air zoom running shoe is shown as a screenshot.Create a mobile screenshot like image that has all these features",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))
image.show()