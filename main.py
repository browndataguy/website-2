from flask import Flask, render_template, jsonify
from database import loads_jobs_from_db, load_job_from_db

main = Flask(__name__)

@main.route("/")
def hello_world():
  jobs = loads_jobs_from_db()
  return render_template('home.html', jobs=jobs)

@main.route("/api/jobs")
def list_jobs():
  jobs = loads_jobs_from_db()
  return jsonify(jobs)

@main.route("/job/<id>")
def show_jo(id):
  job = load_job_from_db(id)
  
  if not job:
    return "Not found", 404
    
  return render_template('jobpage.html', job = job)

if __name__ == "__main__":
  main.run(host = '0.0.0.0', debug = True)
 
