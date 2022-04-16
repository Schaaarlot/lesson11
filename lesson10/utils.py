import json


def get_candidates(path):
    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)

def format_candidates(candidates_list):
    result = '<pre>'
    for candidate in candidates_list:
        result += (
            # <img src = "picture">
            f"Имя кандидата - {candidate['name']}\n"
            f"Позиция кандидата - {candidate['position']}\n"
            f"Навыки через запятую - {candidate['skills']}\n\n"
        )
        result += '<pre>'
    return result

def get_candidate_by_id(candidates_list, candidate_id):
    for candidate in candidates_list:
        if candidate['id'] == candidate_id:
            return candidate

def get_candidates_by_skill(candidates_list, candidate_skill):
    result = []
    for candidate in candidates_list:
        candidate_skills = candidate['skills'].lower().split(', ')

        if candidate_skill.lower() in candidate_skills:
            result.append(candidate)

    return result

