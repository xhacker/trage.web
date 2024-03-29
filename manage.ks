# -*- coding: UTF-8 -*-
session = Session()
SET_UNICODE_OUT("utf-8")

from trage.common.problem import *
from trage.common import judge

def index():
    print "警告！你误闯到了禁区。"

def edit():
    Include("/page_common.py")
    prob_id = THIS.args[0]
    prob = Problem(prob_id)
    prob.load()

    main =  '<form action="/manage/do_edit" method="post">'
    main += '<p><label>Name</label></p><p><input name="name" type="text" value="%s" /></p>' % prob.get_name()
    main += '<p><label>Title</label></p><p><input name="title" type="text" value="%s" /></p>' % prob.get_title()
    main += '<p><label>Desc</label></p><p><textarea name="info_main">%s</textarea></p>' % prob.get_info_main()
    main += '<p><label>Input Desc</label></p><p><textarea name="info_input">%s</textarea></p>' % prob.get_info_input()
    main += '<p><label>Output Desc</label></p><p><textarea name="info_output">%s</textarea></p>' % prob.get_info_output()
    main += '<p><label>Example Input</label></p><p><textarea name="example_input">%s</textarea></p>' % prob.get_example_input()
    main += '<p><label>Example Output</label></p><p><textarea name="example_output">%s</textarea></p>' % prob.get_example_output()
    main += '<p><label>Hint</label></p><p><textarea name="info_hint">%s</textarea></p>' % prob.get_info_hint()
    main += u'<p><label>难度</label></p><p><input name="difficulty" type="text" value="%s" /></p>' % prob.get_difficulty()
    main += u'<p><button type="submit">提交</button>'
    main += '<input name="id" type="hidden" value="%s" /></p>' % prob_id
    main += '</form>'
    js = ''
    title = '禁区'
    nav = '禁区'
    print KT('/main.kt', data=locals(), notify=get_notify(), style=get_style(), this=THIS)

def do_edit(**args):
    prob = Problem(args['id'])
    prob.set_all(args)
    session.notify = "Edit sucessful."
    raise HTTP_REDIRECTION, "/manage/edit/%s" % args['id']

def unlock():
    judge.unlock()
