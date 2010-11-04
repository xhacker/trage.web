# -*- coding: UTF-8 -*-
Include("/page_common.py")
from trage.common.problem import *
from trage.helpers import nl2br

prob = Problem(THIS.args[0])
prob.load()

title = "Problem[%s]: %s" % (prob.get_id(), prob.get_title())
nav = title

if login:
    submit_html = '''<form action="/judge" enctype="multipart/form-data" method="post">
    <p class="small">Should be <em>*.c</em>, <em>*.cpp</em> or <em>*.pas</em>.
    <br />Using <em>file</em> input/output (<em>%(name)s.in</em>, <em>%(name)s.out</em>).</p>
    <p>
        <input type="file" name="source" />
        <input type="hidden" name="prob_id" value="%(id)s" />
        <input type="submit" value="提交" />
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

if get_std(prob.get_id())['c'] or get_std(prob.get_id())['cpp']:
    std_html = '能再想想就再想想吧。如果如果实在做不出来了，<a href="/peep/std/%s" target="_blank">点此偷看…</a>' % prob.get_id()
else:
    std_html = '此题暂无标程，没法偷看…<a href="http://www.google.com.hk/search?q=' + prob.get_title() + '+标程&sa=Google+%E6%90%9C%E7%B4%A2&prog=aff&client=pub-1037665964482161&hl=zh-CN&source=sdo_sb&sdo_rt=ChBKScsMAAfkWwpvwhqoq0kyEg5fX1JMX0RFRkFVTFRfXxoIW1Pqd8JmonQoAVjV0vz7p7mFrogB" target="_blank">点此到网上搜搜</a>。'

hint = ''
if prob.get_info_hint():
    hint = '''<h3>提示</h3>
<p>%s</p>''' % nl2br(prob.get_info_hint())

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
%(hint)s
<h3>提交程序</h3>
<a name="submit"></a>
%(submit)s
<h3>偷看程序</h3>
<p>%(std)s</p>
''' % {
    'emotion': ac_emotion,
    'title': prob.get_title(),
    'info_main': nl2br(prob.get_info_main()),
    'info_input': nl2br(prob.get_info_input()),
    'info_output': nl2br(prob.get_info_output()),
    'example_input': nl2br(prob.get_example_input()),
    'example_output': nl2br(prob.get_example_output()),
    'hint': hint,
    'submit': submit_html,
    'std': std_html }

print KT('/main.kt', data=locals(), notify=get_notify(), style=get_style(), this=THIS)
