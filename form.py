from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Email
from wtforms.widgets import TextArea

class SupportForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    phone=StringField('Phone no',validators=[DataRequired(),Length(min=10,max=13)])
    order=StringField('Enter your query',validators=[DataRequired()],widget=TextArea())
    submit=SubmitField('submit')

    
