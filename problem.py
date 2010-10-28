# -*- coding: UTF-8 -*-
SET_UNICODE_OUT("utf-8")
from trage.common.problem import Problem
prob_source = 'user'
prob = Problem(THIS.args[0])
prob.load()

title = "Problem[%s]: %s" % (prob.get_id(), prob.get_title())
nav = title

main = u'''
<h2>%(title)s <sup>Problem[%(id)s]: %(name)s</sup></h2>
<hr />
<h3>题目描述</h3>
<p>%(info_main)s</p>
<h3>输入说明</h3>
<p>%(info_input)s</p>
<h3>输出说明</h3>
<p>%(info_output)s</p>
<h3>提交程序</h3>
<form action="/judge" enctype="multipart/form-data" method="post">
    <p>Should be <em>%(name)s.c</em>, <em>%(name)s.cpp</em> or <em>%(name)s.pas</em>.
    <p>Using <em>file</em> input/output (<em>%(name)s.in</em>, <em>%(name)s.out</em>).</p>
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
    'info_main': prob.get_info_main(),
    'info_input': prob.get_info_input(),
    'info_output': prob.get_info_output() }

print KT('/main.kt', data=locals(), this=THIS)
