session = Session()

def index():
    print 'I love you. Alloy.'

def login(username, password):
    if not username:
        session.notify = "请输入用户名"
        raise HTTP_REDIRECTION, "/"
    
    from trage.common.user import User
    user = User(username, password)
    if user.load():
        session.notify = "Login failed, wrong password."
        raise HTTP_REDIRECTION, "/"
    else:
        session.login = True
        session.username = username
        session.userid = user.get_id()
        session.realname = user.get_realname()

        session.notify = "Login Sucessful."
        raise HTTP_REDIRECTION, "/"

def change_password(username, password):
    from trage.common.user import User
    user = User(username, '我爸是陶陶')
    user.load()
    user.set_password(password)

    session.notify = "修改成功！"
    raise HTTP_REDIRECTION, "/"

def logout():
    session.login = None

    session.notify = "Logout sucessful."
    raise HTTP_REDIRECTION, "/"

def reg(username, realname, password):
    if not username or not realname:
        session.notify = "请输入用户名和姓名"
        raise HTTP_REDIRECTION, "/"

    from trage.common.user import add_user
    if add_user(username, realname, password):
        session.notify = "用户名重了，换个诡异点的吧～"
        raise HTTP_REDIRECTION, "/"
    login(username, password)

def change_theme(ref):
    if not hasattr(session, "style") or (hasattr(session, "style") and session.style == "cuteblue.css"):
        session.style = "eyecandy.css"
    else:
        session.style = "cuteblue.css"
    raise HTTP_REDIRECTION, ref
