# Synonym Service  
## Using Python, Flask and nltk
Quick and dirty attempt at a synonym service (or thesaurus service)  
  
*And I am serious,this is quick and dirty. It violates a variety of best practices and I bet this readme would be rejected in a pull request by being associated with this code. Happy Hacking!*
  
# Usage
  
To run just the python script,
`python synapp.py -p 8000`  
To run in Docker `./local.sh`  
  
To retrieve a synonym, `curl http://localhost/8000/{your_word}`  
for example  
`$ curl http://localhost:8000/hack`  
`hacker taxi cut taxicab ward-heeler jade hack political_hack machine_politician chop hack_writer literary_hack drudge cut_up cab whoop plug hack_on nag` 


# Local setup commands  

`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`   
`python get-pip.py`  
`pip install --upgrade pip`  
`pip freeze > requirements.txt`  
`pip install requirements.txt`  
