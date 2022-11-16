import requests

ACCESS_TOKEN = "rzK6HA54nZqRBAaYSMIciiIkGQQc.NWQTmIamwhMqUrmZyuOXYxyY1kgnvh95FW-R8MEb.HjWKdNWE6n3.QzjgbO93eKJxr694VGd4KAdrzus2mBamGo9Rr7sM2G.gRP"
HOME_URL = "https://api.surveymonkey.net"
SURVEY_LIST_ENDPOINT = "/v3/surveys"
COLLECTOR_ENDPOINT = "/v3/collectors"


class SurveyMonkeyClient():
    def __init__(self):
        self.session = requests.Session()

        self.headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'Authorization': f"Bearer {ACCESS_TOKEN}"
        }

    def send_survey(self, survey: dict) -> requests.Response:
        response = self.session.post(
            HOME_URL + SURVEY_LIST_ENDPOINT, headers=self.headers, json=survey)
        return response

    def add_collector(self, survey_id: str, type: str = 'email'):
        response = self.session.post(HOME_URL + SURVEY_LIST_ENDPOINT +
                                     f'/{survey_id}/collectors', headers=self.headers, json={'type': type})
        return response

    def add_message_to_collector(self, collector_id, type='invite'):
        json = {
            "type": "invite"
        }

        response = self.session.post(HOME_URL + COLLECTOR_ENDPOINT + f'/{collector_id}/messages', headers=self.headers, json=json)
        return response

    def add_recipients_to_collector(self, collector_id, message_id, recipients):
        json = {
            "contacts": [
                {"email": email} for email in recipients
            ]
        }
        response = self.session.post(
            HOME_URL + COLLECTOR_ENDPOINT + f'/{collector_id}/messages/{message_id}/recipients/bulk', headers=self.headers, json=json)
        return response

    def send_message(self, collector_id, message_id):
        response = self.session.post(
            HOME_URL + COLLECTOR_ENDPOINT + f'/{collector_id}/messages/{message_id}/send', headers=self.headers, json={})
        return response
