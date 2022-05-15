from flask import Flask
from candidates import Candidates

date = 'candidates.json'
app = Flask(__name__)
candidates = Candidates(date)


@app.route("/")                                                     # представление для роута "/"
def page_candidate_pk():
    return f"<pre>" + candidates.oll() + "<pre>"


@app.route("/candidates/<int:pk>")                                  # представление для роута "candidates/<pk>"
def page_choiсe_candidate(pk):
    return f"<pre>" + candidates.choiсe(pk) + "<pre>"


@app.route("/skills/<skill>")                                       # представление для роута "/skills/<skill>"
def page_candidate_skills(skill):
    return f"<pre>" + candidates.choiсe_skills(skill) + "<pre>"


if __name__ == '__main__':
    app.run(host='127.0.0.2', port=8000)

