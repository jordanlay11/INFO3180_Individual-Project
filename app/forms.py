from flask_wtf import FlaskForm
from wtforms import StringField, FileField, IntegerField, FloatField, TextAreaField, SelectField
from wtforms.validators import InputRequired, NumberRange, Length
from flask_wtf.file import FileRequired, FileAllowed

class PropertyForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired(message="Title is required"), Length(max=120)])
    description = TextAreaField("Property Description", validators=[InputRequired(message="Description is required"), Length(max=500, message="Description must be less than 500 characters")])
    bedrooms = IntegerField("Number of bedrooms", validators=[InputRequired(message="Bedrooms is required"), NumberRange(min=1, max=100, message="Enter a valid bedroom count")])
    bathrooms = IntegerField("Number of bathrooms", validators=[InputRequired(message="Bathrooms is required"), NumberRange(min=1, max=100, message="Enter a valid bathroom count")])
    location = StringField("Location of Property", validators=[InputRequired(message="Location is required"), Length(max=150)])
    price = FloatField("Price of Property", validators=[InputRequired(message="Price is required"), NumberRange(min=0, message="Price must be 0 or more")])
    type = SelectField("Type", validators=[InputRequired(message="Property type is required")], choices=[("Apartment", "Apartment"), ("House", "House")])
    photo = FileField(
        "Upload Image",
        validators=[
            FileRequired(message="Please choose a file"),
            FileAllowed({'jpg', 'jpeg', 'png', 'webp'}, message="Only .jpg, .jpeg, .png, .webp files allowed")
        ]
    )