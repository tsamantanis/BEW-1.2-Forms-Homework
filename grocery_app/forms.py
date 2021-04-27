from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    SelectField,
    SubmitField,
    FloatField,
)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL, NumberRange
from grocery_app.models import GroceryStore


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""
    title = StringField("Title", validators=[DataRequired(), Length(min = 2, max = 80)])
    address = StringField("Address", validators=[DataRequired(), Length(min = 2, max = 80)])
    submit = SubmitField("Submit")


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField("Name", validators=[DataRequired(), Length(min = 2, max = 80)])
    price = FloatField("Price", validators=[DataRequired(), NumberRange(min = 0)])
    category = SelectField("Category", choices=["PRODUCE", "DELI", "BAKERY", "PANTRY", "FROZEN", "OTHER"], validators = [DataRequired()])
    photo_url = StringField("Photo Url", validators=[DataRequired(), URL()])
    store = QuerySelectField("Store", query_factory = lambda: GroceryStore.query, allow_blank = False)
    submit = SubmitField("Submit")