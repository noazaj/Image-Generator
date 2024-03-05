from flask import Flask, send_from_directory, abort
import random
import os

app = Flask(__name__)

# The paths for the images
IMAGES_DIR = 'unsplash-images-collection'

@app.route('/random-image', methods=['GET'])
def random_character():
    try:
        image_name = random.choice(os.listdir(IMAGES_DIR))
        response = send_from_directory(IMAGES_DIR, image_name)
        response.headers['Content-Disposition'] = 'attachment; filename="image_name.jpg"'
        return response
    except Exception as err:
        return abort(404, description=str(err))
