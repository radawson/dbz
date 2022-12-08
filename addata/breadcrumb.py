from flask import Blueprint, flash, render_template, request, redirect, send_from_directory, url_for
from werkzeug.utils import secure_filename
import os
import pandas as pd
from . import models

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
    return render_template('breadcrumbs/index.html')

@bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('Please select a file')
            return redirect(request.url)
        flash("Please wait, this can take some time")
        for f in request.files.getlist('file'):
            f.save(os.path.join(UPLOAD_PATH, f.filename))
        #return redirect(url_for('breadcrumb.download_file', name=f.filename))
    return render_template('breadcrumbs/upload.html')

@bp.route('/download/<name>')
def download_file(name):
    return send_from_directory(UPLOAD_PATH, name)

bp.add_url_rule(
    '/download/<name>', endpoint="download_file", build_only=True
)

@bp.route('/import')
def inhale():
    results = []
    for entry in os.scandir(UPLOAD_PATH):
        if '.parquet' in entry.name:
            df = pd.read_parquet(UPLOAD_PATH + '/'+ entry.name)
            df.to_sql("breadcrumbs", con=models.db.engine, if_exists='append')
            results.append(entry.name)
            print(f'Processing {entry.name}')
            os.rename(UPLOAD_PATH +'/'+ entry.name, PROCESSED_PATH +'/'+ entry.name)
    return render_template('breadcrumbs/complete.html', files=results)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS