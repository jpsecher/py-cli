#!/bin/bash -e

scriptdir=$(realpath `dirname $0`)
workdir=${WORKSPACE:-$(realpath $scriptdir/..)}
pushd "$workdir" > /dev/null

source "venv/bin/activate"
mypy src/ $@

popd > /dev/null
