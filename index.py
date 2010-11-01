# -*- coding: UTF-8 -*-
Include("/page_common.py")
from trage.common.problem import *
from trage.helpers import get_difficulty_text
from user import is_login

title = "Home"
nav = title

problist = get_problist()
problist_html = ""
for prob in problist:
    if login:
        AC = get_status(session.userid, prob['id'])
        if AC:
            accepted_text = '<span class="accepted"><abbr title="已经秒掉了！">☻</abbr></span>'
        else:
            accepted_text = '<span class="unaccepted"><abbr title="呃…还没 AC 呢，赶快做吧…">☺</abbr></span>'
    else:
        accepted_text = ''
    problist_html += '<li>[%s] %s <a href="problem/%s">%s</a></li>' % (get_difficulty_text(prob['difficulty']), accepted_text, prob['id'], prob['title'])

if login:
    user_html = '''<h2 class="float: left;">你好，%s。祝你好运！</h2>
<p><a href="/user/logout" style="margin-left: 14px;">登出</a> <a href="#" onclick="change_password();" style="margin-left: 14px;">修改密码</a></p>
<form action="/user/change_password" id="password_form" style="display: none;">
<p>
    <label for="username">新密码</label>
    <input name="username" type="hidden" value="%s" />
    <input class="input" id="password" name="password" type="password" />
</p>
<p>
    <button type="submit">修改</button>
</p>
</form>''' % (session.realname, session.username)
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
}
function change_password()
{
    document.getElementById("password_form").style.display = "block";
}'''

quotes = [
    '好好刷题，天天上树！',
    '磕学研究表明，适量刷题有益身体健康。',
    '人类一刷题，上帝就发笑。',
    '强哥说：“这是鼠标，这是电脑包。”',
    '据了解 AC 对增大幸福指数意义很大。',
    '不刷题的人是寂寞的。',
    '代码如诗。',
    '刷题无极限，黄轶唯最贱！',
    '为什么 RTE ? RP Too Extreme!',
    '强哥穿着黑衣服来上课：“我希望你们都成为黑马！”',
    '编译失败。源代码大喊：“我爸是陶陶！”',
    '人生没有后效性，DP 就是搞不定。',
    '做不出题怎么办？再做！',
    'NOI == Nothing of Informatics.',
    'NOIP == No OI Please!',
    'Trage + dy = Tragedy.',
    'Trage = Train + Judge.',
    '办证：15201187049',
    '黄河母亲，神力无限！',
    '刷题重地，闲人免进。',
    '不刷题的人是孤独的。孤独的人是可耻的。',
]
from random import randint
quote = quotes[randint(0, len(quotes) - 1)]

main = u'''<div class="warn align_left">
<p>欢迎使用 TrageWeb 。这是一个基于 Trage 评测系统的站点，目前处于测试阶段。<br />请反馈任何遇到的问题，谢谢。</p>
<p>目前题目不多，仅用来测试。未来将逐步添加。</p>
</div>
<hr />
<h2>Problem List</h2>
<ul>
    %s
</ul>
<hr />
<a name="login"></a>
%s
<hr />
<p class="align_right">%s</p>''' % (problist_html, user_html, quote)

print KT('/main.kt', data=locals(), notify=get_notify(), style=get_style(), this=THIS)
