# -*- coding: utf-8 -*-
# muMDAU_app init file 
# some debug code of server like update/restart code
from flask import Flask
from flask import render_template 
app = Flask(__name__)

@app.route('/<usernm>')
def indexp(usernm):
    cls = open('./classraw/' + usernm, 'r')
    listcls = cls.readline()
    cals = str(listcls)
    listclass = eval(cals)
    return render_template('index.html', **locals())
