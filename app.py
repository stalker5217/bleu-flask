from flask import Flask, request

import json
import logging

import nltk.translate.bleu_score as bleu

app = Flask(__name__)

@app.route("/score", methods=['GET'])
def score():
	candidate = request.args["candidate"]
	references = request.args.getlist("references")

	# NLTK 패키지 구현되어져 있는 코드로 계산한 BLEU 점수
	score = bleu.sentence_bleu(list(map(lambda ref: ref.split(), references)), candidate.split())
	ret = {}
	ret['score'] = score

	return json.dumps(ret)

if __name__ == "__main__":
	logging.getLogger().setLevel(logging.INFO)
	app.run(host="0.0.0.0")