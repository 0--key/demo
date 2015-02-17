#!/bin/bash

# Run this script with super user privileges to install

mkdir ./demo && cd demo && virtualenv venv && source venv/bin/activate

# Virtual environment is ready to install additional packages

pip install -U numpy && pip install -U nltk

# install NLTK data
sudo mkdir /usr/share/nltk_data
sudo chmod g+w /usr/share/nltk_data/
sudo chgrp antony /usr/share/nltk_data/
python -m nltk.downloader -d /usr/share/nltk_data all
