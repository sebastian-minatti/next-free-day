## Quick Start

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html):

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    conda clean --all

Set up Conda env:

    conda env create -f environment.yml
    conda activate free-day

Set up app package:

    pip install -e .
    
To run a development server with Flask WSGI:

    FLASK_ENV=development FLASK_APP=next_free_day.main flask run --port 5001 --host 0.0.0.0
