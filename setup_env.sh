#!/bin/bash

if [[ ! `which conda` ]]; then
    echo "Installing latest Miniconda (Python 2.7, Linux x86_64) ..."
    wget -O /tmp/Miniconda.sh https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
    bash /tmp/Miniconda.sh -b -p $HOME/miniconda
    export PATH="$HOME/miniconda/bin:$PATH"
    conda update conda
    #conda config --set always_yes yes
fi #post: conda installed

CONDA_ENV="euler"

if [[ ! `conda env list | grep $CONDA_ENV` ]]; then
    echo "Activating conda environment $CONDA_ENV"
    conda env create # environment.yml
fi #post: euler environment exists

source activate $CONDA_ENV
