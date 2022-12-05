TOKEN = '5922185152:AAEz5RbKXiR7bHrLH55lvCyB2fe5up8YkFs'
BOT_NAME = 'KR Washer Bot'
TIMER_FILE_NAME = 'timer_database.txt'
DURATION_FILE_NAME = 'duration_database.txt'
MACHINE_NAME = ['Washer A', 'Washer B', 'Washer C', 'Dryer A', 'Dryer B', 'Dryer C']
CODE_TO_IDX_DICT = {'washer_a' : 0, 'washer_b' : 1, 'washer_c' : 2, 'dryer_a' : 3, 'dryer_b' : 4, 'dryer_c' : 5}
DEFAULT_DUR_DATA = [30, 45]
TXT_WELCOME = f'Welcome to {BOT_NAME}!\nPress /help for some useful commands.'
TXT_ABOUT = f'Thank you for trying the {BOT_NAME}!\nThis bot is still being improved.\nTele @Jsh3ng for feedback and issues.'
TXT_HELP =  """
Here are the available commands:
/start - to begin
/about - More about this bot
/help - Show available commands
/wash - Start a washing cycle timer
/dry - Start a drying cycle timer
/cancel - Cancel a machine's timer
/status - Check all machines' status
/dryer_duration - Modify dryers' duration
/reset - Reset settings
"""
TXT_WASHER_OPTIONS = f'The default timer for washing machines is {DEFAULT_DUR_DATA[0]} minutes.\nBegin timer by selecting the washing machine you have already started:'
TXT_DRYER_OPTIONS = f'The default timer for dryer machines is {DEFAULT_DUR_DATA[1]} minutes.\nPress /dryer_duration to modify.\nBegin timer by selecting the dryer machine you have already started:'
TXT_CANCEL_OPTIONS = 'Please select the machine to cancel:'
TXT_DURATION_OPTIONS = 'Please select the new duration for dryer machines:'
TXT_INVALID_COMMAND = 'You have entered an invalid command.\n/help to find out more.'
TXT_STATUS = 'Time left per machine:\n'
TXT_RESET = 'Default durations have been set.'
TXT_ERROR = 'An Error has occured. Please try again later :('