from flask import Flask, send_from_directory, abort
import random
import os

app = Flask(__name__)

# The paths for the images
IMAGES_DIR = 'imagesAll'

@app.route('/random_character', methods=['GET'])
def random_character():
    try:
        image_name = random.choice(os.listdir(IMAGES_DIR))
        image_path = os.path.join(IMAGES_DIR, image_name)
        return send_from_directory(IMAGES_DIR, image_name)
    except Exception as err:
        return abort(404)
if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)