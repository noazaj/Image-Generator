from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# The paths for the images
IMAGES_DIR = 'imagesAll'

@app.route('/random_character', methods=['GET'])
def random_character():
    selected = random.choice(metadata)
    image_path = os.path.join(IMAGES_DIR, selected['file_name'])
    image_url = f'http://localhost:5000/static/{selected["file_name"]}'
    return jsonify({
        'name': selected['name'],
        'type': selected['type'],
        'image_url': image_url,
    })

if __name__ == '__main__':
    app.run(debug=True)