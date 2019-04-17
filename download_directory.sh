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

local=$(normalize_path $(to_absolute $1))
bucket=$2
remote=$3
creds=$(normalize_path $(to_absolute $4))
image=$5

docker run --mount type=bind,source="$creds",target="/creds/creds.json" -v ${local}:${local} -it ${image} ${local} ${bucket} ${remote} /creds/creds.json
