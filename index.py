# -*- coding: UTF-8 -*-
SET_UNICODE_OUT("utf-8")
from trage.common.problem import *
from trage.helpers import get_difficulty_text

title = "Home"
nav = title

problist = get_problist()
problist_html = ""
for prob in problist:
    problist_html += '<li>[%s] <a href="problem/%s">%s</a></li>' % (get_difficulty_text(prob['difficulty']), prob['id'], prob['title'])

main = u'''<div class="warn align_left">
<p>欢迎使用 TrageWeb 。这是一个基于 Trage 评测系统的站点，目前处于测试阶段。<br />请反馈任何遇到的问题，谢谢。</p>
<p>目前尚缺用户登录等功能。</p>
</div>
<hr />
<h2>Problem List</h2>
<ul>
    %(problist)s
</ul>''' % {'problist': problist_html}

print KT('/main.kt', data=locals(), this=THIS)
