# prediction-appengine-guestbook-python

## Prerequisites

- Install Python-2.7 and virtualenv

- Install google cloud SDK

- Run scripts/setup.sh with the project directory as an argument.

  $ scripts/setup-google-api-client.sh .

## Register your application

- If you don't have a project, go to [Google Developers Console][1]
  and create a new project.

- Enable the "Prediction" API under "APIs & auth > APIs."

## Edit main.py

- DATA_FILE
- MODEL_ID
- API_KEY
- PROJECT_ID

## Deploy

$ gcloud preview app deploy --project=${YOUR_PROJECT_NAME}

[1]: https://console.developers.google.com/project
