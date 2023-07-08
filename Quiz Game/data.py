import requests
question_data = requests.get(url='https://opentdb.com/api.php',
                             params={'amount': 10, 'difficulty': 'hard', 'type': 'boolean'}).json()['results']

