from flask import request, redirect, render_template
from datetime import datetime
from app import app
from tag import Tag

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
      name=request.form['tag-name'],
      defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')


@app.route('/', methods=['GET'])
def show_page():
    return render_template('template.html')
