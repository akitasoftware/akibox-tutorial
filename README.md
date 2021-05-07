# Akibox Tutorial

This is a tutorial project to help you get to know Akita.  It contains a
FastAPI server implementing a toy Dropbox-like file server.  You can use Akita
to generate a spec for its API, make some changes, and see how API-impacting
changes show up in Akita's semantic diffs.

To try out the tutorial, head over
[here](https://docs.akita.software/docs/get-to-know-akita).

## Quickstart

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

### Make some requests!

Use the `test.sh` script to make some requests against your service.

```bash
./test.sh
```

## Building Docker Container

Optionally, you can build Akibox into a Docker container.

```
docker build -t akibox-tutorial .
```

## Integration Tests

Integration tests are defined in `test_main.py`.  To run them:

```bash
pytest
```
