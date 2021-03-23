from flask import request, redirect, render_template
from datetime import datetime
from app import app
from tag import Tag
<<<<<<< HEAD
#follow along update
=======

#@app.route('/', methods=['GET'])
def show_tags():
    tags = Tag.select()
    tags_html = '\n'.join(list(map(lambda x: x.name + "<br>", tags)))
    form_html = "<form action=\"/tags\" method=\"POST\"><label>Enter a tag: </label><input name=\"tag-name\"></form>"
    #embed()
    return "<h1>The Ultimate Tag Manager</h1><h1>Hello World!</h1><img src=\"%s\"><div>%s</div><div>%s</div>" % (app.config['config']['awesome_image'],tags_html, form_html)
>>>>>>> master-css

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
      name=request.form['tag-name'],
      defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')
<<<<<<< HEAD

@app.route('/', methods=['GET'])
def show_page():
    return render_template('template.html')
=======
    
@app.route('/', methods=['GET'])
def show_tags():
    tags = Tag.select()
    tags_html = '\n'.join(list(map(lambda x: x.name + "<br>", tags)))
    form_html = "<form action=\"/tags\" method=\"POST\"><label>Enter a tag: </label><input name=\"tag-name\"></form>"
    #embed()
    return "<h1>The Ultimate Tag Manager</h1><h1>Hello World!</h1><img src=\"%s\" style=\"width:300px\"><div>%s</div><div>%s</div>" % (app.config['config']['awesome_image'], form_html, tags_html)

>>>>>>> 28b850f1e128ed0776e0ee81f130f27426a768bb
