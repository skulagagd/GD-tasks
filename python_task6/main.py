from pathlib import Path
import logging

from survey_loader import load_survey, transform_survey
from surveymonkey_client import SurveyMonkeyClient

PATH_MAILS = Path('./mails.txt')
PATH_SURVEY = Path('./survey.json')

class SurveyError(Exception):
    def __init__(self, message="Failed to create the survey, check logs"):
        self.message = message
        super().__init__(self.message)

def extract_mails(path_to_mails_file: Path) -> list[str]:
    return path_to_mails_file.read_text().splitlines()

client = SurveyMonkeyClient()
mails = extract_mails(PATH_MAILS)
raw_survey = load_survey(PATH_SURVEY)
survey = transform_survey(raw_survey)

survey_response = client.send_survey(survey)
if survey_response.status_code != 201:
    logging.error(survey_response.text)
    raise SurveyError

print(f'Status code: {survey_response.status_code}')
print(f'Response text: {survey_response.text}')
survey_response = survey_response.json()
logging.debug(survey_response)
'''
collector_response = client.add_collector(survey_response['id']).json()
print(collector_response) # WE CANNOT DO A EMAIL COLLECTOR, SO WE CANNOT CREATE MESSAGE, AND WE CANNOT SEND IT

message_response = client.add_message_to_collector(collector_response['id']).json()
recipents_response = client.add_recipients_to_collector(collector_id=collector_response['id'], message_id=message_response['id'])
send_response = client.send_message()

#print(send_response.text)
'''


