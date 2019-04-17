#!/usr/bin/env bash

to_absolute() {
  case $1 in
    /*) absolute=$1;;
    *) absolute=$PWD/$1;;
  esac
  echo ${absolute}
}

function normalize_path()
{
    # Remove all /./ sequences.
    local   path=${1//\/.\//\/}

    # Remove dir/.. sequences.
    while [[ ${path} =~ ([^/][^/]*/\.\./) ]]
    do
        path=${path/${BASH_REMATCH[0]}/}
    done
    echo ${path}
}

task=$1
local=$(normalize_path $(to_absolute $2))
bucket=$3
remote=$4
creds=$(normalize_path $(to_absolute $5))
image=$6

docker run --mount type=bind,source="$creds",target="/creds/creds.json" \
--mount type=bind,source="${local}",target="${local}" -it ${image} ${task} \
${local} ${bucket} ${remote} /creds/creds.json
