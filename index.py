# -*- coding: UTF-8 -*-
session = Session()
SET_UNICODE_OUT("utf-8")
from trage.common.problem import *
from trage.helpers import get_difficulty_text
from user import is_login

title = "Home"
nav = title

notify = ''
if hasattr(session, "notify") and session.notify:
    notify = '<div class="notify"><p class="info">%s</p></div>' % session.notify
    session.notify = None

problist = get_problist()
problist_html = ""
for prob in problist:
    problist_html += '<li>[%s] <a href="problem/%s">%s</a></li>' % (get_difficulty_text(prob['difficulty']), prob['id'], prob['title'])

if hasattr(session, "login") and session.login:
    user_html = '''<h2>你好，%s。祝你好运！</h2>
<p><a href="/user/logout">登出</a></p>''' % session.realname
else:
    user_html = '''<h2>登录或注册</h2>
<form action="/user/login" id="login">
<p>
    <label for="username">用户名</label>
    <input class="input" id="username" name="username" type="text" />
</p>
<p>
    <label for="password">密码</label>
    <input class="input" id="password" name="password" type="password" />
</p>
<p>
    <button type="submit">登录</button>
    <button type="button" onclick="reg();">我要注册</button>
</p>
</form>
<form action="/user/reg" id="reg" style="display: none;">
<p>
    <label for="username">用户名</label>
    <input class="input" id="username" name="username" type="text" />
</p>
<p>
    <label for="realname">姓名</label>
    <input class="input" id="realname" name="realname" type="text" />
</p>
<p>
    <label for="password">密码</label>
    <input class="input" id="password" name="password" type="password" />
</p>
<p>
    <button type="submit">注册</button>
    <button type="button" onclick="login();">我要登录</button>
</p>
</form>'''

js = '''function reg()
{
    document.getElementById("login").style.display = "none";
    document.getElementById("reg").style.display = "block";
}
function login()
{
    document.getElementById("login").style.display = "block";
    document.getElementById("reg").style.display = "none";
}'''

main = u'''<div class="warn align_left">
<p>欢迎使用 TrageWeb 。这是一个基于 Trage 评测系统的站点，目前处于测试阶段。<br />请反馈任何遇到的问题，谢谢。</p>
<p>目前尚缺用户登录等功能。</p>
</div>
<hr />
<h2>Problem List</h2>
<ul>
    %s
</ul>
<hr />
%s''' % (problist_html, user_html)

print KT('/main.kt', data=locals(), this=THIS)
