from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import csv
import os

app = Flask(__name__)
app.secret_key = 'secret_key_here'  # Replace with a real secret key

# Email config (optional)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='andrewf704@gmail.com',
    MAIL_PASSWORD='kanr mkuq cxou vuyd'

,  # Use an app password if using Gmail
)
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['full_name']
        email = request.form['email']
        date = request.form['due_date']
        time = request.form['due_time']

        # Save to CSV file
        with open('guesses.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, email, date, time])

        # Optional: Send email to yourself
        msg = Message('New Baby Due Date Prediction Submission',
                      sender='babyguesser@gmail.com',
                      recipients=['andrewnorly@gmail.com'])
        msg.body = f'Name: {name}\nEmail: {email}\nDate: {date}\nTime: {time}'
        mail.send(msg)

        flash("Thanks for guessing Lil Fishy's due date. We'll let you know who wins on July 1st!")

        return redirect('/')

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)