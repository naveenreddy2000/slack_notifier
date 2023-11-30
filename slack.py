import urllib3
import json
import traceback
import datetime
import time
import os

REST = 59

notifications = {
  "Time": "Message",
  "10:30": "Follow up Reverse Proxy with Tiru",
  "13:00": "Lunch Break",
  "15:29": "Join 1:1 with Daksh",
  "16:45": "Break",
  "21:30": "Blueprint for escore ticket"
}

webhook_url = os.environ['SLACK_WEB_HOOK_URL']
http = urllib3.PoolManager()

def slack_notification(message):
  try:
    slack_message = {'text': message}

    response = http.request('POST',
                            webhook_url,
                            body = json.dumps(slack_message),
                            headers = {'Content-Type': 'application/json'},
                            retries = False)
  except:
    traceback.print_exc()

  return True

while True:
  now = datetime.datetime.now()
  time_string = now.strftime("%H:%M")
  print(time_string)
  if time_string in notifications.keys():
    slack_notification(notifications[time_string])
  time.sleep(REST)
