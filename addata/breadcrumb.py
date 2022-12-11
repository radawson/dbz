from flask import Blueprint, flash, render_template, request, redirect, send_from_directory, url_for, session
from werkzeug.utils import secure_filename
import os
import pandas as pd
from datetime import datetime
from models import models

ALLOWED_EXTENSIONS = {'parquet'}
PROCESSED_PATH = './processed'
UPLOAD_PATH = './upload'

bp = Blueprint(
    'breadcrumb',
    __name__,
    url_prefix="/breadcrumbs"
)

@bp.route('/', methods=['GET', 'POST'])
def breadcrumbs():
    results = models.File.query.all()
    results.sort(key=lambda File: File.filename)
    return render_template('breadcrumbs/index.html', data=results)

@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    results = []
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        for f in request.files.getlist('file'):
            f.save(os.path.join(UPLOAD_PATH, secure_filename(f.filename)))
            results.append(f.filename)
        operation ="File upload complete"
        session['results'] = results
        session['operation'] = operation
        return redirect(url_for('breadcrumb.complete'))
    else:
        return render_template('breadcrumbs/upload.html')

@bp.route('/download/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_PATH, name)

bp.add_url_rule(
    '/download/<name>', endpoint="download_file", build_only=True
)

@bp.route('/import')
def process():
    results = []
    for entry in os.scandir(UPLOAD_PATH):
        if '.parquet' in entry.name:
            # Check for previously processed files
            #for file in old_files:
            query = models.db.select()
            #TODO: disallow duplicate files imports?
            if models.File.query.filter_by(filename=entry.name).first():
                print('File is a duplicate', Warning)
                flash(f'{entry.name} is a duplicate')
            else:   
                df = pd.read_parquet(UPLOAD_PATH + '/'+ entry.name)
                df.to_sql("breadcrumbs", con=models.db.engine, if_exists='append')
                new_file = models.File(filename=entry.name)
                models.db.session.add(new_file)
                models.db.session.commit()
                results.append(entry.name)
                print(f'Processing {entry.name}')
                os.rename(UPLOAD_PATH +'/'+ entry.name, PROCESSED_PATH +'/'+ entry.name)
    operation = "File import complete"
    session['results'] = results
    session['operation'] = operation
    return redirect(url_for('breadcrumb.complete'))

@bp.route('/complete')
def complete():
    results = session.pop('results', None)
    operation = session.pop('operation', None)
    return render_template('breadcrumbs/complete.html', files=results, title=operation)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS