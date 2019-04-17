#!/usr/bin/env bash
local=$1
bucket=$2
remote=$3
creds=$4
image=$5
docker run --mount type=bind,source="$creds",target="/creds/creds.json" -v $local:$local -it $image $local $bucket $remote /creds/creds.json
