#!/bin/sh

docker build -t branning/euler .
docker run -t -v `pwd`:/euler branning/euler python test.py

