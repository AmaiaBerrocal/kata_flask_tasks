from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, ValidationError, AnyOf
from wtforms.widgets import TextArea
from datetime import date

def mayor_que_hoy(form, field):
    hoy = date.today()
    if field.data < hoy:
        raise ValidationError('La fecha debe ser igual o posterior a hoy')

class TaskForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(min=3, max=15, message='La longitud ha de estar entre 3 y 15 caracteres.')])
    description = StringField('Descripción', widget=TextArea())
    date = DateField('Fecha', validators=[DataRequired(), mayor_que_hoy])

    submit = SubmitField('Añadir tarea')

class ProcessTaskForm(FlaskForm):
    ix = HiddenField('ix', validators=[DataRequired()])
    btn = HiddenField('btn', validators=[DataRequired(), AnyOf(['M', 'B'])])
    title = StringField('Título', validators=[DataRequired(), Length(min=3, max=15, message='La longitud ha de estar entre 3 y 15 caracteres.')])
    description = StringField('Descripción', widget=TextArea())
    date = DateField('Fecha', validators=[DataRequired(), mayor_que_hoy])

    submit = SubmitField('Aceptar')