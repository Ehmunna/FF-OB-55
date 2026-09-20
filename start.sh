#!/bin/bash

echo "Checking Python..."

if command -v python3 &> /dev/null
then
    PY=python3
    PIP=pip3
else
    PY=python
    PIP=pip
fi

echo "Installing requirements..."
$PIP install --upgrade pip
$PIP install -r requirements.txt --no-cache-dir

echo "Starting bot with timed restart..."

while true
do
    timeout 1800 $PY main.py
    echo "Restarting bot after 1 hour..."
    sleep 5
done