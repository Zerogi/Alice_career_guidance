from flask import Flask, request
import json
import Levenshtein as lv

app = Flask(__name__)


session = {}  # информация о пользователях


@app.route('/post', methods=['POST'])
def main():
    response = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    answer = request.json['request']['original_utterance']
    user_id = request.json['session']['user_id']  # get user id
    if user_id not in session:  # if it's new user
        greeting(response, user_id)
    elif session[user_id] == 'start':
        if answer.lower() == 'да':
            start(response, user_id)
        elif answer.lower() == 'нет':
            response['response']['text'] = 'Пока'
    elif session[user_id] == 'making choice':
        pass
    return json.dumps(response)


def greeting(res, user):  # greeting and adding to the session
    session[user] = 'start'
    res['response']['text'] = """Привет! Перед тобой встал сложный выбор и 
    тебе нужно помочь выбрать профиль, профессию или вуз?"""


def start(res, user):  # ask what user want
    session[user] = 'making choice'
    res['response']['text'] = """Я могу помочь с выбором профиля, университета или 
    же профессии, если ты выбрал профиль. Что тебя интересует?"""


def making_choice(req, res, user):
    choices = ['профиль', 'универститет', 'профессия']
    max_similarity = [-1, -1]
    for choice in choices:
        pass


def repeat():
    pass


if __name__ == '__main__':
    print('START')
    app.run()