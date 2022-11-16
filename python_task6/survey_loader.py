import json
from pathlib import Path

def _transform_question(description, answers):
    return {
        "headings": [{
            "heading": description,
        }],
        "position": 1,
        "family": "single_choice",
        "subtype": "vertical",
        "answers": {
            "choices": [
                {"text": a} for a in answers
            ]
        }
    }


def load_survey(path_to_survey_json: Path) -> dict:
    raw_survey = json.loads(path_to_survey_json.read_text())
    return raw_survey


def transform_survey(survey: dict) -> dict:
    title, pages = list(survey.items())[0]
    return {
        "title": title,
        "pages": [
            {
                'questions': [_transform_question(q_content['Description'], q_content['Answers'])
                              for p in pages for _, q_content in survey[title][p].items()]
            }
        ]
    }
