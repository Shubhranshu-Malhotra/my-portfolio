from flask import Flask, render_template, request, url_for
import csv
app = Flask(__name__)
print(__name__)


def write_to_file(data):
    with open('database.txt',newline = '', mode = 'a') as csv_database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(name,email,subject,message)


def write_to_csv(data):
    with open('database.csv',mode = 'a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{name},{email},{subject},{message}')

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def about(page_name):
    return render_template('index.html/page_name')
    # return redirect(request.referrer)


@app.route('/submit_contact', methods=['GET', 'POST'])
def submit_contact():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'Thank you for contacting me. I will get back to you soon.'
        except:
            return 'Did not save to database'
    else:
        return 'There was some error in submitting the contact details. Please try again.'
