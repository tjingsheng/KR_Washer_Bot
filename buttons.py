from flask import Flask
from flask import request
from flask import Response
from buttons import *
from constants import *
from functions import *
import requests

def send_wash_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': TXT_WASHER_OPTIONS,
        'reply_markup': {
            'inline_keyboard': [[
                {
                    'text': MACHINE_NAME[0],
                    'callback_data': 'washer_a'
                },
                {
                    'text': MACHINE_NAME[1],
                    'callback_data': 'washer_b'
                },
                {
                    'text': MACHINE_NAME[2],
                    'callback_data': 'washer_c'
                }]
            ]
        }
    }

    result = requests.post(url, json=payload)
    return result


def send_dry_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': TXT_DRYER_OPTIONS,
        'reply_markup': {
            'inline_keyboard': [[
                {
                    'text': MACHINE_NAME[3],
                    'callback_data': 'dryer_a'
                },
                {
                    'text': MACHINE_NAME[4],
                    'callback_data': 'dryer_b'
                },
                {
                    'text': MACHINE_NAME[5],
                    'callback_data': 'dryer_c'
                }]
            ]
        }
    }
    result = requests.post(url, json=payload)
    return result


def send_cancel_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': TXT_CANCEL_OPTIONS,
        'reply_markup': {
            'inline_keyboard': [[
                {
                    'text': MACHINE_NAME[0],
                    'callback_data': 'c_washer_a'
                },
                {
                    'text': MACHINE_NAME[1],
                    'callback_data': 'c_washer_b'
                },
                {
                    'text': MACHINE_NAME[2],
                    'callback_data': 'c_washer_c'
                },
                {
                    'text': MACHINE_NAME[3],
                    'callback_data': 'c_dryer_a'
                },
                {
                    'text': MACHINE_NAME[4],
                    'callback_data': 'c_dryer_b'
                },
                {
                    'text': MACHINE_NAME[5],
                    'callback_data': 'c_dryer_c'
                }]
            ]
        }
    }
    result = requests.post(url, json=payload)
    return result


def send_duration_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': TXT_DURATION_OPTIONS,
        'reply_markup': {
            'inline_keyboard': [[
                {
                    'text': '30',
                    'callback_data': '30'
                },
                {
                    'text': '45',
                    'callback_data': '45'
                },
                {
                    'text': '55',
                    'callback_data': '55'
                },
                {
                    'text': '1:05',
                    'callback_data': '65'
                },
                {
                    'text': '1:15',
                    'callback_data': '75'
                },
                {
                    'text': '1:25',
                    'callback_data': '85'
                },
                {
                    'text': '1:35',
                    'callback_data': '95'
                },
                {
                    'text': '1:39',
                    'callback_data': '99'
                }]
            ]
        }
    }
    result = requests.post(url, json=payload)
    return result