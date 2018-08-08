from flask import Flask
import sys
import optparse
import time
from itertools import chain
from nltk.corpus import wordnet
import nltk
nltk.download('wordnet')

app = Flask(__name__)

start = int(round(time.time()))

# eeek, I'm an open endpoint!
@app.route("/<text>")
def get_synonym(text):

    synonyms = wordnet.synsets(text)
    lemmas = " ".join(set(chain.from_iterable([word.lemma_names() for word in synonyms]))) # lemma names are the synonyms
    return lemmas

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python synapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
