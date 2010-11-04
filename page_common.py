session = Session()
SET_UNICODE_OUT("utf-8")

login = hasattr(session, "login") and session.login
js = ''

def get_notify():
    if hasattr(session, "notify") and session.notify:
        notify = '<div class="notify"><p class="info" id="notify" onclick="hide_notify();">%s</p></div>' % session.notify
        session.notify = None
        return notify
    return ''

def get_style():
    if hasattr(session, "style"):
        return session.style
    return 'eyecandy.css'
