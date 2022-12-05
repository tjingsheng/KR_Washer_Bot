from buttons import *
from constants import *
from functions import *
from time import gmtime, strftime, time
import requests

def convert(seconds):
    return strftime("%H:%M:%S", gmtime(seconds))


def parse_update(obj):
    chat_id = 0
    data = ''
    field = None

    if 'message' in obj:
        chat_id = obj['message']['chat']['id']
        data = obj['message']['text']
        field = 'message'
        
    if 'callback_query' in obj:
        chat_id = obj['callback_query']['message']['chat']['id']
        data = obj['callback_query']['data']
        field = 'callback_query'

    print('-----')
    print('\nRaw_Object : ',obj)
    print('\nChat_ID    : ', chat_id)
    print('\nRaw_Data   : ', data)
    print('-----')

    return chat_id, data, field


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    result = requests.post(url,json=payload)
    return result


def update_timer_database(chat_id, txt):
    with open(TIMER_FILE_NAME, mode = 'r', encoding = 'utf-8') as f:
        timer_data = f.read().splitlines()
    
    with open(DURATION_FILE_NAME, mode = 'r', encoding = 'utf-8') as f:
        dur_data = f.read().splitlines()
        washer_dur = dur_data[0]
        dryer_dur = dur_data[1]
    
    idx = CODE_TO_IDX_DICT[txt]
    dur = washer_dur if idx < 3 else dryer_dur
    timer_data[idx] = str(int(time()) + int(dur) * 60)

    with open(TIMER_FILE_NAME, mode = 'w', encoding = 'utf-8') as f:
        f.writelines(str(line) + '\n' for line in timer_data)
    
    send_message(chat_id, f"{dur} minutes timer started for {MACHINE_NAME[idx]}")


def cancel_timer(chat_id, txt):
    with open(TIMER_FILE_NAME, mode = 'r', encoding = 'utf-8') as f:
        timer_data = f.read().splitlines()
    
    txt = txt.split('_', 1)[1]
    idx = CODE_TO_IDX_DICT[txt]
    timer_data[idx] = str(int(time()))

    with open(TIMER_FILE_NAME, mode = 'w', encoding = 'utf-8') as f:
        f.writelines(str(line) + '\n' for line in timer_data)
    
    send_message(chat_id, f"Timer has been reset for {MACHINE_NAME[idx]}.")


def update_dur_database(chat_id, txt):
    with open(DURATION_FILE_NAME, mode = 'r', encoding = 'utf-8') as f:
        dur_data = f.read().splitlines()
    
    dur = int(txt)
    dur_data[1] = dur

    with open(DURATION_FILE_NAME, mode = 'w', encoding = 'utf-8') as f:
        f.writelines(str(line) + '\n' for line in dur_data)

    send_message(chat_id, f"Dryer default timer duration set to {dur} minutes.")
 

def get_duration():
    with open(DURATION_FILE_NAME, mode = 'r', encoding = 'utf-8') as f:
        dur_data = f.read().splitlines()
    return dur_data


def reset_duration(chat_id):
    with open(DURATION_FILE_NAME, mode = 'w', encoding = 'utf-8') as f:
        f.writelines(str(line) + '\n' for line in DEFAULT_DUR_DATA)
    send_message(chat_id, TXT_RESET)


def send_status(chat_id):
    with open(TIMER_FILE_NAME, mode = 'r', encoding = 'utf-8') as f:
        data = f.read().splitlines()
    
    result = TXT_STATUS
    for idx, item in enumerate(data):

        seconds_left  = max(0, (int(item) - int(time())))
        result = result + f'{MACHINE_NAME[idx]}: {convert(seconds_left)}\n'

    send_message(chat_id, result)