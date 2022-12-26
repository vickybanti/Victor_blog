from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, InputRequired, Email, email_validator
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    # author = StringField("Author", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class LoginForm(FlaskForm):
    email = StringField("Input email", validators=[InputRequired(), Email(message="Invalid email")])
    password = PasswordField("Input password", validators=[DataRequired()])
    submit = SubmitField("Log in")

class Register(FlaskForm):
    email = StringField("Input email",
                        validators=[InputRequired(), Email(message="Invalid email", allow_smtputf8=True)])
    password = PasswordField("Input password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired()])
    name = StringField("Username", validators=[DataRequired()])
    submit = SubmitField("Register")

class Comment(FlaskForm):
    body = CKEditorField("Write your comment here", validators=[DataRequired()])
    submit = SubmitField("Submit comment")

