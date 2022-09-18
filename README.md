# Deploy models with Cog

Cog containers are Docker containers that serve an HTTP server for running predictions on your model. You can deploy them anywhere that Docker containers run.

This guide assumes you have a model packaged with Cog. If you don't, [follow getting started guide](https://github.com/replicate/cog).

## Getting started

First, build your model:

    cog build -t my-model

Then, start the Docker container:

    docker run -d -p 5000:5000 my-model

To run a prediction on the model, call the `/predictions` endpoint, passing input in the format expected by your model:

    curl http://localhost:5000/predictions -X POST \
        --data '{"input": {"image": "https://.../input.jpg"}}'
