import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
from twilio.rest import Client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdertyui'

# Twilio credentials
account_sid = 'AC3c1138eeaaeccb59f36e2668423d4ee9'
auth_token = '90e69fcc0aa8ab1707100af3df949035'
twilio_whatsapp_number = 'whatsapp:+14155238886' 
num = 916382168391   # Replace with the recipient's phone number
client = Client(account_sid, auth_token)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'demo'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MYSQL_CURSOR'] = 'DICTCURSOR'

mysql = MySQL(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        msg = request.form['message']

        # Send WhatsApp message using Twilio
        message = client.messages.create(
            body=f"New Contact Form:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {msg}",
            from_=twilio_whatsapp_number,
            to=f'whatsapp:+{num}'  
        )


        flash("Contact Form Submitted Successfully!", "success")

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/joinus')
def joinus():
    return render_template('joinus.html')

@app.route('/book_service')
def book_service():
    return render_template('bookform.html')


@app.route('/booked' , methods= ['POST','GET'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        service = request.form.get('services')
        description = request.form['description']
        service_date = request.form['service_date']
        

        conn = mysql.connection.cursor()

        sql1 = "INSERT INTO client (name,email,phone,address,service,description,service_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        conn.execute(sql1,[name,email,phone,address,service,description,service_date])

        mysql.connection.commit()
        conn.close()

    # Send WhatsApp message using Twilio
        message = client.messages.create(
            body=f"New service booking:\n\nName: {name}\nService: {service}\nPhone: {phone}\nDate: {service_date}\nDescription: {description}",
            from_=twilio_whatsapp_number,
            to=f'whatsapp:+{num}'
        )

        flash("Service booked successfully!", "success")

        # Redirect to another page or back to the form
        return redirect(url_for('book_service'))

    return render_template('bookform.html')

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    # Check if the file extension is allowed.
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/submit-form', methods=['POST'])
def submit_form():
    if request.method == 'POST':

        if 'resume' not in request.files:
            flash('No file part', 'danger')
            return redirect(url_for('joinus'))  # Corrected redirect

        file = request.files['resume']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)  # Save the file to the server

            # Get the form data
            service = request.form['service']
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            address = request.form['address']

            # Save the form data and file path to the database
            conn = mysql.connection.cursor()
            sql2 = "INSERT INTO worker_request (service, name, email, phone, address, resume_path) VALUES (%s, %s, %s, %s, %s, %s)"
            conn.execute(sql2, [service, name, email, phone, address, file_path])  # Save file path after file is saved
            mysql.connection.commit()
            conn.close()

            message = client.messages.create(
            body=f"New Worker Register:\n\nName: {name}\nService: {service}\nPhone: {phone}\nAddress: {address}",
            from_=twilio_whatsapp_number,
            to=f'whatsapp:+{num}'
            )

            flash('Form submitted successfully!', 'success')
            return redirect(url_for('joinus'))  # Redirect to the form page or a success page

        else:
            flash('Invalid file format', 'danger')
            return redirect(url_for('joinus'))  # Redirect back on invalid file


if __name__ == '__main__':
    app.run(debug=True)