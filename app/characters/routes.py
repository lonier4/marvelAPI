from flask import Blueprint, render_template, request, url_for, flash, redirect
from app.forms import newMarvelForm
from flask_login import login_required

from app.models import db, Marvel

characters = Blueprint('characters', __name__, template_folder='characters_templates')

@characters.route('/addcharacter', methods=['GET', 'POST'])
@login_required
def addcharacter():
    form = newMarvelForm()
    if request.method =='POST':
        if form.validate_on_submit():
            new_marvel = Marvel(character_name=form.character_name.data,
                super_power=form.super_power.data, 
                comics_appeared_in=form.comics_appeared_in.data, 
                hero_or_villain=form.hero_or_villain.data, 
                description=form.description.data
            )

            db.session.add(new_marvel)
            db.session.commit()
            flash('New Marvel Character Added!', category='alert-info')
        else:
            flash('Nop, try again buddy', category='alert-danger')
        return redirect(url_for('characters.addcharacter'))
    return render_template('addcharacter.html', form=form)