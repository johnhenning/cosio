# COSIO - Simple IBM Cloud Object Store Interface

Simple IBM cloud object store interface written in Python

## Local

> For local setup

### Setup

If you're running Linux, all you need is `Python 3.6` and run

> `pip install -r requirements.txt`.

There's an issue with `cos_aspera` on Mac so please use docker if you're on a Mac.

### Run

Run the following to start downloading the file(s):

> `python main.py download <local_directory> <bucket_name> <remote_directory_or_file> <credentials>`

Run the following to start uploading file(s):

> `python main.py download <local_directory_or_file> <bucket_name> <remote_directory> <credentials>`

#### Examples

This is an example

> `python main.py download detections diva-phase-2 dets/ibm creds.json`
- `download` is the task given to start downloading a folder
- `detections` will be a folder in the same directory you're running from. This can be any folder path though.
- `diva-phase-2` is the bucket name
- `dets/ibm` is the folder or file to download from the object store
- `creds.json` is a provided credentials file.

## Docker

> Running in a docker container

### Setup

First build the docker image:

> `docker build -t <image_name> .`

### Run

Run the following to start downloading/uploading the file(s):

> `./run.sh <task> <local_directory_or_file> <bucket_name> <remote_directory_or_file> <credentials> <image_name>`

- These will be the same arguments that were passed directly to the script in the local setup instructions.
- `<task>` will be upload or download depending on what you're trying to do.
- `<image_name>` is the same image name you gave to your built docker container
