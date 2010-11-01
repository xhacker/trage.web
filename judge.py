# -*- coding: UTF-8 -*-
Include("/page_common.py")

from trage.common.judge import Judge
from trage.common.problem import Problem, update_status
from trage.helpers import nl2br

prob_id = _prob_id

# upload file
import os
import shutil
try:
    f = _source.file
except AttributeError:
    session.notify = "没选择源文件呢～"
    raise HTTP_REDIRECTION, "/problem/%s#submit" % prob_id
tmp_name = os.tmpnam() + os.path.basename(_source.filename)
out = open(tmp_name, 'wb')
shutil.copyfileobj(f, out)
out.close()

html = {'judge_info': ''}
AC = False
def judge():
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
        html['judge_info'] += '<p>Compile failed. Error:<br />'
        html['judge_info'] += nl2br(compile_err) + '</p>'
        return
    html['judge_info'] += '<p>Compile Done.</p>'

    html['judge_info'] += '<h3>Judge</h3>\n'
    html['judge_info'] += u'<table><tr><th>测试点</th><th>结果</th><th>时间</th><th>内存</th><th>偷看</th></tr>\n'
    while True:
        tpoint_result = judge.judge()
        if tpoint_result == None:
            break

        if tpoint_result['status'] in ['AC', 'WA']:
            time = '%.2fs / %.1fs' % (tpoint_result['time'], tpoint_result['timelmt'])
            mem = '%.2fM / %dM' % (tpoint_result['mem'],  tpoint_result['memlmt'])
        elif tpoint_result['status'] == 'TLE':
            time = '>%.1fs / %.1fs' % (tpoint_result['timelmt'], tpoint_result['timelmt'])
            mem = 'Unknown / %dM' % tpoint_result['memlmt']
        elif tpoint_result['status'] == 'MLE':
            time = '%.2fs / %.1fs' % (tpoint_result['time'], tpoint_result['timelmt'])
            mem = '>%dM / %dM' % (tpoint_result['memlmt'],  tpoint_result['memlmt'])
        else:
            time = 'Unknown / %.1fs' % tpoint_result['timelmt']
            mem = 'Unknown / %dM' % tpoint_result['memlmt']
        html['judge_info'] += u'''<tr><td>%(tp)d</td><td>%(status)s</td><td>%(time)s</td><td>%(mem)s</td>
        <td><a onclick="return confirm_cheat();" href="/cheat/input/%(prob_id)s/%(tp_real)d" target="_blank">输入</a> · <a onclick="return confirm_cheat();" href="/cheat/output/%(prob_id)s/%(tp_real)d" target="_blank">输出</a></td></tr>\n''' % {
            'tp': tpoint_result['tpoint'],
            'status': tpoint_result['status'],
            'time': time,
            'mem': mem,
            'prob_id': prob_id,
            'tp_real': tpoint_result['tpoint'] - 1 }

    result = judge.get_result()
    global AC
    if result['AC'] == True:
        AC = True
        html['judge_info'] += '<tr><th colspan="5">[ Result: %d / %d ] Accepted.</th></tr>\n' % (result['tpoint_correct'], result['tpoint_count'])
    else:
        html['judge_info'] += '<tr><th colspan="5">[ Result: %d / %d ] Not accepted.</th></tr>\n' % (result['tpoint_correct'], result['tpoint_count'])
    html['judge_info'] += '</table>\n'

judge()
update_status(session.userid, prob_id, AC)

prob = Problem(prob_id)
prob.load()
html['title'] = u"正在评测 " + prob.get_title()
html['id'] = prob.get_id()
html['name'] = prob.get_name()
title = "Judging Problem[%s]: %s" % (prob.get_id(), prob.get_title())
nav = u'<a href="/problem/%s">Problem[%s]: %s</a> » Judge' % (prob.get_id(), prob.get_id(), prob.get_title())
js = '''function confirm_cheat() {
    r = confirm("最好是自己先想想～你真的真的确定要偷看吗……");
    return r;
}'''

main = u'''
<h2>%(title)s</h2>
<hr />
%(judge_info)s
<p><a href="/problem/%(id)s" style="margin-left: 14px;">« 返回该题目</a><a href="/" style="margin-left: 14px;">« 返回首页</a></p>
''' % html

print KT('/main.kt', data=locals(), notify=get_notify(), style=get_style(), this=THIS)
