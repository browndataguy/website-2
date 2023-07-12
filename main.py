from flask import Flask, render_template, jsonify
from database import loads_jobs_from_db

main = Flask(__name__)

@main.route("/")
def hello_world():
  jobs = loads_jobs_from_db()
  return render_template('home.html', jobs=jobs,
                        company_name = 'Jovian')

@main.route("/api/jobs")
def list_jobs():
  jobs = loads_jobs_from_db()
  return jsonify(jobs)

if __name__ == "__main__":
  main.run(host = '0.0.0.0', debug = True)
 
