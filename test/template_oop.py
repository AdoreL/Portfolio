from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from forms import ContactForm
from flask_mail import Mail, Message
import sqlite3
import os

mail = Mail()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'today was yellow and red'
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'comments.db')))

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'ninjalucario98@gmail.com'
app.config["MAIL_PASSWORD"] = ''

mail.init_app(app)
Bootstrap(app)


@app.route('/')
def Home():
    return render_template('template_oop.html', title = 'Home')

@app.route('/About')
def About():
    return render_template('template_oop.html', title = 'About')

@app.route('/Portfolio')
def Portfolio():
    return render_template('template_oop.html', title = 'Portfolio')

@app.route('/Projects')
def Projects():
    return render_template('template_oop.html', title = 'Projects')

@app.route('/Contact', methods=['GET', 'POST'])
def Contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('template_oop.html', title='Contact', form=form)
        else:
            msg = Message(form.subject.data, sender='ninjalucario98@gmail.com', recipients=['david98rp@hotmail.com'])
            msg.body = """
              From: %s <%s>
              %s
              """ % (form.name.data, form.email.data, form.message.data)

            with sqlite3.connect(app.config['DATABASE']) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO contact_table (name, email, subject, comment) VALUES (?,?,?,?)", (form.name.data, form.email.data, form.subject.data, form.message.data))
                con.commit()
            mail.send(msg)
            return render_template('template_oop.html', title='Contact', success=True)

    elif request.method == 'GET':
        return render_template('template_oop.html', title='Contact', form=form)


if __name__ == '__main__':
    #    app.run(port=8080, host='0.0.0.0', debug=True)
    app.run(debug=True)
