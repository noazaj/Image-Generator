# Image-Generator

The image generator is a REST API generating a random image of a pokemon. It pulls from a directory holding all of the pokemon images. The image will be generated upon request from the URL.

## Usage
To acquire an image of a pokemon, you will need to send a ```GET``` request to the following URL: ```https://microservice-image-generator-bd1f70093a8a.herokuapp.com/random-character```. An image of a pokemon should be presented in the middle of the screen. 

## Tech Utilized
This microservice was created with *python* while utilizing the *flask* WGSI. However, the service is deployed through *Heroku* to be accessible on the web.