from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id':1,
    'title':'Data Analyst',
    'location': 'remote',
    'salary':'$60000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location': 'remote',
    'salary':'$78000'
  },
  {
    'id':3,
    'title':'Frontend developer',
    'location': 'remote',
    'salary':'$60000'
  },
  {
    'id':4,
    'title':'Backend developer',
    'location': 'remote',
    'salary':'$75000'
  },
  {
    'id':5,
    'title':'Accountant',
    'location': 'remote',
    'salary':'$72000'
  }
]


@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
  