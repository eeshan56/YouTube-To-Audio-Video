
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

FormatChoices = [('0', 'Video'), ('1', 'Audio')]

class MainForm(FlaskForm):

	url_field = StringField('Enter video URL', validators = [DataRequired()])
	output_format = SelectField(u'Format', choices = FormatChoices)
	submit = SubmitField('Convert')