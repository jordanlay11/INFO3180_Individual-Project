import os
from werkzeug.utils import secure_filename
from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import PropertyForm 
from app.models import Properties
from . import db


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/properties/create', methods=['POST', 'GET'])
def create():
    form = PropertyForm()
    print(app.config['UPLOAD_FOLDER'])

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        bedrooms = form.bedrooms.data
        bathrooms = form.bathrooms.data
        location = form.location.data
        price = form.price.data
        type = form.type.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        photo.save(file_path)
        photo = file_path


        new_property = Properties(
            id=None,  
            title=title,
            description=description,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            location=location,
            price=price,
            type=type,
            photo=filename
        )
        db.session.add(new_property)
        db.session.commit()

        flash('Property successfully added', 'success')
        return redirect(url_for('properties'))

    if request.method == 'POST':
        flash('Property not added.', 'danger')
        flash_errors(form)

    return render_template('create.html', form=form)


@app.route('/properties')
def properties():
    properties = Properties.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/<int:propertyid>')
def property_detail(propertyid):
    prop = Properties.query.get_or_404(propertyid)
    return render_template('property.html', property=prop)

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
