SET_UNICODE_OUT("utf-8")

from trage.common.problem import get_io, get_std, get_usercode

def index():
    print "Chect 不利于身体健康。慎用。"

def input():
    print "<pre>%s</pre>" % get_io('input', THIS.args[0], THIS.args[1])

def output():
    print "<pre>%s</pre>" % get_io('output', THIS.args[0], THIS.args[1])

def std():
    prob_id = THIS.args[0]
    import cgi
    print '''<meta charset="UTF-8" />
    <script type="text/javascript" src="/sh.js"></script>
    <link type="text/css" rel="stylesheet" href="/sh_style.css">
    <body onload="sh_highlightDocument();">'''
    if get_std(prob_id)['c']:
        print '<h2>C 语言：</h2>'
        print '<pre class="sh_c">%s</pre>' % cgi.escape(get_std(prob_id)['c'])
    if get_std(prob_id)['cpp']:
        print '<h2>C++ 语言：</h2>'
        print '<pre class="sh_cpp">%s</pre>' % cgi.escape(get_std(prob_id)['cpp'])
    print '</body>'

def usercode():
    filename = THIS.args[0]
    import cgi
    print '''<meta charset="UTF-8" />
    <script type="text/javascript" src="/sh.js"></script>
    <link type="text/css" rel="stylesheet" href="/sh_style.css">
    <body onload="sh_highlightDocument();">'''
    print '<pre class="sh_c">%s</pre>' % cgi.escape(get_usercode(filename))
    print '</body>'
