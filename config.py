###################################################################
######## Configuration files for Bot   ##########################
###################################################################

"""
    config.py 
    
    This files has all the configurations for your bot.
    
"""

import os
import watson_developer_cloud
from slackclient import SlackClient

location = "/Users/xxxxxxxx/Downloads/Movie_Bot/"  # replace with the full folder path where you downloaded the github repo

###################################################################
######## Slack configuration   ##########################
###################################################################

# note: create Slack App with classic 'bot' scope, https://api.slack.com/apps?new_classic_app=1
# otherwise it will not work, see https://github.com/slackapi/python-slackclient/issues/584
SLACK_BOT_TOKEN='xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx'
SLACK_VERIFICATION_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxx' # some applications might require bot verification, generally not necessary

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

# note: depending on your location you will need to set the AssistantV1 url parameter
# e.g. in Germany you will need to set url='https://api.eu-de.assistant.watson.cloud.ibm.com'
service = watson_developer_cloud.AssistantV1(
    iam_apikey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', # replace with Assistant API key
    version = '2018-09-20'
)

workspace_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # replace with Skill ID

###################################################################
######## Log files configuration   ##########################
###################################################################

log_commands_path = location + "logs/log_commands.py" # do not change this parameter
follow_up_path = location + "logs/followup_email.py" # do not change this parameter

###################################################################
######## Temp files configuration   ##########################
###################################################################

onetime_path = location + "nlp/nlp_solutions/onetime_run_file.py" # do not change this parameter
onetime_file = location + "nlp/nlp_solutions/onetime.txt" # do not change this parameter
