"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github') 

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html", first=first, last=last, github=github)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html") #displays form to submit student info


@app.route("/student-add", methods=['POST'])
def student_add():
	"""Add a student."""
	
	first = request.form.get('first_name')
	last = request.form.get('last_name')
	github = request.form.get('github')

	print first


	

	# payload = {'key1': 'value1', 'key2': 'value2'}
	

	# r = requests.post("/student-add-form", data=payload)
	# print(r.text)





	hackbright.make_new_student(first, last, github)

	#flash('You successfully added a student')

	html = render_template("add_student_success.html", github=github)

	return html




@app.route("/student-add-form")
def new_student_form():
    """Show form for searching for a student."""

    return render_template("add_student_form.html")



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
