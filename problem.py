# -*- coding: UTF-8 -*-
SET_UNICODE_OUT("utf-8")
from trage.common.problem import Problem
from trage.helpers import nl2br

prob = Problem(THIS.args[0])
prob.load()

title = "Problem[%s]: %s" % (prob.get_id(), prob.get_title())
nav = title

main = u'''
<h2>%(title)s</h2>
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
<form action="/judge" enctype="multipart/form-data" method="post">
    <p class="small">Should be <em>%(name)s.c</em>, <em>%(name)s.cpp</em> or <em>%(name)s.pas</em>.
    <br />Using <em>file</em> input/output (<em>%(name)s.in</em>, <em>%(name)s.out</em>).</p>
    <p>
        <input type="file" name="source" />
        <input type="hidden" name="prob_id" value="%(id)s" />
        <input type="submit" />
    </p>
</form>
''' % {
    'title': prob.get_title(),
    'id': prob.get_id(),
    'name': prob.get_name(),
    'info_main': nl2br(prob.get_info_main()),
    'info_input': nl2br(prob.get_info_input()),
    'info_output': nl2br(prob.get_info_output()),
    'example_input': nl2br(prob.get_example_input()),
    'example_output': nl2br(prob.get_example_output()),
    'info_hint': nl2br(prob.get_info_hint()) }

print KT('/main.kt', data=locals(), this=THIS)
