from flask import Flask
from flask import request
from flask import Response
from buttons import *
from constants import *
from functions import *


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        main()
        return Response('ok', status=200)
    else:
        return '<h1> KR Washer Bot Server</h1> Visit @krwasherdryerbot on Telegram.'


def button_received(chat_id, txt):
    if txt == 'washer_a':
        update_timer_database(chat_id, txt)
    elif txt == 'washer_b':
        update_timer_database(chat_id, txt)
    elif txt == 'washer_c':
        update_timer_database(chat_id, txt)
    elif txt == 'dryer_a':
        update_timer_database(chat_id, txt)
    elif txt == 'dryer_b':
        update_timer_database(chat_id, txt)
    elif txt == 'dryer_c':
        update_timer_database(chat_id, txt)
    elif txt == 'c_washer_a':
        cancel_timer(chat_id, txt)
    elif txt == 'c_washer_b':
        cancel_timer(chat_id, txt)
    elif txt == 'c_washer_c':
        cancel_timer(chat_id, txt)
    elif txt == 'c_dryer_a':
        cancel_timer(chat_id, txt)
    elif txt == 'c_dryer_b':
        cancel_timer(chat_id, txt)
    elif txt == 'c_dryer_c':
        cancel_timer(chat_id, txt)
    elif txt == '30':
        update_dur_database(chat_id, txt)
    elif txt == '45':
        update_dur_database(chat_id, txt)
    elif txt == '55':
        update_dur_database(chat_id, txt)
    elif txt == '65':
        update_dur_database(chat_id, txt)
    elif txt == '75':
        update_dur_database(chat_id, txt)
    elif txt == '85':
        update_dur_database(chat_id, txt)
    elif txt == '95':
        update_dur_database(chat_id, txt)
    elif txt == '99':
        update_dur_database(chat_id, txt)
    else: 
        send_message(chat_id, TXT_ERROR)


def command_received(chat_id, txt):
    if txt == '/start':
        send_message(chat_id, TXT_WELCOME)
    elif txt == '/about':
        send_message(chat_id, TXT_ABOUT)
    elif txt == '/help':
        send_message(chat_id, TXT_HELP)
    elif txt == '/wash':
        send_wash_inlinebutton(chat_id)
    elif txt == '/dry':
        send_dry_inlinebutton(chat_id)
    elif txt == '/status':
        send_status(chat_id)
    elif txt == '/cancel':
        send_cancel_inlinebutton(chat_id)
    elif txt == '/dryer_duration':
        send_duration_inlinebutton(chat_id)
    elif txt == '/reset':
        reset_duration(chat_id)
        send_message(chat_id, TXT_RESET)
    else:
        send_message(chat_id,TXT_INVALID_COMMAND)
    

def main():
    obj = request.get_json()
    chat_id, txt, field = parse_update(obj)

    if field == 'message':
        command_received(chat_id, txt)
    
    if field == 'callback_query':
        button_received(chat_id, txt)


if __name__ == '__main__':
    app.run(debug=False) # Set false before production
    app.run(Threaded=True)
