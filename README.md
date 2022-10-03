# Akibox Tutorial

This is a tutorial project to help you get to know Akita.  It contains a
FastAPI server implementing a toy Dropbox-like file server.  You can use Akita
to generate a spec for its API and track API performance.

The Akita Client works by capturing traffic to your service -- Akibox, in this case.
This tutorial showcases a few different ways to run Akibox and the Akita
Client.

Before you get started, you'll need to create a new project in the Akita app.
Follow [these
instructions](https://docs.akita.software/docs/part-1-create-a-project).  Name
your project `akibox`.

## Run Akibox on the Host

Follow these instructions to run Akibox directly on your host and to capture
host traffic with the Akita Client.

### Create a python virtual environment and install dependencies

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Start the Akibox service

```bash
uvicorn main:app --reload
```

### Start the Akita Client

If you haven't already, [install the Akita
Client](https://docs.akita.software/docs/run-locally#install-the-client).

Next, open another terminal window and start the client.

```bash
akita apidump --service akibox --filter "port 8000"
```

### Make some requests!

Use the `test.sh` script to make some requests against your service.

```bash
./test.sh
```

## Run Akibox with Docker

Optionally, you can build Akibox into a Docker container.  In this case, there are two ways to run the Akita Client:
1. In a separate Docker container attached to the Akibox container's network.
1. In the same Docker container, as a wrapper that invokes Akibox.

### Build Akibox in a Separate Docker Container

```bash
docker build -t akibox-tutorial .
```

#### Run Akibox

```bash
docker run -e PORT=8000 -p 8000:8000 --name akibox-tutorial akibox-tutorial
```

#### Start the Akita Client

Open another terminal window and start the client in a Docker container.

```bash
docker run --rm --network container:akibox-tutorial \
  -e AKITA_API_KEY_ID=your-api-key \
  -e AKITA_API_KEY_SECRET=your-secret \
  akitasoftware/cli:latest apidump --service akibox --filter "port 8000"
```

### Build Akibox and the Akita Client in the Same Container

The `Dockerfile.withcli` Docker file shows how to wrap a service with the Akita
Client.

```bash
docker build -t akibox-tutorial -f Dockerfile.withcli .
```

#### Run Akibox and the Akita Client

```bash
docker run -e PORT=8000 -p 8000:8000 -name akibox-tutorial akibox-tutorial
```

### Make some requests!

Once you've started Akibox and the Akita Client, use the `test.sh` script to
make some requests against your service.

```bash
./test.sh
```

## Run Akibox with Docker Compose

You can also use Docker Compose to start Akibox. In this case, the Docker Compose file can also start the Akita Client
in separate container attached to the same Docker network.

```bash
docker-compose up
```

### Make some requests!

Use the `test.sh` script to make some requests against your service.

```bash
./test.sh
```

## Integration Tests

Integration tests are defined in `test_main.py`.  To run them:

```bash
pytest
```
