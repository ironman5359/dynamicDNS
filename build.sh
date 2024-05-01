#!/usr/bin/env bash

GIT_COMMIT=$(git rev-parse --short HEAD)

docker build --build-arg DNS_API_KEY=${DNS_API_KEY} --build-arg DNS_API_SECRET=${DNS_API_SECRET} -t dynamicdns:$GIT_COMMIT .

