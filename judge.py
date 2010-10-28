# -*- coding: UTF-8 -*-
SET_UNICODE_OUT("utf-8")
from trage.common.judge import Judge
from trage.common.problem import Problem
prob_id = _prob_id

html = {'judge_info': ''}
def judge():
    # upload file
    import os
    import shutil
    try:
        f = _source.file
    except AttributeError:
        html['judge_info'] += "Wait...! No source file selected...~"
        return
    tmp_name = os.tmpnam() + os.path.basename(_source.filename)
    out = open(tmp_name, 'wb')
    shutil.copyfileobj(f, out)
    out.close()

    judge = Judge(prob_id, tmp_name)
    load_err = judge.load()
    if load_err == 1:
        html['judge_info'] += '<p>Wrong problem id.</p>'
        return
    if load_err == 2:
        html['judge_info'] += '<p>Problem config file error, please report the bug to the developers.</p>'
        return

    html['judge_info'] += '<h3>Compile</h3>'
    compile_err = judge.compile()
    if compile_err:
        html['judge_info'] += '<p>Compile failed. Error: '
        html['judge_info'] += compile_err + '</p>'
        return
    html['judge_info'] += '<p>Compile Done.</p>'

    html['judge_info'] += '<h3>Judge</h3>'
    while True:
        tpoint_result = judge.judge()

        if tpoint_result == None:
            break

        if tpoint_result['error']:
            html['judge_info'] += '<p>Problem data file error.</p>'
            return

        str = '[ Test %2d ] [ %3s ]' % (tpoint_result['tpoint'], tpoint_result['status'])
        if tpoint_result['status'] in ['AC', 'WA']:
            str += ' [ Time: %.2fs/%.1fs ] [ Mem: %.2fM/%dM ]' % (tpoint_result['time'], tpoint_result['timelmt'], tpoint_result['mem'],  tpoint_result['memlmt'])
        html['judge_info'] += str + '<br />'

    result = judge.get_result()
    if result['AC'] == True:
        html['judge_info'] += '[ Result: %2d/%2d ] Accepted.<br />' % (result['tpoint_correct'], result['tpoint_count'])
    else:
        html['judge_info'] += '[ Result: %2d/%2d ] Not accepted.<br />' % (result['tpoint_correct'], result['tpoint_count'])

judge()

prob = Problem(prob_id)
prob.load()
html['title'] = u"正在评测 " + prob.get_title()
html['id'] = prob.get_id()
html['name'] = prob.get_name()
title = "Judging Problem[%s]: %s" % (prob.get_id(), prob.get_title())
nav = u'<a href="/problem/%s">Problem[%s]: %s</a> » Judge' % (prob.get_id(), prob.get_id(), prob.get_title())

main = u'''
<h2>%(title)s <sup>Problem[%(id)s]: %(name)s</sup></h2>
<hr />
%(judge_info)s
''' % html

print KT('/main.kt', data=locals(), this=THIS)
