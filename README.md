# Movie_Bot

# Installation and Bot Setup

This file will walk you through the steps to setup your bot. Download the entire folder and the follow the steps below.

## Step 1: Create Slack Bot user

Please follows the instructions in the link below to create a Slack App.

https://github.com/Sundar0989/Movie_Bot/blob/master/slack/Create_slack_app.ipynb

## Step 2: Create a IBM Watson account

Please follows the instructions in the link below to create a Slack App.

https://github.com/Sundar0989/Movie_Bot/blob/master/nlp/IBM_Watson_Conversation_setup.ipynb

## Step 3: Install required packages

Install the required packages listed in the requirements.txt file. To install the required packages, please use the code below. I might have missed some packages to include in the requirements.txt file. __When you initiate the bot, it might fail that a particular module does not exist. Please install it and then initiate bot again, which will fix the issue.__

```sh
pip3 install -r requirements.txt
```
It would be recommended to use Python 3.5.x or 3.6.x version for this project. 

## Step 4: Update the config files with the Slack and Watson API details

Please make sure that you modified the API details both for Slack and Watson in the config.py file

## Step 5: Create "onetime.txt" file

Navigate to the folder where the you downloaded the scripts and execute the code below.

```sh
python3 nlp/nlp_solutions/onetime_run_file.py
```
This will create the onetime.txt file automatically. If you need to rename this file, update the name in config.py file.

## Step 6: Initiate Bot

Navigate to the folder where the main python script exists and run the code below.

```sh
python3 main.py
```

# Bot Design

The Movie bot framework used here is a closed domain chatbot. The entire framework design is shown below. 

![](https://github.com/Sundar0989/Movie_Bot/blob/master/Bot%20design.png)

### Step 1 (User asks question):
Users can interact with Kelly via Slack. Once the user post a question via the interface, the question is passed to the backend system for analysis

### Step 2 (NLP processing):
All the natural language processing happens in step 2.  

### Step 3 (Return the NLP results):
After the NLP processing is completed, we have three outputs from it
1) Intents - What the user is trying to ask or query?
2) Entities - What is the exact field or column they are looking for?
3) Dialog/Interaction - Provide the appropriate request/response for the user question.

### Step 4 and 5(Query the data):

Currently, the data resides in a excel file. However, you can add multiple databases/excel files if needed, to access different sources. Based on the results from step 3, the appropriate database/excel file is queried and the results are returned.

### Step 6 (Post the result to user):

The results obtained from the backend is posted to user via Slack

### Step 7 (Log maintenance):

The interactions between the users are logged and stored in a flatfile format in a log file. Also, if the bot is not able to identify the user questions it will add those questions to a followup file.
