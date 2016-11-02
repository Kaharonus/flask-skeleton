"""
Logic for dashboard related routes
"""

from flask import Blueprint, render_template
from flask import redirect

from .forms import LogUserForm, LogCPUForm
from ..data.database import db
from ..data.models import LogUser, AddCPU
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)
@blueprint.route('/vypis_cpu',methods=['GET'])
def vypis_cpu():
    pole = db.session()


@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/addcpu',methods=['GET','POST'])
def AddCpuForm():
    form = LogCPUForm()
    if form.validate_on_submit():
        AddCPU.create(**form.data)
    return render_template("public/AddCpu.tmpl", form=form)

def smazat(id):
    pole = db.session.query(vypis_cpu).filter_by(vypis_cpu.id==id).first()
    try:
        db.session.remove(pole)
    except:
        status = ["Chyba uložení","error"]
        return redirect(ListuserLog)
    return True
