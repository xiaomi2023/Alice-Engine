##  简介

Alice Engine（v0.1）是一个文字游戏引擎，旨在让游戏开发者简便地开发属于自己的文字游戏。引擎使用python语言开发，操作简单，新手可轻松上手。

## 使用方式

在进行开发前，请确认是否已经安装好了引擎所需的python库（tkinter、queue）。
将上述三个文件部署于同一目录，就可以在同一目录下于脚本文件“script.as”中进行游戏脚本编写。
Alice Engine引擎运行的基本单位是节点（Point)，节点分属着各自的选项（Choice），选项再链接到各自的节点。
当游戏开始时，游戏画面会显示此时的节点文本，下面会列出一系列选项。当玩家点击一个选项后，游戏会跳转到选项所对应的节点。
引擎使用如下的语法定义一个节点：

`{节点文本...`
`#选项一...`
`#选项二...`
`#...`
`}`

其中，换行和缩进是可选的，合适的换行和缩进可以让脚本文件更具可读性。
而选项的语法为：

`\#选项名
{对应的节点...
}`

转义字符是如同“$a”、“$n”等的字符串，用以替代一些字符，从而能被编译器正常编译。编译后，它们将被转换为其原本的字符。
如果你的游戏文本中含有“{”、“}”和“#”等脚本语言的保留字符，请用转义字符替代它们，以免被脚本文件编译器错误编译。
此外，如果你的游戏文本中含有空格键、换行符等，我们同样推荐你使用转义字符替代它们，从而降低脚本文件编译器出现错误的概率。
现有的转义字符如下：
`$n->换行符
$s->空格
$t->制表符（“\t”）
$p->井号
$l->左大括号
$r->右大括号
$b->回车（“\r”）
$k->斜杠（“/”）`

你可以在脚本的节点添加python代码，当游戏来到一节点时，其相应的代码会被执行。
python代码用一对“@”括起来，下面为调用示例：
`@a = 3@`
在python代码调用中，你可以定义和调用变量，还可以调用部分python内置函数（注意：为了游戏运行的安全性和稳定性，部分python内置函数将被屏蔽从而避免被调用）
此外，你还可以通过使用`@api.func()@`格式调用引擎提供的接口库api，来调用引擎的接口函数。
目前共有两个接口函数：echo(text)的功能和python内置函数print类似，其将接受一个字符串参数，并在控制台打印出来；而create_gui()函数则会创建并返回一个新的GUI对象。

你还可以在脚本中添加注释，以提高代码的可读性和可维护性。
注释以`/*`开始，以`*/`结束。
以下是一个示例注释：
`/*这是一段注释*/`

最后，不要忘记在脚本文件的开头加上游戏名。
设置游戏名的格式为：

`游戏名&`

示例脚本文件运行后，效果如下：
![d2ViXzMwMDFfNzU4MTg5OV8wXzE3Mzg3Nzg4NTYyNTBfNDNlNjBjYzg](https://github.com/user-attachments/assets/a84f1a88-648a-453a-8b80-2fad4ac434df)
点击“选项一”后，会显示：
![d2ViXzMwMDFfNzU4MTg5OV8wXzE3Mzg3Nzg4OTMwMzJfNjEzOTA2YjU](https://github.com/user-attachments/assets/c1cc9519-00e8-4e44-acb0-48ae9c8d4fe5)
