<!DOCTYPE html>
<html>
<html lang="zh-CN">
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="chrome=1" />
    <title>$data.title - TrageWeb</title>
    <link rel="stylesheet" type="text/css" id="css" href="/$style" />
    <script type="text/javascript">$data.js
function hide_notify() {
    document.getElementById("notify").style.display = "none";
}
var button_clicked = false;
function robot_button()
{
     var button = document.getElementById('robot_button');
     if (button_clicked) {
          button.style.visibility = "hidden";
     } else {
          button.innerHTML = "请不要重复点击此按钮";
          button_clicked = true;
     }
}
    </script>
</head>
<body>
$notify
<div id="wrapper">
<h1>十一学校的小破评测系统 shiyihcc.com:1234</h1>
<p class="small"><a href="/">TrageWeb</a> » $data.nav<a href="/user/change_theme?ref=$this.url" style="float: right;">✿ 切换主题 ✿</a></p>
<hr />
$data.main
<hr />
<p class="xsmall"><a onclick="alert('别点我！有意思吗？')">♥</a> Proudly powered by <a href="http://code.google.com/p/trage/">TrageWeb</a>. Made in Beijing National Day School.<button id="robot_button" onclick="robot_button();" style="float: right;">他们有一个计划</button></p>
</div>
</body>
</html>
