from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {"id":1,
     "Job title":"Data Analyst",
     "salary":"$10,000"}, 

     {"id":2,
     "Job title":"Data scientest",
     "salary":"$14,000"},

     {"id":3,
     "Job title":"Machine Learning Engineer",
     "salary":"$18,000"}, 

     {"id":4,
     "Job title":"Backend Engineer",
     "salary":"$12,000"}, 

     {"id":5,
     "Job title":"Frontend Engineer",
     "salary":"$8,000"},

]

@app.route("/")
def hello_world():
    return render_template("home.html", jobs = JOBS)

@app.route("/")
def list_jobs():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)