# -*- coding: UTF-8 -*-
session = Session()
SET_UNICODE_OUT("utf-8")
from trage.common.problem import *
from trage.helpers import nl2br

login = hasattr(session, "login") and session.login

prob = Problem(THIS.args[0])
prob.load()

title = "Problem[%s]: %s" % (prob.get_id(), prob.get_title())
nav = title
js = ''

notify = ''
if hasattr(session, "notify") and session.notify:
    notify = '<div class="notify"><p class="info">%s</p></div>' % session.notify
    session.notify = None

if login:
    submit_html = '''<form action="/judge" enctype="multipart/form-data" method="post">
    <p class="small">Should be <em>*.c</em>, <em>*.cpp</em> or <em>*.pas</em>.
    <br />Using <em>file</em> input/output (<em>%(name)s.in</em>, <em>%(name)s.out</em>).</p>
    <p>
        <input type="file" name="source" />
        <input type="hidden" name="prob_id" value="%(id)s" />
        <input type="submit" />
    </p>
</form>''' % {
    'id': prob.get_id(),
    'name': prob.get_name() }
else:
    submit_html = '<p>还没<a href="/#login">登录</a>呢，别想交题！！</p>'

if login:
    AC = get_status(session.userid, prob.get_id())
    if AC:
        ac_emotion = '<span class="accepted"><abbr title="已经秒掉了！">☻</abbr></span>'
    else:
        ac_emotion = '<span class="unaccepted"><abbr title="呃…还没 AC 呢，赶快做吧…">☺</abbr></span>'
else:
    ac_emotion = ''

main = u'''
<h2>%(emotion)s %(title)s</h2>
<hr />
<h3>题目描述</h3>
<p>%(info_main)s</p>
<h3>输入说明</h3>
<p>%(info_input)s</p>
<h3>输出说明</h3>
<p>%(info_output)s</p>
<h3>样例输入</h3>
<p>%(example_input)s</p>
<h3>样例输出</h3>
<p>%(example_output)s</p>
<h3>提示</h3>
<p>%(info_hint)s</p>
<h3>提交程序</h3>
<a name="submit"></a>
%(submit)s
''' % {
    'emotion': ac_emotion,
    'title': prob.get_title(),
    'info_main': nl2br(prob.get_info_main()),
    'info_input': nl2br(prob.get_info_input()),
    'info_output': nl2br(prob.get_info_output()),
    'example_input': nl2br(prob.get_example_input()),
    'example_output': nl2br(prob.get_example_output()),
    'info_hint': nl2br(prob.get_info_hint()),
    'submit': submit_html}

print KT('/main.kt', data=locals(), this=THIS)
