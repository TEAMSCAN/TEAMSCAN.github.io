from flask import Flask,render_template,flash,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from form import SupportForm
from datetime import datetime

app=Flask(__name__)
app.config['SECRET_KEY']='canyoufeelmyheart'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)

class Requestlist(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    username=db.Column(db.String(20),nullable=False)
    phone=db.Column(db.String(14),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    order=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"{self.id}^{self.date}^{self.username}^{self.phone}^{self.email}^{self.order}\n"
       


@app.route('/')
def home():
    print(Requestlist.query.all())
    return render_template('home.html')

@app.route('/support',methods=["GET","POST"])
def support():
    form=SupportForm()
    if form.validate_on_submit():
        requestlist=Requestlist(username=form.username.data,phone=form.phone.data,email=form.email.data,order=form.order.data)
        db.session.add(requestlist)
        db.session.commit()
        flash(f'Form submitted')
        return redirect(url_for('home'))
    return render_template('support.html',form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order',methods=["GET","POST"])
def order():
    data=0
    if request.method == "POST":
        key = request.form['password']
        if key=='SCAN000':
           data=list(Requestlist.query.all())
        else:
            flash(f'Sorry user that page is for admins only')
            return redirect(url_for('home'))
    return render_template('order.html',data=data)

if __name__ =='__main__':
    app.run(debug=True)
