# Object Store Directory Dowloader

Simple object downloader written in

## Local

> For local setup

### Setup

If you're running Linux, all you need is `Python 3.6` and run

> `pip install -r requirements.txt`.

There's an issue with `cos_aspera` on Mac so please use docker if you're on a Mac.

### Run

Run the following to start running folder:

> `python download_object_store_directory.py <local_directory> <bucket_name> <remote_directory> <credentials>`

#### Example

> `python download_object_store_directory.py detections diva-phase-2 dets/ibm creds.json`

- `detections` will be a folder in the same directory you're running from.
- `diva-phase-2` is the bucket name
- `dets/ibm` is the prefix folders on the object store
- `creds.json` is a provided credentials file.

## Docker

> Running in a docker container

### Setup

First build the docker image:

> `docker build -t downloader .`

### Run

Run the following to start downloading the files:

> `./download_directory.sh <local_directory> <bucket_name> <remote_directory> <credentials>`

- These will be the same arguments passed directly to the script.
