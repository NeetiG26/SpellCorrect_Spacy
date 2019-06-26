from flask import Flask, request, render_template
from spacy_spellcheck import *

app = Flask(__name__)

@app.route('/spellCorrect')
def get_page():
	return render_template('page.html')

@app.route('/spellCorrect', methods=['POST'])
def spellCorrect():
	word = request.form['word']
	word = word.lower()
	tokens = spacy_tokenize(word)
	corrected_text = get_spell_corrector(tokens)
	return render_template('page.html', original_text = word, correct_text=corrected_text )

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port=8080)