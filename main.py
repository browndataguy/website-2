from flask import Flask, render_template, jsonify

main = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs 10,000,000'
  },

    {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs 15,000,000'
  },

  {
    'id': 3,
    'title': 'Front End',
    'location': 'Mumbai, India',
    'salary': 'Rs 12,000,000'
  },

  {
    'id': 4,
    'title': 'Backend engineer',
    'location': 'San francisco',
    'salary': '$ 120,000'
  }

  
]

@main.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS,
                        company_name = 'Jovian')

@main.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  main.run(host = '0.0.0.0', debug = True)
 
