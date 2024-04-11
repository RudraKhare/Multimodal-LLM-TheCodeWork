import sys

from monsterapi import client
              
# Initialize the client with your API key
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjM4MTM0YWE3YzcyNzhmMGZlZTU4YjMxNDlhMjc3M2IyIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDQtMTBUMTc6NTQ6MzEuOTE1NjQyIn0.anl_7S6cdKuDQhDc93jdoRpcPIO8irbavGMzA4UXK8k'  # Replace 'your-api-key' with your actual Monster API key
monster_client = client(api_key)



model = 'txt2img'  # Replace with the desired model name
input_data = {
'prompt': text,
'negprompt': 'deformed, bad anatomy, disfigured, poorly drawn face',
'samples': 2,
'steps': 50,
'aspect_ratio': 'square',
'guidance_scale': 7.5,
'seed': 2414,
            }


result = monster_client.generate(model, input_data)

print(result['output'])