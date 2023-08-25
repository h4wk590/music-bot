## Happybot

### A Discord Music Bot - Play Music in Your own Discord Server


#### This bot can play music on a discord voice channel using commands.


## Requirements

- Python 3
- ffmpeg installed locally if not using Docker
- pip


## Running Locally

- Clone/Download repository
- In the project directory run:

```pip install -r requirements.txt```


## Running on Docker

- Clone/Download repository
- In the project directory 

### Build Image

```docker build -t <image-name> .```

The image will build from Dockerfile, takes a little bit.

Now run the container from image:

```docker run -d --name <container-name> <image-name>```


