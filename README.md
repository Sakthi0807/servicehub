# Electrician and Plumbing Service Website

This project is a web application designed to connect users with professional electricians and plumbers. The platform allows users to request services, submit inquiries, and upload their resumes if they are interested in joining as service providers.

## Features

- **Service Requests**: Users can select a service type (electrician or plumber) and provide details about their needs.
- **Resume Upload**: Interested professionals can upload their resumes to apply for jobs.
- **Contact Form**: Allows users to contact the company with their queries.
- **Google Maps Integration**: Displays the location of the service center.

## Technologies Used

- **Frontend**: 
  - HTML
  - CSS (Bootstrap Framework)
  - JavaScript

- **Backend**: 
  - Python (Flask Framework)

- **Database**: 
  - MySQL

- **Other Tools**:
  - Twilio API (for sending notifications)
  - Google Maps API (for embedding maps)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/electrician-plumbing-service.git
   cd electrician-plumbing-service
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For Linux/macOS
   myenv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file and add the following:
   ```env
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   UPLOAD_FOLDER=static/uploads
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DB=service_db
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_WHATSAPP_NUMBER=whatsapp:+your_twilio_number
   ```

5. **Initialize Database**
   Create a MySQL database and run the SQL script in `schema.sql` to create the required tables.

6. **Run the Application**
   ```bash
   flask run
   ```

7. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- Navigate to the home page to view services.
- Use the service request form to book a service.
- Upload resumes via the "Join Us" form.
- View the location of the service center via the embedded Google Map.

## Folder Structure

```
├── static/
│   ├── css/
│   ├── js/
│   ├── uploads/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── joinus.html
│   ├── contact.html
├── app.py
├── requirements.txt
├── schema.sql
└── README.md
```

## Contribution

Feel free to contribute to the project. Fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries, reach out to:
- **Email**: your-email@example.com
- **Phone**: +91 1234567890
