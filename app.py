from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "student_registration_portal_secret_key"  # needed for flash messages

# ------------------------------------------------------
# Temporary in-memory storage (No Database)
# ------------------------------------------------------
students = []


# ------------------------------------------------------
# Home Page
# ------------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# ------------------------------------------------------
# Register Student
# ------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        mobile = request.form.get('mobile', '').strip()
        course = request.form.get('course', '').strip()

        # Validation: all fields required
        if not name or not email or not mobile or not course:
            flash('All fields are required!', 'error')
            return redirect(url_for('register'))

        # Save student in the list (No Database)
        student = {
            'name': name,
            'email': email,
            'mobile': mobile,
            'course': course
        }
        students.append(student)

        flash('Student Registered Successfully', 'success')
        return redirect(url_for('register'))

    return render_template('register.html')


# ------------------------------------------------------
# View Students
# ------------------------------------------------------
@app.route('/students')
def view_students():
    return render_template('students.html', students=students)


# ------------------------------------------------------
# About Page
# ------------------------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')


# ------------------------------------------------------
# Contact Page
# ------------------------------------------------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('contact'))

        flash('Thanks for contacting us.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')


# ------------------------------------------------------
# Custom 404 Page
# ------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# ------------------------------------------------------
# Run App
# ------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
