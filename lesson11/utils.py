import json

__data = []


def load_candidates_from_json(path):
    """
    Возвращает список всех кандидатов
    """
    global __data
    with open(path, 'r', encoding='utf-8') as file:
        __data = json.load(file)
    return __data


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    """
    for candidate in __data:
        if candidate['id'] == candidate_id:
            return {
                'name': candidate['name'],
                'position': candidate['position'],
                'picture': candidate['picture'],
                'skills': candidate['skills']
            }

def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    """
    return [candidate for candidate in __data if candidate_name.lower() in candidate['name'].lower()]

def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    """
    candidates = []
    for candidate in __data:
        skills = candidate['skills'].lower().split(', ')
        if skill_name in skills:
            candidates.append(candidate)
    return candidates

