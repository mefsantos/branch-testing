# branch-testing
Testing branches, merges, different files within branches, etc
Testing python package deployment, travis CI, coveralls and pytest

## Instalation Instructions

To install the package you are required to have pip in order to install all the 
pacakge dependencies (later the pacake itself)
Furthermore you are assumed to have python installed. Reffer to [https://www.python.org/downloads/] otherwise.

### Install Python-pip
Depending on your permissions as user, you may choose one of the following options:

#### Option 1 - Machine Owner
Can and Want to install the software for every possible user:

`sudo apt-get install python-pip`

(adding installation commands for other OSs soon)

#### Option 2 - Limited User
Do not have admin previlegies

You may want to reffer to [https://gist.github.com/saurabhshri/46e4069164b87a708b39d947e4527298]

TL;DR:
1. Open terminal:
2. Download pip: `wget https://bootstrap.pypa.io/get-pip.py`
3. Install into local directory `python get-pip.py --user`
4. Add the instalation path to the $PATH environment: `echo -e '#extending path\nexport PATH=$PATH:~/.local/bin' >> ~/.bashrc`
5. Reload .bashrc file: `source ~/.bashrc`

#### Install package dependencies / requirements
pip install --user -r requirements.txt

#### Install Package
python setup.py install

