# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict(message="Hello World, This is My First Application")

def error():
    return dict()

def first():
    form = FORM(INPUT(_name='visitor_name',requires=IS_NOT_EMPTY()), INPUT(_type="submit"))
    if form.process().accepted:
        session.visitor_name = form.vars.visitor_name
        redirect(URL('second'))
    return dict(form=form)

def second():
    return dict()
