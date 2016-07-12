# prediction-appengine-guestbook-python

## Phases
This project is associated with this tutorial:

https://cloud.google.com/appengine/articles/prediction_service_accounts

Each directory represents a phase in the tutorial. phase1 is the basic skeleton, phase2
represents the project after Step 4 of the tutorial (sentiment analysis), phase3 represents
the final code product of the tutorial and includes language detection.

## Prerequisites

- Install Python-2.7 and virtualenv

- Install google cloud SDK

- Change into the directory of your choice and run

  $ pip install -r requirements.txt -t libs

## Register your application

- If you don't have a project, go to [Google Developers Console][1]
  and create a new project.

- Enable the "Prediction" API under "APIs & auth > APIs."

## Edit main.py

- DATA_FILE
- MODEL_ID
- PROJECT_ID

## Deploy

$ gcloud app deploy --project=${YOUR_PROJECT_NAME}

[1]: https://console.developers.google.com/project
