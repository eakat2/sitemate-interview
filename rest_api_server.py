import json
import time
from flask import Flask, request

app = Flask(__name__)

database = []

class Issue:
  def __init__(self, id, createdBy, issueLevel, summary, title):
    self.id = id
    self.createBy = createdBy
    self.issueLevel = issueLevel
    self.title = title
    self.summary = summary
    self.createdDateTime = time.time()


@app.route("/issues", methods=['POST'])
def create_issue():
    try:
        input_data = request.get_json()
        id = len(database)
        new_issue = Issue(id, input_data["createdBy"], input_data["issueLevel"], input_data["summary"], input_data["title"])
        database[id] = new_issue
        response = {
           'id': id
        }

        return json.dumps(response)
    except Exception as e:
        return json.dumps(e)





