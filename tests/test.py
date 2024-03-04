import requests
from PIL import Image
from io import BytesIO

# Microservice URL
url = 'https://microservice-image-generator-bd1f70093a8a.herokuapp.com/random-image'

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Open the image from the response content
    image = Image.open(BytesIO(response.content))
    # Display the image
    image.show()
else:
    print(f"Error: {response.status_code}, Description: {response.text}")
