Quick and dirty attempt at a synonym service (or thesaurus service)

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py  
python get-pip.py  
pip install --upgrade pip  
pip freeze > requirements.txt  
pip install requirements.txt


