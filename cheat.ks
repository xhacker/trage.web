from trage.common.problem import get_io

def index():
    print "Chect 不利于身体健康。慎用。"

def input(prob_id, tp):
    print "<pre>%s</pre>" % get_io('input', prob_id, tp)

def output(prob_id, tp):
    print "<pre>%s</pre>" % get_io('output', prob_id, tp)

def source(prob_id, tp):
    print '^ ^'
