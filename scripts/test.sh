#!/bin/bash -e

scriptdir=$(realpath `dirname $0`)
workdir=${WORKSPACE:-$(realpath $scriptdir/..)}
pushd "$workdir" > /dev/null

source "venv/bin/activate"
pytest --cov --cov-report=xml:test-reports/coverage.xml --junitxml test-reports/junit.xml $@

popd > /dev/null
