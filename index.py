# -*- coding: UTF-8 -*-
Include("/page_common.py")
from trage.common.problem import *
from trage.common.user import User, get_code_list
from trage.helpers import get_difficulty_text

title = "Home"
nav = title

problist = get_problist()
problist_html = ""
count = 0
for prob in problist:
    if count == int((len(problist) + 1) / 2):
        problist_html += '</ul><ul class="col2">'
    if login:
        AC = get_status(session.userid, prob['id'])
        if AC:
            accepted_text = '<span class="accepted"><abbr title="已经秒掉了！">☻</abbr></span>'
        else:
            accepted_text = '<span class="unaccepted"><abbr title="呃…还没 AC 呢，赶快做吧…">☺</abbr></span>'
    else:
        accepted_text = ''
    problist_html += '<li>[%s] %s <a href="/problem/%s">%s</a></li>' % (get_difficulty_text(prob['difficulty']), accepted_text, prob['id'], prob['title'])
    count += 1

if login:
    user = User(session.username, '我爸是陶陶')
    user.load()
    accept_text = ''
    if user.get_accept_count():
		accept_text = "恭喜你，通过 %s 题了，通过率 %s%%。" % (user.get_accept_count(), user.get_accept_rate())
    user_html = '''<h2 class="float: left;">你好，%s。祝你好运！</h2>
<p><a href="/user/logout" style="margin-left: 14px;">登出</a> <a href="#login" onclick="change_password(); return false;" style="margin-left: 14px;">修改密码</a><span style="margin-left: 14px;">%s</span></p>
<form action="/user/change_password" id="password_form" style="display: none;">
<p>
    <label for="username">新密码</label>
    <input name="username" type="hidden" value="%s" />
    <input class="input" id="password" name="password" type="password" />
</p>
<p>
    <button type="submit">修改</button>
</p>
</form>''' % (session.realname, accept_text, session.username)
    code_list = get_code_list(session.userid)
    code_html = ""
    count = 0
    for code in code_list:
        if count == int((len(code_list) + 1) / 2):
            code_html += '</ul><ul class="xsmall col2">'
        prob = Problem(code['prob_id'])
        prob.load()
        from time import localtime, strftime
        ftime = strftime("%m月%d日 %H:%M", localtime(code['time']))
        code_html += '<li><a href="/peep/usercode/%s" target="_blank">[%s] %s</a></li>' % (code['filename'], ftime, prob.get_title())
        count += 1
    user_html += '<h3>通过的代码备份</h3><ul class="xsmall col1">%s</ul>' % code_html
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

js = '''function reg() {
    document.getElementById("login").style.display = "none";
    document.getElementById("reg").style.display = "block";
}
function login() {
    document.getElementById("login").style.display = "block";
    document.getElementById("reg").style.display = "none";
}
function change_password() {
    if (document.getElementById("password_form").style.display == "none") {
        document.getElementById("password_form").style.display = "block";
        document.getElementById("password").focus();
    } else {
        document.getElementById("password_form").style.display = "none";
    }
}
'''

if REQUEST.has_key("focuslogin"):
    js += '''function focus_on_login()
{
    document.getElementById("username").focus();
}
if (document.all) {
	// IE
	window.attachEvent('onload', focus_on_login);
} else {
	// Firefox, etc.
	window.addEventListener('load', focus_on_login, false);
}'''

quotes = [
    '好好刷题，天天上树！',
    '磕学研究表明，适量刷题有益身体健康。',
    '人类一刷题，上帝就发笑。',
    '强哥说：“这是鼠标，这是电脑包。”',
    '据了解 AC 对增大幸福指数意义很大。',
    '不刷题的人是寂寞的。',
    '代码如诗。',
    '''<span onclick='var soundEmbed = null;
function play(filename) {
	stop();
	soundEmbed = document.createElement("embed");
	soundEmbed.setAttribute("src", filename);
	soundEmbed.setAttribute("hidden", true);
	soundEmbed.setAttribute("autostart", true);
	document.body.appendChild(soundEmbed);
}
function stop() {
	if ( soundEmbed ) {
		document.body.removeChild(soundEmbed);
		soundEmbed = null;
	}
}
play("brush.ogg");'>刷题无极限，黄轶唯最贱！</span>''',
    '为什么 RTE ? RP Too Extreme! 人品大爆发！',
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
    '自从用了“long long”之后，一切都不同了。。。<br />/* 友情提示：NOIP 今年可以用 long long */',
    '你再背一遍 maxlongint？记着，2147483647。',
    '没有什么坎是迈不过去的，没有什么坑是阴不到人的。',
    'Brush question without limit, Huang Yiwei most foolish.',
    'KMP ==  Kill My Patience',
    'while not inOrder(deck) do<br />shuffle(deck);',
    '无限猴子定理告诉我们：不要乱拍键盘！！',
]
musics = [
    '2080205',
    '2086590',
    '2080203',
    '2052167',
    '2052166',
    '2116177',
    '2103609',
    '2080202',
    '2080205',
    '2070741',
    '393543',
    '2052921',
    '2085229',
    '3566565',
]
from random import randint
quote = quotes[randint(0, len(quotes) - 1)]
music = musics[randint(0, len(musics) - 1)]

main = u'''<div class="warn align_left">
<p>欢迎使用 NDSOJ，十一信息学非官方训练系统。使用前请查看<a href="/help">帮助文档</a>。</p>
<p>关于十一 OI 人物系列，有几个是仅仅改了剧情的换汤不换药之作…如有雷同，不是巧合。</p>
<p>还有不到两天了，大家都加油。</p>
<p>另：<a href="http://172.17.17.17" target="_blank">这里</a>有一些资料，大家可以看看。欢迎查看最新 <a href="http://172.17.17.17/Conquer%%20NOIP.pdf" target="_blank">NOIP 攻略</a>。</p>
</div>
<hr />
<h2>Problem List</h2>
<ul class="col1">
    %s
</ul>
<hr />
<a name="login"></a>
%s
<hr />
<div><p style="float: left;"><embed src="http://www.xiami.com/widget/803973_%s/singlePlayer.swf" type="application/x-shockwave-flash" width="257" height="33" wmode="transparent"></embed></p><p class="align_right" style="float: right;">%s</p></div>''' % (problist_html, user_html, music, quote)

print KT('/main.kt', data=locals(), notify=get_notify(), style=get_style(), this=THIS)
