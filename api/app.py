from flask import Flask, url_for
import celery.states as states
import sys 
sys.path.append("..")
# udf 
from worker import celery

app = Flask(__name__)

@app.route('/scrap_task')
def run_github_scrape():
    task = celery.send_task('tasks.scrap_task',kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/scrap_task_api/<string:account>/<string:repo_name>')
def run_github_scrape_api():
    task = celery.send_task('tasks.scrape_github_api',kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/indeed_scrap_task')
def run_indeed_scrape():
    task = celery.send_task('tasks.indeed_scrap_task',kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/indeed_scrap_api_V1/<string:city_set>')
def run_indeed_scrape_api(city_set: str):
    print ('city_set :', city_set)
    task = celery.send_task('tasks.indeed_scrap_api_V1',city_set,kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response

@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)