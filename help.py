# -*- coding: UTF-8 -*-
Include("/page_common.py")

title = "Help"
nav = title

main = u'''
<h2>帮助文档</h2>
<h3>反馈</h3>
<p>NDSOJ 目前还有许多地方需要完善。所以，在你遇到任何不爽的地方时，哪怕是一点点不完美，都请反馈给我们。反馈的方法是…直接说话～告诉柳东原或者告诉胡颖健都成。有什么问题，先看看下面的“Q&amp;A”，如果找不到答案就去问健健！</p>
<h3>评测机</h3>
<p>该评测系统采用了性能十分低下的国测机（全国复测评测机）进行评测，很接近竞赛实际评测环境。</p>
<h3>需注意</h3>
<ul>
    <li>换行符可能是“\\n”、“\\r\\n”或“\\r”。所以，做字符串题的时候，直接用 %s 读是最安全的。</li>
    <li>NDSOJ 允许使用 long long，但是 NOIP 是不能使用的。所以刷 NOIP 题的时候尽量不要用 long long。</li>
</ul>
<h3>标程</h3>
<p>如果觉得哪题你写得不错，又还没有标程，那么可以整理得规范些，加点注释，然后成为标程。<br />/* 交题的时候把程序命名为“我想成为标程.c”就行了 */</p>
<h3>我们的故事</h3>
<p>NDSOJ，Not Damn Smart Online Judge (aka Nation Day School Online Judge，北京市十一学校在线评测系统)。这个评测系统在二〇〇九年十一月十五日，NOIP 前夕诞生（看看<a href="http://www.shiyihcc.com/~xhacker/NDSOJ/" target="_blank">那时的雏形</a>）。还有几天就要复赛了，一个蛋疼的人却为之奉献了好几天的大好时光。然而…她一直是个只能看题不能评测的半残的破玩意儿。</p>
<p>接下来，NOIP 逝去，到了十二月，寒冷的天气令人缺少激情，NDSOJ 的开发停止了。将近一年时间，我把时间花在了 Trage 这个本地的评测系统上，她很好用。</p>
<p>二〇一〇年十月，将迎来又一届 NOIP。突然，想要重拾 NDSOJ。说干就干，准备期中考试的时间被挪用了。可喜的是，基于 Trage 和 Karrigell，NDSOJ 在被冷落了近一年后获得了新生。希望，她能为十一的信息学竞赛做出一些贡献。</p>
<h3>Q &amp; A</h3>

<p>Q：Trage…？<br />A：Treap = Tree + Heap. 于是，Train + Judge = Trage。后来发现…Tragedy 了……</p>
<p>Q：什么是 TLE、MLE、RTE、…？<br />A：<br />
&nbsp;&nbsp;&nbsp;&nbsp;* AC：通过。<br />
&nbsp;&nbsp;&nbsp;&nbsp;* WA：哇！答案错了。<br />
&nbsp;&nbsp;&nbsp;&nbsp;* TLE：太冷呃…时间超过限制。<br />
&nbsp;&nbsp;&nbsp;&nbsp;* MLE：妈勒…= = 内存超过限制。<br />
&nbsp;&nbsp;&nbsp;&nbsp;* RTE：RP Too Extreme...运行时错误。</p>
<p>Q：为什么 RTE？<br />A：因为你 RP Too Extreme，人品大爆发！下面是可能出现的错误：<br />
    &nbsp;&nbsp;&nbsp;&nbsp;* 除数为 0 或对 0 取余。<br />
    &nbsp;&nbsp;&nbsp;&nbsp;* 输入文件错误。<br />
    &nbsp;&nbsp;&nbsp;&nbsp;* 访问无效的内存（可能是下标越界、指针指向无效的内存区域等）。
</p>
<p>Q：这是什么？<br />A：“这是鼠标，这是电脑包。” ——马强</p>
<h3>Enjoy brushing!</h3>
'''

print KT('/main.kt', data=locals(), notify=get_notify(), style=get_style(), this=THIS)
