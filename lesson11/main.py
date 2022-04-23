from flask import Flask, render_template

from utils import get_candidate, load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

data = load_candidates_from_json('candidates.json')

@app.route("/")
def index():
    return render_template('list.html', candidates=data)


@app.route('/candidate/<int:candidate_id>')
def profile(candidate_id):
    candidate = get_candidate(candidate_id)
    return render_template('single.html', candidate=candidate)


@app.route('/search/<name>')
def search(name):
    candidates = get_candidates_by_name(name)
    print(candidates)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route("/skill/<skill_name>")
def get_skills(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, candidates_len=len(candidates), skill=skill_name)


app.run()
