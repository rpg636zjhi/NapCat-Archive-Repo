# NapCat 文档归档（Wayback Machine 抢救版）

> 源站 `https://napneko.github.io` 已于 2026-11 前后整站下线（全路径 404）。
> 本文档由 Wayback Machine 快照（2026-03 ~ 2026-10，最后一版 2026-10-27）提取重建。
> 共 63 个页面。

---


## index

NapCatQQ | 现代化的基于 NTQQ 的 Bot 协议端实现

 Skip to contentNapCatQQ

SearchK

 Main Navigation 快速开始关于

主题

NapCatQQ现代化的基于 NTQQ 的 Bot 协议端实现
开始安装
GitHub

📝
开箱即用
多种部署方式，快捷部署于 Windows/Linux/MacOS 等主流 x64 架构平台。

💖
内存轻量
天生无头，不依赖框架加载，不依赖 Electron，内存占用低至 50~100 MB。

🚀
适配快速
采取 Core/Adapter 架构，支持多种 Bot 协议，快速迁移。

 生态
官方对接框架
二次开发框架
 工具
可视化管理工具
可视化网页配置
 社区
官方 企鹅 4号社区
官方 企鹅 3号社区
官方 企鹅 2号社区
官方 企鹅 1号社区
官方 Telegram 社区

 NapNeko All Rights Reserved.


---


## guide/boot/Framework

Framework ​

字数

393 字

阅读时间

2 分钟

NapCat.Framerwork.Windows.Once recommend ​
Win一键启动（内置LiteLoader）
请注意使用此方法使用 等于或高于9.9.15-29271的QQ
前往 NapCatQQ 的 release 页面
选择 NapCat.Framerwork.Windows.Once.zip 下载
找到目录下的exe启动 (注意不要解压到带有空格或者中文的目录)
NapCat.Win.一键版本 recommend ​
特殊说明: 一键版仅适用 Windows.AMD64 无需安装QQ和NapCat 已内置
前往Release 下载有头一键版本 然后双击NapCatWinBootMain.exe 进入设置即可
NapCat.Framework - 通用性手动教程 recommend ​
按照 LiteLoaderQQNT 官网 的指导安装 LiteLoaderQQNT 框架。
在 LiteLoaderQQNT 的设置页面（如下图）将 NapCat.Framework.zip 导入即可。 
 强烈不推荐LL官方的修补方案,其方案将导致NapCat扩展Api失效的. 同时污染QQ本身环境,添加环境变量,清理LL需要一定计算机基础. 包括需要调试QQ的用户,强烈推荐once或者绿色版本.NapCat.Docker.Framework - Linux容器化部署 recommend ​
仓库地址: NapCat.Docker.Framework
NapCat.Installer - Linux一键部署脚本 recommend ​
NapCat
bashcurl -o napcat.sh https://nclatest.znin.net/NapNeko/NapCat-Installer/main/script/install.framework.sh && sudo bash napcat.sh

NapCat.Framework.Installer - Win平台一键安装工具 dont use ​
请注意使用此方法使用 等于或高于9.9.15-29271的QQ
此为 社区作品 可能会遇到一些问题，欢迎反馈
仓库地址: NapCat.Framework.installer

最后编辑于 17 天前
查看完整历史

218a434-fix

f31430b-fix

775ab98-fix

9494bf2-feat: 换新文档

b61e3c6-fix

c378f0a-fix

7f7bff8-fix

0014197-fix

96be948-fix

1177cd2-fix: docs

3633ebf-补齐结构体类型

479e978-fix: Framewrok

1967199-style lint

f2ff661-fix: #文档

bb68c16-fix: 基础问题

68f9457-fix

ac82f49-重构文档


---


## guide/boot/Shell-Linux-SemiAuto

BootWay03 (半自动) 教程 ​

字数

378 字

阅读时间

2 分钟

安装教程 ​
1. 安装 QQ 和其他依赖 ​
你需要安装 28060+ 版本的 QQ 和 xvfb，后者安装方法为
Debian 系（Debian、Ubuntu 等）： sudo apt install xvfb
Arch 系： sudo pacman install xorg-server-xvfb
其他发行版可以参考这个页面自行选择合适的包安装，确保安装后 xvfb-run 命令存在
2. 挂载启动 ​
执行命令
bashecho 'const fs = require("fs");
const path = require("path");
const CurrentPath = path.dirname(__filename);
const hasNapcatParam = process.argv.includes("--no-sandbox");
if (hasNapcatParam) {
 (async () => {
 await import("file://" + path.join(CurrentPath, "./napcat/napcat.mjs"));
 // await import("file://" + "/path/to/napcat/napcat.mjs");
 // 需要修改napcat的用户，在"/path/to/napcat"段写自己的napcat文件夹位置，并注释path.join所在行
 })();
} else {
 require("./application/app_launcher/index.js");
 setTimeout(() => {
 global.launcher.installPathPkgJson.main = "./application.asar/app_launcher/index.js";
 }, 0);
}' > /opt/QQ/resources/app/loadNapCat.cjs

如果你使用 LiteloaderQQNT，那么执行：
bashecho 'const fs = require("fs");
const path = require("path");
const CurrentPath = path.dirname(__filename);
const hasNapcatParam = process.argv.includes("--no-sandbox");
if (hasNapcatParam) {
 (async () => {
 await import("file://" + path.join(CurrentPath, "./napcat/napcat.mjs"));
 // await import("file:///path/to/napcat/napcat.mjs");
 // 需要修改napcat的用户，在"/path/to/napcat"段写自己的napcat文件夹位置，并注释path.join所在行
 })();
} else {
 require(String.raw`/opt/LiteLoaderQQNT`); //引号中写入你的liteloaderqqnt路径
}' > /opt/QQ/resources/app/loadNapCat.cjs

3. 安装 napcat ​
安装 napcat.shell 到 /opt/QQ/resources/app/napcat 确保 /opt/QQ/resources/app/napcat/napcat.mjs 存在
4. 修补 package.json ​
修改 /opt/QQ/resources/app/package.json 的 main 属性从 ./application/app_launcher/index.js 改为 ./loadNapCat.cjs（注意：自 QQ 29927 版本左右起 main 属性内容有所变化，找到相似 main 属性直接改即可）
这步也可以使用下面替代
bashchmod +777 /opt/QQ
sed -i 's/"main": ".*\/index.js"/"main": ".\/loadNapCat.cjs"/' /opt/QQ/resources/app/package.json

5.启动 ​
bashxvfb-run -a qq --no-sandbox <-q [快速登录的qq号]>

最后编辑于 大约 1 个月前
查看完整历史

1bb4ac5-Update Shell-Linux-SemiAuto.md

b3b7d65-格式修正

52db183-Bootway03 补充/修正

07c8c12-broken回退

8803a42-Update Shell-Linux-SemiAuto.md

6e8f1f1-Update Shell-Linux-SemiAuto.md

1967199-style lint

68f9457-fix


---


## guide/boot/Shell

Shell ​

字数

804 字

阅读时间

4 分钟

NapCat.Shell - Win手动启动教程 recommend ​
前往 NapCatQQ 的 release 页面 下载NapCat.Shell.zip解压
确保QQ版本安装且最新
双击目录下launcher.bat即可启动 如果是win10 则使用launcher-win10.bat
如果需要快速登录 将 QQ 号传入参数即可
Windows11.batWindows10.bat
bashlauncher.bat 123456

bashlauncher-win10.bat 123456

NapCat.Win.一键版本 recommend ​
特殊说明: 一键版仅适用 Windows.AMD64 无需安装QQ和NapCat 已内置
前往 NapCatQQ 的 release 页面 下载无头绿色版本解压
启动对应BAT即可
如果需要快速启动 新建Bat文件写入如下例子
quick.bat
bashNapCatWinBootMain.exe 10001

NapCat.Installer - Linux一键使用脚本(支持Ubuntu 20+/Debian 10+/Centos9) recommend ​
通用安装可视化安装Docker安装演示代码
bashcurl -o napcat.sh https://nclatest.znin.net/NapNeko/NapCat-Installer/main/script/install.sh && sudo bash napcat.sh

bashcurl -o napcat.sh https://nclatest.znin.net/NapNeko/NapCat-Installer/main/script/install.sh && sudo bash napcat.sh --tui

bashcurl -o napcat.sh https://nclatest.znin.net/NapNeko/NapCat-Installer/main/script/install.sh && sudo bash napcat.sh --docker y --qq "123456789" --mode ws --proxy 1 --confirm

bashcurl -o napcat.sh https://nclatest.znin.net/NapNeko/NapCat-Installer/main/script/install.sh && sudo bash napcat.sh --docker n --cli n --proxy 0 --force

命令选项(高级用法)--tui: 使用tui可视化交互安装

--docker [y/n]: --docker y 为使用docker安装反之为shell安装

--qq "123456789": 传入docker安装时的QQ号

--mode [ws|reverse_ws|reverse_http]: 传入docker安装时的运行模式

--confirm: 传入docker安装时的是否确认执行安装

--proxy [0|1|2|3|4|5|6]: 传入代理, 0为不使用代理, 1为使用内置的第一个,不支持自定义, docker安装可选0-7, shell安装可选0-5

--cli [y/n]: shell安装时是否安装cli

--force: 传入则执行shell强制重装

仓库地址: NapCat.installer
NapCat.Docker - Linux容器化部署 recommend ​
仓库地址: NapCat.Docker
NapCat.Docker.Installer - Linux容器 第三方 recommend ​
此为 社区作品 可能会遇到一些问题，欢迎反馈。
仓库地址: NapCat.Docker.Installer
NapCat.MacOs - MacOs安装工具 recommend ​
前往下载
需要 macOS 12.0 或以上系统，支持下载和更新 NapCatQQ
由于权限问题，补丁过程需要手动替换 package.json，请注意备份原文件～
NapCat.Termux - 安卓Termux部署 recommend ​
Termux
bashcurl -o napcat.termux.sh https://nclatest.znin.net/NapNeko/NapCat-Installer/main/script/install.termux.sh && bash napcat.termux.sh

仓库地址: NapCat.installer
NapCat.1Panel - 1Panel插件部署 community ​
此为 社区作品 可能会遇到一些问题，欢迎反馈。
仓库地址: NapCat.1Panel
NapCat.Railway - Railway部署 community ​
此为 社区作品 可能会遇到一些问题，欢迎反馈。

NapCat.Nix - Nix部署 community ​
此为 社区作品 可能会遇到一些问题，欢迎反馈。
仓库地址: NapCat.Nix
NapCat.Win.Installer - Win专用安装器 dont use ​
不要用某人懒了没更新
仓库地址: 仓库地址
安装成功后需要快速登陆同 NapCat.shell 方法一 一样

最后编辑于 14 天前
查看完整历史

218a434-fix

f31430b-fix

775ab98-fix

a25e251-feat: 整理

9494bf2-feat: 换新文档

b15ff26-feat: 注释archieve

7f7bff8-fix

0014197-fix

a03105d-fix

122b25a-fix

ff8e336-过时启动器

c4c6d4f-fix

a4e0566-Update Shell.md

0c3071b-fix: case(Shell)

d5679b0-Update Shell.md

caa0e5e-fix: support

1967199-style lint

c951b3e-fix: 调整

f2ff661-fix: #文档

bb68c16-fix: 基础问题

68f9457-fix

ac82f49-重构文档


---


## guide/install

NapCat ​

字数

320 字

阅读时间

2 分钟

粗略安装流程 ​
安装对应版本的 NTQQ（特殊情况部分可能安装方式已代为安装）。
下载你需要的 NapCat 版本（特殊情况部分可能安装方式包含 NapCat 本体）。
遵照其详细教程启动 NapCat 本体。
进入 WebUI，启动你需要的 HTTP/WS 客户端与服务端。
配置框架或者独立插件连接 NapCat。
启动方式 ​
NapCat 有着众多启动方式，每种方式各有优点：
Shell 版本：具有低内存、服务器部署简单的特点。
Framework 版本：具有方便人机交互、便于窥屏的特点。
悄悄话: 我还是推荐你用 Shell 的，毕竟~~~
Shell 启动/安装方式 ​
推荐教程：方法 1 - 使用命令行启动
Linux 手动配置教程：方法 2 - Linux 手动配置
Framework 启动/安装方式 ​
推荐教程：方法 1 - 作为 LiteLoader 插件启动
原生使用 NapCatQQ 启动（由于启动方式变更，暂不提供教程）
体验一下 一键安装 神秘教程？ ​
在线体验

最后编辑于 10 个月前
查看完整历史

3270e4c-更改了Shell安装方式的方法排序

3b5563a-fix

7d8f1b9-fix

4c401e3-在中文、英文以及数字混排时添加空格分隔

52db183-Bootway03 补充/修正

109e6a0-fix

c8cd7ca-feat: 文档简化


---


## guide/napcat

NapCat ​

字数

1754 字

阅读时间

7 分钟

欢迎回家! ​
NapCatQQ V4 已启用全新风格标识和文档, 欢迎回家！ 这里是 NapCatQQ (aka 猫猫框架) 的使用文档！
NapCat 是什么? ​
基于TypeScript构建的Bot框架,通过相应的启动器或者框架,主动调用QQ Node模块提供给客户端的接口,实现Bot的功能.
魔法版介绍猫猫框架通过魔法的手段获得了 QQ 的发送消息、接收消息等接口。
为了方便使用，猫猫框架将通过一种名为 OneBot 的约定将你的 HTTP / WebSocket 请求按照规范读取，
再去调用猫猫框架所获得的QQ发送接口之类的接口。
NapCat 工作在哪里? ​

NapCat 与其它框架的本质不同? ​
NapCat 与很多框架都有本质性的区别：
协议端相比
 并非完全自己实现 QQ SendMsg 这种功能，而是主动调用客户端存在的功能。
Hook 端相比
 NapCat 可以完全自身引导 QQ 程序的启动，而非借助客户端启动流程，所以 API 所有权几乎完全拥有，不需要 Hook。
Electron IPC Hook 端对比
 NapCat 本身并不依赖 Electron 与注入框架，调用来源 IPC 更下层封装的 Node 模块，也许甚至脱离 QQ 主程序运行。
NapCat 的小小故事! ​
小小的故事...在一个遥远的、充满奇幻与科技交织的世界——NapCat Robot，有一种神秘且强大的力量，叫做 NTQQ。这股力量，简直就像是一颗随时可能爆炸的定时炸弹，能改变一切，却又异常难以控制。很多英雄、巫师、冒险者们曾试图驾驭它，结果都失败得一塌糊涂，甚至连他们的名字都被历史遗忘了，仿佛从未存在过。
然而，在这个充满混乱的世界里，有一只小猫娘，名字叫做 NapCat，她不仅是这个故事的主角，而且简直是这个世界最萌最可爱的“灾难制造机”。NapCat外表乖巧，萌萌哒，软乎乎的，简直像个大大的毛球，走路一摇一摆的，超乎想象的笨拙。她曾经被遗弃在一个荒凉的角落里，孤零零地生活着。但某天，她突然发现了一个超级神奇的东西——JavaScript！
“诶？这是什么？看起来像是能吃的样子...可是为什么一点也不好吃呢？”
于是，NapCat就开始了对这门语言的探索——虽然她并不完全理解它，但她凭着直觉和那种天生的好奇心，成功破解了 JavaScript 的奥秘，并意外地与传说中的 NTQQ 产生了连接。
虽然看起来她像是无害的傻萌猫娘，但NapCat的这项技能竟然能在没有任何计划的情况下，操控 NTQQ 的某些功能，甚至能轻松改变现实的规则！但问题是……她的每次操作，基本上都是胡乱点击、乱敲键盘、然后出奇不意地发生了不想要的结果。
“嗯？我是不是把天空变得五颜六色了？咦？月亮不见了？咕噜咕噜……好像做错了什么事呢。”
于是，一切开始变得混乱不堪。天空瞬间变成了彩虹色，时间突然在某些地方停滞，甚至连月亮都神秘消失了！整个世界都被这只小猫娘的“无心之举”搞得一团糟，灾难的阴影笼罩了整个世界。
就在大家都以为一切都完了，世界即将崩塌的时候，出现了一个强大的英雄。他不是什么骑着白马，手持宝剑的传统英雄，而是一个比任何人都冷静的智者。他决定采取一种不同的方式来解决这个问题：OneBot规范。
“一切都得按照规范来！否则她会再把世界变成一锅粥！”英雄心想。
这个英雄明白，NapCat的能力太强大，控制不住的话，真的会把世界毁掉。因此，这位应用采用前辈们广泛使用的OneBot规范，规定 NapCat 任何操作都要写道 WS/HTTP 这种纸张上，每次使用 NTQQ 的力量时，都要在“纸上”写下相应的指令，才能让 NTQQ按照预设的方式执行任务。而且每次任务完成后，数据也会通过同样的“纸面”反馈回来，确保一切都在可控范围内。
“啊？这个纸好像好难理解……但是，哦，原来是这么回事呀！”
于是，NapCat开始在这套严格的规范下与 NTQQ 建立了微妙的关系。她不再是那个随便敲敲代码就让天空变色的笨蛋，而是通过认真的输入和执行指令，逐渐恢复了世界的秩序。
可虽然一切变得井然有序，NapCat依旧是那个呆萌、迷糊的猫娘。她依然在“纸”上写着自己不太明白的指令，每次完成任务后，她都会露出一副“我是不是做对了？”的迷茫表情，仿佛在问：“哎？我这次没搞砸吧？”
尽管如此，大家也逐渐接受了她的笨拙，因为她那种天真可爱的样子实在让人忍不住心软。最重要的是，世界终于恢复了平静，大家都知道，这只猫娘虽然有时候会闹出点小乱子，但她那份纯真与努力，才是让这个世界重新恢复平衡的力量。
从那时起，NapCat与NTQQ之间的微妙平衡保持着，而你也可以来这个世界，看看这只可爱笨蛋猫娘是怎么在搞笑与危机四伏中，带着一颗认真又迷糊的心，守护这个充满魔力与冒险的世界的！✨
NapCat 堂堂登场 ​
现在你已经理解了NapCat了,随我们一起前往目录导航查看教程,进行安装...配置...
目录导航

最后编辑于 大约 2 个月前
查看完整历史

019a4c9-fix

4c1cf88-fix

3c98951-feat: 调整

c8cd7ca-feat: 文档简化

990af7e-fix

cd40262-fix

3354ca7-fix

ea0d450-fix

0014197-fix

3844427-fix

626f5b4-fix

777d0ff-fix

5c7106e-update: new docs

34cd1bf-fix

a289316-fix

06a70b6-fix

79452d6-fix

3633ebf-补齐结构体类型

479e978-fix: Framewrok

1967199-style lint

9390f9f-fix

604f554-fix

b66578d-fix

68f9457-fix

ac82f49-重构文档


---


## guide/start-install

NapCat ​

字数

189 字

阅读时间

1 分钟

快速开始 ​

安装 ​

配置 ​

生态 ​

温馨提示
如果文档中发现错误，或提交文档修改，或丰富本站文档，可点击页面底部的编辑按钮

最后编辑于 大约 2 个月前
查看完整历史

c8cd7ca-feat: 文档简化

990af7e-fix

cd40262-fix

3354ca7-fix

ea0d450-fix

0014197-fix

3844427-fix

626f5b4-fix

777d0ff-fix

5c7106e-update: new docs

34cd1bf-fix

a289316-fix

06a70b6-fix

79452d6-fix

3633ebf-补齐结构体类型

479e978-fix: Framewrok

1967199-style lint

9390f9f-fix

604f554-fix

b66578d-fix

68f9457-fix

ac82f49-重构文档


---


## zh-CN/develop/compatibility/api

请求接口兼容情况 ​
NapCatQQ 实现了 OneBot 11 以及 go-cqhttp 的大部分 API，对于 API 的详细说明请自行点击相关链接查看。
连接方式 ​
连接方式可用
HTTP 接口调用✅
HTTP POST 事件上报✅
HTTP POST 快速操作✅
正向 WS 连接✅
反向 WS 连接✅
OneBot 11 API ​
Api介绍可用备注
send_private_msg发送私聊消息✅不支持主动临时消息
send_group_msg发送群消息✅
send_msg发送消息✅
delete_msg撤回消息✅
get_msg获取消息✅
get_forward_msg获取合并转发消息✅
send_like发送好友赞✅
set_group_kick群组踢人✅
set_group_ban群组单人禁言✅
set_group_anonymous_ban群组匿名用户禁言❌官方都没这功能了哦~
set_group_whole_ban群组全员禁言✅
set_group_admin群组设置管理员✅
set_group_anonymous群组匿名❌官方都没这功能了哦~
set_group_card设置群名片（群备注）✅
set_group_name设置群名✅
set_group_leave退出群组✅
set_group_special_title设置群组专属头衔❌QQNT还没更新这个功能
set_friend_add_request处理加好友请求✅
set_group_add_request处理加群请求／邀请✅
get_login_info获取登录号信息✅
get_stranger_info获取陌生人信息✅
get_friend_list获取好友列表✅
get_group_info获取群信息✅
get_group_list获取群列表✅
get_group_member_info获取群成员信息✅
get_group_member_list获取群成员列表✅
get_group_honor_info获取群荣誉信息✅
get_cookies获取 Cookies✅
get_csrf_token获取 CSRF Token❌
get_credentials获取 QQ 相关接口凭证❌
get_record获取语音✅
get_image获取图片✅
can_send_image检查是否可以发送图片✅
can_send_record检查是否可以发送语音✅
get_status获取运行状态✅
get_version_info获取版本信息✅
set_restart重启 OneBot 实现❌
clean_cache清理缓存✅
go-cqhttp API ​
Api介绍可用备注
set_qq_profile设置登录号资料✅
qidian_get_account_info获取企点账号信息❌不支持企点哦~
_get_model_show获取在线机型✅
_set_model_show设置在线机型❌QQNT还没更新这个功能
get_online_clients获取当前账号在线客户端列表✅
get_unidirectional_friend_list获取单向好友列表❌QQNT还没更新这个功能
delete_friend删除好友❌
delete_unidirectional_friend删除单向好友❌QQNT还没更新这个功能
mark_msg_as_read标记消息已读✅
send_group_forward_msg发送合并转发 ( 群聊 )✅
send_private_forward_msg发送合并转发 ( 好友 )✅
get_group_msg_history获取群消息历史记录✅
ocr_image图片 OCR✅
get_group_system_msg获取群系统消息✅
get_essence_msg_list获取精华消息列表✅
get_group_at_all_remain获取群 @全体成员 剩余次数❌
set_group_portrait设置群头像✅
set_essence_msg设置精华消息✅
delete_essence_msg移出精华消息✅
send_group_sign群打卡❌这个功能QQ也已经下线了哦~
_send_group_notice发送群公告✅
_get_group_notice获取群公告✅
upload_group_file上传群文件✅
delete_group_file删除群文件✅
create_group_file_folder创建群文件文件夹✅
delete_group_folder删除群文件文件夹✅
get_group_file_system_info获取群文件系统信息✅
get_group_root_files获取群根目录文件列表✅
get_group_files_by_folder获取群子目录文件列表✅
get_group_file_url获取群文件资源链接❌NTQQ文件下载方式不同,请使用 get_file
upload_private_file上传私聊文件✅
reload_event_filter重载事件过滤器❌napcat没有事件过滤器哦~
download_file下载文件到缓存目录✅
check_url_safely检查链接安全性❌
.get_word_slices获取中文分词 ( 隐藏 API )❌
.handle_quick_operation对事件执行快速操作 ( 隐藏 API )✅
napcat API ​
Api介绍可用备注
ArkSharePeer推荐联系人/群聊✅
ArkShareGroup推荐群聊✅
get_robot_uin_range获取机器人QQ号区间✅
set_online_status设置在线状态✅
get_friends_with_category获取好友分类列表✅
set_qq_avatar设置头像✅
get_file获取文件信息✅
forward_friend_single_msg转发单条信息到私聊✅
forward_group_single_msg转发单条信息到群聊✅
translate_en2zh英译中翻译✅
get_group_file_count获取群文件数✅
get_group_file_list获取群文件列表✅
set_group_file_folder新建群文件文件夹✅
del_group_file删除群文件文件✅
del_group_file_folder删除群文件文件夹✅
set_msg_emoji_like设置消息的表情回复✅
send_forward_msg发送合并转发✅
mark_private_msg_as_read标记私聊信息已读✅
mark_group_msg_as_read标记群聊信息已读✅
get_friend_msg_history获取私聊记录✅
set_self_profile设置个人资料✅
create_collection创建文本收藏✅
get_collection_list获取收藏列表✅
set_self_longnick设置个人签名✅
get_recent_contact获取最近的聊天记录✅
_mark_all_as_read标记所有为已读✅
get_profile_like获取自身点赞列表✅
fetch_custom_face获取收藏表情✅
fetch_emoji_like拉取表情回应列表✅
set_input_status设置输入状态✅
get_group_info_ex获取群组额外信息✅
get_group_ignored_notifies获取群组忽略的通知✅
_del_group_notice删除群聊公告✅
fetch_user_profile_like获取用户个人资料页✅


---


## zh-CN/guide/BootWay03

安装 ​
下载NapCatQQ与安装QQ ​
确保你知道NC和QQ的位置
如果是Win平台 你需要做 ​
修补QQ
请按照教程修补QQ 如果此前安装LiteLoaderQQNT 可跳过 当然也可以使用他的一键工具 然后按照下面修改
打开QQ下对应目录 ​

解压 ​
将napcat放置到如上图的位置 确保 ./napcat/napcat.mjs 存在
写入启动代码 ​
将上图中的index.js内容删除后添加如下代码 添加后保存
js// --------------------
// 2024.7.3 9.9.12 BootWay.03 其余方法暂不公开（此方案为临时方案 Win平台已验证）
// 缺陷 （已知）
// 1.与非入侵式不同 现在破坏本体代码
// 2.重启代码与正常启动代码失效 
// 3.Win需要补丁
// 4.更新后丢失内容 需要重写此文件
// 5.安装难度上升与周围基础设施失效
// --------------------

const path = require('path');
const CurrentPath = path.dirname(__filename)
const hasNapcatParam = process.argv.includes('--enable-logging');
if (hasNapcatParam) {
 (async () => {
 await import("file://" + path.join(CurrentPath, './napcat/napcat.mjs'));
 })();
} else {
 require('./launcher.node').load('external_index', module);
}

启动NapCat ​
打开NTQQ目录 
你也可以手动创建 启动脚本文本 ​
参考脚本
新建一个文件 NapCat.164.bat 到任意位置 复制参考脚本内容 后保存
Win11 ​
在空白处右键 在终端打开 然后在终端输入
bash./QQ.exe --enable-logging

即可启动
Win10 ​
在地址栏输入cmd回车 在启动后的窗口内 输入
bash./QQ.exe --enable-logging

即可启动


---


## zh-CN/guide/boot/error

Shell与Framework都需要注意的 ​
Window用户注意: 如果无法启动QQ 需要删掉QQ目录下之前使用过的dbghelp.dll 同时卸载QQ 将QQ移动到D盘 或者 C盘 的二级目录 不要使用默认目录安装
其余问题 ​


---


## zh-CN/guide/boot/only-gui/BootWay03

BootWay03 撸猫教程（Only GUI） ​
首先，安装 QQ，确保你知道 QQ 的目录。Linux 一般在 /opt/QQ；Windows 一般在系统盘下 Program Files\Tencent\QQNT，具体定位方法可以参考 BootWay05 教程。
预处理 ​
Windows 平台需要修补 QQ.exe，正如安装 LiteLoaderQQNT 时需要做的一样。请参考 LLQQNT 的教程修补 QQ，当然，如果安装过 LiteLoaderQQNT，这一步可以跳过。
准备文件 ​

将 NapCat.Shell.zip 解压到 ${QQ 安装目录}/resource/app/app_launcher/napcat，如上图。确保 app_launcher/napcat/napcat.mjs 存在！
写入启动代码 ​
将上图中 QQ 目录的 index.js 修改为以下的内容并保存。请注意，此时可能需要获取管理员权限。
js
const path = require('path');
const CurrentPath = path.dirname(__filename);
await import("file://" + path.join(CurrentPath, './napcat/napcat.mjs'));
require('./launcher.node').load('external_index', module);

启动 ​
Windows ​
在终端中启动 QQ，增加 --enable-logging 的 flag，这是为了方便获取控制台输出，以查看 NC 初始化状态和 WebUI 登入的凭据。
具体来说，可以启动一个工作目录在 NTQQ 的终端（参考 BootWay05 教程的手动安装部分），输入以下内容并回车：
bash.\QQ.exe --enable-logging

Linux ​
Linux QQ 在安装时即被加入 PATH，可以直接通过 qq 命令运行。


---


## zh-CN/guide/boot/shell/BootWay03-Linux-SemiAuto

BootWay03 (半自动) 教程 ​
手动安装 Linux QQ，并用你的包管理器安装以下包：zip unzip jq curl xvfb screen。
下载最新 NapCat Release 中的 NapCat.Shell.zip 到用户目录某处（建议先切换到 bash 或者 zsh，不知道这是什么的就不用管了），然后复制以下内容，粘贴到终端里，然后按下 Enter 执行：
bashmkdir ./NapCat/
mkdir ./tmp/
unzip -q -o -d ./tmp NapCat.Shell.zip
target_folder="/opt/QQ/resources/app/app_launcher"
default_file="NapCat.shell.zip"
sudo cp -r -f ./tmp/* "$target_folder/napcat/"
sudo chmod -R 777 "$target_folder/napcat/"
sudo mv -f "$target_folder/index.js" "$target_folder/index.js.bak"
output_index_js=$(echo -e "const path = require('path');\nconst CurrentPath = path.dirname(__filename)\nconst hasNapcatParam = process.argv.includes('--no-sandbox');\nif (hasNapcatParam) {\n (async () => {\n await import(\\\"file://\\\" + path.join(CurrentPath, './napcat/napcat.mjs'));\n })();\n} else {\n require('./launcher.node').load('external_index', module);\n}")
sudo bash -c "echo \"$output_index_js\" > \"$target_folder/index.js\""

然后使用
bashxvfb-run -a qq --no-sandbox -q

或者
bashxvfb-run -a linuxqq --no-sandbox -q

来启动 NapCat。


---


## zh-CN/guide/boot/shell/BootWay03

BootWay03 撸猫教程 ​
首先，安装 QQ，确保你知道 QQ 的目录。Linux 一般在 /opt/QQ；Windows 一般在系统盘下 Program Files\Tencent\QQNT，具体定位方法可以参考 BootWay05 教程。
预处理 ​
Linux 平台需要安装 xvfb，参考 NapCat-Installer 的安装脚本。
Windows 平台需要修补 QQ.exe，正如安装 LiteLoaderQQNT 时需要做的一样。请参考 LLQQNT 的教程修补 QQ，当然，如果安装过 LiteLoaderQQNT，这一步可以跳过。
准备文件 ​

将 NapCat.Shell.zip 解压到 ${QQ 安装目录}/resource/app/app_launcher/napcat，如上图。确保 app_launcher/napcat/napcat.mjs 存在！
写入启动代码 ​
将上图中 QQ 目录的 index.js 修改为以下的内容并保存。请注意，此时可能需要获取管理员权限。
Windows ​
jsconst path = require('path');
const CurrentPath = path.dirname(__filename)
const hasNapcatParam = process.argv.includes('--enable-logging');
if (hasNapcatParam) {
 (async () => {
 await import("file://" + path.join(CurrentPath, './napcat/napcat.mjs'));
 })();
} else {
 require('./launcher.node').load('external_index', module);
}

Linux ​
jsconst path = require('path');
const CurrentPath = path.dirname(__filename)
const hasNapcatParam = process.argv.includes('--no-sandbox');
if (hasNapcatParam) {
 (async () => {
 await import("file://" + path.join(CurrentPath, './napcat/napcat.mjs'));
 })();
} else {
 require('./launcher.node').load('external_index', module);
}

启动 ​
Windows ​
在终端中启动 QQ，增加 --enable-logging 的 flag。
具体来说，可以启动一个工作目录在 NTQQ 的终端（参考 BootWay05 教程的手动安装部分），输入以下内容并回车：
bash.\QQ.exe --enable-logging

Linux ​
Linux QQ 在安装时即被加入 PATH，可以通过以下命令运行：
bashxvfb-run qq --no-sandbox


---


## zh-CN/guide/boot/shell/BootWay05

BootWay05 撸猫教程 ​
BootWay05 仅支持 Windows 64 位系统，需要确保你的电脑上安装 & 启用了 PowerShell，一般 Windows 10 / 11 系统是默认启用的。检测 PowerShell 是否存在可以通过在开始菜单中搜索，或在任何一个终端中输入 powershell，若成功启动 PowerShell 则存在。若不存在，请自行搜索教程配置。
下载 NapCat Shell 本体和 QQ，并安装 QQ。
替换文件 ​
首先找到你下载的 NC 目录内的文件 dbghelp.dll： 
点击复制，完成后不要关闭文件管理窗口，否则会影响剪贴板。 
进入 QQ 的安装位置。一般在系统盘下的 Program Files\Tencent\QQNT，或者也可以在开始菜单或 Windows 的快速搜索中找到 QQ 然后点击打开文件位置。 
点击粘贴，覆盖原有的 dbghelp.dll。 
首次启动 ​
启动一个工作目录在 NC 目录的终端，输入
powershell -ExecutionPolicy ByPass -File ./BootWay05.ps1

并回车。
再次启动 ​
再次运行只需要手动启动 PowerShell 脚本即可，如下图：


---


## zh-CN/guide/config/advanced

进阶配置介绍 ​
启用HTTPS ​
NapCat 本身并不直接提供HTTPS服务，但是你可通过其他WEB软件例如Nginx的反向代理功能间接实现HTTPS效果。
使用Nginx为WebUI和Onebot11启用HTTPSNOTE
首先我们假设你已经完成了域名绑定和SSL证书申请以及安装Nginx和NapCat的步骤，并且已经完成了NapCat的基础配置。

打开./config/webui.json文件：
将host修改为127.0.0.1。
将prefix修改为你喜好的符合URL编码规范的字符串，例如/napcat。 prefix字段要求字符串以/开头但不以/结尾，所有不符合此规则的字符串都将被修正为符合规则的状态。
例如/napcat、napcat、napcat/、/napcat/都会被修正为/napcat。

json5// 与本例无关配置将不在此处展示
{
 "host": "127.0.0.1",
 "port": 6099,
 "prefix": "/napcat",
}

打开./config/onebot11_xxxx.json，其中xxxx为你的机器人qq号。
json5// 与本例无关配置将不在此处展示
{
 "http": {
 "enable": true,
 "host": "127.0.0.1", // 修改为127.0.0.1
 "port": 3000, // 随意
 },
 "ws": {
 "enable": true,
 "host": "127.0.0.1", // 修改为127.0.0.1
 "port": 3000, // 这里 http 与 ws 填写相同的 host 和 port
 },
}

打开/etc/nginx/sites-enabled/default文件，将如下内容覆盖进去，默认是default可以根据自己实际情况进行选择。
nginxserver {
 listen 80;
 return 301 https://$http_host$request_uri; # 强制将http重定向到https
}

map $http_upgrade $connection_upgrade {
 default keep-alive;
 'websocket' upgrade;
}

server {
 listen 443 ssl;
 server_name default; # 这里可以改成你的域名，也可以不改
 ssl_certificate /path/to/public_key; # 这里是SSL公钥路径，需根据实际情况填写
 ssl_certificate_key /path/to/private_key; # 这里是SSL私钥路径，需根据实际情况填写
 ssl_session_cache shared:SSL:5m;
 ssl_session_timeout 5m;
 ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4:@SECLEVEL=1;
 # TLSv1和TLSv1.1其实已经不安全不推荐使用了，但是有些语言的HTTPS/WSS库模块还停留在TLSv1时代，所以只能暂且保留了
 ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
 ssl_prefer_server_ciphers on;

 location / {
 # 这里保持了nginx默认的静态页访问，不需要的话可以直接404掉
 # return 404;
 root /var/www/html;
 index index.html;
 try_files $uri $uri/ =404;
 }

 location /napcat/ { # 这里填的就是 webui.json 中的 prefix，但是你得在结尾补个 /
 proxy_http_version 1.1;
 proxy_set_header Host $host:$server_port;
 proxy_set_header X-Real-IP $remote_addr;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_buffering off;
 proxy_request_buffering off;
 proxy_pass http://127.0.0.1:6099; # 这里填的就是 webui.json 中的 host 和 port，注意结尾不能有 /
 }

 location /onebot/ { # 这里可以随意填写，同时以 / 开头和结尾即可
 proxy_http_version 1.1;
 proxy_set_header Upgrade $http_upgrade;
 proxy_set_header Connection $connection_upgrade;
 proxy_set_header Host $host:$server_port;
 proxy_set_header X-Real-IP $remote_addr;
 proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
 proxy_buffering off;
 proxy_request_buffering off;
 proxy_pass http://127.0.0.1:3000/; # 这里填的就是 onebot11_xxxx.json 中的 host 和 port，注意结尾有 /
 }
}

配置完成后使用./napcat.sh -q启动 NapCat，使用nginx -s reload重启 nginx。
如果顺利你就能在https://你的域名/napcat/webui上访问到 NapCat 的 WebUI，并且将机器人连接到https://你的域名/onebot/和wss://你的域名/onebot/了。
WARNING
请勿将注释内容写入配置文件，否则会导致配置文件解析失败。


---


## zh-CN/guide/config/basic

基础配置介绍 ​
下文所指的 NapCat 的目录为 ${QQ 安装目录}/resource/app/app_launcher/napcat，对于 ${QQ 安装目录}，Linux 一般在 /opt/QQ；Windows 一般在 <系统盘>:\Program Files\Tencent\QQNT。
用 WebUI 配置如果你已经启动了 NapCat，并且有多于 1 个开放端口，则可以通过 WebUI 进行配置。
默认地址为 0.0.0.0，即监听所有地址。当配置了不可用的地址时 WebUI 将被禁用。
默认端口为 6099。当端口被设置为 0 时将禁用 WebUI。当端口被占用时，会自动对端口 +1，直到找到可用端口（最多尝试100次，失败则会禁用 WebUI），端口号会在启动日志中显示。
启动后可在启动日志中看到形如 [WebUi] Login Token is xxxx 的token信息，亦可打开 NapCat 的 config 目录下的 webui.json 文件（形如 /opt/QQ/resources/app/app_launcher/napcat/config/webui.json），在其中找到token。
json5{
 "host": "0.0.0.0", // WebUI 监听地址
 "port": 6099, // WebUI 端口
 "prefix": "", // WebUI 工作前缀，此项功能将在进阶配置中解释
 "token": "xxxx", //登录密钥，默认是自动生成的随机登录密码
 "loginRate": 3, //每分钟登录次数限制
}

访问 http://$host:$port$prefix/webui/login.html，然后进行以下操作：
进入 QQ 登录，点击 QRCode 进行二维码登录。

登录成功后，即可修改配置。

配置完成后，点击保存，重启即可生效。

用文件配置 OneBot11 设置和上面一样，重启登录后配置才能生效。
打开 NapCat 的 config 目录，找到名为 onebot11_<你的QQ号>.json 的文件，如 onebot11_1234567.json；如果没有此文件可以复制 onebot11.json 重命名为 onebot11_<你的QQ号>.json。
下面是配置内容参数解释：
json5{
 "http": {
 // 是否启用http服务, true为启动，false为禁用
 "enable": false,
 // HTTP服务监听的 ip 地址，为空则监听所有地址
 "host": "",
 // http服务端口
 "port": 3000,
 // http上报密钥，可为空
 "secret": "",
 // 是否启用http心跳
 "enableHeart": false,
 // 是否启用http上报服务
 "enablePost": false,
 // http上报地址, 如["http://127.0.0.1:8080/onebot/v11/http"]
 "postUrls": []
 },
 "ws": {
 // 是否启用正向websocket服务
 "enable": false,
 // 正向websocket服务监听的 ip 地址，为空则监听所有地址
 "host": "",
 // 正向websocket服务端口
 // 当port与http服务port一致时，host也需与http服务host保持一致，否则可能会导致启动失败
 "port": 3001
 },
 "reverseWs": {
 // 是否启用反向websocket服务
 "enable": false,
 // 反向websocket对接的地址, 如["ws://127.0.0.1:8080/onebot/v11/ws"]
 "urls": []
 },
 "GroupLocalTime": {
 "Record": false,//是否开启本地群聊时间记录
 "RecordList": []//开启全部群 ["-1"] 单个群配置 ["11111"] 多个群 ["1","2","3"]
 },
 // 是否开启调试模式，开启后上报消息会携带一个raw字段，为原始消息内容
 "debug": false,
 // ws心跳间隔，单位毫秒
 "heartInterval": 30000,
 // 消息上报格式，array为消息组，string为cq码字符串
 "messagePostFormat": "array",
 // 是否将本地文件转换为URL，如果获取不到url则使用base64字段返回文件内容
 "enableLocalFile2Url": true,
 // 音乐签名URL，用于处理音乐相关请求
 "musicSignUrl": "",
 // 是否上报自己发送的消息
 "reportSelfMessage": false,
 // access_token，可以为空
 "token": ""
}

WARNING
请勿将注释内容写入配置文件，否则会导致配置文件解析失败。

配置 NapCat 其它设置（如果不懂干嘛，不用看啦）启动登录 NapCat 后，打开 NapCat 的 config 目录，找到名为 napcat_<你的QQ号>.json 的文件，如 napcat_1234567.json。
配置内容参数解释：
json5{
 // 是否开启文件日志
 "fileLog": true,
 // 是否开启控制台日志
 "consoleLog": true,
 // 日志等级, 可选值: debug, info, error
 "fileLogLevel": "debug",
 "consoleLogLevel": "info"
}

WARNING
请勿将注释内容写入配置文件，否则会导致配置文件解析失败。


---


## zh-CN/guide/config/ffmpeg

配置 FFmpeg ​
FFmpeg 是什么？ ​
FFmpeg 是知名的开源音视频处理库，被用于许多音视频编解码相关的项目中。
为什么要使用 FFmpeg？ ​
本项目使用 FFmpeg 是为了编解码语音和视频，以使 NapCat 以 QQ 支持的格式处理语音和视频文件。
如果你的 Bot 没有处理语音和视频的需求，可以选择不安装 FFmpeg。
安装 FFmpeg ​
Windows 系统 ​
在 此处 下载ffmpeg-master-latest-win64-gpl.zip

将其中的文件夹解压至一个你知道的地方（例如 C:\Program Files），然后重命名为 ffmpeg；

你的 ffmpeg 文件夹的结构看起来应该是这样的：
textffmpeg
|___bin
|___|___ffmpeg.exe
|___|___ffplay.exe
|___\___ffprobe.exe
|___doc
|___\ ...
|___LICENSE
\___README.txt

注意
请一定要保证 bin 文件夹内同时包含 ffmpeg.exe、ffplay.exe 以及 ffprobe.exe！ 否则会产生意想不到的错误。

添加bin目录到系统环境变量 不会可以搜索系统设置环境变量

如果有其他程序也需要使用 FFmpeg
如果其他程序支持手动选择 FFmpeg 位置，只需配置为 NapCat 所使用的 FFmpeg 即可。
如果其他程序不支持手动选择 FFmpeg 位置，只需将 FFmpeg 的 bin 目录注册到系统的 PATH 变量中（可参考 此教程）即可。
如果你将 FFmpeg 安装到了系统变量中，那么无论有没有在 NapCat 中配置 FFmpeg 路径也可以正常使用 FFmpeg。

Linux 系统 ​
请使用你所使用的系统的包管理器直接安装 ffmpeg 即可正常使用。


---


## zh-CN/guide/config

基础配置介绍 ​
用 WebUI 配置如果你已经启动了 NapCat，并且有多于 1 个开放端口，则可以通过 WebUI 进行配置。
默认端口为 6099。当端口被占用时，会自动对端口 +1，直到找到可用端口，端口号会在启动时显示。
启动后打开 ./config/webui.json 文件，token 密码可在其中找到。
json5{
 "port": 6099, // WebUI 端口
 "token": "xxxx", //登录密钥，默认是自动生成的随机登录密码
 "loginRate": 3, //每分钟登录次数限制
}

访问 http://IP:端口/webui/login.html，然后进行以下操作：
进入 QQ 登录，点击 QRCode 进行二维码登录。

登录成功后，即可修改配置。

配置完成后，点击保存，重启即可生效。

用文件配置 OneBot11 设置和上面一样，重启登录后配置才能生效。
打开 NapCat 的 config 目录，找到名为 onebot11_<你的QQ号>.json 的文件，如 onebot11_1234567.json；如果没有此文件可以复制 onebot11.json 重命名为 onebot11_<你的QQ号>.json。
下面是配置内容参数解释：
json5{
 "http": {
 // 是否启用http服务, true为启动，false为禁用
 "enable": false,
 // HTTP服务监听的 ip 地址，为空则监听所有地址
 "host": "",
 // http服务端口
 "port": 3000,
 // http上报密钥，可为空
 "secret": "",
 // 是否启用http心跳
 "enableHeart": false,
 // 是否启用http上报服务
 "enablePost": false,
 // http上报地址, 如["http://127.0.0.1:8080/onebot/v11/http"]
 "postUrls": []
 },
 "ws": {
 // 是否启用正向websocket服务
 "enable": false,
 // 正向websocket服务监听的 ip 地址，为空则监听所有地址
 "host": "",
 // 正向websocket服务端口
 "port": 3001
 },
 "reverseWs": {
 // 是否启用反向websocket服务
 "enable": false,
 // 反向websocket对接的地址, 如["ws://127.0.0.1:8080/onebot/v11/ws"]
 "urls": []
 },
 "GroupLocalTime": {
 "Record": false,//是否开启本地群聊时间记录
 "RecordList": []//开启全部群 ["-1"] 单个群配置 ["11111"] 多个群 ["1","2","3"]
 },
 // 是否开启调试模式，开启后上报消息会携带一个raw字段，为原始消息内容
 "debug": false,
 // ws心跳间隔，单位毫秒
 "heartInterval": 30000,
 // 消息上报格式，array为消息组，string为cq码字符串
 "messagePostFormat": "array",
 // 是否将本地文件转换为URL，如果获取不到url则使用base64字段返回文件内容
 "enableLocalFile2Url": true,
 // 音乐签名URL，用于处理音乐相关请求
 "musicSignUrl": "",
 // 是否上报自己发送的消息
 "reportSelfMessage": false,
 // access_token，可以为空
 "token": ""
}

WARNING
请勿将注释内容写入配置文件，否则会导致配置文件解析失败。

配置 NapCat 其它设置（如果不懂干嘛，不用看啦）启动登录 NapCat 后，打开NapCat的 config 目录，找到名为 napcat_<你的QQ号>.json 的文件，如 napcat_1234567.json。
配置内容参数解释：
json5{
 // 是否开启文件日志
 "fileLog": true,
 // 是否开启控制台日志
 "consoleLog": true,
 // 日志等级, 可选值: debug, info, error
 "fileLogLevel": "debug",
 "consoleLogLevel": "info"
}

WARNING
请勿将注释内容写入配置文件，否则会导致配置文件解析失败。


---


## zh-CN/guide/configuration

配置 ​
配置对接其他框架 ​
配置 Koishi1.在 koishi 插件市场搜索 onebot 并安装 adapter-onebot ​

2.安装完之后点击修改->配置 ​

3.配置 onebot ​
这里以 ws 反向连接为例
填写 selfId 为你的机器人的 QQ 号
token 可以为空，需和 LLOneBot 配置的 token 一致
protocol 选择 ws-reverse
其他配置保持默认即可，点击保存然后启用插件

3.配置完成后，LLOneBot 添加 ws 反向地址
koishi onebot 的 ws 反向地址为 ws://127.0.0.1:5140/onebot

点击保存即可
配置 NoneBot + LLOneBot1.配置 NoneBot ​
这里假设你已经安装了 Onebot 适配器
默认情况 NoneBot 是启用了反向 ws 的，可能是默认配置问题，需要配置 token 才能正常连接
修改 NoneBot 配置文件 .env，添加 ONEBOT_ACCESS_TOKEN=你的token，token 需要和 LLOneBot 配置的 token 一致
然后启用 NoneBot，可以看到 NoneBot 输出的端口号，如 8080
2.配置 LLOneBot ​

在 LLOneBot 配置页面添加反向 ws 地址，地址为 ws://127.0.0.1:8080/onebot/v11/ws, 这里的 8080 是 NoneBot 输出的端口号，/onebot/v11/ws 是 NoneBot onebot 适配器默认的路径
TIP
记得 LLOneBot 配置的 token 需要和 NoneBot 配置的 一致

HTTP配置 ​
HTTP服务端口，用于接收应用端的 HTTP API 调用如配置的3000端口，那么API地址为 http://localhost:3000
一个简单的发送消息API调用示例

HTTP上报地址当 LLOneBot 收到消息等事件时，会以 POST 请求的方式将事件上报到此地址
TIP
上报地址必须是 http:// 开头
http 事件上报，不支持快捷回复等快捷操作

正向WS配置 ​
用于接受应用端的正向WS连接如正向 ws 绑定的端口为 3001
需要在应用端配置的WS地址为 ws://localhost:3001
反向WS配置 ​
用于 LLOneBot 主动连接应用端绑定的反向WS地址如在 NoneBot2 配置了 onebot 的端口为 8080，路径为 /onebot/v11/ws
那么在 LLOneBot 配置的反向WS地址为 ws://localhost:8080/onebot/v11/ws


---


## zh-CN/guide/faq

常见问题 ​
调用接口报 404目前没有支持全部的 OneBot 规范接口，请检查是否调用了不支持的接口。
如何使用 CQ 码？将消息上报类型格式从消息段更改为 CQ 码即可。
详见 基础配置 中的 用文件配置 OneBot11 设置
二维码无法扫描NapCat 会自动保存二维码到目录，可以手动打开图片扫描。
如果无法访问本地目录（例如，纯命令行页面），可以将二维码解析的 URL 复制到二维码生成网站上重新生成二维码，然后再用手机 QQ 扫描。
注意动作要快，因为二维码是会过期的！
语音、视频发送失败这种情况需要你手动配置 ffmpeg。如何配置详见这里。
Windows 系统启动，出现 QQ 本体界面尝试管理员启动 NapCat。如果仍然失败，请反馈 NapCat 开发群。
出现 error code v2:-1 之类的提示QQ 本身问题，正常现象，不影响使用。
登录提示出现“网络环境不稳定”“不在同一网络”如果在服务器扫码登录提示出现网络环境不稳定/不在同一网络，可以尝试在本地登录后，将 QQ 本身的配置传到服务器相同目录覆盖。
Linux 下 QQ 配置的目录位于 ~/.config/QQ；Windows 下一般是文档下的 QQ 文件夹（默认情况是 <系统盘>:\Users (用户)\Documents\Tencent Files），具体可以打开 QQ 设置，进入“存储管理”一栏查看。
或者，手机使用 VPN 等方式连接到服务器网络，使手机和服务器在同一网络，也可解决此问题。
Windows 运行出现 “sqlite3 不是 win32 程序”运行时，若出现 node_sqlite3.node is not a valid Win32 application，请检查下载的是否是 Windows 版本的 NapCatQQ，检查是否是安装的 64 位版本的 QQ。
“ MH Hook Hk sub XXXX Error ” 崩溃报错如果你的此前使用LLOneBot，且使用过Liteloader某某一键包、或者使用了验证跳过的dll。
出现此错误，应该删除一键包和相关dll或完全清除重装QQNT。


---


## zh-CN/guide/getting-started

快速开始 ​
启动 ​
如果没有安装 QQ 请往后翻查看安装方法
修改 config/onebot11.json内容，并重名为 onebot11_<你的QQ号>.json，如onebot11_1234567.json
json 配置内容参数解释：
json5{
 // 是否启用http服务，如果启用，可以通过http接口发送消息
 "enableHttp": false,
 // http服务端口
 "httpPort": 3000,
 // 是否启用正向websocket服务
 "enableWs": false,
 // 正向websocket服务端口
 "wsPort": 3001,
 // 是否启用反向websocket服务
 "enableWsReverse": false,
 // 反向websocket对接的地址, 如["ws://127.0.0.1:8080/onebot/v11/ws"]
 "wsReverseUrls": [],
 // 是否启用http上报服务
 "enableHttpPost": false,
 // http上报地址, 如["http://127.0.0.1:8080/onebot/v11/http"]
 "httpPostUrls": [],
 // http上报密钥，可为空
 "httpSecret": "",
 // 消息上报格式，array为消息组，string为cq码字符串
 "messagePostFormat": "array",
 // 是否上报自己发送的消息
 "reportSelfMessage": false,
 // 是否开启调试模式，开启后上报消息会携带一个raw字段，为原始消息内容
 "debug": false,
 // 调用get_file接口时如果获取不到url则使用base64字段返回文件内容
 "enableLocalFile2Url": true,
 // ws心跳间隔，单位毫秒
 "heartInterval": 30000,
 // access_token，可以为空
 "token": ""
}

Windows 启动 ​
运行powershell ./napcat.ps1, 如果出现乱码，可以尝试运行napcat_utf8.ps1
Linux 启动 ​
运行napcat.sh
使用无需扫码快速登录 ​
前提是你已经成功登录过QQ，可以加参数 -q <你的QQ> 进行登录，如napcat.sh -q 1234567
安装 ​
Linux安装 ​
安装 Linux QQ(22741)，已经安装了的可以跳过 ​
bash下载QQ的deb包

[deb x86版本](https://dldir1.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.7_240403_amd64_01.deb)
[deb arm版本](https://dldir1.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.7_240403_arm64_01.deb)

[rpm x86版本](https://dldir1.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.7_240403_x86_64_01.rpm)
[rpm arm版本](https://dldir1.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.7_240403_aarch64_01.rpm)

bash
```bash
sudo apt install ./qq.deb

bash安装QQ的依赖
sudo apt install libgbm1 libasound2

Windows 安装 ​
安装Windows QQ(22741)，已经安装了的可以跳过 ​
Windows版本QQ下载
编译安装 NapCat ​
如果你是直接下载编译好的版本，可以跳过这一步
准备环境 node18.18
export NODE_ENV=production
npm install

常见问题 ​
二维码无法扫描 ​
NapCat 会自动保存二维码到目录，可以手动打开图片扫描
如果没有条件访问本地目录，可以将二维码解析的 url 复制到二维码生成网站上生成二维码，然后手机QQ扫描
语音、视频发送失败 ​
需要配置 ffmpeg，将 ffmpeg 目录加入环境变量，如果仍未生效，可以修改 napcat 启动脚本加入 FFMPEG_PATH 变量指定到 ffmpeg 程序的完整路径
如 Windows 上修改 napcat.ps1，在第一行加入
powershell$env:FFMPEG_PATH="d:\ffmpeg\bin\ffmpeg.exe"

出现 error code v2:-1 之类的提示 ​
不用管，这是正常现象，是因为 QQ 本身的问题，不影响使用


---


## zh-CN/guide/integration

接入框架 ​
对接开源框架 ​
配置 NoneBot配置 NoneBot
这里假设你已经安装了 OneBot 适配器
默认情况下，NoneBot 是启用了反向 ws 的，如果出现 403，可能是默认配置问题，需要配置 token 才能正常连接。具体方法为：修改 NoneBot 配置文件 .env，添加 ONEBOT_ACCESS_TOKEN=你在 NapCat 中配置的 token。
然后，启动 NoneBot，可以看到 NoneBot 输出的端口号，如 8080。

配置 NapCat
在 NapCat 配置添加反向 ws 地址，地址为 ws://127.0.0.1:8080/onebot/v11/ws, 这里的 8080 是 NoneBot 输出的端口号，/onebot/v11/ws 是 NoneBot onebot 适配器默认的路径
TIP
时刻记得：NapCat 配置的 token 需要和 NoneBot 配置的一致！

配置 Koishi在 Koishi 插件市场搜索 onebot 并安装 adapter-onebot，如下图：

安装完之后，点击修改→配置

配置 OneBot
这里以 WS 反向连接为例：
selfId 为你的机器人的 QQ 号
token 需和 NapCat 配置的 token 一致，当然，如果没有配置 token，则留空。
protocol 选择 ws-reverse
其他配置保持默认即可，点击保存，然后启用插件。

配置完成后，在 NapCat 的配置中添加 WS 反向地址。Koishi OneBot 的 ws 反向地址为 ws://127.0.0.1:5140/onebot。添加完成后，点击保存即可。

配置 HTTP 服务 ​
HTTP 服务的配置主要有两方面：一方面是 HTTP 监听端口（应当由你的应用端来调用），另一方面是 HTTP 上报地址（由 NapCat 来调用你的应用端）。
HTTP 监听端口例如，配置的端口号为 3000，那么 API 地址为 http://localhost:3000。
HTTP 上报地址当 NapCat 收到消息等事件时，会以 POST 请求的方式将事件上报到此地址。
TIP
上报地址必须是 http:// 开头

配置 WebSocket 服务 ​
OneBot 11 标准中，对“正向 WS”“反向 WS”的定义较为模糊，这里明确如下：正向指接受应用端的 WS 连接；反向指 NapCat 主动连接应用端监听的反向 WS 地址。
正向 WS 配置例如，配置的端口号为 3001，那么需要在应用端配置的 WS 地址为 ws://localhost:3001。
反向 WS 配置例如，在 NoneBot2 配置 OneBot 的端口为 8080，路径为 /onebot/v11/ws，那么配置的反向 WS 地址为 ws://localhost:8080/onebot/v11/ws。


---


## zh-CN/guide/resource

社区资源 ​
NC-nonebot平台更新工具 nonebot-plugin-ncupdateauthor: tianyisama
nonebot-plugin-ncupdate
Node开发SDK node-napcat-tsauthor: huankong233
node-napcat-ts
推荐项目 ​
OlivOS 青果核心交互栈author: OlivOS-Team
OlivOS
Rust开发SDK onebotv11_rsauthor: canxin121
onebotv11_rs


---


## zh-CN

NapCat

 Skip to content NapCat

Main Navigation指南开发简体中文
English

简体中文
English

主题

NapCat
基于 NTQQ 实现的 QQ BOT
~
快速开始
Github

开箱即用
多种部署方式，快捷部署大多数平台大多数指令集架构，与NTQQ支持平台一致。

内存轻量
天生无头,不依赖框架加载不依赖Electron，10~50Mb内存使用。

适配快速
基于Core/Adapter实现，支持多种Bot协议，快速迁移。


---


## develop/api

请求接口兼容情况 V4 ​

字数

1087 字

阅读时间

5 分钟

NapCatQQ 实现了 Onebot 的大部分 API，对于 API 的详细说明请自行点击导航协议或者链接查看相关实现。
详细 NapCatQQ All API 用例参考 https://napcat.apifox.cn
连接方式 ​
连接方式可用
HTTP 接口调用✅
HTTP POST 事件上报✅
HTTP POST 快速操作✅
正向 WS 连接✅
反向 WS 连接✅
OneBot 11 API ​
Api介绍可用备注
send_private_msg发送私聊消息✅
send_group_msg发送群消息✅
send_msg发送消息✅
delete_msg撤回消息✅
get_msg获取消息✅
get_forward_msg获取合并转发消息✅
send_like发送好友赞✅请注意调用频率
set_group_kick群组踢人✅
set_group_ban群组单人禁言✅
set_group_whole_ban群组全员禁言✅
set_group_admin群组设置管理员✅
set_group_card设置群名片（群备注）✅
set_group_name设置群名✅
set_group_leave退出群组✅
set_group_special_title设置群组专属头衔✅
set_friend_add_request处理加好友请求✅
set_group_add_request处理加群请求／邀请✅
get_login_info获取登录号信息✅
get_stranger_info获取陌生人信息✅
get_friend_list获取好友列表✅
get_group_info获取群信息✅
get_group_list获取群列表✅
get_group_member_info获取群成员信息✅
get_group_member_list获取群成员列表✅
get_group_honor_info获取群荣誉信息✅
get_cookies获取 Cookies✅
get_csrf_token获取 CSRF Token✅
get_credentials获取 QQ 相关接口凭证✅
get_record获取语音✅
get_image获取图片✅
can_send_image检查是否可以发送图片✅
can_send_record检查是否可以发送语音✅
get_status获取运行状态✅
get_version_info获取版本信息✅
clean_cache清理缓存✅
go-cqhttp API ​
Api介绍可用备注
set_qq_profile设置登录号资料✅
_get_model_show获取在线机型✅仅为兼容性
_set_model_show设置在线机型✅仅为兼容性
get_online_clients获取当前账号在线客户端列表✅
delete_friend删除好友✅
mark_msg_as_read标记消息已读✅
send_group_forward_msg发送合并转发 ( 群聊 )✅
send_private_forward_msg发送合并转发 ( 好友 )✅
get_group_msg_history获取群消息历史记录✅
ocr_image图片 OCR✅
.ocr_image图片 OCR✅
get_group_system_msg获取群系统消息✅
get_essence_msg_list获取精华消息列表✅
get_group_at_all_remain获取群 @全体成员 剩余次数✅
set_group_portrait设置群头像✅
set_essence_msg设置精华消息✅
delete_essence_msg移出精华消息✅
send_group_sign群打卡✅
_send_group_notice发送群公告✅
_get_group_notice获取群公告✅
upload_group_file上传群文件✅
delete_group_file删除群文件✅
create_group_file_folder创建群文件文件夹✅
delete_group_folder删除群文件文件夹✅
get_group_file_system_info获取群文件系统信息✅
get_group_root_files获取群根目录文件列表✅
get_group_files_by_folder获取群子目录文件列表✅
get_group_file_url获取群文件资源链接✅
upload_private_file上传私聊文件✅
download_file下载文件到缓存目录✅
check_url_safely检查链接安全性✅
.handle_quick_operation对事件执行快速操作 ( 隐藏 API )✅
napcat API ​
Api介绍可用备注
set_group_sign群签到✅
ArkSharePeer推荐联系人/群聊✅
ArkShareGroup推荐群聊✅
get_robot_uin_range获取机器人 QQ 号区间✅
set_online_status设置在线状态✅
get_friends_with_category获取好友分类列表✅
set_qq_avatar设置头像✅
get_file获取文件信息✅
forward_friend_single_msg转发单条信息到私聊✅
forward_group_single_msg转发单条信息到群聊✅
translate_en2zh英译中翻译✅
set_msg_emoji_like设置消息的表情回复✅
send_forward_msg发送合并转发✅
mark_private_msg_as_read标记私聊信息已读✅
mark_group_msg_as_read标记群聊信息已读✅
get_friend_msg_history获取私聊记录✅
create_collection创建文本收藏✅
get_collection_list获取收藏列表✅
set_self_longnick设置个人签名✅
get_recent_contact获取最近的聊天记录✅
_mark_all_as_read标记所有为已读✅
get_profile_like获取自身点赞列表✅
fetch_custom_face获取收藏表情✅
fetch_emoji_like拉取表情回应列表✅
set_input_status设置输入状态✅
get_group_info_ex获取群组额外信息✅
get_group_ignore_add_request获取群组忽略的通知✅
_del_group_notice删除群聊公告✅
friend_poke私聊戳一戳✅
group_poke群聊戳一戳✅
nc_get_packet_status获取 PacketServer 状态✅
nc_get_user_status获取陌生人在线状态✅
nc_get_rkey获取 Rkey✅
get_group_shut_list获取群聊被禁言用户✅
get_mini_app_ark签名小程序卡片✅如B站分享卡片
get_ai_recordAI 文字转语音✅
get_ai_characters获取 AI 语音角色列表✅
send_group_ai_record群聊发送 AI 语音✅
send_poke群聊/私聊戳一戳✅

最后编辑于 4 个月前
查看完整历史

c9b6a5e-修正文件名拼写、导航链接 (#127)

4c401e3-在中文、英文以及数字混排时添加空格分隔

cb48f6d-feat

f307545-fix

2af84e1-fix

3c98951-feat: 调整

fee38d3-新增send_poke

dac2947-Update api.md

84b3b91-fix

c4ee686-fix

20dc3a2-fix

f7ba7e6-fix

42538dd-添加get_ai_record,get_ai_characters,send_group_ai_record的接口文档

7a24b21-fix

cbcfa7d-Update api.md

850a447-fix

48431aa-feat: 全部绿起来

c1cd506-feat: 通通绿起来

16744ac-添加群签到到api.md

f8f2437-doc: update

7a895c7-fix

c608875-去除不再支持的接口

14aed61-fix

8b42c72-[+] 修正接口兼容情况

ba5b47d-[-] 去除重复接口

288331d-[+] 补全接口列表

c4c93fb-fix

3fd1cd1-fix

ac82f49-重构文档

5256ad0-添加戳一戳接口文档

55ef6a1-[*] 优化接口兼容情况

9125c73-chore: api

400ac26-Update api.md

134c040-chore: docs - 修改事件的兼容情况 - 修改消息格式的兼容情况

e79395f-chore: docs - 修改文档目录关系 - 修改兼容性情况 - 优化零碎的教程


---


## develop/api/type

状态类型 developing ​

字数

598 字

阅读时间

4 分钟

施工中...
状态列表 ​
在线 ​
json5{ status: 10, extStatus: 0, batteryStatus: 0 }

Q我吧 ​
json5{ status: 60, extStatus: 0, batteryStatus: 0 }

离开 ​
json5{ status: 30, extStatus: 0, batteryStatus: 0 }

忙碌 ​
json5{ status: 50, extStatus: 0, batteryStatus: 0 }

请勿打扰 ​
json5{ status: 70, extStatus: 0, batteryStatus: 0 }

隐身 ​
json5{ status: 40, extStatus: 0, batteryStatus: 0 }

听歌中 ​
json5{ status: 10, extStatus: 1028, batteryStatus: 0 }

春日限定 ​
json5{ status: 10, extStatus: 2037, batteryStatus: 0 }

一起元梦 ​
json5{ status: 10, extStatus: 2025, batteryStatus: 0 }

求星搭子 ​
json5{ status: 10, extStatus: 2026, batteryStatus: 0 }

被掏空 ​
json5{ status: 10, extStatus: 2014, batteryStatus: 0 }

今日天气 ​
json5{ status: 10, extStatus: 1030, batteryStatus: 0 }

我 crash 了 ​
json5{ status: 10, extStatus: 2019, batteryStatus: 0 }

爱你 ​
json5{ status: 10, extStatus: 2006, batteryStatus: 0 }

恋爱中 ​
json5{ status: 10, extStatus: 1051, batteryStatus: 0 }

好运锦鲤 ​
json5{ status: 10, extStatus: 1071, batteryStatus: 0 }

水逆退散 ​
json5{ status: 10, extStatus: 1201, batteryStatus: 0 }

嗨到飞起 ​
json5{ status: 10, extStatus: 1056, batteryStatus: 0 }

元气满满 ​
json5{ status: 10, extStatus: 1058, batteryStatus: 0 }

宝宝认证 ​
json5{ status: 10, extStatus: 1070, batteryStatus: 0 }

一言难尽 ​
json5{ status: 10, extStatus: 1063, batteryStatus: 0 }

难得糊涂 ​
json5{ status: 10, extStatus: 2001, batteryStatus: 0 }

emo中 ​
json5{ status: 10, extStatus: 1401, batteryStatus: 0 }

我太难了 ​
json5{ status: 10, extStatus: 1062, batteryStatus: 0 }

我想开了 ​
json5{ status: 10, extStatus: 2013, batteryStatus: 0 }

我没事 ​
json5{ status: 10, extStatus: 1052, batteryStatus: 0 }

想静静 ​
json5{ status: 10, extStatus: 1061, batteryStatus: 0 }

悠哉哉 ​
json5{ status: 10, extStatus: 1059, batteryStatus: 0 }

去旅行 ​
json5{ status: 10, extStatus: 2015, batteryStatus: 0 }

信号弱 ​
json5{ status: 10, extStatus: 1011, batteryStatus: 0 }

出去浪 ​
json5{ status: 10, extStatus: 2003, batteryStatus: 0 }

肝作业 ​
json5{ status: 10, extStatus: 2012, batteryStatus: 0 }

学习中 ​
json5{ status: 10, extStatus: 1018, batteryStatus: 0 }

搬砖中 ​
json5{ status: 10, extStatus: 2023, batteryStatus: 0 }

摸鱼中 ​
json5{ status: 10, extStatus: 1300, batteryStatus: 0 }

无聊中 ​
json5{ status: 10, extStatus: 1060, batteryStatus: 0 }

timi中 ​
json5{ status: 10, extStatus: 1027, batteryStatus: 0 }

睡觉中 ​
json5{ status: 10, extStatus: 1016, batteryStatus: 0 }

熬夜中 ​
json5{ status: 10, extStatus: 1032, batteryStatus: 0 }

追剧中 ​
json5{ status: 10, extStatus: 1021, batteryStatus: 0 }

有亿点冷 ​
json5{ status: 10, extStatus: 2050, batteryStatus: 0 }

一月你好 ​
json5{ status: 10, extStatus: 2053, batteryStatus: 0 }

我的电量 ​
json5{ 
 status: 10, 
 extStatus: 1000,
 batteryStatus: 0, //这个是电量？
}

最后编辑于 大约 1 年前
查看完整历史

4c401e3-在中文、英文以及数字混排时添加空格分隔

b7cecd0-Update type.md

3c98951-feat: 调整

82cf165-补全NapCat扩展接口文档（未完工）

3633ebf-补齐结构体类型


---


## develop/event

上报事件兼容情况 V4 ​

字数

586 字

阅读时间

3 分钟

meta_event 事件 ​
事件名说明可用备注
meta_event.lifecycle生命周期✅
meta_event.lifecycle.enable生命周期 - OneBot 启用❌
meta_event.lifecycle.disable生命周期 - OneBot 停用❌
meta_event.lifecycle.connect生命周期 - WebSocket 连接成功✅
meta_event.heartbeat心跳✅
message 事件 ​
事件名说明可用备注
message.private私聊消息✅
message.private.friend私聊消息 - 好友✅
message.private.group私聊消息 - 群临时✅
message.private.group_self私聊消息 - 群中自身发送❌
message.private.other私聊消息 - 其他❌
message.group群聊消息✅
message.group.normal群聊消息 - 普通✅
message.group.notice群聊消息 - 系统提示❌
message_sent 事件 ​
事件名说明可用备注
message_sent.private私聊消息✅
message_sent.private.friend私聊消息 - 好友✅
message_sent.private.group私聊消息 - 群临时✅
message_sent.private.group_self私聊消息 - 群中自身发送❌
message_sent.private.other私聊消息 - 其他❌
message_sent.group群聊消息✅
message_sent.group.normal群聊消息 - 普通✅
message_sent.group.notice群聊消息 - 系统提示❌
request 事件 ​
事件名说明可用备注
request.friend加好友请求✅
request.group.add加群请求✅
request.group.invite邀请登录号入群✅
notice 事件 ​
事件名说明可用备注
notice.friend_add好友添加✅
notice.friend_recall私聊消息撤回✅
notice.offline_file接收到离线文件❌
notice.client_status其他客户端在线状态变更❌
notice.group_admin群聊管理员变动✅
notice.group_admin.set群聊管理员变动 - 增加✅
notice.group_admin.unset群聊管理员变动 - 减少✅
notice.group_ban群聊禁言✅
notice.group_ban.ban群聊禁言 - 禁言✅
notice.group_ban.lift_ban群聊禁言 - 取消禁言✅
notice.group_card群成员名片更新✅
notice.group_decrease群聊成员减少✅
notice.group_decrease.leave群聊成员减少 - 主动退群✅
notice.group_decrease.kick群聊成员减少 - 成员被踢✅
notice.group_decrease.kick_me群聊成员减少 - 登录号被踢✅
notice.group_increase群聊成员增加✅
notice.group_increase.approve群聊成员增加 - 管理员已同意入群✅
notice.group_increase.invite群聊成员增加 - 管理员邀请入群✅
notice.group_recall群聊消息撤回✅
notice.group_upload群聊文件上传✅
notice.group_msg_emoji_like群聊表情回应⏹仅收自己的 其余扩展接口拉取
notice.essence群聊设精✅
notice.essence.add群聊设精 - 增加✅
notice.notify.poke戳一戳✅
notice.notify.input_status输入状态更新✅
notice.notify.title群成员头衔变更✅
notice.notify.profile_like点赞✅

最后编辑于 超过 1 年前
查看完整历史

2c760fe-Update event.md

8264eb0-fix

0712ca7-fix

cf55fa4-fix

f307545-fix

1587ff8-fix

3c98951-feat: 调整

d8831b5-feat: 订正错误

8b42c72-[+] 修正接口兼容情况

ac82f49-重构文档

4e1789f-[*] 优化上报事件兼容情况

87af040-fix: update notice.notify.title

134c040-chore: docs - 修改事件的兼容情况 - 修改消息格式的兼容情况

e79395f-chore: docs - 修改文档目录关系 - 修改兼容性情况 - 优化零碎的教程

670d937-improve docs behavior

b84c2bf-change

34ea1d2-doc: 大量文字表述上的修改，使表意更加明确

1bab76f-doc: update

9c73e2c-doc: update

e9f9949-init


---


## develop/file

NapCat 文件处理框架指南 ​

字数

1268 字

阅读时间

6 分钟

重要提示： 从 v4.8.115+ 开始，NapCat 引入了新的 Stream API 方案，推荐用于大文件传输和跨设备部署。
🚀 Stream API (推荐方案) ​
适用版本： v4.8.115+
核心概念 ​
Stream API 提供了三种类型的接口，专门用于处理大文件传输和跨设备部署场景：
API 类型描述使用场景
Normal普通接口，兼容 OneBot 标准日常操作，无切片传输
Download下载流接口大文件下载，流式传输
Upload上传流接口大文件上传，流式传输
API 列表 ​
Normal 类型 ​
clean_stream_temp_file - 清理临时文件
Download 类型 ​
test_download_stream - 测试下载流
download_file_stream - 文件下载流
Upload 类型 ​
upload_file_stream - 文件上传流
⚠️ 注意： Upload/Download 组 API 的 action name 必须以 stream 结尾
示例代码 ​
python# Python 调用 upload_file_stream 示例
# 详见：https://github.com/NapNeko/NapCatQQ/blob/main/packages/napcat-onebot/action/stream/test_upload_stream.py

upload_file_stream
响应格式 ​
Stream API 使用特殊的响应格式来处理流式传输：
流传输状态标识 ​
状态type 字段描述
传输中stream数据块传输
传输完成response流传输成功结束
传输失败error流传输异常结束
状态stream 字段描述
普通接口normal-action标准OneBot接口
流式接口stream-action新的流式传输接口
响应示例 ​
数据传输中：
json{
 "status": "ok",
 "retcode": 0,
 "data": {
 "type": "stream",
 "data": "Index-> 1",
 "data_type": "data_chunk"
 },
 "message": "",
 "wording": "",
 "echo": "c5dc7stum6g",
 "stream": "stream-action"
}

传输完成：
json{
 "status": "ok",
 "retcode": 0,
 "data": {
 "type": "response",
 "data_type": "data_complete",
 "data": "Stream transmission complete"
 },
 "message": "",
 "wording": "",
 "echo": "c5dc7stum6g",
 "stream": "stream-action"
}

传输失败：
json{
 "status": "failed",
 "retcode": 200,
 "data": {
 "type": "error",
 "data_type": "error"
 },
 "message": "This is a test error",
 "wording": "This is a test error",
 "echo": "ei2vqkdb6cb",
 "stream": "stream-action"
}

优势与适用场景 ​
大文件传输：适用于需要传输大于 100MB 的文件，避免内存溢出。
跨设备部署：适用于 NapCat 与 QQ 客户端不在同一台机器的场景。
旧文档 ​
发送文件： ​
至少启动一个 HTTP 端口（可以和 WebSocket 服务端复用端口），并采用此端口在需要文件时通过 URL 传递文件。
接收文件： ​
大部分文件提供了 URL 上报
没有 URL 时应该通过 get_file 获取本地文件
注意：音频给出的 URL 是 raw silk 格式未处理
非视频 图片 音频的普通文件的链接下载次数影响，可通过下面接口再次获取直链
通常方法获取直链和文件下载 ​
获取文件直链 (Raw) ​
通过以下端点获取文件直链：
群聊文件：/get_group_file_url
参数：file_id 字符串 必须
group 字符串 必须

私聊文件：/get_private_file_url
参数：file_id 字符串 必须

下载到本地或者输出base64 (Raw) ​
通过以下端点获取文件：
文件下载：/get_file参数：file_id 字符串 可选（file_id 或 file 任意一个用于标记文件获取）
file 字符串 可选（file_id 或 file 任意一个用于标记唯一文件获取）

File: 音频文件的处理 ​
重点问题 ​
在接收音频时，NapCat 通常需要将音视频文件以本地文件的形式传递，无法直接提供 URL。这是因为：
NTQQ 内部只能调用下载接口到本地，不能获取 URL（NapCat 虽然有能力获取，但存在新问题）
腾讯的音频文件为 silk 格式，必须使用 silk 和本地 ffmpeg 转码才能通用
在发送时也需要 silk 进行编码
NapCat设计 ​
接收时：接口请求后，NapCat 下载到本地，可选内置 silk/ffmpeg 进行转码，提供给外部 mp3 等通用格式
发送时：接口请求后，NapCat 下载到本地，内置 silk/ffmpeg 进行转码 silk 后并进行发送
如何获取音频文件 ​
通过以下端点获取音频文件：
音频文件获取：/get_record参数：file_id 字符串 可选（file_id 或 file 任意一个用于标记文件获取）
file 字符串 可选（file_id 或 file 任意一个用于标记唯一文件获取）
out_format 字符串 可选（mp3, amr, wma, m4a, spx, ogg, wav, flac）

如何发送音频文件 ​
通过通常的方法发送音频文件，无需特别注意。
File: 视频文件的处理 ​
提示 ​
视频文件最大 100MB，超过此大小请通过群文件方式发送。
File: 图片文件的处理 ​
提示 ​
图片的链接具有约 2 小时的过期时间，当过期后会提示 url expired。
此时可以调用 nc_get_rkey 获取新 rkey 替换 rkey 使用，或者通过 get_image、get_file、get_msg 刷新获取新的 URL。

最后编辑于 7 个月前
查看完整历史

f44bada-Clean up file.md by removing an empty line

7a0f4bf-docs: update upload_file_stream link in documentation

43a1b34-Update Stream API docs with new interface details

c6d8fdc-简化流传输状态标识表结构

b71dc51-Update file.md

420c967-在中文、英文以及数字混排时添加空格分隔 #2

081a13a-fix

1e638c3-feat: 更新文档


---


## develop/http-sse

HTTP-SSE ​

字数

249 字

阅读时间

1 分钟

介绍 ​
HTTP Server-Sent Events (SSE) 是一种服务器推送技术，允许服务器通过 HTTP 持久连接向客户端发送实时更新。相比于传统的轮询方式，SSE 更加高效，减少了服务器的压力。
扩展原因 ​
基于轮询或双CS的HTTP Bot框架需要双方配置两次C/S或者造成服务器压力。
模型架构 ​
事件通知: 通过 HTTP-SSE 通知获取。
API 操作: 通过 HTTP-GET 和 HTTP-POST 请求操作。
至此完成双向主动通讯。该方式协议端完全作为 Server，应用端完全作为 Client，复用 HTTP 路径，同时规避轮询。
如何启用 ​
在WebUi中启用 重启后重新查看配置，可以设置更多内容。
事件接口 ​
要订阅事件，请访问 /_events 端点。
常规接口 ​
例如 /send_msg 端点直接请求即可。

最后编辑于 大约 2 个月前
查看完整历史

ad61967-fix

d0b53bc-fix

4aaa956-fix


---


## develop/msg

消息格式兼容情况 V4 ​

字数

1029 字

阅读时间

6 分钟

消息列表 ​
支持使用 CQ码 发送
标有 <JSON> 的表示 收到的时候的消息类型是 json
消息格式介绍收发备注
text纯文本✅✅
faceqq 表情✅✅
image图片✅✅
record语音✅✅
video视频✅✅
at@某人✅✅
rps猜拳魔法表情✅✅
dice骰子✅✅
shake私聊窗口抖动✅❌
poke群聊戳一戳✅✅事件上报与接口调用 不通过消息
share <JSON>链接分享✅❌
contact <JSON>推荐好友/群✅✅
location <JSON>位置✅❌
music <JSON>音乐分享✅✅
reply回复消息✅✅
forward转发消息✅✅
node转发消息节点✅✅
jsonjson 信息✅✅
mfaceqq 表情包✅✅以image消息段上报(子类型区分) 支持mface/image消息段发送
file文件✅✅
markdownmarkdown✅✅发是在双层合并转发内 无法直接发送
lightapp<JSON>小程序卡片✅✅发是调用扩展接口get_mini_app_ark
注释提示 ​
标有 [收] 仅限收到
标有 [发] 仅限发送
标有 [选] 发送可选
特性提醒 ​
自4.4.14开始 NapCat采用JSON5标准解析请求,支持在JSON中尾随逗号与注释使用,以调用ws/http
text ​
json{
 "type": "text",
 "data": {
 "text": "文本"
 }
}

face ​
json{
 "type": "face",
 "data": {
 "id": "123"
 }
}

image ​
普通图片 ​
json{
 "type": "image",
 "data": {
 "name": "", // [发] [选]
 "summary": "", // [选]
 "file": "",
 "sub_type": "", // [选]
 "file_id": "", // [收]
 "url": "", // [收]
 "path": "", // [收]
 "file_size": "", // [收]
 "file_unique": "", // [收]
 }
}

商城表情 ​
json{
 "type": "image",
 "data": {
 "name": "", // [发] [选]
 "summary": "", // [选]
 "file": "marketface",
 "file_id": "", // [收]
 "url": "", // [收]
 "path": "", // [收]
 "file_unique": "", // [收]
 }
}

record ​
json{
 "type": "record",
 "data": {
 "file": "",
 "name": "", // [发] [选]
 "url": "", // [收]
 "path": "", // [收]
 "file_id": "", // [收]
 "file_size": "", // [收]
 "file_unique": "", // [收]
 }
}

video ​
json{
 "type": "video",
 "data": {
 "file": "",
 "name": "", // [发] [选]
 "thumb": "", // [发] [选]
 "url": "", // [收]
 "path": "", // [收]
 "file_id": "", // [收]
 "file_size": "", // [收]
 "file_unique": "", // [收]
 }
}

at ​
json{
 "type": "at",
 "data": {
 "qq": "10001",
 "qq": "all" // @全体
 }
}

rps ​
json{
 "type": "rps",
 "data": {
 "result": "" // [收]
 }
}

dice ​
json{
 "type": "dice",
 "data": {
 "result": "" // [收]
 }
}

contact ​
json{
 "type": "contact",
 "data": {
 "type": "qq", // [发] 推荐好友
 "type": "group", // [发] 推荐群聊
 "id": "10001" // [发] QQ号或群号
 }
}

music ​
现有音源 ​
json{
 "type": "music",
 "data": {
 "type": "qq", // [发]
 "type": "163", // [发]
 "type": "kugou", // [发]
 "type": "migu", // [发]
 "type": "kuwo", // [发]
 "id": "" // [发]
 }
}

自定义音源 ​
json{
 "type": "music",
 "data": {
 "type": "custom", // [发]
 "url": "", // [发] 点击后跳转目标 URL
 "audio": "", // [发] 音乐 URL
 "title": "", // [发]
 "image": "kuwo", // [发] [选]
 "singer": "kuwo", // [发] [选]
 }
}

reply ​
json{
 "type": "reply",
 "data": {
 "id": ""
 }
}

forward ​
json{
 "type": "forward",
 "data": {
 "id": "",
 "content": [] // [收]
 }
}

node ​
TIP
id 和 content 二选一

现有信息 ​
json{
 "type": "node",
 "data": {
 "id": "", // [发]
 "content": [] // [发]
 }
}

伪造信息 ​
json{
 "type": "node",
 "data": {
 "user_id": "10001", // [发]
 "nickname": "雪雪看不见我", // [发]
 "id": "", // [发]
 "content": [] // [发]
 }
}

json ​
json{
 "type": "json",
 "data": {
 "data": ""
 }
}

mface ​
json{
 "type": "mface",
 "data": {
 "emoji_id": "", // [发]
 "emoji_package_id": "", // [发]
 "key": "", // [发]
 "summary": "" // [选]
 }
}

file ​
json{
 "type": "file",
 "data": {
 "name": "", // [发] [选]
 "file": "empty",
 "path": "empty", // [收]
 "url": "empty", // [收]
 "file_id": "empty", // [收]
 "file_size": "empty", // [收]
 "file_unique": "empty" // [收]
 }
}

最后编辑于 16 天前
查看完整历史

0bfd075-fix

444da3e-fix

54695c3-fix

f995ca4-fix

3c98951-feat: 调整

ed99dd1-fix

850a447-fix

f79b8bc-feat: 清理不可能的

3633ebf-补齐结构体类型

8b42c72-[+] 修正接口兼容情况

45dfd48-fix: 调整

ac82f49-重构文档

26c2676-[*] 修正消息类型错误描述

134c040-chore: docs - 修改事件的兼容情况 - 修改消息格式的兼容情况

e79395f-chore: docs - 修改文档目录关系 - 修改兼容性情况 - 优化零碎的教程

1c18f02-docs: update

670d937-improve docs behavior

34ea1d2-doc: 大量文字表述上的修改，使表意更加明确

cee18ad-doc: update

1bab76f-doc: update

9c73e2c-doc: update

e9f9949-init


---


## develop/plugin/advanced

进阶功能开发 ​

字数

1624 字

阅读时间

8 分钟

本章节将介绍 NapCat 插件的高级功能，包括高级 API 路由使用、数据持久化存储以及与其他插件的交互。
1. 高级路由与网络服务 ​
NapCatPluginContext 提供了强大的路由注册能力，支持 GET/POST/PUT/DELETE 等多种 HTTP 方法，并自动处理插件路径前缀。
路由注册 API 概览 ​
所有的路由注册方法都在 ctx.router 对象下，分为三类：
需要鉴权的路由 ​
路径前缀：/api/Plugin/ext/<plugin-id>/
方法签名说明
get(path, handler)注册 GET 接口
post(path, handler)注册 POST 接口
put(path, handler)注册 PUT 接口
delete(path, handler)注册 DELETE 接口
api(method, path, handler)通用方法，method 支持 'get' | 'post' | 'put' | 'delete' | 'patch' | 'all'
无需鉴权的路由 ​
路径前缀：/plugin/<plugin-id>/api/
方法签名说明
getNoAuth(path, handler)注册 GET 开放接口
postNoAuth(path, handler)注册 POST 开放接口
putNoAuth(path, handler)注册 PUT 开放接口
deleteNoAuth(path, handler)注册 DELETE 开放接口
apiNoAuth(method, path, handler)通用方法
静态文件与页面 ​
方法签名路径前缀说明
static(urlPath, localPath)/plugin/<plugin-id>/files/<urlPath>/注册本地静态文件服务
staticOnMem(urlPath, files)/plugin/<plugin-id>/mem/<urlPath>/注册内存静态文件服务
page(pageDefinition)/plugin/<plugin-id>/page/<path>注册单个页面
pages(pageDefinitions)同上批量注册页面
请求/响应对象 ​
路由处理器接收包装后的请求和响应对象：
typescript// 请求对象 PluginHttpRequest
interface PluginHttpRequest {
 path: string; // 请求路径
 method: string; // 请求方法
 query: Record<string, string | string[] | undefined>; // 查询参数
 body: unknown; // 请求体
 headers: Record<string, string | string[] | undefined>; // 请求头
 params: Record<string, string>; // 路由参数
 raw: unknown; // 原始请求对象
}

// 响应对象 PluginHttpResponse
interface PluginHttpResponse {
 status(code: number): PluginHttpResponse; // 设置状态码
 json(data: unknown): void; // 发送 JSON 响应
 send(data: string | Buffer): void; // 发送文本响应
 setHeader(name: string, value: string): PluginHttpResponse; // 设置响应头
 sendFile(filePath: string): void; // 发送文件
 redirect(url: string): void; // 重定向
 raw: unknown; // 原始响应对象
}

示例：实现一个 Webhook 接收器 ​
假设你需要接收 GitHub Webhook 推送通知到 QQ 群：
typescript// src/services/webhook.ts
import type { NapCatPluginContext, OB11PostSendMsg } from "napcat-types";

export function registerWebhook(ctx: NapCatPluginContext) {
 // 注册无需鉴权的 POST 接口
 // 外部访问地址: http://napcat-ip:port/plugin/<your-plugin-id>/api/webhook/github
 ctx.router.postNoAuth('/webhook/github', async (req, res) => {
 const event = req.headers['x-github-event'];
 const payload = req.body as any;

 ctx.logger.info(`收到 GitHub 事件: ${event}`);

 if (event === 'push') {
 const repo = payload.repository.full_name;
 const pusher = payload.pusher.name;
 const msg = `项目 ${repo} 收到来自 ${pusher} 的新提交`;

 // 通过 actions 发送消息到群 (建议从配置读取群号)
 const params: OB11PostSendMsg = {
 message: msg,
 message_type: 'group',
 group_id: '123456',
 };
 await ctx.actions.call('send_msg', params, ctx.adapterName, ctx.pluginManager.config);
 }

 res.json({ status: 'ok' });
 });
}

2. 数据持久化 ​
插件通常需要保存运行时数据（如签到记录、积分等），NapCat 提供了数据目录供插件使用。
获取数据目录 ​
使用 ctx.dataPath 获取分配给当前插件的专属数据目录。也可以通过 ctx.pluginManager.getPluginDataPath(pluginId) 获取。
typescriptimport fs from 'fs';
import path from 'path';
import { NapCatPluginContext } from "napcat-types";

// 保存数据
function saveData(ctx: NapCatPluginContext, data: any) {
 const filePath = path.join(ctx.dataPath, 'data.json');
 // 确保目录存在（NapCat 通常会自动创建 dataPath，但为了保险）
 if (!fs.existsSync(ctx.dataPath)) {
 fs.mkdirSync(ctx.dataPath, { recursive: true });
 }
 fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
}

// 读取数据
function loadData(ctx: NapCatPluginContext) {
 const filePath = path.join(ctx.dataPath, 'data.json');
 if (fs.existsSync(filePath)) {
 return JSON.parse(fs.readFileSync(filePath, 'utf-8'));
 }
 return {};
}

推荐：使用轻量级数据库 ​
对于复杂数据，建议使用 sqlite3 或 leveldb (如 keyv)。
3. 插件间通信 ​
有时候一个插件需要调用另一个插件的功能（例如积分插件调用经济插件的接口）。
使用 ctx.getPluginExports ​
NapCat 提供了 ctx.getPluginExports<T>(pluginId) 方法来获取其他已加载插件的导出对象（即该插件的 PluginModule）。
插件 A (Provider):
typescript// src/index.ts
import { NapCatPluginContext } from "napcat-types";

export const plugin_init = (ctx: NapCatPluginContext) => {
 ctx.logger.log('Plugin A initialized');
};

// 导出公共方法供其他插件调用
export const somePublicMethod = () => {
 return "Hello from Plugin A";
}

插件 B (Consumer):
typescript// src/index.ts
import { NapCatPluginContext, PluginModule } from "napcat-types";

// 定义 Plugin A 的导出类型（可选，用于类型安全）
interface PluginAExports extends PluginModule {
 somePublicMethod: () => string;
}

export const plugin_init = (ctx: NapCatPluginContext) => {
 // 获取插件 A 的导出，泛型参数用于类型提示
 const pluginA = ctx.getPluginExports<PluginAExports>('plugin-a-id');
 if (pluginA && pluginA.somePublicMethod) {
 console.log(pluginA.somePublicMethod()); // "Hello from Plugin A"
 }
}

4. 调试与日志 ​
使用 ctx.logger 输出日志，日志会自动带上插件名称前缀，方便排查问题。
ctx.logger 实现了 PluginLogger 接口，提供以下方法：
typescriptctx.logger.log("普通日志"); // 通用日志输出
ctx.logger.debug("调试信息"); // 仅在 debug 模式显示
ctx.logger.info("普通信息"); // 信息级别
ctx.logger.warn("警告信息"); // 警告级别
ctx.logger.error("错误信息", new Error("oops")); // 错误级别

在开发过程中，建议开启 debug: true 配置以便通过控制台查看详细的调试日志。
提示
NapCat 插件模板中，配置更新通常通过 WebUI 触发。插件可以通过 plugin_on_config_change 钩子实时感知配置变更，实现无需重启的热重载。

5. 定时任务 (Cron Job) ​
如果你的插件需要定时执行任务（如每天早上发送早报），可以使用 node-schedule 或 cron 库。
注意: 在插件卸载 (plugin_cleanup) 时，务必取消所有定时任务，否则会导致内存泄漏或重复执行。
typescript// src/services/cron-service.ts
import cron from "node-cron";

let task: cron.ScheduledTask;

export function startDailyReport() {
 // 每天 8:00 执行
 task = cron.schedule("0 8 * * *", () => {
 console.log("发送早报...");
 // sendReport();
 });
}

export function stopDailyReport() {
 if (task) task.stop();
}

在 src/index.ts 中：
typescriptimport { NapCatPluginContext } from "napcat-types";
import { startDailyReport, stopDailyReport } from "./services/cron-service";

export const plugin_init = (ctx: NapCatPluginContext) => {
 startDailyReport();
};

export const plugin_cleanup = (ctx: NapCatPluginContext) => {
 stopDailyReport();
};

6. 插件管理器 API ​
通过 ctx.pluginManager 可以管理其他插件。IPluginManager 接口提供以下方法：
方法说明
getPluginPath()获取插件根目录
getPluginConfig()获取插件启用状态配置
getAllPlugins()获取所有已扫描的插件列表
getLoadedPlugins()获取所有已加载的插件列表
getPluginInfo(pluginId)获取指定插件信息
setPluginStatus(pluginId, enable)启用/禁用插件
loadPluginById(pluginId)加载指定插件
unregisterPlugin(pluginId)注销插件
uninstallPlugin(pluginId, cleanData?)卸载并删除插件
reloadPlugin(pluginId)重新加载插件
loadDirectoryPlugin(dirname)从目录加载插件
getPluginDataPath(pluginId)获取插件数据目录
getPluginConfigPath(pluginId)获取插件配置目录

最后编辑于 3 天前
查看完整历史

56176cd-feat: 新增插件机制文档、发布指南、WebUI 开发以及项目结构最佳实践


---


## develop/plugin/api/doc

NapCat 插件开发 API 参考文档 ​

字数

1094 字

阅读时间

5 分钟

NapCatPluginContext ​
插件的核心上下文对象，包含了几乎所有你需要的功能。在所有生命周期函数中作为第一个参数传入。
属性一览 ​
属性类型说明
coreNapCatCoreNapCat 底层核心实例
oneBotNapCatOneBot11AdapterOneBot11 协议适配器
actionsActionMapOneBot11 Action 调用器
pluginNamestring当前插件名称
pluginPathstring插件所在目录
configPathstring插件配置文件路径
dataPathstring插件数据存储目录
NapCatConfigNapCatConfigClass配置构建工具类
adapterNamestring适配器名称
pluginManagerIPluginManager插件管理器
loggerPluginLogger日志记录器
routerPluginRouterRegistry路由注册器
getPluginExports<T>(pluginId: string) => T | undefined获取其他插件的导出
ctx.actions ​
OneBot11 Action 调用器。
调用签名:
typescriptctx.actions.call(actionName, params, ctx.adapterName, ctx.pluginManager.config)

actionName: Action 名称（字符串）
params: 请求参数（不同 action 参数不同，无参数时传 void 0）
adapter: 适配器名称，使用 ctx.adapterName
config: 网络配置，使用 ctx.pluginManager.config
常用 Action 示例:
typescript// 通用发送消息 (推荐用法)
const params: OB11PostSendMsg = {
 message: 'Hello',
 message_type: 'group',
 group_id: '123456',
};
await ctx.actions.call('send_msg', params, ctx.adapterName, ctx.pluginManager.config);

// 获取登录信息
const info = await ctx.actions.call('get_login_info', void 0, ctx.adapterName, ctx.pluginManager.config);

// 获取群列表
const groups = await ctx.actions.call('get_group_list', void 0, ctx.adapterName, ctx.pluginManager.config);

// 获取版本信息
const version = await ctx.actions.call('get_version_info', void 0, ctx.adapterName, ctx.pluginManager.config);

// 撤回消息
await ctx.actions.call('delete_msg', { message_id }, ctx.adapterName, ctx.pluginManager.config);

ctx.logger ​
带有插件名称前缀的日志记录器，实现 PluginLogger 接口。
方法说明
log(...)输出普通日志
debug(...)输出调试日志（仅 debug 模式可见）
info(...)输出信息日志
warn(...)输出警告日志
error(...)输出错误日志
ctx.pluginManager ​
插件管理器接口 (IPluginManager)，提供对其他插件的管理能力。
方法返回值说明
getPluginPath()string获取插件根目录
getPluginConfig()PluginStatusConfig获取插件启用状态配置
getAllPlugins()PluginEntry[]获取所有已扫描的插件列表
getLoadedPlugins()PluginEntry[]获取所有已加载的插件列表
getPluginInfo(pluginId)PluginEntry | undefined获取指定插件信息
setPluginStatus(pluginId, enable)Promise<void>启用/禁用插件
loadPluginById(pluginId)Promise<boolean>加载指定插件
unregisterPlugin(pluginId)Promise<void>注销插件
uninstallPlugin(pluginId, cleanData?)Promise<void>卸载并删除插件
reloadPlugin(pluginId)Promise<boolean>重新加载插件
loadDirectoryPlugin(dirname)Promise<void>从目录加载插件
getPluginDataPath(pluginId)string获取插件数据目录
getPluginConfigPath(pluginId)string获取插件配置目录
ctx.router ​
WebUI 和 API 路由注册器 (PluginRouterRegistry)。
需要鉴权的路由 ​
路径前缀：/api/Plugin/ext/<plugin-id>/
方法签名说明
api(method, path, handler)注册指定 HTTP 方法的 API
get(path, handler)注册 GET API
post(path, handler)注册 POST API
put(path, handler)注册 PUT API
delete(path, handler)注册 DELETE API
无需鉴权的路由 ​
路径前缀：/plugin/<plugin-id>/api/
方法签名说明
apiNoAuth(method, path, handler)注册指定 HTTP 方法的开放 API
getNoAuth(path, handler)注册 GET 开放 API
postNoAuth(path, handler)注册 POST 开放 API
putNoAuth(path, handler)注册 PUT 开放 API
deleteNoAuth(path, handler)注册 DELETE 开放 API
页面与静态文件 ​
方法签名路径前缀说明
page(pageDefinition)/plugin/<plugin-id>/page/<path>注册页面
pages(pageDefinitions)同上批量注册页面
static(urlPath, localPath)/plugin/<plugin-id>/files/<urlPath>/注册本地静态文件服务
staticOnMem(urlPath, files)/plugin/<plugin-id>/mem/<urlPath>/注册内存静态文件服务
ctx.NapCatConfig ​
配置构建工具类，提供便捷的静态方法生成 PluginConfigItem：
方法签名说明
text(key, label, defaultValue?, description?, reactive?)文本输入
number(key, label, defaultValue?, description?, reactive?)数字输入
boolean(key, label, defaultValue?, description?, reactive?)布尔开关
select(key, label, options, defaultValue?, description?, reactive?)下拉单选
multiSelect(key, label, options, defaultValue?, description?, reactive?)下拉多选
html(content)HTML 展示
plainText(content)纯文本展示
combine(...items)合并多个配置项为 Schema
ctx.getPluginExports ​
typescriptgetPluginExports<T = PluginModule>(pluginId: string): T | undefined

获取其他已加载插件的导出模块对象。支持泛型参数以获得类型提示。
OB11Message 消息对象 ​
当收到 plugin_onmessage 事件时，传递的消息对象。
属性 ​
属性类型说明
message_idnumber消息 ID
user_idnumber发送者 QQ
group_idnumber群号（私聊时为 0）
message_type'private' | 'group'消息类型
raw_messagestring原始消息文本
messageMessageSegment[]消息段数组
senderOB11Sender发送者信息
timenumber时间戳
更多详细类型定义请参考 TypeScript 提示或查阅 napcat-types 包。

最后编辑于 11 天前
查看完整历史

56176cd-feat: 新增插件机制文档、发布指南、WebUI 开发以及项目结构最佳实践


---


## develop/plugin/api/type

NapCat Types 定义参考 ​

字数

1195 字

阅读时间

7 分钟

本文档列出了开发插件时最常用的类型定义。完整的类型定义请参考 napcat-types 源码。
注意
随着 napcat-types 的更新，部分内容可能已过时，本文仅供参考。请以 napcat-types 最新源码为准。

插件上下文 ​
typescriptexport interface NapCatPluginContext {
 core: NapCatCore;
 oneBot: NapCatOneBot11Adapter;
 actions: ActionMap;
 pluginName: string;
 pluginPath: string;
 configPath: string;
 dataPath: string;
 NapCatConfig: NapCatConfigClass;
 adapterName: string;
 pluginManager: IPluginManager;
 logger: PluginLogger;
 router: PluginRouterRegistry;
 getPluginExports: <T = PluginModule>(pluginId: string) => T | undefined;
}

插件模块定义 ​
typescriptexport interface PluginModule<T extends OB11EmitEventContent = OB11EmitEventContent, C = unknown> {
 // 必选：插件初始化
 plugin_init: (ctx: NapCatPluginContext) => void | Promise<void>;
 // 可选：消息/事件处理（需通过 event.post_type 判断事件类型）
 plugin_onmessage?: (ctx: NapCatPluginContext, event: OB11Message) => void | Promise<void>;
 // 可选：事件处理（非消息类 OneBot 事件）
 plugin_onevent?: (ctx: NapCatPluginContext, event: T) => void | Promise<void>;
 // 可选：插件卸载/清理
 plugin_cleanup?: (ctx: NapCatPluginContext) => void | Promise<void>;
 // 可选：配置 Schema（用于 WebUI 自动生成配置面板）
 plugin_config_schema?: PluginConfigSchema;
 // 可选：配置 UI（同 plugin_config_schema）
 plugin_config_ui?: PluginConfigSchema;
 // 可选：自定义配置读取
 plugin_get_config?: (ctx: NapCatPluginContext) => C | Promise<C>;
 // 可选：自定义配置保存
 plugin_set_config?: (ctx: NapCatPluginContext, config: C) => void | Promise<void>;
 // 可选：配置 UI 控制器（运行时动态控制配置界面）
 plugin_config_controller?: (
 ctx: NapCatPluginContext,
 ui: PluginConfigUIController,
 initialConfig: Record<string, unknown>
 ) => void | (() => void) | Promise<void | (() => void)>;
 // 可选：配置变更回调
 plugin_on_config_change?: (
 ctx: NapCatPluginContext,
 ui: PluginConfigUIController,
 key: string,
 value: unknown,
 currentConfig: Record<string, unknown>
 ) => void | Promise<void>;
}

配置 UI 定义 ​
typescriptexport type PluginConfigSchema = PluginConfigItem[];

export interface PluginConfigItem {
 key: string;
 type: 'string' | 'number' | 'boolean' | 'select' | 'multi-select' | 'html' | 'text';
 label: string;
 description?: string;
 default?: unknown;
 options?: { label: string; value: string | number }[];
 placeholder?: string;
 /** 标记此字段为响应式：值变化时触发 schema 刷新 */
 reactive?: boolean;
 /** 是否隐藏此字段 */
 hidden?: boolean;
}

配置 UI 控制器 ​
typescriptexport interface PluginConfigUIController {
 updateSchema: (schema: PluginConfigSchema) => void;
 updateField: (key: string, field: Partial<PluginConfigItem>) => void;
 removeField: (key: string) => void;
 addField: (field: PluginConfigItem, afterKey?: string) => void;
 showField: (key: string) => void;
 hideField: (key: string) => void;
 getCurrentConfig: () => Record<string, unknown>;
}

日志接口 ​
typescriptexport interface PluginLogger {
 log(...args: unknown[]): void;
 debug(...args: unknown[]): void;
 info(...args: unknown[]): void;
 warn(...args: unknown[]): void;
 error(...args: unknown[]): void;
}

路由相关类型 ​
typescriptexport type HttpMethod = 'get' | 'post' | 'put' | 'delete' | 'patch' | 'all';

export interface PluginRouterRegistry {
 // 需要鉴权
 api(method: HttpMethod, path: string, handler: PluginRequestHandler): void;
 get(path: string, handler: PluginRequestHandler): void;
 post(path: string, handler: PluginRequestHandler): void;
 put(path: string, handler: PluginRequestHandler): void;
 delete(path: string, handler: PluginRequestHandler): void;
 // 无需鉴权
 apiNoAuth(method: HttpMethod, path: string, handler: PluginRequestHandler): void;
 getNoAuth(path: string, handler: PluginRequestHandler): void;
 postNoAuth(path: string, handler: PluginRequestHandler): void;
 putNoAuth(path: string, handler: PluginRequestHandler): void;
 deleteNoAuth(path: string, handler: PluginRequestHandler): void;
 // 页面
 page(page: PluginPageDefinition): void;
 pages(pages: PluginPageDefinition[]): void;
 // 静态文件
 static(urlPath: string, localPath: string): void;
 staticOnMem(urlPath: string, files: MemoryStaticFile[]): void;
}

export interface PluginHttpRequest {
 path: string;
 method: string;
 query: Record<string, string | string[] | undefined>;
 body: unknown;
 headers: Record<string, string | string[] | undefined>;
 params: Record<string, string>;
 raw: unknown;
}

export interface PluginHttpResponse {
 status(code: number): PluginHttpResponse;
 json(data: unknown): void;
 send(data: string | Buffer): void;
 setHeader(name: string, value: string): PluginHttpResponse;
 sendFile(filePath: string): void;
 redirect(url: string): void;
 raw: unknown;
}

export type PluginNextFunction = (err?: unknown) => void;
export type PluginRequestHandler = (
 req: PluginHttpRequest,
 res: PluginHttpResponse,
 next: PluginNextFunction
) => void | Promise<void>;

export interface PluginPageDefinition {
 path: string; // 页面路径
 title: string; // 页面标题
 icon?: string; // 页面图标
 htmlFile: string; // HTML 文件路径（相对于插件目录）
 description?: string; // 页面描述
}

export type MemoryFileGenerator = () => string | Buffer | Promise<string | Buffer>;

export interface MemoryStaticFile {
 path: string; // 文件路径
 content: string | Buffer | MemoryFileGenerator; // 文件内容或生成器
 contentType?: string; // MIME 类型
}

插件管理器接口 ​
typescriptexport interface IPluginManager {
 readonly config: NetworkAdapterConfig;
 getPluginPath(): string;
 getPluginConfig(): PluginStatusConfig;
 getAllPlugins(): PluginEntry[];
 getLoadedPlugins(): PluginEntry[];
 getPluginInfo(pluginId: string): PluginEntry | undefined;
 setPluginStatus(pluginId: string, enable: boolean): Promise<void>;
 loadPluginById(pluginId: string): Promise<boolean>;
 unregisterPlugin(pluginId: string): Promise<void>;
 uninstallPlugin(pluginId: string, cleanData?: boolean): Promise<void>;
 reloadPlugin(pluginId: string): Promise<boolean>;
 loadDirectoryPlugin(dirname: string): Promise<void>;
 getPluginDataPath(pluginId: string): string;
 getPluginConfigPath(pluginId: string): string;
}

export interface PluginEntry {
 id: string;
 fileId: string;
 name?: string;
 version?: string;
 description?: string;
 author?: string;
 pluginPath: string;
 entryPath?: string;
 packageJson?: PluginPackageJson;
 enable: boolean;
 loaded: boolean;
 runtime: PluginRuntime;
}

export type PluginRuntimeStatus = 'loaded' | 'error' | 'unloaded';

export interface PluginRuntime {
 status: PluginRuntimeStatus;
 error?: string;
 module?: PluginModule;
 context?: NapCatPluginContext;
}

NapCatConfig 构建器 ​
typescriptexport interface INapCatConfigStatic {
 text(key: string, label: string, defaultValue?: string, description?: string, reactive?: boolean): PluginConfigItem;
 number(key: string, label: string, defaultValue?: number, description?: string, reactive?: boolean): PluginConfigItem;
 boolean(key: string, label: string, defaultValue?: boolean, description?: string, reactive?: boolean): PluginConfigItem;
 select(key: string, label: string, options: { label: string; value: string | number }[],
 defaultValue?: string | number, description?: string, reactive?: boolean): PluginConfigItem;
 multiSelect(key: string, label: string, options: { label: string; value: string | number }[],
 defaultValue?: (string | number)[], description?: string, reactive?: boolean): PluginConfigItem;
 html(content: string): PluginConfigItem;
 plainText(content: string): PluginConfigItem;
 combine(...items: PluginConfigItem[]): PluginConfigSchema;
}

事件类型枚举 ​
typescriptexport enum EventType {
 META = "meta_event",
 REQUEST = "request",
 NOTICE = "notice",
 MESSAGE = "message",
 MESSAGE_SENT = "message_sent"
}

在 plugin_onmessage 中需要通过 event.post_type 判断事件类型：
typescriptif (event.post_type !== EventType.MESSAGE) return;

ActionMap ​
ActionMap 提供 call 方法调用 OneBot11 Action：
typescript// call 方法签名
actions.call(
 actionName: string, // Action 名称
 params: unknown, // 请求参数，无参数时传 void 0
 adapter: string, // 适配器名称，使用 ctx.adapterName
 config: NetworkAdapterConfig // 网络配置，使用 ctx.pluginManager.config
): Promise<any>

消息发送参数 ​
typescriptexport interface OB11PostSendMsg {
 message_type?: "private" | "group"; // 消息类型
 user_id?: string; // 用户 QQ 号（私聊时）
 group_id?: string; // 群号（群聊时）
 message: string | MessageSegment[]; // 消息内容
 auto_escape?: boolean | string; // 是否作为纯文本发送
}

最后编辑于 11 天前
查看完整历史

56176cd-feat: 新增插件机制文档、发布指南、WebUI 开发以及项目结构最佳实践


---


## develop/plugin/hot-reload

热重载开发 ​

字数

2677 字

阅读时间

12 分钟

在传统的插件开发流程中，每次修改代码都需要手动构建、复制文件、重启 NapCat，效率较低。NapCat 提供了 热重载（HMR） 机制，允许你在开发过程中修改代码后自动重新加载插件，无需重启 NapCat。
适用场景
热重载适用于 本地开发和调试阶段。当你完成开发并准备发布时，仍然使用 发布插件 中的标准流程。

安全警告
调试服务基于 WebSocket 通信，默认不启用认证（无 token），任何能访问该端口的客户端都可以执行插件管理操作（加载、卸载、重载插件等）。
强烈建议在本地环境调试（默认监听 127.0.0.1），避免远程调试
未配置 token 时，切勿将调试端口暴露在公网中，否则任何人都可以连接并操控你的 NapCat 插件
如果确实需要远程调试，必须同时启用认证并设置高强度 token，且通过防火墙严格限制来源 IP

架构概览 ​
热重载机制由三个组件协同工作：

组件说明
napcat-plugin-debugNapCat 端插件，启动 WebSocket 服务器（默认 ws://127.0.0.1:8998），将 PluginManager 的 API 暴露为 JSON-RPC 接口
napcatHmrPlugin (Vite 插件)集成到 Vite 构建流程中，在每次 writeBundle 时自动连接调试服务、复制 dist/ 到远程、调用 reloadPlugin。来自 napcat-plugin-debug-cli/vite
napcat-plugin-debug-cli可选的 CLI 工具，提供交互式 REPL、手动部署等功能
前置配置 ​
1. NapCat 端：安装调试插件 ​
在 NapCat 的插件市场中搜索并安装 napcat-plugin-debug（插件调试服务），启用后它会自动在 ws://127.0.0.1:8998 启动 WebSocket 调试服务。
调试服务配置项在 NapCat WebUI 的插件配置中可以修改以下参数：
配置项默认值说明
调试服务端口8998WebSocket 监听端口
监听地址127.0.0.1请勿改为 0.0.0.0，除非你清楚安全风险
启用认证false启用后客户端需提供 token
认证 Token空客户端连接时的认证 token
默认配置仅监听本地回环地址 127.0.0.1，只有本机可以连接，这是最安全的方式。如果将监听地址改为 0.0.0.0 且未启用认证，等同于将插件管理权限完全暴露在网络中。
2. 插件项目：安装依赖 ​
在你的插件项目中，安装 napcat-plugin-debug-cli 和 ws 作为开发依赖：
bashpnpm add -D napcat-plugin-debug-cli ws

TIP
如果你使用 napcat-plugin-template 模板，这些依赖和配置已经预置好，无需额外操作。

3. 配置 Vite 插件 ​
在 vite.config.ts 中引入并添加 napcatHmrPlugin（模板中已预置）：
typescriptimport { napcatHmrPlugin } from 'napcat-plugin-debug-cli/vite'

export default defineConfig({
 // ...其他配置
 plugins: [
 nodeResolve(),
 copyAssetsPlugin(),
 napcatHmrPlugin(), // 构建完成后自动部署+重载
 ],
})

可选配置项：
typescriptnapcatHmrPlugin({
 wsUrl: 'ws://192.168.1.100:8998', // 调试服务地址（默认 ws://127.0.0.1:8998）
 token: 'mySecret', // 认证 token
 enabled: true, // 是否启用（默认 true）
})

关于远程连接
上述 wsUrl 指向远程地址仅作为示例。实际开发中 建议在本地调试（使用默认的 ws://127.0.0.1:8998）。如果你的 NapCat 运行在远程服务器上，请确保调试服务已启用 token 认证，并通过 SSH 隧道或防火墙限制访问，而非直接将端口暴露在公网。

4. 配置 npm scripts ​
在 package.json 中添加以下脚本（模板中已预置）：
json{
 "scripts": {
 "build": "vite build",
 "push": "vite build",
 "dev": "vite build --watch"
 }
}

脚本说明
build仅构建（如调试服务在线则自动部署）
push构建 + 自动部署到远程 + 重载插件
dev持续构建 + 每次构建后自动部署 + 热重载
不要使用 deploy 作为脚本名
pnpm 有内置的 pnpm deploy 命令（用于 workspace 部署），会覆盖 package.json 中的同名脚本，导致 ERR_PNPM_CANNOT_DEPLOY 错误。请使用 push 或其他名称代替。

因为 napcatHmrPlugin 已集成到 Vite 构建流程中，所以 push 和 dev 只需要 vite build / vite build --watch 即可，无需额外启动 CLI 进程。
开发流程 ​
一、首次部署 ​
首次开发时，使用 push 命令将插件构建并部署到 NapCat：
bashpnpm run push

执行 vite build 时，Vite 插件 napcatHmrPlugin 会在构建完成的 writeBundle 钩子中自动执行部署流程：

插件如何知道 NapCat 的插件目录？ ​
Vite 插件 不需要你手动配置 NapCat 的安装路径。它的工作流程是：
构建完成后，napcatHmrPlugin 连接 NapCat 端的 napcat-plugin-debug WebSocket 服务（默认 ws://127.0.0.1:8998）
通过 JSON-RPC 调用 getDebugInfo() 方法，NapCat 返回当前实际的插件目录绝对路径
读取 dist/package.json 的 name 字段，确定插件名称
将 dist/ 的内容复制到 <远程插件目录>/<插件名>/ 下
调用 reloadPlugin 或 loadDirectoryPlugin 触发热重载
这意味着无论 NapCat 安装在哪里，Vite 插件都能自动适配。整个流程在一个进程中完成，无需启动额外的 CLI。
二、持续开发（热重载） ​
完成首次部署后，使用 dev 命令进入热重载开发模式：
bashpnpm run dev

等价于带 --watch 的 vite build，只需要 一个进程：
Vite watch 模式：监听 src/ 下的源码变更，自动重新构建到 dist/
napcatHmrPlugin：每次 writeBundle（构建完成）时自动部署到远程并调用热重载

改一行代码，保存即生效，无需重启 NapCat。
NapCat 端在收到重载指令后会：
调用旧插件实例的 plugin_cleanup() 释放资源
清除 Node.js 模块缓存
重新 import() 加载新代码
调用 plugin_init(ctx) 初始化新实例
注意 plugin_cleanup
热重载依赖 plugin_cleanup 正确释放资源（如定时器、WebSocket 连接、事件监听器等）。如果不清理，可能导致重复注册或内存泄漏。请务必在 plugin_cleanup 中做好清理工作。

三、交互调试（REPL） ​
直接运行 CLI 而不带 --watch 或 --deploy 参数，会进入交互式 REPL 模式：
bashnpx napcat-debug

在 REPL 中可以使用以下命令：
命令说明
list列出所有插件及其加载状态
reload <id>手动重载指定插件
load <id>加载指定插件
unload <id>卸载指定插件
info <id>查看插件详细信息（路径、版本、状态等）
deploy [dir]部署插件到远程并重载
watch <dir>启动文件监听
unwatch停止文件监听
status查看调试服务状态和 HMR 状态
ping心跳测试（含延迟）
quit退出
CLI 完整用法 ​
CLI 是独立的调试工具，提供 REPL 交互、手动部署等功能。日常开发推荐使用上述 Vite 插件方式（pnpm run dev），无需手动运行 CLI。
bashnapcat-debug [ws-url] [options]

参数说明
ws://host:port调试服务地址（默认 ws://127.0.0.1:8998）
-t, --token <token>认证 token（当调试服务启用认证时使用）
-w, --watch <dir>监听指定目录，文件变更时自动热重载
-W, --watch-all监听远程插件目录下的所有插件
-d, --deploy [dir]部署插件到远程并重载（默认当前目录）
-v, --verbose详细输出（显示事件通知等）
常用组合 ​
bash# 默认连接本地调试服务，进入 REPL
napcat-debug

# 连接远程 NapCat
napcat-debug ws://192.168.1.100:8998

# 带认证连接
napcat-debug --token mySecret

# 构建后一键部署
napcat-debug --deploy .

# 监听 dist/ 目录自动热重载
napcat-debug --watch ./dist

# 监听远程所有插件（用于直接编辑远程文件的场景）
napcat-debug --watch-all

完整数据流 ​
源码修改 (src/)
 │
 ▼
Vite --watch 重新构建 → dist/
 │
 ▼
napcatHmrPlugin writeBundle 钩子
 → 复制 dist/ → 远程插件目录/<pluginName>/
 │
 ▼
WebSocket → JSON-RPC reloadPlugin(pluginId)
 │
 ▼
NapCat 端:
 1. plugin_cleanup(ctx) — 卸载旧实例、释放资源
 2. 清除 Node.js 模块缓存 — 确保 import() 拿到新代码
 3. import(pluginEntry) — 重新加载插件模块
 4. plugin_init(ctx) — 初始化新实例、注册路由等

常见问题 ​
热重载后插件行为异常？ ​
检查 plugin_cleanup 是否正确清理了所有资源：
定时器（clearInterval / clearTimeout）
WebSocket 连接
文件监听器
事件监听器
连接调试服务失败？ ​
确认 napcat-plugin-debug 已在 NapCat 中启用
检查端口是否正确（默认 8998）
如果启用了认证，确认 token 正确（Vite 插件通过 napcatHmrPlugin({ token: '...' }) 配置）
如果 NapCat 运行在远程机器上，建议通过 SSH 隧道转发端口（如 ssh -L 8998:127.0.0.1:8998 user@server），而非直接开放端口
安全最佳实践 ​
场景建议做法
本地开发（NapCat 和编辑器在同一台机器）使用默认配置即可，无需额外设置
远程开发（NapCat 在远程服务器）使用 SSH 隧道转发端口，保持调试服务监听 127.0.0.1
必须直接远程连接启用认证 + 设置高强度 token + 防火墙限制来源 IP
生产环境不要启用调试插件，仅在开发阶段使用
部署时提示 dist/ 不存在？ ​
先运行 pnpm run build 构建项目，确保 dist/ 目录已生成。

最后编辑于 5 天前
查看完整历史

6bd94c1-docs: 增加热重载安全警告和最佳实践建议

9f74eae-docs: rename deploy to push, add pnpm deploy warning

f2d9faf-feat: 新增热重载开发文档，提升插件开发效率


---


## develop/plugin

本体开发 - 基于 NapCat 定制化开发方案 V4 ​

字数

560 字

阅读时间

3 分钟

该方案可以与NapCat本体代码进行捆绑 也可以使用各种内部接口 自由度大 简单代码实现方便
环境配置 ​
拉取 NapCat 仓库后，在命令行执行 npm run dev:depend 安装 NapCat 本体和 WebUi 依赖。

初次构建 NapCat，运行 npm run build:shell 或者 npm run build:framework，此次构建将会初始化 WebUi 打包文件和 NapCat。

启动 NetWork/Plugin 适配器，在 /src/onebot/index.ts 文件中，找到 NapCatOneBot11Adapter->InitOneBot 方法，解除相关注释代码，即可注册 Plugin 适配器。

打开 /src/onebot/network/plugin.ts 文件，可以修改 Plugin 适配器的以下配置：
typescriptmessagePostFormat: 'array', // array 为消息段，string 为 CQ 码
reportSelfMessage: false, // 上报自身消息
enable: true, // 启用适配器
debug: false, // 调试模式

再次构建时可选择 npm run dev:shell 或者 npm run dev:framework，跳过重复构建 WebUi 过程。

开始开发 ​
恭喜你完成了基础配置。现在打开 /src/plugin/index.ts 文件中的 plugin_onmessage 方法，在此方法中监听消息并处理。
当你需要调用 NTQQ Api 时，可以通过多种方法调用，下面为例子：
typescriptcore.apis.GroupApi.banMember()
// 调用 NapCat Core Api 用于禁言成员

await action.get('send_group_msg')?.handle({ group_id: String(message.group_id), message: 'pong' }, adapter);
// 调用 NapCat OneBot Action 用于发送消息接口，adapter 固定（此值固定为 plugin 用于标记适配器） 功能与下面的几乎无差异

new SendGroupMsg(obCore, core)
 .handle({ group_id: message.group_id, message: '正在设置头衔...', auto_escape: false }, adapter);
// 创建并调用 NapCat OneBot Action 用于发送消息接口，adapter 固定（此值固定为 plugin 用于标记适配器）

obCore.apis.MsgApi.createSendElements()
// 调用 NapCat OneBot Api 用于创建消息 从OneBot构建QQNT内部消息

前两种方法比较常用，obCore.apis 主要用于 OB->NT 消息内容转换，实际内容不多。
下面为 发送ping 回应ping 的群消息示例 /src/plugin/index.ts
typescriptimport { NapCatOneBot11Adapter, OB11Message } from "@/onebot";
import { NapCatCore } from "../core";
import { ActionMap } from "@/onebot/action";

export const plugin_onmessage = async (adapter: string, core: NapCatCore, obCore: NapCatOneBot11Adapter, message: OB11Message, action: ActionMap) => {
 if (message.raw_message === 'ping') {
 const ret = await action.get('send_group_msg')?.handle({ group_id: String(message.group_id), message: 'pong' }, adapter);
 console.log(ret);
 }
}

最后编辑于 大约 6 小时前
查看完整历史

3c98951-feat: 调整

81dbb0f-fix

bdeaec9-fix

f21cee2-fix

f300538-fix

1d238f9-fix

4d91d41-fix


---


## develop/plugin/index

NapCat 插件开发概览 ​

字数

2659 字

阅读时间

12 分钟

NapCat 提供了一套灵活的插件系统，支持开发者扩展 Bot 的功能。本文档介绍 NapCat 插件的开发流程。
前置知识
如果你还不了解 NapCat 插件系统的工作原理，建议先阅读 插件机制原理。

说明
推荐使用 napcat-plugin-template 模板仓库快速开始开发。

开发前准备 ​
在开始开发之前，你需要了解以下资源：
napcat-plugin-template: 官方提供的插件开发模板，内置了构建流程和 CI/CD，推荐使用。
napcat-plugin-index: 插件索引仓库，发布后的插件会收录在这里。
快速开始 ​
1. 使用模板创建项目 ​
最简单的方式是直接通过 napcat-plugin-template 创建你的 GitHub 仓库。该模板提供了完整的开发环境配置，包括 TypeScript 支持、构建脚本以及 CI/CD 流程。
2. 项目结构说明 ​
一个标准的 NapCat 插件项目结构如下 (以模板为例)：
napcat-plugin-template/
├── src/
│ ├── index.ts # 插件主入口，负责导出生命周期函数
│ ├── config.ts # 配置文件定义及 WebUI Schema
│ ├── types.ts # TypeScript 类型定义
│ ├── core/
│ │ └── state.ts # 全局状态管理
│ ├── handlers/ # 业务逻辑处理模块
│ │ └── message-handler.ts # 示例：消息处理器
│ ├── services/ # 服务层，API 路由等
│ └── webui/ # (可选) 插件的 WebUI 前端代码
├── package.json # 项目依赖及元数据
└── tsconfig.json # TypeScript 配置

编写核心逻辑 ​
在 src/index.ts 中，你需要导出插件的生命周期函数。这是插件被 NapCat 加载时执行的入口点。请务必遵循 NapCat 的生命周期。
插件入口 (src/index.ts) ​
插件需要导出 PluginModule 接口中定义的生命周期函数。其中 plugin_init 是唯一必选的函数。
typescriptimport type { PluginModule, OB11Message, OB11PostSendMsg } from "napcat-types";
import { EventType } from "napcat-types";

// 1. 插件初始化（必选）
// 插件加载时调用，用于初始化资源、注册路由等
export const plugin_init: PluginModule['plugin_init'] = async (ctx) => {
 ctx.logger.log('My Plugin has been initialized!');

 // 初始化时可以做一些准备工作
};

// 2. 消息处理（可选）
// 收到事件时调用，需要通过 post_type 判断是否为消息事件
export const plugin_onmessage: PluginModule['plugin_onmessage'] = async (ctx, event) => {
 // 过滤非消息事件
 if (event.post_type !== EventType.MESSAGE) return;

 // 简单的 Ping-Pong 示例
 if (event.raw_message === 'ping') {
 ctx.logger.log(`收到来自 ${event.user_id} 的 ping`);

 // 构造发送消息的参数
 const params: OB11PostSendMsg = {
 message: 'pong',
 message_type: event.message_type,
 ...(event.message_type === 'group' && event.group_id
 ? { group_id: String(event.group_id) }
 : {}),
 ...(event.message_type === 'private' && event.user_id
 ? { user_id: String(event.user_id) }
 : {}),
 };
 // 通过 actions 调用 OneBot11 Action (需传入 adapter 和 config)
 await ctx.actions.call('send_msg', params, ctx.adapterName, ctx.pluginManager.config);
 }
};

// 3. 事件处理（可选）
// 处理所有 OneBot 事件（包括通知、请求等）
export const plugin_onevent: PluginModule['plugin_onevent'] = async (ctx, event) => {
 ctx.logger.log('收到事件:', event);
};

// 4. 插件卸载（可选）
// 插件重载或卸载时调用，必须清理定时器、关闭连接等
export const plugin_cleanup: PluginModule['plugin_cleanup'] = (ctx) => {
 ctx.logger.log('My Plugin is cleaning up...');
 // 清理资源
};

关于 actions.call 调用
ctx.actions.call(actionName, params, adapter, config) 需要 4 个参数：
actionName: OneBot11 Action 名称（如 'send_msg'、'get_login_info' 等）
params: 请求参数
adapter: 适配器名称，使用 ctx.adapterName
config: 网络配置，使用 ctx.pluginManager.config

生命周期函数一览 ​
函数名是否必选说明
plugin_init必选插件加载时调用，用于初始化
plugin_onmessage可选收到事件时调用（需通过 post_type 判断事件类型）
plugin_onevent可选收到所有 OneBot 事件时调用
plugin_cleanup可选插件卸载/重载时调用
plugin_config_schema可选导出配置 Schema（同 plugin_config_ui）
plugin_config_ui可选导出配置 Schema，用于在 WebUI 生成配置面板
plugin_get_config可选获取插件配置的自定义实现
plugin_set_config可选保存插件配置的自定义实现
plugin_config_controller可选配置 UI 控制器，用于动态控制配置界面
plugin_on_config_change可选配置变更时触发的回调
消息处理的最佳实践 ​
为了保持代码整洁，建议将复杂的业务逻辑分离到 src/handlers 目录下的独立文件中，而不是全部写在 plugin_onmessage 里。
例如创建 src/handlers/message.ts：
typescriptimport type { NapCatPluginContext, OB11Message, OB11PostSendMsg } from "napcat-types";

export async function handleGroupMessage(ctx: NapCatPluginContext, message: OB11Message) {
 const { raw_message, group_id } = message;

 // 封装发送群消息的辅助函数
 async function sendGroupMsg(text: string) {
 const params: OB11PostSendMsg = {
 message: text,
 message_type: 'group',
 group_id: String(group_id),
 };
 await ctx.actions.call('send_msg', params, ctx.adapterName, ctx.pluginManager.config);
 }

 // 示例：简单的关键词回复
 if (raw_message.includes("喵")) {
 await sendGroupMsg("喵喵喵？");
 }

 // 示例：调用 OneBot 11 Action
 if (raw_message === "#info") {
 const loginInfo = await ctx.actions.call(
 'get_login_info', void 0, ctx.adapterName, ctx.pluginManager.config
 );
 await sendGroupMsg(`当前登录账号: ${loginInfo.nickname} (${loginInfo.user_id})`);
 }
}

然后在 index.ts 中引入使用：
typescriptimport type { PluginModule } from "napcat-types";
import { EventType } from "napcat-types";
import { handleGroupMessage } from "./handlers/message";

export const plugin_onmessage: PluginModule['plugin_onmessage'] = async (ctx, event) => {
 if (event.post_type !== EventType.MESSAGE) return;
 if (event.message_type === "group") {
 await handleGroupMessage(ctx, event);
 }
};

NapCatPluginContext 核心属性 ​
NapCatPluginContext 是插件开发中最重要的上下文对象，包含以下属性：
ctx.core: NapCatCore 实例，底层核心。
ctx.oneBot: NapCatOneBot11Adapter 实例，OneBot11 适配器。
ctx.actions: ActionMap 对象，通过 ctx.actions.call(actionName, params, ctx.adapterName, ctx.pluginManager.config) 调用 OneBot11 Action。
ctx.pluginName: 当前插件名称。
ctx.pluginPath: 插件所在目录路径。
ctx.configPath: 插件配置文件路径。
ctx.dataPath: 插件数据存储目录路径。
ctx.NapCatConfig: 配置构建工具类，提供 text/number/boolean/select 等静态方法。
ctx.adapterName: 适配器名称。
ctx.pluginManager: 插件管理器，支持查询/启停其他插件。
ctx.logger: 使用 NapCat 内置的日志系统，保持日志格式统一。
ctx.router: 路由注册器，用于注册 API 路由、页面和静态文件。
ctx.getPluginExports(pluginId): 获取其他已加载插件的导出对象。
配置文件 ​
NapCat 插件支持通过导出 plugin_config_ui 或 plugin_config_schema 来定义配置项。这允许用户在 WebUI 中修改插件的设置。
typescriptimport { PluginConfigSchema } from 'napcat-types';

export const plugin_config_ui: PluginConfigSchema = [
 {
 key: 'enable',
 label: '启用插件',
 type: 'boolean',
 default: true,
 description: '是否启用本插件的核心功能'
 },
 {
 key: 'prefix',
 label: '命令前缀',
 type: 'string',
 default: '/',
 placeholder: '请输入命令前缀，例如 / 或 #',
 description: '触发命令的前缀符号'
 }
];

WebUI 开发 (可选) ​
如果插件需要提供图形化界面，可以在 src/webui 目录下进行 React 开发。模板中已经配置好了 Vite 构建脚本，运行 npm run build 时，构建后的静态资源会被自动打包进插件中，用户可以通过 NapCat 的管理界面访问。
发布插件 ​
发布插件流程 ​
配置 package.json: 确保你的 package.json 包含正确的插件元数据：json{
 "name": "napcat-plugin-your-plugin",
 "plugin": "我的插件",
 "version": "1.0.0",
 "main": "index.mjs",
 "description": "这是我的 NapCat 插件",
 "author": "YourName",
 "napcat": {
 "tags": ["工具", "娱乐"], 
 "minVersion": "4.14.0",
 "homepage": "https://github.com/yourname/napcat-plugin-your-plugin" 
 }
}

发布版本: 推送 v* 格式的 Git Tag (例如 v1.0.0) 到你的远程仓库。
CI/CD 自动发布: 如果你基于模板开发并配置了 Secret，GitHub Actions 会自动构建并发布 Release。
提交索引: 同时 CI 会自动向 napcat-plugin-index 提交 PR。等待维护者审核合并后，你的插件就会出现在 NapCat 的插件市场中供用户下载。
自动化发布 (CI/CD) ​
NapCat 插件模板内置了 GitHub Actions 工作流，可自动完成构建、发布 Release 以及提交到插件市场的全过程。
工作流介绍 ​
模板仓库包含两个主要的工作流文件：
release.yml: 负责插件的构建和 Release 发布。
触发条件: 当你推送 v* 格式的 tag (如 v1.0.0) 时自动触发。
主要任务: 安装依赖 (pnpm install)
构建插件 (npm run build)
打包构建产物为 .zip 文件
创建 GitHub Release 并上传 .zip 包

update-index.yml: 负责将发布后的插件自动提交到 NapCat 插件索引仓库。
触发条件: 当 release.yml 成功发布 Release 后触发。
主要任务: 抓取 package.json 中的插件元数据 (版本、描述、作者等)
向 NapCat 插件索引仓库提交 Pull Request (PR)
等待仓库维护者审核合并

配置步骤 ​
为了让自动提交索引的功能正常工作，你需要进行少量的配置：
1. 设置 Repository Secret ​
由于 GitHub Actions 默认权限无法跨仓库提交 PR，你需要提供一个具有权限的 Token。
生成 Token:
访问 GitHub Developer Settings
生成一个新的 Personal Access Token (Classic)
勾选 public_repo (对于公开仓库) 权限
复制生成的 Token

配置 Secret:
进入你的插件仓库 -> Settings -> Secrets and variables -> Actions
点击 New repository secret
Name: INDEX_PAT (必须完全一致)
Value: 粘贴刚才复制的 Token
点击 Add secret 保存

2. 完善 package.json ​
自动化脚本会从 package.json 读取插件信息，请务必完整填写：
json{
 "name": "napcat-plugin-demo", // 插件ID (必须以 napcat-plugin- 开头)
 "plugin": "插件显示名称", // 插件在 WebUI 中的显示名称
 "version": "1.0.0", // 版本号
 "main": "index.mjs", // 入口文件
 "description": "这是插件描述", // 插件描述
 "author": "YourName", // 作者
 "napcat": {
 "tags": ["工具", "娱乐"], // 插件标签
 "minVersion": "4.14.0", // 最低支持的 NapCat 版本
 "homepage": "https://..." // 项目主页
 }
}

完整的发布操作 ​
配置完成后，发布新版本的流程如下：
修改版本号: 更新 package.json 中的 version 字段 (例如 1.0.1)。
提交代码: 将修改推送到 GitHub。
打标签:bashgit tag v1.0.1
git push origin v1.0.1

等待执行: GitHub Actions 会自动运行 release.yml 构建并发布 Release。
随后触发 update-index.yml，自动向官方索引仓库提交 PR。

完成: 等待 PR 被合并后，插件将收录至 NapCat 插件市场。
另请参阅 ​
热重载开发 — 使用调试服务实现改代码即时生效，无需重启 NapCat
NapCat 插件模板
NapCat 插件索引


---


## develop/plugin/mechanism

插件机制原理 ​

字数

1657 字

阅读时间

7 分钟

在开始开发 NapCat 插件之前，了解插件系统的运作机制有助于更合理地设计和编写插件。
插件是什么？ ​
NapCat 插件本质上是一个 TypeScript/JavaScript 模块，它被 NapCat 的插件管理器加载后，通过生命周期钩子与 NapCat 主程序进行交互。
插件的工作方式可以概括为：
NapCat 加载你的插件 → 传给你一个上下文对象 ctx → 你通过 ctx 调用 NapCat 提供的各种能力
核心架构 ​
整个插件系统由三个关键部分组成：

ctx 能做什么？ ​
ctx（即 NapCatPluginContext）是插件与 NapCat 交互的唯一桥梁。它提供了 三个层次 的能力：
层次一：调用 OneBot Action（最常用） ​
通过 ctx.actions.call(...) 调用标准的 OneBot11 协议 Action，这是最主要的使用方式。
typescript// 发送消息
await ctx.actions.call('send_msg', params, ctx.adapterName, ctx.pluginManager.config);

// 获取群列表
await ctx.actions.call('get_group_list', void 0, ctx.adapterName, ctx.pluginManager.config);

// 撤回消息
await ctx.actions.call('delete_msg', { message_id }, ctx.adapterName, ctx.pluginManager.config);

这些 Action 就是 NapCat 对外暴露的 OneBot11 API（如 send_msg、get_group_list、set_group_ban 等），与通过 HTTP/WebSocket 调用的 API 完全一致，只是插件内部可以直接调用，无需走网络请求。
API 查阅方式
使用 AI 查询：官方插件模板 napcat-plugin-template 的 .vscode/mcp.json 中已预配置了 napcat.apifox.cn 的 MCP 服务器。使用 VS Code + GitHub Copilot 打开项目后，可以直接在 Copilot Chat 中用自然语言查询 OneBot 和 NapCat 提供的各种 API 接口。
手动查阅：也可以直接访问 https://napcat.apifox.cn/ 浏览完整的 API 文档。

层次二：使用插件框架能力 ​
ctx 还提供了一系列插件框架本身的能力，这些与 OneBot 协议无关：
能力通过用途
路由注册ctx.router注册 HTTP API、静态文件、WebUI 页面
日志记录ctx.logger统一格式的日志输出
数据存储ctx.dataPath / ctx.configPath插件的数据和配置持久化
配置面板ctx.NapCatConfig在 WebUI 生成配置界面
插件管理ctx.pluginManager管理其他插件（查询、启停、加载）
插件通信ctx.getPluginExports()获取其他插件的导出对象，实现插件间交互
层次三：访问 NapCat 底层（高级用法） ​
ctx 还暴露了 NapCat 的内部实例，允许执行标准 OneBot 协议之外的操作：
ctx.core — NapCat 底层核心实例
ctx.oneBot — OneBot11 适配器实例
注意
直接使用 ctx.core 和 ctx.oneBot 属于高级用法，这些内部 API 可能在版本升级时发生变化。一般情况下优先使用 ctx.actions.call(...) 来调用标准 OneBot Action。

插件的两种典型用途 ​
根据你要实现的功能，NapCat 插件大致可以分为两种模式（或两者结合）：
模式一：Bot 功能型插件 ​
这是最常见的模式。监听消息/事件 → 调用 OneBot Action 做出响应。
typescript// 典型流程：收到消息 → 处理 → 调用 OneBot Action 回复
export const plugin_onmessage = async (ctx, event) => {
 if (event.raw_message === 'ping') {
 // 通过 ctx.actions 调用 OneBot Action 发送消息
 await ctx.actions.call('send_msg', {
 message: 'pong',
 message_type: event.message_type,
 group_id: String(event.group_id),
 }, ctx.adapterName, ctx.pluginManager.config);
 }
};

适用场景：关键词回复、命令处理、定时任务、消息转发、群管理等。
模式二：WebUI 功能型插件 ​
不处理任何 QQ 消息，仅通过 ctx.router 注册路由和页面，在 NapCat 的 WebUI 中提供额外的管理界面或工具。
typescriptexport const plugin_init = async (ctx) => {
 // 注册一个 WebUI 页面
 ctx.router.page({
 path: 'dashboard',
 title: '数据面板',
 htmlFile: 'webui/index.html',
 });

 // 注册 API
 ctx.router.getNoAuth('/stats', (req, res) => {
 res.json({ code: 0, data: { visits: 42 } });
 });
};

适用场景：数据可视化面板、配置管理工具、系统监控等。
模式三：两者结合 ​
实际开发中，很多插件会 同时 使用这两种模式 —— 处理消息的同时提供一个 WebUI 管理界面。官方插件模板 napcat-plugin-template 就是这种模式的典型示例。
关于插件模板
napcat-plugin-template 会随着 NapCat 项目的更新而持续调整（如 API 变化、最佳实践优化等）。建议开发前以模板仓库的最新版本为准，并关注仓库的 Release 和 README 以了解变更。

生命周期概览 ​
NapCat 通过调用你导出的特定函数来驱动插件运行：

与外部 OneBot 框架的区别 ​
既然可以通过 HTTP/WebSocket 调用 OneBot API，为什么还需要插件？以下是两种方式的对比：
对比项外部 OneBot 客户端NapCat 插件
通信方式网络请求 (HTTP/WS)直接函数调用
部署方式独立进程/独立服务嵌入 NapCat 内部
性能有网络开销零网络开销，直接调用
能力范围仅限 OneBot 协议OneBot + NapCat 内部 API
WebUI 集成需要独立搭建前端直接嵌入 NapCat WebUI
用户安装需要额外配置放入 plugins 目录即可
综上，插件是一种更轻量、集成度更高的开发方式，适用于需要与 NapCat WebUI 联动或对性能有较高要求的场景。
下一步 ​
快速开始开发插件
项目结构与最佳实践
热重载开发 — 改代码即时生效，提升开发效率
插件 API 参考

最后编辑于 5 天前
查看完整历史

f2d9faf-feat: 新增热重载开发文档，提升插件开发效率

56176cd-feat: 新增插件机制文档、发布指南、WebUI 开发以及项目结构最佳实践


---


## develop/plugin/publish

发布插件 ​

字数

3186 字

阅读时间

14 分钟

本章节将详细介绍如何通过 CI/CD 自动化流程发布你的 NapCat 插件，并将其收录到官方插件索引中。
前提条件
你已经基于 napcat-plugin-template 创建了自己的插件仓库
插件代码已经开发完成，并可以正常构建
你有一个 GitHub 账号

整体流程 ​
整个发布流程是自动化的，只需完成两步操作：配置 Secrets 和 推送 tag。

模板仓库内置了两个 GitHub Actions 工作流，分别负责：
工作流文件功能
release.yml自动构建项目、打包 zip、创建 GitHub Release
update-index.ymlRelease 发布后，自动向插件索引仓库提交更新 PR
第一步：填写插件元信息 ​
编辑你的 package.json，确保以下字段已正确填写：
json{
 "name": "napcat-plugin-your-name", // 插件唯一 ID，必须以 napcat-plugin- 开头
 "plugin": "你的插件显示名", // 在插件市场中显示的名称
 "version": "1.0.0",
 "description": "插件功能描述",
 "author": "你的名字",
 "napcat": { // 索引专用字段
 "tags": ["工具"], // 插件标签，见下方可用标签
 "minVersion": "4.14.0", // 支持的最低 NapCat 版本
 "homepage": "" // 留空则默认使用仓库地址
 }
}

命名规范 ​
name 字段（即插件 ID）必须以 napcat-plugin- 开头
仅允许小写字母、数字和短横线 -，禁止使用中文或大写字母
例如：napcat-plugin-music、napcat-plugin-group-manager
可用标签 ​
以下标签可在 napcat.tags 数组中使用：
官方 工具 娱乐 AI 群管 管理 自动化 语音 表情 撤回 游戏 音乐 图片 视频 搜索 翻译 天气 签到 抽奖 其他
第二步：配置仓库 Secrets ​
在你的插件仓库的 Settings > Secrets and variables > Actions 中，需要添加以下 Secret：
必选配置 ​
Secret 名称说明
INDEX_PATGitHub Personal Access Token，用于自动 fork 索引仓库并提交 PR
如何创建 Personal Access Token (PAT)推荐方式：Classic Token（简单快速）
进入 GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)
点击 Generate new token (classic)
设置名称，例如 napcat-plugin-index
勾选 public_repo 权限（位于 repo 下）
设置合理的过期时间
点击 Generate token，立即复制并保存，此 Token 只会显示一次
回到你的插件仓库，在 Settings > Secrets and variables > Actions 中添加名为 INDEX_PAT 的 Secret，值为上一步复制的 Token
备选方式：Fine-grained Token（更精确的权限控制）
进入 GitHub Settings > Developer settings > Personal access tokens > Fine-grained tokens
点击 Generate new token
设置名称，例如 napcat-plugin-index
Resource owner 选择你自己的账号
Repository access 选择 All repositories（因为 CI 会自动 fork 索引仓库到你的账号下）
展开 Repository permissions，设置以下权限： Contents: Read and write（推送分支到 fork 仓库）
Pull requests: Read and write（创建 PR）
Workflows: Read and write（触发工作流）

设置合理的过期时间
点击 Generate token，立即复制并保存
回到你的插件仓库，添加名为 INDEX_PAT 的 Secret
无需手动 fork 索引仓库
工作流会自动完成以下操作，你只需配置 INDEX_PAT 即可：
通过 PAT 获取你的 GitHub 用户名
自动 fork napcat-plugin-index 到你的账号下（如果尚未 fork）
同步 fork 到上游最新状态
将更新推送到你的 fork
从 fork 向官方仓库发起 PR

可选配置（AI Release Note） ​
如果你希望每次发布时自动用 AI 生成 Release Note，可以额外配置：
Secret 名称必填说明
AI_API_URL是兼容 OpenAI 格式的 API 地址（如 https://api.openai.com/v1/chat/completions）
AI_API_KEY是对应的 API 密钥
AI_MODEL否模型名称，默认 gpt-4o-mini
TIP
不配置 AI 相关 Secret 不影响发布流程。未配置或 AI 调用失败时，会自动回退到默认的 Release Note 模板。

第三步：发布！ ​
配置完成后，执行以下命令即可触发发布流程：
bashgit tag v1.0.0
git push origin v1.0.0

推送 v* 格式的 tag 后，CI 将自动完成后续所有步骤。
你也可以在 GitHub 仓库页面的 Actions 标签页中，手动触发 Build and Release 工作流并填入版本号。
CI 工作流详解 ​
release.yml — 自动构建与发布 ​
这个工作流在你推送 v* tag 或手动触发时执行，完成以下任务：

核心步骤说明 ​
1. 版本号解析
CI 会按优先级获取版本号：
手动触发时输入的版本号
tag 名称（如 v1.0.0 → 1.0.0）
自动生成时间戳版本（兜底）
2. 构建与打包
执行 pnpm run build 构建项目后，自动将产物打包为 zip 文件：
release/
├── index.mjs # 插件主入口
├── package.json # 精简后的 package.json
└── webui/ # WebUI 构建产物（如有）

修改插件名称
如果你的插件不叫 napcat-plugin-template，需要修改 release.yml 中 Prepare release package 步骤的 PLUGIN_NAME 环境变量为你的实际插件名。

3. Release Note 生成
如果配置了 AI Secret → 使用 AI 根据 commit 记录生成结构化 Release Note
如果未配置或 AI 调用失败 → 使用 .github/prompt/default.md 模板回退
如果模板也不存在 → 直接使用 commit log
你可以自定义 AI 的提示词，在 .github/prompt/release_note_prompt.txt 文件中修改即可。
4. 触发索引更新
Release 创建成功后，会通过 workflow_dispatch 自动触发 update-index.yml 工作流。
为什么要手动触发？
因为 GitHub Actions 中，由默认 GITHUB_TOKEN 创建的 Release 不会自动触发 on.release 事件。所以 release.yml 在最后一步通过 API 手动触发索引更新工作流。

update-index.yml — 自动更新插件索引 ​
这个工作流在 Release 发布后被触发，完成以下任务：

核心步骤说明 ​
1. 提取元信息
CI 会从你的 package.json 中自动读取：
字段来源映射到索引字段
nameid
plugin (或 name)name
descriptiondescription
authorauthor
napcat.tagstags
napcat.minVersionminVersion
napcat.homepage (或 homepage)homepage
下载链接会自动构造为：https://github.com/<你的仓库>/releases/download/<版本号>/<插件ID>.zip
2. 验证资源可达
CI 会 curl 检查下载链接是否可访问。如果第一次失败，会等待 30 秒后重试（因为 Release 资源上传可能有延迟）。两次都失败则跳过索引更新。
3. 自动 fork 与同步
CI 会通过 GitHub API 自动完成以下操作：
使用 INDEX_PAT 获取你的 GitHub 用户名
检查你账号下是否已有 napcat-plugin-index 的 fork，如果没有则自动创建
调用 merge-upstream API 将 fork 同步到官方索引仓库的最新状态
4. 提交 PR
CI 会 checkout 官方索引仓库，使用 Node.js 脚本更新 plugins.v4.json 文件：
如果插件 ID 已存在 → 更新该条目
如果是新插件 → 追加到列表
然后通过 peter-evans/create-pull-request Action 的 push-to-fork 功能，将更新推送到你的 fork 仓库，并从 fork 向官方索引仓库发起 PR。
为什么要通过 fork 提交？
你的 PAT 没有官方索引仓库 napcat-plugin-index 的写入权限，这是正常的。工作流自动将你的 fork 作为中转，完整流程是：
自动 fork 索引仓库 → 同步到上游最新 → 推送更新到 fork → 从 fork 向官方仓库发起 PR

索引仓库的自动审核 ​
你的 PR 提交到 napcat-plugin-index 后，索引仓库有一套完善的自动化审核流程：
工作流触发条件功能
PR 自动审核 (validate-pr.yml)PR 修改 plugins.v4.json校验 JSON 格式、字段完整性、ID 唯一性、版本号格式、包名规范、下载链接可达性
校验结果评论 (comment-on-pr.yml)审核完成后在 PR 中评论校验结果，自动打标签（新插件 / 插件更新 / 插件删除）
AI 安全审计 (security-scan.yml)PR 更新/新增插件下载插件 zip 进行静态代码分析 + AI 深度审查，检测高危代码
链接定时巡检 (check-links.yml)每天定时执行检查所有已索引插件的下载链接是否有效，失效时自动创建 Issue
审核结果 ​
校验通过 + 无安全风险 → 低风险 PR 自动合并，或等待维护者审核合并
校验未通过 → Bot 会在 PR 下评论具体的错误信息，你需要修复后重新提交
发现高危代码 → 需要人工审核
常见校验失败原因
插件 ID 不符合 napcat-plugin-xxx 格式
必填字段为空
downloadUrl 不是可访问的 .zip 链接
版本号不符合 semver 格式
插件包内 package.json 的 name 与索引中的 id 不一致

版本更新发布 ​
后续版本更新流程与首次发布完全一致：
修改 package.json 中的 version（可选，CI 会以 tag 为准）
推送新 tag：bashgit tag v1.1.0
git push origin v1.1.0

CI 自动构建、发布、更新索引
自定义 Release Note 模板 ​
默认模板 ​
在 .github/prompt/default.md 中自定义默认 Release Note 模板，支持 {VERSION} 占位符：
markdown## {VERSION}

### 核心更新
- 更新版本至 {VERSION}

### 安装说明
1. 下载 `你的插件名.zip`
2. 解压到 NapCat 的 `plugins` 目录
3. 重启 NapCat

AI Prompt 自定义 ​
在 .github/prompt/release_note_prompt.txt 中自定义 AI 生成 Release Note 的 system prompt，支持 {VERSION} 和 {PREV_VERSION} 占位符。
常见问题 ​
Q: 能不能手动提交 PR 到索引仓库？ ​
不建议。索引仓库已采用全自动审核机制，手动提交的 PR 将不会被合入。请使用模板仓库的 CI 自动提交流程。
如果你不想使用模板仓库，请自行实现等效的 CI 工作流。
Q: 不用模板仓库，自己写 CI 行不行？ ​
可以，只要你的 CI 能够：
构建产物并打包为 <插件ID>.zip（包含 index.mjs、package.json、webui/）
创建 GitHub Release 并上传 zip
向 NapNeko/napcat-plugin-index 仓库提交 PR，更新 plugins.v4.json
可以参考模板仓库的 release.yml 和 update-index.yml。
Q: INDEX_PAT Token 过期了怎么办？ ​
重新生成一个新的 PAT，更新仓库 Secret 即可。建议设置较长的过期时间，或使用 Fine-grained Token。
Q: 提交 PR 到索引仓库时报 403 / Permission denied？ ​
请检查以下几点：
PAT 权限不足：Classic Token 需要 public_repo 权限；Fine-grained Token 需要 Contents: Read and write + Pull requests: Read and write 权限，且 Repository access 需要选择 All repositories
PAT 已过期：重新生成并更新 Secret
工作流版本过旧：确保你使用的是最新版模板的 update-index.yml，新版工作流已内置自动 fork 功能，无需手动 fork 或修改工作流
Q: Release 发布了但索引没更新？ ​
检查 Actions 页面中 update-index.yml 的运行日志。常见原因：
INDEX_PAT 未配置或已过期
PAT 权限不足（见上一条）
下载链接验证失败（Release 资源尚未上传完成）
package.json 中缺少必要字段
Q: 下载链接验证失败？ ​
GitHub Release 资源上传可能有延迟。CI 已内置 30 秒重试机制。如果仍失败，可以等资源上传完成后手动触发 update-index.yml 工作流。

最后编辑于 3 天前
查看完整历史

b48358e-feat: 更新插件发布文档，增加自动 fork 和同步功能说明

56176cd-feat: 新增插件机制文档、发布指南、WebUI 开发以及项目结构最佳实践


---


## develop/plugin/start-webui

插件配置与 WebUI 开发 ​

字数

1679 字

阅读时间

8 分钟

NapCat 插件不仅支持配置文件，还支持提供图形化界面（WebUI）供用户交互。本指南将介绍如何定义配置以及开发 WebUI 界面。
1. 配置文件定义 ​
在 src/index.ts 中，你需要导出配置的 WebUI Schema 和可选的配置读写钩子。
定义配置接口 ​
首先定义 TypeScript 接口，以便在代码中获得类型提示。
typescript// src/types.ts
export interface PluginConfig {
 enable: boolean;
 prefix: string;
 adminList: number[];
}

定义 WebUI Schema ​
NapCat 使用 PluginConfigSchema 来自动生成配置面板。这是最推荐的配置方式，无需手动编写前端代码即可拥有一个漂亮的配置界面。
通过导出 plugin_config_ui 或 plugin_config_schema 来定义：
typescript// src/index.ts
import { PluginConfigSchema } from 'napcat-types';

export const plugin_config_ui: PluginConfigSchema = [
 {
 key: 'enable',
 label: '启用插件',
 type: 'boolean',
 default: true,
 description: '是否启用本插件的核心功能'
 },
 {
 key: 'prefix',
 label: '命令前缀',
 type: 'string',
 default: '/',
 placeholder: '请输入命令前缀，例如 / 或 #',
 description: '触发命令的前缀符号'
 },
 {
 key: 'adminList',
 label: '管理员列表',
 type: 'multi-select',
 default: [],
 options: [
 { label: '用户A', value: 123456 },
 { label: '用户B', value: 654321 }
 ],
 description: '拥有管理员权限的用户 QQ 号'
 }
];

支持的控件类型 ​
PluginConfigItem 的 type 字段支持以下值：
类型说明
string文本输入框
number数字输入框
boolean开关
select下拉单选
multi-select下拉多选
text多行文本框
html自定义 HTML 展示（不保存值）
PluginConfigItem 完整属性 ​
typescriptinterface PluginConfigItem {
 key: string; // 配置项唯一标识
 type: 'string' | 'number' | 'boolean' | 'select' | 'multi-select' | 'html' | 'text';
 label: string; // 显示标签
 description?: string; // 描述说明
 default?: unknown; // 默认值
 options?: { label: string; value: string | number }[]; // select/multi-select 的选项
 placeholder?: string; // 输入框占位符
 reactive?: boolean; // 标记为响应式：值变化时触发 schema 刷新
 hidden?: boolean; // 是否隐藏此字段
}

使用 NapCatConfig 构建器 ​
除了手动编写 Schema 数组，你还可以使用 ctx.NapCatConfig 提供的静态方法快速构建：
typescriptimport { NapCatPluginContext, PluginConfigSchema } from 'napcat-types';

export const plugin_init = (ctx: NapCatPluginContext) => {
 // NapCatConfig 提供了便捷的构建方法
 const schema: PluginConfigSchema = ctx.NapCatConfig.combine(
 ctx.NapCatConfig.text('apiKey', 'API Key', '', 'OpenAI API 密钥'),
 ctx.NapCatConfig.number('maxRetries', '最大重试次数', 3),
 ctx.NapCatConfig.boolean('debug', '调试模式', false, '开启后输出详细日志'),
 ctx.NapCatConfig.select('model', '模型选择', [
 { label: 'GPT-3.5', value: 'gpt-3.5-turbo' },
 { label: 'GPT-4', value: 'gpt-4' }
 ], 'gpt-3.5-turbo'),
 ctx.NapCatConfig.multiSelect('features', '启用功能', [
 { label: '翻译', value: 'translate' },
 { label: '摘要', value: 'summary' }
 ], ['translate']),
 ctx.NapCatConfig.html('<p style="color:gray">这是一段说明文字</p>'),
 ctx.NapCatConfig.plainText('纯文本说明内容')
 );
};

自定义配置读写 ​
默认情况下 NapCat 会自动管理配置读写。如果需要自定义行为，可以导出以下钩子：
typescriptimport type { PluginModule } from 'napcat-types';
import { PluginConfig } from './types';

// 自定义配置读取
export const plugin_get_config: PluginModule['plugin_get_config'] = async (ctx) => {
 // 从自定义位置读取配置
 return loadMyConfig(ctx.configPath);
};

// 自定义配置保存
export const plugin_set_config: PluginModule['plugin_set_config'] = async (ctx, config) => {
 saveMyConfig(ctx.configPath, config);
};

配置 UI 动态控制 ​
通过 plugin_config_controller 可以在运行时动态修改配置界面：
typescriptimport type { PluginModule, PluginConfigUIController } from 'napcat-types';

export const plugin_config_controller: PluginModule['plugin_config_controller'] = async (_ctx, ui, initialConfig) => {
 // 根据初始配置动态显示/隐藏字段
 if (initialConfig.mode === 'simple') {
 ui.hideField('advancedOption');
 }

 // 返回清理函数（可选）
 return () => {
 // 清理资源
 };
};

// 配置变更时的回调
export const plugin_on_config_change: PluginModule['plugin_on_config_change'] = async (_ctx, ui, key, value, _currentConfig) => {
 // 当 mode 字段变化时，动态调整 UI
 if (key === 'mode') {
 if (value === 'advanced') {
 ui.showField('advancedOption');
 } else {
 ui.hideField('advancedOption');
 }
 }
};

PluginConfigUIController 提供以下方法：
方法说明
updateSchema(schema)更新整个配置 Schema
updateField(key, field)更新指定字段的部分属性
removeField(key)移除指定字段
addField(field, afterKey?)添加新字段（可指定位置）
showField(key)显示指定字段
hideField(key)隐藏指定字段
getCurrentConfig()获取当前配置值
2. 在 WebUI 中使用自定义前端 ​
如果你需要更复杂的交互界面（如数据可视化、文件管理等），可以使用 React/Vue 开发完整的 SPA 页面。napcat-plugin-template 的 webui 目录正是为此准备的。
开启 WebUI 路由 ​
在 src/index.ts 中注册 API 和静态资源：
typescript// src/index.ts
import type { PluginModule } from "napcat-types";
import { registerApiRoutes } from './services/api-service';

export const plugin_init: PluginModule['plugin_init'] = async (ctx) => {
 // 1. 注册后端 API (供前端调用)
 registerApiRoutes(ctx);

 // 2. 托管静态文件 (前端 build 产物)
 // 假设你的前端 build output 在插件目录下的 webui/dist
 // 访问路径: http://host:port/plugin/<plugin-id>/files/<urlPath>/
 ctx.router.static('/static', 'webui/dist');

 // 3. 注册侧边栏页面入口 (可选)
 // 访问路径: http://host:port/plugin/<plugin-id>/page/dashboard
 ctx.router.page({
 title: '我的插件',
 path: 'dashboard', // 路由路径
 htmlFile: 'webui/dist/index.html', // 入口 HTML 文件
 icon: '🔌', // 页面图标
 description: '插件管理面板' // 页面描述
 });

 // 4. 也可以使用内存静态文件（适合动态生成内容）
 // 访问路径: http://host:port/plugin/<plugin-id>/mem/dynamic/config.json
 ctx.router.staticOnMem('/dynamic', [
 {
 path: '/config.json',
 content: () => JSON.stringify({ version: '1.0.0' }),
 contentType: 'application/json'
 }
 ]);
};

开发 WebUI 前端 ​
模板中的 src/webui 是一个标准的 React + Vite 项目。
启动开发服务: 进入 src/webui 运行 npm install && npm run dev。
调用后端接口: 使用 fetch 或 axios 调用你在插件中注册的 API。
路由前缀说明 ​
路由类型前缀注册方法
鉴权 API/api/Plugin/ext/<plugin-id>/ctx.router.get/post/put/delete/api
无鉴权 API/plugin/<plugin-id>/api/ctx.router.getNoAuth/postNoAuth/putNoAuth/deleteNoAuth/apiNoAuth
静态文件/plugin/<plugin-id>/files/<urlPath>/ctx.router.static(urlPath, localPath)
内存文件/plugin/<plugin-id>/mem/<urlPath>/ctx.router.staticOnMem(urlPath, files)
扩展页面/plugin/<plugin-id>/page/<path>ctx.router.page(definition)
建议在前端封装请求工具，自动处理前缀。
前后端通信示例 ​
后端 (node):
typescript// src/services/api-service.ts
import type { NapCatPluginContext } from "napcat-types";

export function registerApiRoutes(ctx: NapCatPluginContext) {
 // 注册需要鉴权的 GET 接口
 // 访问: /api/Plugin/ext/<plugin-id>/status
 ctx.router.get('/status', (_req, res) => {
 res.json({ status: 'ok', time: Date.now() });
 });

 // 注册无需鉴权的 POST 接口
 // 访问: /plugin/<plugin-id>/api/webhook
 ctx.router.postNoAuth('/webhook', async (req, res) => {
 const data = req.body;
 ctx.logger.info('收到 webhook:', data);
 res.status(200).json({ received: true });
 });
}

前端 (react):
typescript// src/webui/src/App.tsx
useEffect(() => {
 // 假设封装了 fetcher 自动添加前缀
 fetcher.get('/status').then(data => {
 console.log('插件状态:', data);
 });
}, []);

3. 构建与发布 ​
当你运行插件根目录的 npm run build 时，构建脚本通常会：
构建插件 TypeScript 代码 (src/index.ts 等)。
构建 WebUI 前端代码 (src/webui)。
将前端产物 (dist) 复制到插件输出目录 (dist/webui/dist)。
打包为 napcat-plugin-xxx.zip 或直接发布文件夹。
确保 package.json 中的 files 字段包含了所有必要的文件。

最后编辑于 2 天前
查看完整历史

56176cd-feat: 新增插件机制文档、发布指南、WebUI 开发以及项目结构最佳实践


---


## develop/plugin/structure

项目结构与最佳实践 ​

字数

980 字

阅读时间

4 分钟

NapCat 插件模板（napcat-plugin-template）提供了一套经过生产验证的项目结构。理解该结构有助于编写更易维护和扩展的插件。
目录结构详解 ​
以下是一个标准的插件项目的目录树：
src/
├── index.ts # [入口] 插件的主入口文件
├── config.ts # [配置] 定义插件配置结构及默认值
├── types.ts # [类型] 定义插件内部使用的 TypeScript 类型
├── core/
│ └── state.ts # [状态] 全局状态管理单例
├── handlers/ # [逻辑] 具体的业务逻辑处理
│ └── message-handler.ts
├── services/ # [服务] 外部服务接口或复杂功能封装
│ └── api-service.ts
└── webui/ # [前端] 插件的 WebUI 界面代码

1. index.ts - 插件入口 ​
这是插件被 NapCat 加载的地方。它的主要职责是：
导出插件的生命周期函数（实现 PluginModule 接口）。
在 plugin_init 中初始化全局状态、注册路由等。
在 plugin_onmessage 中处理消息。
在 plugin_cleanup 中清理资源。
最佳实践：不要在 index.ts 中编写具体的业务逻辑。应该将逻辑委托给 handlers/ 中的函数。
2. core/state.ts - 全局状态管理 ​
插件通常需要维护一些全局状态，例如：
NapCat 的上下文对象 (NapCatPluginContext)
当前的配置信息 (config)
插件的元数据（名称、路径等）
模板中使用了一个单例模式的 PluginState 类来管理这些信息。这种方式允许在项目的任意位置（包括深层嵌套的函数中）直接访问 ctx 或 config，无需逐层传递参数。
typescript// 使用示例
import { pluginState } from "../core/state";

export function doSomething() {
 // 直接获取 logger
 pluginState.logger.info("Doing something...");

 // 直接获取配置
 if (pluginState.config.enableFeatureA) {
 // ...
 }
}

3. handlers/ - 业务逻辑 ​
这里存放具体的事件处理函数。
message-handler.ts: 处理群消息、私聊消息。
request-handler.ts: 处理加群请求、好友请求。
notice-handler.ts: 处理群通知（如成员变动）。
建议将不同类型的逻辑拆分到不同的文件中。
4. services/ - 服务层 ​
如果你的插件需要调用外部 API（如查询天气、获取游戏数据），或者包含复杂的独立功能模块（如定时任务管理器），建议放在 services/ 目录下。
5. webui/ - 前端界面 ​
NapCat 插件支持通过 WebUI 提供图形化配置或展示界面。模板中预置了基于 React + Vite 的前端项目结构。
构建脚本会自动将 webui/ 下的代码打包，并嵌入到插件发布包中。
在 plugin_init 中通过 ctx.router.static 将 WebUI 静态资源暴露给用户访问。
常用开发模式 ​
依赖注入 vs 全局单例 ​
虽然依赖注入（Dependency Injection）在大型应用中很常见，但在插件开发中，使用 全局单例 (pluginState) 通常更简洁高效。它避免了在每个函数调用中透传 ctx 对象。
错误处理 ​
在 handlers 中捕获错误非常重要，防止一个未捕获的异常导致整个插件甚至 Bot 崩溃。
typescripttry {
 // 你的逻辑
} catch (e) {
 pluginState.logger.error("处理消息时发生错误", e);
}

配置热重载 ​
NapCat 支持配置的热重载。当用户在 WebUI 中修改配置后，插件可以通过 plugin_on_config_change 钩子感知变化：
typescriptimport type { PluginModule } from "napcat-types";

export const plugin_on_config_change: PluginModule['plugin_on_config_change'] = async (_ctx, ui, key, value, _currentConfig) => {
 _ctx.logger.info(`配置项 ${key} 已变更为:`, value);
 // 根据变更更新内存中的状态
};

或者通过 plugin_config_controller 获得更完整的 UI 控制能力。

最后编辑于 大约 1 个月前
查看完整历史

56176cd-feat: 新增插件机制文档、发布指南、WebUI 开发以及项目结构最佳实践


---


## develop/security

9月5日 OneBot 安全问题复盘 ​

字数

471 字

阅读时间

2 分钟

资料 ​

前情提要 ​
2025年9月5日，OneBot 生态内爆发了一场严重的安全事件，导致多个使用 OneBot 协议的机器人平台攻击，发送违法信息，甚至引发了大规模的网络攻击。作为主要沦陷框架将对事件的起因、经过及后续影响进行详细分析。
事件起因 ​
经过数据分析和溯源，事件的起因被锁定在 OneBot 协议无Token问题上，大量用户采用一键包和一键脚本，暴露公网环境，导致攻击者通过扫描工具发现了大量暴露的 OneBot 机器人实例。
问题整理 ​
大量用户不修改OneBot Token，导致攻击者可以轻易地通过空Token访问机器人实例。
受影响的主要为OneBot Http Server/WebSocket Server，攻击者通过发送恶意请求，控制机器人发送违法信息。
事件中，攻击者利用机器人发送了违法信息，甚至引发了大规模的网络攻击，影响范围广泛。
NapCat 未提供随机OneBot Token默认随机填充 (部分用户偷懒)
NapCat 多数服务以0.0.0.0 IPV4全监听，导致公网暴露 (方便用户致使问题)
其余安全问题 ​
NapCat 存在大量公网暴露的实例 WebUi也存在强安全风险 (并非此次事件问题)
意见 ​
随机默认Onebot Token
可禁止局域网外访问
登录速率配置
登录随机化WebUi密钥
采用账号消息通知用户Token更新
强制要求用户登录后修改密码

最后编辑于 3 个月前
查看完整历史

c9b6a5e-修正文件名拼写、导航链接 (#127)

100c2bd-Add security incident review and related images

69ca703-Create secrity.md


---


## onebot/api

NapCatQQ API 接口文档 ​

字数

1731 字

阅读时间

8 分钟

以下仅仅是Api接口列表 一览
详细 NapCatQQ All API 用例参考 https://napcat.apifox.cn
账号相关 ​
接口字符串功能参数
get_login_info获取登录信息无参数
get_status获取在线状态无参数
get_version_info获取版本信息无参数
bot_exit退出机器人无参数
clean_cache清除缓存无参数
set_self_longnick设置个性签名longNick: string
set_input_status设置输入状态user_id: number/string, event_type: number
set_diy_online_status设置自定义在线状态face_id: number/string, face_type: number/string, wording: string
set_online_status设置在线状态根据状态码设置不同的在线状态
set_qq_profile设置QQ资料个人资料相关参数
set_qq_avatar设置QQ头像头像相关参数
get_clientkey获取客户端密钥无参数
好友相关 ​
接口字符串功能参数
get_friend_list获取好友列表可选 no_cache: boolean/string
get_friends_with_category获取分类好友列表无参数
send_private_msg发送私聊消息user_id: number/string, message: string/array, 其他可选参数
delete_msg撤回消息message_id: number/string
get_msg获取消息message_id: number/string
send_like发送好友点赞user_id: number/string, times: number/string
set_friend_add_request处理好友添加请求flag: string/number, approve: boolean/string, remark: string
set_friend_remark设置好友备注user_id: number/string, remark: string
delete_friend删除好友user_id: number/string
get_unidirectional_friend_list获取单向好友列表无参数
friend_poke好友戳一戳user_id: number/string
mark_private_msg_as_read标记私聊消息为已读user_id: number/string, time: number
get_friend_msg_history获取私聊消息历史user_id: number/string, count: number
forward_friend_single_msg转发单条好友消息user_id: number/string, message_id: string
get_profile_like获取个人资料点赞信息无参数
fetch_emoji_like获取表情点赞信息无参数
nc_get_user_status获取用户状态user_id: number/string
群相关 ​
接口字符串功能参数
get_group_list获取群列表可选 no_cache: boolean/string
get_group_info获取群信息group_id: number/string, 可选 no_cache: boolean/string
get_group_info_ex获取群扩展信息group_id: number/string
send_group_msg发送群消息group_id: number/string, message: string/array, 其他可选参数
set_group_add_request处理群添加请求flag: string/number, approve: boolean/string, reason: string
set_group_kick踢出群成员group_id: number/string, user_id: number/string, reject_add_request: boolean/string
set_group_ban设置群禁言group_id: number/string, user_id: number/string, duration: number/string
set_group_whole_ban设置全员禁言group_id: number/string, enable: boolean/string
set_group_admin设置群管理员group_id: number/string, user_id: number/string, enable: boolean/string
set_group_card设置群名片group_id: number/string, user_id: number/string, card: string
set_group_name设置群名称group_id: number/string, group_name: string
set_group_leave退出群聊group_id: number/string, is_dismiss: boolean/string(仅群主可用)
set_group_special_title设置专属头衔group_id: number/string, user_id: number/string, special_title: string
get_group_member_info获取群成员信息group_id: number/string, user_id: number/string, 可选 no_cache: boolean/string
get_group_member_list获取群成员列表group_id: number/string, 可选 no_cache: boolean/string
get_group_honor_info获取群荣誉信息group_id: number/string, 可选 type: string
get_essence_msg_list获取精华消息group_id: number/string
set_essence_msg设置精华消息message_id: number/string
delete_essence_msg删除精华消息message_id: number/string
group_poke群内戳一戳group_id: number/string, user_id: number/string
mark_group_msg_as_read标记群消息已读group_id: number/string, time: number
forward_group_single_msg转发单条群消息group_id: number/string, message_id: string
set_group_portrait设置群头像group_id: number/string, file: string, cache: number
_send_group_notice发送群公告group_id: number/string, content: string, 其他可选参数
_get_group_notice获取群公告group_id: number/string
_del_group_notice删除群公告group_id: number/string, notice_id: string
get_group_at_all_remain获取@全体成员剩余次数group_id: number/string
get_group_ignore_add_request获取群添加请求忽略列表无参数
get_group_ignored_notifies获取群通知忽略列表无参数
get_group_system_msg获取群系统消息无参数
get_group_shut_list获取群禁言列表group_id: number/string
set_group_remark设置群备注group_id: number/string, remark: string
set_group_sign设置群签到group_id: number/string
send_group_sign发送群签到group_id: number/string
消息相关 ​
接口字符串功能参数
send_msg发送消息message_type: string, user_id/group_id: number/string, message: string/array
get_record获取语音file: string, 可选 out_format: string
get_image获取图片file: string
can_send_image检查是否能发送图片无参数
can_send_record检查是否能发送语音无参数
get_file获取文件file: string, type: string
_mark_all_as_read标记所有消息为已读无参数
ocr_image图片OCR识别(标准)image: string
.ocr_image图片OCR识别(增强)image: string
get_recent_contact获取最近联系人count: number/string
send_poke发送戳一戳根据不同上下文需要不同参数
get_forward_msg获取合并转发消息message_id: string
mark_msg_as_read标记消息已读消息相关参数
文件相关 ​
接口字符串功能参数
upload_group_file上传群文件group_id: number/string, file: string, name: string, 可选 folder: string
delete_group_file删除群文件group_id: number/string, file_id: string, busid: number
create_group_file_folder创建群文件文件夹group_id: number/string, name: string
delete_group_folder删除群文件文件夹group_id: number/string, folder_id: string
get_group_file_system_info获取群文件系统信息group_id: number/string
get_group_root_files获取群根目录文件列表group_id: number/string
get_group_files_by_folder获取群子目录文件列表group_id: number/string, folder_id: string
get_group_file_url获取群文件链接group_id: number/string, file_id: string, busid: number
move_group_file移动群文件group_id: number/string, file_id: string, target_dir: string
trans_group_file转发群文件group_id: number/string, file_id: string, target_group_id: number/string
rename_group_file重命名群文件group_id: number/string, file_id: string, current_parent_directory: string, new_name: string
upload_private_file上传私聊文件user_id: number/string, file: string, name: string
get_private_file_url获取私聊文件URL文件相关参数
download_file下载文件url: string, thread_count: number, headers: string[]
AI 相关 ​
接口字符串功能参数
get_ai_characters获取AI角色列表无参数
get_ai_record获取AI语音character: string, group_id: number/string, text: string
send_group_ai_record发送群AI语音character: string, group_id: number/string, text: string
转发与分享 ​
接口字符串功能参数
send_group_forward_msg发送合并转发(群)group_id: number/string, messages: array
send_private_forward_msg发送合并转发(私聊)user_id: number/string, messages: array
send_forward_msg发送合并转发messages: array
ArkSharePeer分享联系人用户相关参数
ArkShareGroup分享群群相关参数
get_mini_app_ark获取小程序卡片小程序相关参数
其他功能 ​
接口字符串功能参数
get_cookies获取Cookies可选 domain: string
get_csrf_token获取CSRF Token无参数
get_credentials获取凭证信息可选 domain: string
get_doubt_friends_add_request获取可疑好友添加请求无参数
set_doubt_friends_add_request设置可疑好友添加请求请求相关参数
get_stranger_info获取陌生人信息user_id: number/string, 可选 no_cache: boolean
get_rkey获取Rkey无参数
click_inline_keyboard_button点击内联键盘按钮group_id: number/string, bot_appid: string, button_id: string, callback_data: string, msg_seq: string
translate_en2zh英文翻译成中文text: string
create_collection创建收藏收藏相关参数
get_collection_list获取收藏列表无参数
fetch_custom_face获取自定义表情表情相关参数
nc_get_packet_status获取数据包状态无参数
get_robot_uin_range获取机器人UIN范围无参数
get_guild_list获取频道列表无参数
get_guild_service_profile获取频道资料无参数
_get_model_show获取模型展示无参数
_set_model_show设置模型展示无参数
get_group_msg_history获取群消息历史group_id: number/string, count: number
check_url_safely检查URL安全性url: string
.get_word_slices获取词语切片content: string
.handle_quick_operation处理快速操作context: object, operation: object
send_packet发送数据包数据包相关参数
set_msg_emoji_like设置消息表情点赞消息和表情相关参数
get_online_clients获取在线客户端列表无参数
unknown未知操作未知参数

最后编辑于 5 天前
查看完整历史

cb48f6d-feat


---


## onebot/basic_event

OneBot 11 事件基础结构与消息结构 ​

字数

1558 字

阅读时间

8 分钟

1. 事件基础字段 ​
所有事件都包含以下基础字段：
字段名类型说明
timenumber事件发生的时间戳（秒）
post_typestring事件类型
self_idnumber收到事件的机器人 QQ 号
示例：
json{
 "time": 1718000000,
 "post_type": "message",
 "self_id": 123456789
}

2. 消息事件结构 ​
消息事件是最常见的事件类型，分为私聊消息和群消息。
2.1 私聊消息（OB11PrivateMessage） ​
字段名类型说明
timenumber事件发生时间戳
post_type'message' | 'message_sent'事件类型
message_type'private'消息类型：私聊
sub_type'friend'子类型：好友
message_idnumber消息 ID
user_idnumber发送者 QQ 号
messageOB11Segment[]消息段数组
raw_messagestring原始消息内容
fontnumber字体
target_id?number临时会话目标 QQ 号（可选）
temp_source?number临时会话来源（可选）
senderFriendSender发送者信息
self_idnumber机器人 QQ 号
私聊消息示例：
json{
 "time": 1718000000,
 "post_type": "message",
 "message_type": "private",
 "sub_type": "friend",
 "message_id": 1001,
 "user_id": 234567890,
 "message": [
 { "type": "text", "data": { "text": "你好" } }
 ],
 "raw_message": "你好",
 "font": 0,
 "sender": {
 "user_id": 234567890,
 "nickname": "小明",
 "sex": "male",
 "age": 18
 },
 "self_id": 123456789
}

临时会话私聊消息示例：
json{
 "time": 1718000002,
 "post_type": "message",
 "message_type": "private",
 "sub_type": "group",
 "message_id": 1002,
 "user_id": 234567891,
 "target_id": 987654321,
 "temp_source": 0,
 "message": [
 { "type": "text", "data": { "text": "临时会话消息" } }
 ],
 "raw_message": "临时会话消息",
 "font": 0,
 "sender": {
 "user_id": 234567891,
 "nickname": "小红",
 "sex": "female"
 },
 "self_id": 123456789
}

2.2 群消息（OB11GroupMessage） ​
字段名类型说明
timenumber事件发生时间戳
post_type'message' | 'message_sent'事件类型
message_type'group'消息类型：群聊
sub_type'normal' | 'anonymous' | 'notice'子类型
message_idnumber消息 ID
user_idnumber发送者 QQ 号
group_idnumber群号
messageOB11Segment[]消息段数组
raw_messagestring原始消息内容
fontnumber字体
senderGroupSender发送者信息
self_idnumber机器人 QQ 号
普通群消息示例：
json{
 "time": 1718000001,
 "post_type": "message",
 "message_type": "group",
 "sub_type": "normal",
 "message_id": 2002,
 "user_id": 345678901,
 "group_id": 987654321,
 "message": [
 { "type": "at", "data": { "qq": 123456789 } },
 { "type": "text", "data": { "text": "大家好！" } }
 ],
 "raw_message": "[CQ:at,qq=123456789]大家好！",
 "font": 0,
 "sender": {
 "user_id": 345678901,
 "nickname": "群友A",
 "sex": "female",
 "card": "管理员",
 "role": "admin"
 },
 "self_id": 123456789
}

3. 通知事件结构（Notice Event） ​
通知事件用于描述平台自动推送的各种状态变更、操作通知，如群成员变动、消息撤回、禁言等。
字段名类型说明
timenumber事件发生时间戳
post_type'notice'事件类型
self_idnumber收到事件的机器人 QQ 号
notice_typestring通知类型（见下表）
常见通知类型及主要字段：
notice_type说明主要字段补充说明
group_upload群文件上传group_id, user_id, file（id, name, size, busid）
group_admin群管理员变动sub_type: 'set'/'unset', group_id, user_id
group_decrease群成员减少sub_type: 'leave'/'kick'/'kick_me', group_id, operator_id, user_id
group_increase群成员增加sub_type: 'approve'/'invite', group_id, operator_id, user_id
group_ban群禁言sub_type: 'ban'/'lift_ban', group_id, operator_id, user_id, duration
friend_add新添加好友user_id
group_recall群消息撤回group_id, user_id, operator_id, message_id
friend_recall好友消息撤回user_id, message_id
poke戳一戳sub_type: 'poke', group_id?, user_id, target_id
lucky_king运气王sub_type: 'lucky_king', group_id, user_id, target_id
honor荣誉变更sub_type: 'honor', group_id, honor_type, user_id
group_msg_emoji_like群表情回应group_id, user_id/operator_id, message_id, likes/code, count
essence群精华sub_type: 'add'/'delete', group_id, message_id, sender_id, operator_id
group_card群名片变更group_id, user_id, card_new, card_old
群成员增加通知示例：
json{
 "time": 1718000010,
 "post_type": "notice",
 "notice_type": "group_increase",
 "group_id": 987654321,
 "operator_id": 123456789,
 "user_id": 345678902,
 "sub_type": "invite",
 "self_id": 123456789
}

群禁言通知示例：
json{
 "time": 1718000011,
 "post_type": "notice",
 "notice_type": "group_ban",
 "group_id": 987654321,
 "operator_id": 123456789,
 "user_id": 345678903,
 "duration": 600,
 "sub_type": "ban",
 "self_id": 123456789
}

4. 请求事件结构（Request Event） ​
请求事件用于描述需要机器人处理的请求，如加好友、加群等。
字段名类型说明
timenumber事件发生时间戳
post_type'request'事件类型
self_idnumber收到事件的机器人 QQ 号
request_type'friend'/'group'请求类型
flagstring请求 flag
user_idnumber发送请求的 QQ 号
commentstring验证信息
不同请求类型的补充字段：
request_type说明主要字段补充说明
friend好友请求无
group群请求sub_type: 'add'（加群申请）/'invite'（被邀请入群），group_id
加好友请求示例：
json{
 "time": 1718000020,
 "post_type": "request",
 "request_type": "friend",
 "flag": "request_flag_1",
 "user_id": 456789012,
 "comment": "我是机器人粉丝",
 "self_id": 123456789
}

加群申请请求示例：
json{
 "time": 1718000021,
 "post_type": "request",
 "request_type": "group",
 "sub_type": "add",
 "group_id": 987654321,
 "flag": "request_flag_2",
 "user_id": 456789013,
 "comment": "想加入群聊",
 "self_id": 123456789
}

5. 消息段结构（OB11Segment） ​
每条消息由若干消息段（Segment）组成，每个消息段包含类型和对应数据。
字段名类型说明
typestring段落类型（如 'text'）
dataobject各类型对应的数据内容
常见 type 及 data 字段说明：
text：{ text: string } —— 纯文本内容
image：{ file: string, url?: string, ... } —— 图片
at：{ qq: number } —— @某人
face：{ id: number } —— QQ 表情
reply：{ id: number } —— 回复消息
消息段示例：
json[
 { "type": "text", "data": { "text": "你好" } },
 { "type": "image", "data": { "file": "abc.jpg", "url": "http://..." } },
 { "type": "at", "data": { "qq": 123456789 } },
 { "type": "face", "data": { "id": 123 } },
 { "type": "reply", "data": { "id": 1001 } }
]

6. 发送者信息结构 ​
6.1 FriendSender（私聊发送者） ​
字段名类型说明
user_idnumber发送者 QQ 号
nicknamestring昵称
sex'male' / 'female' / 'unknown'性别
group_idnumber?群临时会话群号（可选）
私聊发送者示例：
json{
 "user_id": 234567890,
 "nickname": "小明",
 "sex": "male"
}

6.2 GroupSender（群聊发送者） ​
字段名类型说明
user_idnumber发送者 QQ 号
nicknamestring昵称
sex'male' / 'female' / 'unknown'性别
cardstring?群名片/备注（可选）
role'owner' / 'admin' / 'member'角色
群聊发送者示例：
json{
 "user_id": 345678901,
 "nickname": "群友A",
 "sex": "female",
 "card": "管理员",
 "role": "admin"
}

说明：
字段后带 ? 表示该字段为可选项。
消息段（OB11Segment）可包含多种类型，具体内容以实际消息为准。
发送者信息结构根据消息类型（私聊/群聊）有所不同。

最后编辑于 超过 1 年前
查看完整历史

cb48f6d-feat


---


## onebot/event

OneBot 事件系统结构详解 ​

字数

2297 字

阅读时间

11 分钟

本文档详细说明 OneBot 事件系统的架构、事件类型及其继承关系
开篇讲解 ​
NapCat 迭代周期非常快，如果你需要准确靠谱的定义应当 源代码 查看.
这部分并不复杂，如果你有 IDE 并初始化依赖，可以轻松理解这部分的字段和定义。
目录 ​
基础事件结构
元事件 (Meta Event)
通知事件 (Notice Event)
请求事件 (Request Event)
消息事件 (Message Event)
事件继承关系总结
OneBot 事件系统包含多种不同类型的事件，所有事件都继承自 OneBotEvent 基类。事件按照类型分为四大类：元事件（Meta）、通知事件（Notice）、请求事件（Request）和消息事件（Message）。
基础事件结构 ​
OneBotEvent (基类) ​
所有事件的基类，定义了共有字段。
typescriptabstract class OneBotEvent {
 time: number; // 事件发生的时间戳
 self_id: number; // 机器人自身 QQ 号
 abstract post_type: EventType; // 事件类型
}

事件类型枚举 ​
typescriptenum EventType {
 META = 'meta_event', // 元事件
 REQUEST = 'request', // 请求事件
 NOTICE = 'notice', // 通知事件
 MESSAGE = 'message', // 消息事件
 MESSAGE_SENT = 'message_sent', // 消息发送事件
}

元事件 (Meta Event) ​
元事件是与协议相关的事件，如心跳、生命周期等
OB11BaseMetaEvent ​
typescriptabstract class OB11BaseMetaEvent extends OneBotEvent {
 post_type = EventType.META;
 abstract meta_event_type: string; // 元事件类型
}

OB11HeartbeatEvent ​
心跳事件，用于确认连接状态
typescriptinterface HeartbeatStatus {
 online: boolean | undefined, // 是否在线
 good: boolean // 状态是否良好
}

class OB11HeartbeatEvent extends OB11BaseMetaEvent {
 meta_event_type = 'heartbeat'; // 心跳事件
 status: HeartbeatStatus; // 状态信息
 interval: number; // 心跳间隔时间(ms)
}

OB11LifeCycleEvent ​
生命周期事件，用于通知框架生命周期变化
typescriptenum LifeCycleSubType {
 ENABLE = 'enable', // 启用
 DISABLE = 'disable', // 禁用
 CONNECT = 'connect' // 连接
}

class OB11LifeCycleEvent extends OB11BaseMetaEvent {
 meta_event_type = 'lifecycle'; // 生命周期事件
 sub_type: LifeCycleSubType; // 子类型
}

通知事件 (Notice Event) ​
通知事件用于接收各类通知，如好友添加、群组变动等
OB11BaseNoticeEvent ​
所有通知事件的基类
typescriptabstract class OB11BaseNoticeEvent extends OneBotEvent {
 post_type = EventType.NOTICE;
 // 具体通知类型在子类中定义
}

群组通知事件基类 ​
处理群相关的通知事件
typescriptabstract class OB11GroupNoticeEvent extends OB11BaseNoticeEvent {
 group_id: number; // 群号
 user_id: number; // 用户 QQ 号
}

好友添加通知 ​
typescriptclass OB11FriendAddNoticeEvent extends OB11BaseNoticeEvent {
 notice_type = 'friend_add'; // 好友添加通知
 user_id: number; // 新好友 QQ 号
}

好友消息撤回通知 ​
typescriptclass OB11FriendRecallNoticeEvent extends OB11BaseNoticeEvent {
 notice_type = 'friend_recall'; // 好友消息撤回
 user_id: number; // 消息发送者 QQ 号
 message_id: number; // 被撤回的消息 ID
}

群消息撤回通知 ​
typescriptclass OB11GroupRecallNoticeEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_recall'; // 群消息撤回
 operator_id: number; // 操作者 QQ 号
 message_id: number; // 被撤回的消息 ID
}

群成员增加通知 ​
typescriptclass OB11GroupIncreaseEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_increase'; // 群成员增加
 operator_id: number; // 操作者 QQ 号
 sub_type: 'approve' | 'invite'; // 子类型：同意加群/邀请加群
}

群成员减少通知 ​
typescripttype GroupDecreaseSubType = 'leave' | 'kick' | 'kick_me' | 'disband';

class OB11GroupDecreaseEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_decrease'; // 群成员减少
 sub_type: GroupDecreaseSubType; // 子类型：主动退群/被踢/我被踢/群解散
 operator_id: number; // 操作者 QQ 号
}

群管理员变动通知 ​
typescriptclass OB11GroupAdminNoticeEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_admin'; // 群管理员变动
 sub_type: 'set' | 'unset'; // 设置/取消管理员
}

群禁言通知 ​
typescriptclass OB11GroupBanEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_ban'; // 群禁言
 operator_id: number; // 操作者 QQ 号
 duration: number; // 禁言时长(秒)
 sub_type: 'ban' | 'lift_ban'; // 禁言/解除禁言
}

群文件上传通知 ​
typescriptinterface GroupUploadFile {
 id: string, // 文件 ID
 name: string, // 文件名
 size: number, // 文件大小(Byte)
 busid: number, // 文件总线 ID
}

class OB11GroupUploadNoticeEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_upload'; // 群文件上传
 file: GroupUploadFile; // 文件信息
}

群名片变更通知 ​
typescriptclass OB11GroupCardEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_card'; // 群名片变更
 card_new: string; // 新名片
 card_old: string; // 旧名片
}

群名变更通知 ​
typescriptclass OB11GroupNameEvent extends OB11GroupNoticeEvent {
 notice_type = 'notify'; // 通知
 sub_type = 'group_name'; // 群名变更
 name_new: string; // 新群名
}

群头衔变更通知 ​
typescriptclass OB11GroupTitleEvent extends OB11GroupNoticeEvent {
 notice_type = 'notify'; // 通知
 sub_type = 'title'; // 头衔变更
 title: string; // 新头衔
}

群精华消息通知 ​
typescriptclass OB11GroupEssenceEvent extends OB11GroupNoticeEvent {
 notice_type = 'essence'; // 精华消息
 message_id: number; // 消息 ID
 sender_id: number; // 消息发送者 QQ 号
 operator_id: number; // 操作者 QQ 号
 sub_type: 'add' | 'delete'; // 添加/删除精华
}

群灰条消息通知 ​
typescriptexport class OB11GroupGrayTipEvent extends OB11BaseNoticeEvent {
 notice_type = 'notify'; // 通知
 sub_type = 'gray_tip'; // 群灰条
 group_id: number; // 收取群号
 user_id: number; // 真实发送者QQ（如果是伪造的灰条，这就是攻击者）
 message_id: number; // 消息ID，可用于撤回
 busi_id: string; // 业务ID
 content: string; // 灰条内容（JSON字符串）
 raw_info: unknown; // 原始信息
}

表情回应通知 ​
typescriptinterface MsgEmojiLike {
 emoji_id: string, // 表情 ID
 count: number // 回应数量
}

class OB11GroupMsgEmojiLikeEvent extends OB11GroupNoticeEvent {
 notice_type = 'group_msg_emoji_like'; // 表情回应
 message_id: number; // 消息 ID
 likes: MsgEmojiLike[]; // 表情信息列表
}

戳一戳通知 ​
typescriptclass OB11PokeEvent extends OB11BaseNoticeEvent {
 notice_type = 'notify'; // 通知
 sub_type = 'poke'; // 戳一戳
 target_id: number; // 被戳者 QQ 号
 user_id: number; // 戳者 QQ 号
}

class OB11FriendPokeEvent extends OB11PokeEvent {
 raw_info: unknown; // 原始信息
 sender_id: number; // 发送者 QQ 号
}

class OB11GroupPokeEvent extends OB11PokeEvent {
 group_id: number; // 群号
 raw_info: unknown; // 原始信息
}

个人资料点赞通知 ​
typescriptclass OB11ProfileLikeEvent extends OB11BaseNoticeEvent {
 notice_type = 'notify'; // 通知
 sub_type = 'profile_like'; // 资料点赞
 operator_id: number; // 操作者 QQ 号
 operator_nick: string; // 操作者昵称
 times: number; // 点赞次数
 time: number; // 时间戳
}

输入状态通知 ​
typescriptclass OB11InputStatusEvent extends OB11BaseNoticeEvent {
 notice_type = 'notify'; // 通知
 sub_type = 'input_status'; // 输入状态
 status_text: string; // 状态文本
 event_type: number; // 事件类型
 user_id: number; // 用户 QQ 号
 group_id: number; // 群号(如适用)
}

机器人离线通知 ​
typescriptclass BotOfflineEvent extends OB11BaseNoticeEvent {
 notice_type = 'bot_offline'; // 机器人离线
 user_id: number; // 机器人 QQ 号
 tag: string; // 标签
 message: string; // 离线消息
}

请求事件 (Request Event) ​
请求事件用于处理各类需要回应的请求，如好友请求、加群请求等
好友请求事件 ​
typescriptclass OB11FriendRequestEvent extends OB11BaseNoticeEvent {
 post_type = EventType.REQUEST; // 请求事件
 request_type = 'friend'; // 好友请求
 user_id: number; // 请求者 QQ 号
 comment: string; // 验证信息
 flag: string; // 请求标识
}

群请求事件 ​
typescriptclass OB11GroupRequestEvent extends OB11GroupNoticeEvent {
 post_type = EventType.REQUEST; // 请求事件
 request_type = 'group'; // 群请求
 user_id: number; // 请求者 QQ 号
 comment: string; // 验证信息
 flag: string; // 请求标识
 sub_type: string; // 请求子类型
}

消息事件 (Message Event) ​
消息事件用于接收各类消息，包括私聊和群聊消息
OB11BaseMessageEvent ​
所有消息事件的基类
typescriptabstract class OB11BaseMessageEvent extends OneBotEvent {
 post_type = EventType.MESSAGE; // 消息事件
 // 具体消息类型在子类中定义
 message_id: number; // 消息 ID
 user_id: number; // 发送者 QQ 号
 message: string | any[]; // 消息内容
 raw_message: string; // 原始消息内容
}

私聊消息事件 ​
typescriptclass OB11PrivateMessageEvent extends OB11BaseMessageEvent {
 message_type = 'private'; // 私聊消息
 sub_type: 'friend' | 'group' | 'other'; // 子类型
 sender: { // 发送者信息
 user_id: number, // QQ 号
 nickname: string, // 昵称
 sex: 'male' | 'female' | 'unknown', // 性别
 age: number // 年龄
 };
}

群聊消息事件 ​
typescriptclass OB11GroupMessageEvent extends OB11BaseMessageEvent {
 message_type = 'group'; // 群聊消息
 group_id: number; // 群号
 anonymous: any | null; // 匿名信息
 sender: { // 发送者信息
 user_id: number, // 发送者 QQ 号
 nickname: string, // 昵称
 card: string, // 群名片
 role: 'owner' | 'admin' | 'member', // 角色
 title: string, // 专属头衔
 level: string // 成员等级
 };
}

消息发送事件 ​
typescriptclass OB11MessageSentEvent extends OB11BaseMessageEvent {
 post_type = EventType.MESSAGE_SENT; // 消息发送事件
 message_type: 'private' | 'group'; // 消息类型
 target_id: number; // 目标 ID（好友 QQ 号或群号）
 // 其他字段根据消息类型不同而变化
}

事件继承关系总结 ​

事件类型总览表 ​
事件类型描述主要子类型
元事件 (Meta)与协议相关的系统事件心跳、生命周期
通知事件 (Notice)各类通知事件好友添加、群组变动、消息撤回等
请求事件 (Request)需要回应的请求事件好友请求、加群请求
消息事件 (Message)接收和发送的消息私聊消息、群聊消息
事件处理流程 ​
接收事件数据
根据 post_type 字段识别事件大类
根据具体事件类型（如 notice_type、meta_event_type 等）确定子类型
实例化对应的事件对象
传递给事件处理器进行处理

最后编辑于 7 个月前
查看完整历史

888a7fa-Add GroupGrayTipEvent to event.md (#118)

420c967-在中文、英文以及数字混排时添加空格分隔 #2

cb48f6d-feat


---


## onebot

NapCat-OneBot 实现 ​

字数

184 字

阅读时间

1 分钟

NapCat 尽量遵守了大部分 OneBot 规范。在遇到无法实现或需要扩展的场景时，会进行差异化实现。
请注意，OneBot 是一个已经脱轨且停滞的协议规范，对框架本身没有实质性约束。
文档导航 ​
网络通讯基础
事件基础结构
事件字段详情
接口基础接口
消息元素定义
差异实现说明
提示： 建议开发者按照上述导航顺序阅读文档，全面了解 NapCat 对 OneBot 的实现细节与差异，便于高效开发与集成。


---


## onebot/index

NapCat-OneBot 实现 ​

字数

182 字

阅读时间

1 分钟

NapCat 尽量遵守了大部分 OneBot 规范。在遇到无法实现或需要扩展的场景时，会进行差异化实现。
请注意，OneBot 是一个已经脱轨且停滞的协议规范，对框架本身没有实质性约束。
文档导航 ​
网络通讯基础
事件基础结构
事件字段详情
基础接口
消息元素定义
差异实现说明
提示： 建议开发者按照上述导航顺序阅读文档，全面了解 NapCat 对 OneBot 的实现细节与差异，便于高效开发与集成。


---


## onebot/napcat

NapCat 资源与消息 ID 设计说明 ​

字数

391 字

阅读时间

2 分钟

NapCat 由于无数据库设计，采用了 LRU（最近最少使用）缓存机制来管理消息和文件资源。消息的 ID 并非连续数字，而是基于哈希算法生成的完全正整数。每条消息的 ID 都是唯一的，且在大约 5000 条消息后会因 LRU 策略而过期并被清理。文件（file）标识的生成同样受 LRU 缓存机制管理。
⚠️ 由于 NapCat 不存储历史数据，已撤回的消息无法被再次获取或恢复，请注意消息的时效性。
NapCat 资源 URL 参数类型 ​
NapCat 支持多种资源 URL 规范，便于灵活引用和传递文件资源。主要支持以下几种格式：
base64 以 base64:// 协议开头，内容为 base64 编码的文件数据。
 例如：
base64://iVBORw0KGgoAAAANSUhEUgAA...

path
 本地文件路径，适用于本地资源访问。
 例如：
C:/Users/xxx/Pictures/image.png

fileurl
 NapCat 规范的文件 URL，通常用于内部文件标识。
 例如：
file://1234567890
 其中 1234567890 为 NapCat 生成的文件哈希 ID。

http/https
 标准的网络资源 URL。
 例如：
https://example.com/image.png

dataurl-base64
 以 data: 协议开头，内容为 base64 编码的文件数据。
 例如：
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...

通过上述设计，NapCat 能够高效地管理消息和文件资源，既保证了唯一性和安全性，又兼顾了资源的灵活访问与过期清理。

最后编辑于 超过 1 年前
查看完整历史

eec6230-fix

cb48f6d-feat


---


## onebot/network

OneBot 网络基础 ​

字数

1098 字

阅读时间

5 分钟

本章节介绍 NapCatQQ 与 OneBot 11 进行 HTTP 和 WebSocket 通信的基本方式。请根据 NapCatQQ 的实际部署角色选择合适的通信模式。
1. HTTP 通信 ​
OneBot 11 的 HTTP 通信分为两种角色：
HTTP 客户端：NapCatQQ 作为客户端，向 OneBot 11 的 HTTP API 主动发送请求（如发送消息）。
HTTP 服务器：NapCatQQ 作为服务器，接收 OneBot 11 推送的事件（event push）。
1.1 NapCatQQ 作为 HTTP 客户端发送请求 ​
NapCatQQ 可以通过 HTTP POST 请求向 OneBot 11 的 API 地址发送指令。
示例：发送私聊消息
httpPOST http://<host>:<port>/send_private_msg
Content-Type: application/json

{
 "user_id": 123456789,
 "message": "你好，NapCatQQ！"
}

返回示例：
json{
 "status": "ok",
 "retcode": 0,
 "data": {
 "message_id": 1234
 }
}

代码演示：Python HTTP 客户端发送 API 请求
pythonimport requests

url = "http://<host>:<port>/send_private_msg"
payload = {
 "user_id": 123456789,
 "message": "你好，NapCatQQ！"
}
resp = requests.post(url, json=payload)
print(resp.json())

🐱‍💻 小贴士：别忘了替换 <host>:<port> 为实际的 OneBot 11 地址哦！如果遇到连接失败，记得检查防火墙和 API 是否开启。
1.2 NapCatQQ 作为 HTTP 服务器接收事件 ​
要接收事件，需要配置 OneBot 11 的 HTTP 上报（event push），即让 OneBot 11 向 NapCatQQ 指定的 HTTP 服务器推送事件数据。NapCatQQ 需要实现一个 HTTP 服务器，监听 POST 请求，解析收到的 JSON 数据。
事件推送示例：
json{
 "post_type": "message",
 "message_type": "private",
 "user_id": 123456789,
 "message": "你好"
}

代码演示：Python HTTP 服务器接收事件
pythonfrom flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_event():
 event = request.json
 print("收到事件：", event)
 return "OK"

if __name__ == "__main__":
 app.run(port=8080)

🐱‍👓 小提醒：Flask 默认监听 127.0.0.1，如需外部访问请加 host="0.0.0.0"。别忘了安装 Flask：pip install flask！
2. WebSocket 通信 ​
WebSocket 通信同样分为两种角色：
WebSocket 客户端：NapCatQQ 作为客户端，主动连接 OneBot 11 的 WebSocket 服务端，进行双向通信。
WebSocket 服务器：NapCatQQ 作为服务器，OneBot 11 作为客户端主动连接 NapCatQQ 的 WebSocket 服务端，推送事件和处理请求。
2.1 NapCatQQ 作为 WebSocket 客户端 ​
NapCatQQ 通过 WebSocket 连接到 OneBot 11 的 ws 或 wss 地址。连接建立后，发送 JSON 格式的事件和处理请求。
发送群消息示例：
json{
 "action": "send_group_msg",
 "params": {
 "group_id": 123456,
 "message": "大家好！"
 },
 "echo": "自定义标识"
}

响应示例：
json{
 "status": "ok",
 "retcode": 0,
 "data": {
 "message_id": 5678
 },
 "echo": "自定义标识"
}

事件推送示例：
json{
 "post_type": "message",
 "message_type": "group",
 "group_id": 123456,
 "user_id": 654321,
 "message": "你好"
}

代码演示：Python WebSocket 客户端接收事件
pythonimport asyncio
import websockets
import json

async def main():
 uri = "ws://<host>:<port>/"
 async with websockets.connect(uri) as ws:
 # 发送请求
 req = {
 "action": "send_group_msg",
 "params": {"group_id": 123456, "message": "大家好！"},
 "echo": "test"
 }
 await ws.send(json.dumps(req))
 # 接收响应或事件
 while True:
 msg = await ws.recv()
 print("收到消息：", msg)

asyncio.run(main())

🐱‍🚀 温馨提示：记得安装 websockets 库：pip install websockets。WebSocket 地址要写对，wss 代表加密连接哦！
2.2 NapCatQQ 作为 WebSocket 服务器接收事件和请求 ​
NapCatQQ 也可以实现 WebSocket 服务器，让 OneBot 11 作为客户端主动连接 NapCatQQ 的服务器。连接建立后，OneBot 11 会通过该连接推送事件和接收 NapCatQQ 的请求。NapCatQQ 需要处理来自 OneBot 11 的消息，并根据需要发送请求。
代码演示：Python WebSocket 服务器接收事件和请求
pythonimport asyncio
import websockets

async def handler(websocket, path):
 async for message in websocket:
 print("收到消息：", message)
 # 可根据需要回复消息
 # await websocket.send(...)

start_server = websockets.serve(handler, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

🐱‍🏍 小技巧：服务器监听 0.0.0.0 可让外部设备访问。别忘了端口不要被占用，否则会启动失败！
总结 ​
HTTP 支持 NapCatQQ 作为客户端（主动请求）和服务器（被动接收事件）两种模式。
WebSocket 支持 NapCatQQ 作为客户端（主动连接 OneBot 11）和服务器（被动接收 OneBot 11 连接）两种模式，推荐优先使用 WebSocket，实时性更好。
🐾 最后提醒：接口字段、端口、地址等都要和实际环境对应，小粗心是不行的！

最后编辑于 超过 1 年前
查看完整历史

2c2ecef-fix

cb48f6d-feat


---


## onebot/segment

OneBot 11 消息段类型详解文档 ​

字数

1662 字

阅读时间

8 分钟

概述 ​
OneBot 11 协议定义了多种消息段类型，用于表示不同类型的消息内容。本文档详细介绍这些消息段的类型、数据结构及其用途，帮助开发者更好地理解和使用 OneBot 11 消息格式。
基本结构 ​
每个 OneBot 11 消息段都遵循以下基本结构：
typescriptinterface OB11MessageData {
 type: OB11MessageDataType; // 消息段类型
 data: any; // 根据类型不同，包含不同的数据字段
}

文本类消息段 ​
1. 文本消息 (text) ​
用于发送纯文本内容。
发送时字段:
text: 要发送的文本内容
接收时字段:
text: 接收到的文本内容
typescript{
 type: "text",
 data: {
 text: string
 }
}

2. @提及 (at) ​
用于在消息中 @ 特定用户或全体成员。
发送时字段:
qq: 要 @ 的 QQ 号，使用 "all" 表示 @全体成员
接收时字段:
qq: 被 @ 的 QQ 号或 "all"
typescript{
 type: "at",
 data: {
 qq: string
 }
}

3. 回复 (reply) ​
用于回复特定消息。
发送时字段:
id: 被回复消息的唯一 ID
接收时字段:
id: 被回复消息的唯一 ID
typescript{
 type: "reply",
 data: {
 id: string
 }
}

表情类消息段 ​
1. QQ 表情 (face) ​
用于发送QQ内置表情。
发送时字段:
id: 表情 ID
接收时字段:
id: 表情 ID
raw: 表情原始数据
resultId: 骰子或石头剪刀布结果 ID
chainCount: 连续发送次数
typescript{
 type: "face",
 data: {
 id: string,
 raw?: any,
 resultId?: string,
 chainCount?: number
 }
}

2. 商城表情 (mface) ​
用于发送QQ商城表情。
发送时字段:
emoji_id: 表情 ID
emoji_package_id: 表情包 ID
key: 表情 key
summary: 表情名称
接收时字段:
通常转换为image类型，包含额外字段: key: 表情 key
emoji_id: 表情 ID
emoji_package_id: 表情包 ID

typescript{
 type: "mface",
 data: {
 emoji_id: string,
 emoji_package_id: string,
 key?: string,
 summary?: string
 }
}

3. 骰子 (dice) ​
用于发送骰子表情。
发送时字段:
无需特定字段，系统会随机生成结果
接收时字段:
result: 骰子点数结果(1-6)
typescript{
 type: "dice",
 data: {
 result: string
 }
}

4. 石头剪刀布 (rps) ​
用于发送石头剪刀布表情。
发送时字段:
无需特定字段，系统会随机生成结果
接收时字段:
result: 石头剪刀布结果(1-3，分别代表石头、剪刀、布)
typescript{
 type: "rps",
 data: {
 result: string
 }
}

5. 戳一戳 (poke) ​
用于发送戳一戳消息。
发送时字段:
type: 戳一戳类型
id: 戳一戳 ID
接收时字段:
type: 戳一戳类型
id: 戳一戳 ID
typescript{
 type: "poke",
 data: {
 type: string,
 id: string
 }
}

多媒体类消息段 ​
1. 图片消息 (image) ​
用于发送图片。
发送时字段:
file: 图片文件路径、URL 或 Base64 编码
url: 图片 URL(可选)
summary: 图片描述(可选)
sub_type: 图片子类型(可选)
接收时字段:
file: 图片文件名
url: 图片在线 URL
summary: 图片描述
sub_type: 图片子类型
file_size: 文件大小(字节)
如果是商城表情转换而来，还会包含： key: 表情 key
emoji_id: 表情 ID
emoji_package_id: 表情包 ID

typescript{
 type: "image",
 data: {
 file: string,
 url?: string,
 summary?: string,
 sub_type?: number,
 file_size?: number,
 key?: string,
 emoji_id?: string,
 emoji_package_id?: string
 }
}

2. 语音 (record) ​
用于发送语音消息。
发送时字段:
file: 语音文件路径、URL 或 Base64 编码
接收时字段:
file: 语音文件标识
file_size: 文件大小(字节)
path: 文件路径
typescript{
 type: "record",
 data: {
 file: string,
 file_size?: number,
 path?: string
 }
}

3. 视频 (video) ​
用于发送视频。
发送时字段:
file: 视频文件路径、URL 或 Base64 编码
thumb: 视频缩略图(可选)
接收时字段:
file: 视频文件标识
url: 视频在线 URL
file_size: 文件大小(字节)
typescript{
 type: "video",
 data: {
 file: string,
 url?: string,
 file_size?: number,
 thumb?: string
 }
}

4. 文件 (file) ​
用于发送文件。
发送时字段:
file: 文件路径、URL 或 Base64 编码
name: 文件名(可选)
接收时字段:
file: 文件名
file_id: 文件 ID
file_size: 文件大小(字节)
typescript{
 type: "file",
 data: {
 file: string,
 file_id?: string,
 file_size?: number
 }
}

富媒体类消息段 ​
1. JSON消息 (json) ​
用于发送JSON格式的卡片消息。
发送时字段:
data: JSON 字符串或对象
接收时字段:
data: JSON 数据
typescript{
 type: "json",
 data: {
 data: string | object
 }
}

2. 音乐分享 (music) ​
用于分享音乐，仅支持发送，接收时会转换为 json 类型。
发送时字段:
type: 音乐平台(qq、163、kugou、kuwo、migu、custom)
id: 音乐 ID(平台非 custom 时必填)
url: 音乐链接(custom 时必填)
image: 封面图片(custom 时必填)
singer: 歌手(可选)
title: 标题(可选)
content: 内容描述(可选)
typescript{
 type: "music",
 data: {
 type: string,
 id?: string,
 url?: string,
 image?: string,
 singer?: string,
 title?: string,
 content?: string
 }
}

3. 转发消息 (forward) ​
用于发送合并转发消息。
发送时字段:
id: 转发消息ID
接收时字段:
id: 转发消息 ID
content: 转发的消息内容列表(仅当解析转发内容时)
typescript{
 type: "forward",
 data: {
 id: string,
 content?: OB11Message[]
 }
}

消息段组合演示 ​
多个消息段可以组合成一个完整的消息，按顺序依次发送。例如：
typescriptconst message: OB11MessageData[] = [
 {
 type: "at",
 data: { qq: "12345678" }
 },
 {
 type: "text",
 data: { text: "你好，这是一条带图片和语音的消息。" }
 },
 {
 type: "image",
 data: { file: "https://example.com/image.jpg", summary: "示例图片" }
 }
];

每个元素为一个消息段，最终会被依次拼接发送，效果为：@某人 + 文本 + 图片 + 语音。

最后编辑于 4 个月前
查看完整历史

c9b6a5e-修正文件名拼写、导航链接 (#127)

420c967-在中文、英文以及数字混排时添加空格分隔 #2

4c401e3-在中文、英文以及数字混排时添加空格分隔

cb48f6d-feat


---


## onebot/sement

OneBot 11 消息段类型详解文档 ​

字数

1662 字

阅读时间

8 分钟

概述 ​
OneBot 11 协议定义了多种消息段类型，用于表示不同类型的消息内容。本文档详细介绍这些消息段的类型、数据结构及其用途，帮助开发者更好地理解和使用 OneBot 11 消息格式。
基本结构 ​
每个 OneBot 11 消息段都遵循以下基本结构：
typescriptinterface OB11MessageData {
 type: OB11MessageDataType; // 消息段类型
 data: any; // 根据类型不同，包含不同的数据字段
}

文本类消息段 ​
1. 文本消息 (text) ​
用于发送纯文本内容。
发送时字段:
text: 要发送的文本内容
接收时字段:
text: 接收到的文本内容
typescript{
 type: "text",
 data: {
 text: string
 }
}

2. @提及 (at) ​
用于在消息中@特定用户或全体成员。
发送时字段:
qq: 要@的QQ号，使用"all"表示@全体成员
接收时字段:
qq: 被@的QQ号或"all"
typescript{
 type: "at",
 data: {
 qq: string
 }
}

3. 回复 (reply) ​
用于回复特定消息。
发送时字段:
id: 被回复消息的唯一ID
接收时字段:
id: 被回复消息的唯一ID
typescript{
 type: "reply",
 data: {
 id: string
 }
}

表情类消息段 ​
1. QQ表情 (face) ​
用于发送QQ内置表情。
发送时字段:
id: 表情ID
接收时字段:
id: 表情ID
raw: 表情原始数据
resultId: 骰子或石头剪刀布结果ID
chainCount: 连续发送次数
typescript{
 type: "face",
 data: {
 id: string,
 raw?: any,
 resultId?: string,
 chainCount?: number
 }
}

2. 商城表情 (mface) ​
用于发送QQ商城表情。
发送时字段:
emoji_id: 表情ID
emoji_package_id: 表情包ID
key: 表情key
summary: 表情名称
接收时字段:
通常转换为image类型，包含额外字段: key: 表情key
emoji_id: 表情ID
emoji_package_id: 表情包ID

typescript{
 type: "mface",
 data: {
 emoji_id: string,
 emoji_package_id: string,
 key?: string,
 summary?: string
 }
}

3. 骰子 (dice) ​
用于发送骰子表情。
发送时字段:
无需特定字段，系统会随机生成结果
接收时字段:
result: 骰子点数结果(1-6)
typescript{
 type: "dice",
 data: {
 result: string
 }
}

4. 石头剪刀布 (rps) ​
用于发送石头剪刀布表情。
发送时字段:
无需特定字段，系统会随机生成结果
接收时字段:
result: 石头剪刀布结果(1-3，分别代表石头、剪刀、布)
typescript{
 type: "rps",
 data: {
 result: string
 }
}

5. 戳一戳 (poke) ​
用于发送戳一戳消息。
发送时字段:
type: 戳一戳类型
id: 戳一戳ID
接收时字段:
type: 戳一戳类型
id: 戳一戳ID
typescript{
 type: "poke",
 data: {
 type: string,
 id: string
 }
}

多媒体类消息段 ​
1. 图片消息 (image) ​
用于发送图片。
发送时字段:
file: 图片文件路径、URL或Base64编码
url: 图片URL(可选)
summary: 图片描述(可选)
sub_type: 图片子类型(可选)
接收时字段:
file: 图片文件名
url: 图片在线URL
summary: 图片描述
sub_type: 图片子类型
file_size: 文件大小(字节)
如果是商城表情转换而来，还会包含： key: 表情key
emoji_id: 表情ID
emoji_package_id: 表情包ID

typescript{
 type: "image",
 data: {
 file: string,
 url?: string,
 summary?: string,
 sub_type?: number,
 file_size?: number,
 key?: string,
 emoji_id?: string,
 emoji_package_id?: string
 }
}

2. 语音 (record) ​
用于发送语音消息。
发送时字段:
file: 语音文件路径、URL或Base64编码
接收时字段:
file: 语音文件标识
file_size: 文件大小(字节)
path: 文件路径
typescript{
 type: "record",
 data: {
 file: string,
 file_size?: number,
 path?: string
 }
}

3. 视频 (video) ​
用于发送视频。
发送时字段:
file: 视频文件路径、URL或Base64编码
thumb: 视频缩略图(可选)
接收时字段:
file: 视频文件标识
url: 视频在线URL
file_size: 文件大小(字节)
typescript{
 type: "video",
 data: {
 file: string,
 url?: string,
 file_size?: number,
 thumb?: string
 }
}

4. 文件 (file) ​
用于发送文件。
发送时字段:
file: 文件路径、URL或Base64编码
name: 文件名(可选)
接收时字段:
file: 文件名
file_id: 文件ID
file_size: 文件大小(字节)
typescript{
 type: "file",
 data: {
 file: string,
 file_id?: string,
 file_size?: number
 }
}

富媒体类消息段 ​
1. JSON消息 (json) ​
用于发送JSON格式的卡片消息。
发送时字段:
data: JSON字符串或对象
接收时字段:
data: JSON数据
typescript{
 type: "json",
 data: {
 data: string | object
 }
}

2. 音乐分享 (music) ​
用于分享音乐，仅支持发送，接收时会转换为json类型。
发送时字段:
type: 音乐平台(qq、163、kugou、kuwo、migu、custom)
id: 音乐ID(平台非custom时必填)
url: 音乐链接(custom时必填)
image: 封面图片(custom时必填)
singer: 歌手(可选)
title: 标题(可选)
content: 内容描述(可选)
typescript{
 type: "music",
 data: {
 type: string,
 id?: string,
 url?: string,
 image?: string,
 singer?: string,
 title?: string,
 content?: string
 }
}

3. 转发消息 (forward) ​
用于发送合并转发消息。
发送时字段:
id: 转发消息ID
接收时字段:
id: 转发消息ID
content: 转发的消息内容列表(仅当解析转发内容时)
typescript{
 type: "forward",
 data: {
 id: string,
 content?: OB11Message[]
 }
}

消息段组合演示 ​
多个消息段可以组合成一个完整的消息，按顺序依次发送。例如：
typescriptconst message: OB11MessageData[] = [
 {
 type: "at",
 data: { qq: "12345678" }
 },
 {
 type: "text",
 data: { text: "你好，这是一条带图片和语音的消息。" }
 },
 {
 type: "image",
 data: { file: "https://example.com/image.jpg", summary: "示例图片" }
 }
];

每个元素为一个消息段，最终会被依次拼接发送，效果为：@某人 + 文本 + 图片 + 语音。

最后编辑于 11 天前
查看完整历史

cb48f6d-feat


---


## api

API 文档 | NapCatQQ

 Skip to contentNapCatQQ

SearchK

 Main Navigation 快速开始关于

主题

菜单回到顶部

 Sidebar Navigation 
快速开始

目录导航

什么是 NapCatQQ

启动方式

安装方式

Shell

Framework

配置

基础配置

高级配置

使用

接入框架

社区资源

开发

请求接口

上报事件

消息类型

处理文件

插件开发

插件机制原理

快速开始

项目结构

配置与 WebUI

进阶功能

热重载开发

发布插件

API 参考

API 文档

类型定义

完整接口定义

接口

类型

API 文档

版本选择

协议

协议概述

网络通讯

事件基础结构

事件字段详情

接口基础接口

消息元素定义

差异实现说明

其余

喵喵

安全

联系

字数

2 字

阅读时间

1 分钟

📚 API 文档
选择一个版本查看完整的 OpenAPI 接口文档
v4.17.10最新版本
NapCat OneBot 11 HTTP API
v4.17.8历史版本
NapCat OneBot 11 HTTP API
v4.17.5历史版本
NapCat OneBot 11 HTTP API
v4.17.4历史版本
NapCat OneBot 11 HTTP API
v4.17.2历史版本
NapCat OneBot 11 HTTP API
v4.17.1历史版本
NapCat OneBot 11 HTTP API
v4.17.0历史版本
NapCat OneBot 11 HTTP API
v4.16.0历史版本
NapCat OneBot 11 HTTP API
v4.15.19历史版本
NapCat OneBot 11 HTTP API
v4.15.18历史版本
NapCat OneBot 11 HTTP API
v4.15.17历史版本
NapCat OneBot 11 HTTP API
v4.15.13历史版本
NapCat OneBot 11 HTTP API
v4.15.12历史版本
NapCat OneBot 11 HTTP API
v4.15.8历史版本
NapCat OneBot 11 HTTP API
v4.15.6历史版本
NapCat OneBot 11 HTTP API
v4.15.5历史版本
NapCat OneBot 11 HTTP API
v4.15.3历史版本
NapCat OneBot 11 HTTP API
v4.15.1历史版本
NapCat OneBot 11 HTTP API
v4.14.20历史版本
NapCat OneBot 11 HTTP API
v4.14.16历史版本
NapCat OneBot 11 HTTP API
v4.14.13历史版本
NapCat OneBot 11 HTTP API
v4.14.8历史版本
NapCat OneBot 11 HTTP API
v4.14.6历史版本
NapCat OneBot 11 HTTP API
v4.14.4历史版本
NapCat OneBot 11 HTTP API
v4.14.3历史版本
NapCat OneBot 11 HTTP API
v4.13.5历史版本
NapCat OneBot 11 HTTP API
v4.13.3历史版本
NapCat OneBot 11 HTTP API
v4.13.1历史版本
NapCat OneBot 11 HTTP API
v4.13.0历史版本
NapCat OneBot 11 HTTP API
v4.12.1历史版本
NapCat OneBot 11 HTTP API
v4.12.0历史版本
NapCat OneBot 11 HTTP API


---


## config/advanced

高级配置 ​

字数

704 字

阅读时间

3 分钟

配置 FFmpeg ​
自 v4.4.11 起无需配置 FFmpeg 可享受音视频处理，除了手动安装的 Linux 用户。
FFmpeg 是什么？ ​
FFmpeg 是知名的开源音视频处理库，被用于许多音视频编解码相关的项目中。
为什么要使用 FFmpeg？ ​
本项目使用 FFmpeg 是为了编解码语音和视频，以使 NapCat 以 QQ 支持的格式处理语音和视频文件。
如果你的 Bot 没有处理语音和视频的需求，可以选择不安装 FFmpeg。
安装 FFmpeg ​
Windows 系统 ​
在 此处 下载 ffmpeg-master-latest-win64-gpl.zip；

将其中的文件夹解压至一个你知道的地方（例如 C:\Program Files），然后重命名为 ffmpeg；

你的 ffmpeg 文件夹的结构看起来应该是这样的：
textffmpeg
|___bin
|___|___ffmpeg.exe
|___|___ffplay.exe
|___\___ffprobe.exe
|___doc
|___\ ...
|___LICENSE
\___README.txt

注意
请一定要保证 bin 文件夹内同时包含 ffmpeg.exe、ffplay.exe 以及 ffprobe.exe！ 否则会产生意想不到的错误。

添加 bin 目录到系统环境变量，不会可以搜索系统设置环境变量

注意安装完成后可能需要重启

如果有其他程序也需要使用 FFmpeg
如果其他程序支持手动选择 FFmpeg 位置，只需配置为 NapCat 所使用的 FFmpeg 即可。
如果其他程序不支持手动选择 FFmpeg 位置，只需将 FFmpeg 的 bin 目录注册到系统的 PATH 变量中（可参考 此教程）即可。
如果你将 FFmpeg 安装到了系统变量中，那么无论有没有在 NapCat 中配置 FFmpeg 路径也可以正常使用 FFmpeg。

Linux 系统 ​
请使用你所使用的系统的包管理器直接安装 ffmpeg 即可正常使用。
MacOS 系统 ​
由于系统存在沙盒机制，无法运行外部程序，因此暂不支持。
配置 PacketBackend ​
这是干什么的? ​
这是用来提供 NTQQ 本身没有的功能的 DLC，以下配置方式二选一即可。
配置 PacketBackend (Native) ​
TIP
NapCat v3.6.0 及以后的版本在 Linux 平台 (amd64, arm64)，MacOS平台(amd64, arm64)，Windows平台 (amd64) 已内置 PacketBackend 实现 ，您无需进行额外的配置即可享受 DLC 的欢乐 (/≧▽≦)/

当前支持版本 ​
平台版本Native
Windows Amd64 28418-36580✅
Linux Amd64 28498-36580✅
Linux Arm64 28498-36580✅
MacOS Arm64 29456-29456✅
MacOS Amd64 29456-29456✅
扩展进度 ​
支持功能
✅设置群头衔
✅发送 poke
✅独立 Rkey 获取
✅陌生人状态获取
✅伪造合并转发
✅文件直链获取
✅MarkDown
✅群签到
✅小程序卡片分享
✅AI 声聊
✅高性能 OCR

最后编辑于 4 个月前
查看完整历史

c9b6a5e-修正文件名拼写、导航链接 (#127)

7ec1ed6-fix

420c967-在中文、英文以及数字混排时添加空格分隔 #2

4c401e3-在中文、英文以及数字混排时添加空格分隔

f40204e-fix

3b6deae-feat: 版本

1110d72-feat:33800

abde249-fix

dfa8bb4-fix

edc4b4b-fix

f3cd13c-fix

c2d04fb-fix

5336215-fix

v4.2.29

80d9896-fix: 30483

c7b9215-30366

c218bea-29927

783e7c5-MacOS amd64 adapt

4a10b2a-fix

f80e6f3-fix

907eb77-backend info sync

f89f642-fix

a14db30-fix

f2aa4c1-make mac happy

bebc80e-fix: 更新 文档

1aabe7b-arm64

068c6ae-simplify

6004948-simplify

1e74692-feat: PacketBackend

ef83623-fix

4651043-fix

f492585-fix

6a29533-fix

850a447-fix

b09dd8d-feat: MacOS

d90a798-feat: 抬高兼容版本

fdca1a2-fix

953a7f8-feat: docs

f93a7bf-fix: typo

78e19de-fix

1967199-style lint

09c765c-fix

b423203-fix

c060565-[*] 修复高级配置标题层级错误

7333f88-fix

8a39176-fix

604f554-fix

37f2e02-fix

e7563e4-fix: 显示

ac82f49-重构文档

a98431c-feat: support macOS

de3f9ab-fix

e79395f-chore: docs - 修改文档目录关系 - 修改兼容性情况 - 优化零碎的教程

41e5e80-rearrange directory structure

670d937-improve docs behavior

f3c3338-fix

e9f9949-init


---


## config/basic

💖 NapCatのWebUI配置指南💖 ​

字数

1454 字

阅读时间

7 分钟

WARNING
低于 v4.4.7 请勿将注释内容写入配置文件，否则会导致配置文件解析失败，新版本不受限制。

配置网络类型 必备知识 ​
类型描述
HTTP 服务端NapCat 作为 Http 请求接受方 接收对应接口调用并回应 的单工模型
HTTP 客户端NapCat 作为 Http 请求发起方 将事件推送至插件/应用框架 的单工模型
WebSocket 服务端通常指正向 WS 既能主动推送事件也能接收请求 的双工模型
WebSocket 客户端通常指反向 WS 既能主动推送事件也能接收请求 的双工模型
通过 WebUI 配置 OneBot 服务 Shell Version ​
如果你已经启动了 NapCat，并且有多于 1 个开放端口，则可以通过 WebUI 进行配置。
默认地址为 0.0.0.0，即监听所有地址。当配置了不可用的地址时 WebUI 将被禁用。
默认端口为 6099。
当端口被设置为 0 时将禁用 WebUI。
当端口被占用时，会自动对端口 +1，直到找到可用端口（最多尝试 100 次，失败则会禁用 WebUI），端口号会在启动日志中显示。
启动后可在启动日志中看到形如 [info] [NapCat] [WebUi] WebUi User Panel Url: http://127.0.0.1:6099/webui?token=xxxxx 的 token 信息。
也可打开 webui.json 文件，在其中找到token。(使用 NapCat.Installer - Linux 一键脚本安装时，该文件位于 /opt/QQ/resources/app/app_launcher/napcat/config/webui.json)
webui.json
json5{
 "host": "0.0.0.0", // WebUI 监听地址
 "port": 6099, // WebUI 端口
 "token": "xxxx", // 登录密钥, 默认是自动生成的随机登录密码
 "loginRate": 3, // 每分钟登录次数限制
}

访问 http://ip:port/webui/，然后进行以下操作：
进入 QQ 登录，点击 QRCode 进行二维码登录。

此时会刷新WebUi Token 请到 手机端查看自身消息/NapCat控制台查看 获取随机Token。

再次进入WebUi后会强制要求修改密码 否则禁用大部分功能

登录成功后，即可进入网络配置，点击 "新建" 创建对应的服务器或客户端。(如果是公网部署, 请务必启用 Token)

请在创建时勾选保存时启用，或者创建完成后手动启用。

访问 http://ip:port 检查端口是否正常。(此处的 port 指 4 中配置的端口, 请不要与 WebUI 端口混淆)

注：WebUI 自 v4.4 版本后不支持 prefix 配置。
通过 TUI-CLI 配置 OneBot 服务 Shell Version ​
前置条件，使用 Shell 安装时同意安装 TUI-CLI 或者使用 --cli y 参数详见Shell 安装 recommend。
只需要你在终端中输入 sudo napcat 即可进入 TUI-CLI 界面。
通过 文件 配置OneBot服务 Any Version ​
非常不推荐 除非你非常熟悉
v4.5.3 后支持载入 ./config/onebot11.json 作为默认配置
该配置文件名为 ./config/onebot11_xxxx.json 其中 xxxx 为对应 QQ 账户
HTTP 服务端HTTP 客户端WS 服务端WS 客户端
json5{
 "network": {
 // Http服务器组 可以配置多个 这里演示为一个
 "httpServers": [
 {
 "name": "httpServer",// 名字不能重复 唯一标识
 "enable": false,//启用状态
 "port": 3000,// 监听端口
 "host": "0.0.0.0",// 监听主机
 "enableCors": true,// 暂时没有作用
 "enableWebsocket": true,// 暂时没有作用
 "messagePostFormat": "array",// 消息上报格式 string/array
 "token": "",// 鉴权密钥
 "debug": false,// raw数据上报
 }
 ],
 "httpClients": [],
 "websocketServers": [],
 "websocketClients": []
 },
 "musicSignUrl": "",
 "enableLocalFile2Url": false,
 "parseMultMsg": false
}

json5{
 "network": {
 "httpServers": [],
 // Http客户端组 可以配置多个 这里演示为一个
 "httpClients": [
 {
 "name": "httpClient",// 名字不能重复 唯一标识
 "enable": false,//启用状态
 "url": "http://localhost:8080",// 上报地址
 "messagePostFormat": "array",// 消息上报格式 string/array
 "reportSelfMessage": false,// 是否上报自身消息
 "token": "",// 鉴权密钥
 "debug": false,// raw数据上报
 }
 ],
 "websocketServers": [],
 "websocketClients": []
 },
 "musicSignUrl": "",
 "enableLocalFile2Url": false,
 "parseMultMsg": false
}

json5{
 "network": {
 "httpServers": [],
 "httpClients": [],
 // WS服务端组/正向WS 可以配置多个 这里演示为一个
 "websocketServers": [
 {
 "name": "WsServer",// 名字不能重复 唯一标识
 "enable": false,//启用状态
 "host": "0.0.0.0",// 监听主机
 "port": 3001,// 监听端口
 "messagePostFormat": "array",// 消息上报格式 string/array
 "reportSelfMessage": false,// 是否上报自身消息
 "token": "",// 鉴权密钥
 "enableForcePushEvent": true,// 暂时没有作用
 "debug": false,// raw数据上报
 "heartInterval": 30000,// 心跳周期
 }
 ],
 "websocketClients": []
 },
 "musicSignUrl": "",
 "enableLocalFile2Url": false,
 "parseMultMsg": false
}

json5{
 "network": {
 "httpServers": [],
 "httpClients": [],
 "websocketServers": [],
 // WS客户端组/反向WS 可以配置多个 这里演示为一个
 "websocketClients": [
 {
 "name": "WsClient",// 名字不能重复 唯一标识
 "enable": false,//启用状态
 "url": "ws://localhost:8082",// 上报地址
 "messagePostFormat": "array",// 消息上报格式 string/array
 "reportSelfMessage": false,// 是否上报自身消息
 "reconnectInterval": 5000,// 重连间隔
 "token": "",// 鉴权密钥
 "debug": false,// raw数据上报
 "heartInterval": 30000,// 心跳周期
 }
 ]
 },
 "musicSignUrl": "",
 "enableLocalFile2Url": false,
 "parseMultMsg": false
}

配置 NapCat 其它设置 ​
如果不懂干嘛，不用看啦 在这里你可以修改日志等基础设置
v4.5.3 后支持载入 ./config/napcat.json作为默认配置
启动登录 NapCat 后，打开 NapCat 的 config 目录，找到名为 napcat_<你的QQ号>.json 的文件，如 napcat_1234567.json。
配置内容参数解释：
napcat_xxxx.json
json5{
 // 是否开启文件日志
 "fileLog": true,
 // 是否开启控制台日志
 "consoleLog": true,
 // 日志等级, 可选值: debug, info, error
 "fileLogLevel": "debug",
 "consoleLogLevel": "info",
 "packetServer":""
}

最后编辑于 4 个月前
查看完整历史

c9b6a5e-修正文件名拼写、导航链接 (#127)

b1575a2-docs：update docs (#119)

d4b0b10-Update WebUI login and setup instructions

420c967-在中文、英文以及数字混排时添加空格分隔 #2

4c401e3-在中文、英文以及数字混排时添加空格分隔

45fefe0-feat(basic/shell):新增了关于TUI-CLI的描述，展开linux一键部署的演示代码

1e638c3-feat: 更新文档

94541f0-fix

2322fa5-更新 WebUI 配置教程

97dfb17-fix

feb0401-增加 webui.json 文件路径说明

a7abe1b-Update basic.md

7cc1aa8-Update basic.md

e5d7b0b-Update basic.md

2332813-fix

fb7e193-fix

cf24609-fix

4c1cf88-fix

0cfe0f0-fix

7711e1b-fix

9b95cb4-fix

578710d-fix

5c7106e-update: new docs

3095ca5-fix

ac82f49-重构文档

a98431c-feat: support macOS

3a439a7-Update basic.md

a4c0f64-Update basic.md

8a5648c-Update basic.md

3433791-Update basic.md

a5137b3-Update basic.md

41e5e80-rearrange directory structure

73d5253-docs: 增加配置https的方案

670d937-improve docs behavior

78a3336-fix

e1a2208-docs: config change

34ea1d2-doc: 大量文字表述上的修改，使表意更加明确

524e75b-doc: update

ee33ffa-doc: update

dd72b4f-doc: update

8638068-fix

402edb6-fix


---


## use/community

社区资源 ​

字数

155 字

阅读时间

1 分钟

NC-nonebot平台更新工具 nonebot-plugin-ncupdateauthor: tianyisama
nonebot-plugin-ncupdate
Node开发SDK node-napcat-tsauthor: huankong233
node-napcat-ts
OlivOS 青果核心交互栈author: OlivOS-Team
OlivOS
Rust开发SDK onebotv11_rsauthor: canxin121
onebotv11_rs
Kovi - 用 Rust 实现的 Onebot 机器人开发框架author: Threkork
Kovi
napcat拓展插件
Python开发SDK：NcatBotauthor: 木子
✨使用简单易上手的python开发属于你的napcatqq机器人，采用简单的代码就可以实现复杂的任务，支持直接发送图片markdown。
使用NcatBot，让机器人🤖开发更简单。
NcatBot

最后编辑于 3 个月前
查看完整历史

2150443-更新 community.md

02bc7b2-更新 community.md

bc99d93-更新 community.md

5b84668-Update community.md

db24996-fix

208cefa-fix

1a85573-fix

1fcaf78-fix

ac82f49-重构文档

39c9dd2-feat

cab6a41-chore: NapCat-Desktop 没有维护 暂时移除

2e97dc9-chore: 推荐项目

e79395f-chore: docs - 修改文档目录关系 - 修改兼容性情况 - 优化零碎的教程

f1d38b4-docs: fix style

8c25eaf-docs: update


---


## use/integration

接入框架 ​

字数

605 字

阅读时间

3 分钟

NoneBot ​
配置 NoneBot
这里假设你已经安装了 OneBot 适配器
默认情况下，NoneBot 是启用了反向 ws 的，如果出现 403，可能是默认配置问题，需要配置 token 才能正常连接。
具体方法为：修改 NoneBot 配置文件 .env，添加 ONEBOT_ACCESS_TOKEN=你在 NapCat 中配置的 token。
然后，启动 NoneBot，可以看到 NoneBot 输出的端口号，如 8080。

配置 NapCat
在 NapCat 配置添加反向 ws 地址，地址为 ws://127.0.0.1:8080/onebot/v11/ws, 这里的 8080 是 NoneBot 输出的端口号，/onebot/v11/ws 是 NoneBot onebot 适配器默认的路径

Koishi ​
在 Koishi 插件市场搜索 onebot 并安装 adapter-onebot，如下图：

安装完之后，点击修改→配置

配置 OneBot
这里以 WS 反向连接为例：
selfId 为你的机器人的 QQ 号
token 需和 NapCat 配置的 token 一致，当然，如果没有配置 token，则留空。
protocol 选择 ws-reverse
其他配置保持默认即可，点击保存，然后启用插件。

配置完成后，在 NapCat 的配置中添加 WS 反向地址。Koishi OneBot 的 ws 反向地址为 ws://127.0.0.1:5140/onebot。添加完成后，点击保存即可。

AstrBot ​
配置AstrBot
选择 配置→消息平台→消息平台适配器→aiocqhttp(qq)，默认即可，可根据需要更改。

配置OneBot
在 NapCat WebUI页面选择 网络配置→新建→WebSocket客户端，URL填入ws://127.0.0.1:6199/ws，添加完成后，点击保存即可。 

OlivOS ​
支持正向和反向ws以及http详见 文档
onebotv11_rs ​
支持正向和反向ws以及http
node-napcat-ts ​
配置 NapCat
在 NapCat 配置启用正向 ws

配置 node-napcat-ts
详见 node-napcat-ts 文档
如果出现连接失败，可能是配置问题，需要配置 token 才能正常连接。

Minato ​
基于 node-napcat-ts 实现的，所以需要的配置类似
只需要配置几个插件 /src/plugins 即可运行, 配置方法: 复制 config.default.ts 文件到 config.ts 并配置其中配置项即可运行
Kovi ​
Rust Onebot V11 插件框架。
将 NapCat 配置启用正向ws。
编写插件或使用社区插件，编译启动即可。（文档里面非常详细哦）
编写插件可使用 NapCat Api 拓展 。

最后编辑于 3 天前
查看完整历史

2992b94-fix:修改AstrBot教程错误

82837cc-Fix integration.md

4a2c377-Update integration.md

9ff1465-Update integration.md

24a8937-Update integration.md

ac82f49-重构文档


---


## other/about-copy

涉及Copy原理部分分析 ​

字数

685 字

阅读时间

4 分钟

自2024下半部年与某些人切割后，某些人仍然不遵守规范与守则，由某位提供的压缩包，本文对对隔壁框架开发关于PBHook抄袭部分认定
文件来源：某群友(某框架群内转发)
文件原始内容：https://share.weiyun.com/vqlePMqd
第一部分 确定程序开发栈 ​
首先我们对使用ida pro拖入 转到字符串视图 发现大量关于py的字样
我们推测其基于 python+nuikta/pyinstaller 构建的onefile 搜索pyinstaller关键词 确认是pyinstaller
第二部分 使用pyinstxtractor工具解压内部文件 ​
使用 https://github.com/extremecoders-re/pyinstxtractor/blob/master/pyinstxtractor.py
解压后文件包括js hook_server 两部分均被混淆 技术栈为frida+websockets
第三步部分 对JS部分代码抄袭部分确认 ​
javascriptconst MODULE_NAME = 'wrapper.node';
function hexDump(_0x56ac13) {
 const _0x481bdb = Array['from'](new Uint8Array(_0x56ac13))['map'](_0x156c80 => _0x156c80['toString'](0x10)['padStart'](0x2, '0'))['join']('');
 return _0x481bdb;
}
function readUTF8Str(_0x4c1e14) {
 let _0x481cae = '';
 if ((_0x4c1e14['readU8']() & 0x1) === 0x0)
 _0x481cae = _0x4c1e14['add'](0x1)['readUtf8String']();
 else {
 const _0x146a47 = _0x4c1e14['add'](0x10)['readPointer'](), _0x27773f = _0x4c1e14['add'](0x8)['readU64']();
 try {
 _0x481cae = _0x146a47['readUtf8String'](_0x27773f);
 } catch (_0x56eda0) {
 _0x481cae = '';
 }
 }
 return _0x481cae;
}
function writeCPPString(_0x3764e7, _0x484599) {
 _0x3764e7['add'](0x8)['writeU32'](_0x484599['length']), _0x3764e7['add'](0x10)['readPointer']()['writeUtf8String'](_0x484599);
}
function main() {
 const _0x117541 = Module['findBaseAddress'](MODULE_NAME);
 if (!_0x117541)
 return setTimeout(main, 0x1);
 function _0x1999ec() {
 const _0x49b89d = 0x1cfac38, _0x432c82 = _0x117541['add'](_0x49b89d), _0x482d6f = new NativeFunction(_0x432c82, 'int', [
 'pointer',
 'pointer'
 ]);
 Interceptor['replace'](_0x432c82, new NativeCallback((_0x378c8a, _0x276455) => {
 try {
 const _0x4abd43 = _0x276455['readPointer'](), _0x409db3 = _0x4abd43['readPointer'](), _0x5a1e79 = _0x4abd43['readPointer']()['add'](0x20)['readPointer'](), _0x5efd68 = _0x5a1e79['readPointer'](), _0x1691a1 = _0x5efd68, _0x2076b0 = _0x5a1e79['add'](0x8)['readU64']();
 let _0x15862d = _0x2076b0 - _0x1691a1, _0x263d55 = readUTF8Str(_0x409db3);
 console['log']('cmd:\x20' + _0x263d55);
 const _0x1e76e7 = _0x4abd43['add'](0x8 * 0x8)['readU64']();
 let _0x2123bc = !![];
 _0x263d55 === 'trpc.o3.report.Report.SsoReport' && (send({
 'type': 'process_send_pb',
 'cmd': _0x263d55,
 'seq': _0x1e76e7,
 'pb': _0x47dde2
 }), recv('process_send_pb_response_' + _0x1e76e7, _0x3436f3 => {
 let _0x5aea67 = _0x3436f3['payload']['pb'];
 if (_0x5aea67['length'] === 0x0) {
 _0x2123bc = ![];
 return;
 }
 const _0x41ef77 = _0x5aea67['length'] / 0x2, _0x22cf42 = Memory['alloc'](_0x41ef77);
 Memory['writeByteArray'](_0x22cf42, _0x5aea67['match'](/../g)['map'](_0xd57414 => parseInt(_0xd57414, 0x10))), Memory['copy'](_0x5efd68, _0x22cf42, _0x41ef77), _0x5a1e79['add'](0x8)['writePointer'](_0x5efd68['add'](_0x41ef77));
 })['wait'](0x1388));
 if (_0x263d55 === 'OidbSvcTrpcTcp.0xED3_1') {
 }
 const _0x47dde2 = hexDump(_0x5efd68['readByteArray'](_0x15862d));
 return _0x263d55 = readUTF8Str(_0x409db3), console['log']('cmd:\x20' + _0x263d55 + '\x0apb:\x20' + _0x47dde2), _0x2123bc ? _0x482d6f(_0x378c8a, _0x276455) : 0x0;
 } catch (_0x6c1c1d) {
 return console['error'](_0x6c1c1d), _0x482d6f(_0x378c8a, _0x276455);
 }
 }, 'int', [
 'pointer',
 'pointer'
 ]));
 }
 function _0x4ed2f3() {
 const _0x1d1f65 = 0x1cfd038, _0x24d9af = _0x117541['add'](_0x1d1f65);
 Interceptor['attach'](_0x24d9af, {
 'onEnter'(_0x2817bd) {
 const _0x392919 = _0x2817bd[0x0], _0xe366ce = _0x2817bd[0x1], _0x37e865 = _0x2817bd[0x2], _0x4fad83 = _0xe366ce['readPointer'](), _0xeb9819 = _0x4fad83['add'](0x18)['readU64'](), _0x3b041f = _0x4fad83['add'](0x20), _0x14325e = readUTF8Str(_0x3b041f), _0x7f2763 = _0x4fad83['add'](0x38)['readPointer'](), _0x1e5e20 = _0x7f2763['add'](0x8)['readU64']() - _0x7f2763['readPointer'](), _0x4e0e70 = _0x7f2763['readPointer']()['readByteArray'](_0x1e5e20), _0xf82460 = hexDump(_0x4e0e70);
 console['log']('\x0a|-\x20Receive\x20packet,\x20' + new Date() + '\x0a|-\x20cmd:\x20' + _0x14325e + '\x0a|-\x20seq:\x20' + _0xeb9819 + '\x0a|-\x20protobuf:\x20' + _0xf82460 + '\x0a|-\x20err:\x20' + _0x37e865 + '\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20');
 }
 });
 }
 _0x1999ec(), _0x4ed2f3();
}
main();

样本下载: https://share.weiyun.com/n5yKimjk
原始napcat方代码
javascriptlet cmd = Memory.readPointer(args[1]).add(32);
let cmd_type = new Uint8Array(cmd.readByteArray(1))[0] & 0x1;
let seq = Memory.readPointer(args[1]).add(24);
let uin = Memory.readPointer(args[1]);
let uin_type = new Uint8Array(uin.readByteArray(1))[0] & 0x1;
let bufferPtr = Memory.readPointer(Memory.readPointer(args[1]).add(56));
let buffer_start = Memory.readPointer(bufferPtr);
let buffer_end = Memory.readPointer(bufferPtr.add(8));
let buffer_len = buffer_end - buffer_start;

对比后发现 buffer_len 对应 _0x15862d = _0x2076b0 - _0x1691a1之类高度一致
其Hook点与NapCat一致 一般来说函数有很多层 很多位置 但选择同样位置的情况很少
等等其余代码不再做对比 napcat最早提交时间与2024年10月
第四部分 补充 ​
以下是时间与代码证据 有必要该仓库可以public

napcat原始仓库 暂未public 但是你仍可以通过反编译moehoo获得napcat逻辑 napcat自3.6.0版本已内置native能力的Hook库 可通过x64dbg ida pro 自行验证 hook点与逻辑

https://github.com/NapNeko/napcat.packet/blob/main/napcat.packet.old.py
https://github.com/NapNeko/napcat.packet/blob/main/napcat.packet.py

最后编辑于 20 天前
查看完整历史

35b9489-feat

5a2651f-fix

133f1c1-某框架抄袭说明


---


## other/about

联系 ​

字数

114 字

阅读时间

1 分钟

社群 ​
QQ Group
Telegram
DeepWiki
QQ群因为特殊原因需要入群密钥，请在webui关于页面获取，仅最新的100个版本以内有效。
下面的QQ Group 无需密钥，随时清理不活跃人员和Bot，仅500人容量。
困困猫猫的高中

最后编辑于 5 个月前
查看完整历史

727b049-Update community links and about page

ee4d5e1-Update about.md

3091877-fix

1110d72-feat:33800

6450d01-fix

f63ce89-fix

8eb1b1e-fix

51a63c4-fix

16f0742-fix

832681c-chore: link

def4eb1-fix

ac82f49-重构文档

e79395f-chore: docs - 修改文档目录关系 - 修改兼容性情况 - 优化零碎的教程

670d937-improve docs behavior

d3fb84e-doc: update

7ed43e5-docs: instuction

e9f9949-init


---


## other/napcat

Logos ​

字数

9 字

阅读时间

1 分钟

最后编辑于 大约 2 个月前
查看完整历史

f191b2f-feat: 2 logos

1967199-style lint

fc63033-fix: 测试

c951b3e-fix: 调整


---


## other/security

安全相关 ​

字数

603 字

阅读时间

3 分钟

WebUI 安全与一些冷知识 ​
WebUI 的安全性设计较为完善，具体特性如下：
鉴权过程全程使用 SHA256 加盐处理，有效避免密钥泄露风险
对来源 IP 实施限速控制，防止暴力破解
基于时间的 HMAC 密钥动态生成机制，确保鉴权在重启后立即失效
可通过将端口设置为 0 完全关闭网页面板，关闭后可安全删除 ./static/ 静态资源
终端控制功能可通过删除 ./pty/ 目录完全禁用
支持 SSL 加密，只需在 ./config/ 目录添加 cert.pem 与 key.pem 文件并重启即可生效
WARNING
NapCat WebUI 默认使用弱密码（密钥为 napcat），如果部署在公网环境中，请立即修改密码或关闭 WebUI。

OneBot 接口安全 ​
服务端工作模式：NapCat 作为服务端，鉴权由 NapCat 负责提供来源验证。

客户端工作模式：NapCat 作为客户端，鉴权由外部服务端负责提供来源验证。

重要提示：如果采用服务端工作模式且未配置鉴权，将应用暴露在公网环境中会带来严重安全风险。
QQ 账号安全性 ​
避免在同一 IP/设备上同时登录 Bot 账号与常用账号，以防常用账号受到异常影响
频繁掉线问题可通过更换账号或设备来有效改善
遇到社交风控时，解除限制后重新运行即可，此类限制通常不会频繁触发
如无法更换账号或设备，可尝试在配置中将 o3Hook 设置为 0 以关闭包拦截
网络环境复杂导致登录困难时，可联系云服务商更换 IP 或重新拨号，或通过设置环境变量 NAPCAT_PROXY_ADDRESS = 127.0.0.1 与 NAPCAT_PROXY_PORT = 80 配置 SOCKS5 代理
NapCat 卸载与残留风险 ​
Windows 环境：只需删除 NapCat 目录即可完全卸载，不会产生残留文件，且不影响 QQ 的更新或卸载
Linux 环境：Docker 方案不会对设备造成残留问题；直接本机安装的情况下，重装 QQ 即可完成卸载

最后编辑于 10 天前
查看完整历史

e9639ba-feat:注意事件


---


## demo/demo

NapCat

 特性
 文档
 发布

 基于 NTQQ Bot 框架

 零配置，跨平台，100 MB 常驻内存。

 选择平台安装体验

 Linux
 Windows
 macOS

 重新体验
 复制日志


---


## en-US/guide/getting-started

NapCatQQ ​
NapCatQQ is a QQ Bot framework based on the PC NTQQ client body, which is stable, secure, and quickly deployable.
Advantages of NapCatQQ ​
No need for a graphical environment, performs well on Linux, and has a fundamental difference from existing Hook frameworks, far superior in performance and memory usage.

Simple configuration, supports remote browser access for configuration, easy and simple to complete.

Rapid adaptation to NTQQ functions, continuous updates to follow the latest version of QQ.

Things to Know Before Starting (Read Three Times!) ​
WARNING
NapCat is a QQ Bot framework based on the PC NTQQ client body, so you need to install the QQ version corresponding to NapCatQQ in advance to run NapCat.

When NapCat is online, you cannot achieve human-computer unity using the PC QQ client, but you can choose to log in synchronously on the mobile client. If you want human-computer unity on PC, please use LLOneBot.

NapCat is different from protocol implementation; it is based on the QQ client. Things that cannot be done on the QQ client, NapCat >_< can't do it either!

Install QQ ​
NapCatQQ v1.4.7:
Windows 9.9.10-24108 | Linux 3.2.7-23361
Linux does not need a desktop to install NTQQ. The specific command is as follows:
shellsudo apt install libgbm1 libasound2
sudo apt install ./qq.deb

For more versions, please refer to Version Update Log.
Download NapCatQQ ​
Download link: https://github.com/NapNeko/NapCatQQ/releases
Configuration ​
To avoid secondary startup, you can pre-configure the basic settings of NapCat, see Configure NapCat.
Startup ​
WindowsAfter installing the corresponding version of QQ, in most cases, you only need to unzip NapCat and place it anywhere you want. But be careful, the path cannot contain spaces. Then, double-click napcat.bat to run!
Wait! If you encounter garbled characters, you can try double-clicking napcat-utf8.bat to start.
If the above method still does not work, you can try to start with PowerShell:
Start PowerShell, run powershell ./napcat.ps1 or napcat.bat, if garbled characters appear, you can try to run napcat-utf8.ps1 or napcat-utf8.bat.
If it still doesn't work, you can try powershell.exe -ExecutionPolicy Bypass -File ".\napcat.ps1".
It is recommended to directly click the bat to run, because PowerShell itself will occupy about 20 MB of memory.
Linux One-Click ScriptHighly recommended!
curl -o napcat.sh https://nclatest.znin.net/NapNeko/NapCat-Installer/main/script/install.sh && sudo bash napcat.sh
Linux DockerLinux Non-DockerRun in the terminal
shellchmod u+x ./napcat.sh
./napcat.sh

Do not start with sh napcat.sh, as it may cause path problems and fail to start.
Android TermuxQuick Login (No Need to Scan)If you have successfully logged in to the official QQ or NapCatQQ, you can add the parameter -q <Your QQ> for quick login without scanning. For example, napcat.bat -q 1234567 or napcat.sh -q 1234567.
After Startup ​
Congratulations, if you see this, you have successfully started NapCat, you can try reading the advanced instructions below!
How to Configure NapCat's Basic Settings
How to Configure NapCat's Voice Sending Refer to the entry Voice/Video Sending Failed
How to Solve NapCat Crash Issues


---


## en-US/guide/integration

Framework Integration ​
Integrating with Open Source Frameworks ​
Using Koishi and NoneBot as examples.
Configuring KoishiSearch for onebot in the Koishi plugin market and install adapter-onebot as shown below:

After installation, click on modify → configuration

Configure OneBot
Here's an example using WS reverse connection:
selfId is your bot's QQ number
token should match the token configured in NapCat. If no token is configured, leave it blank.
Select protocol as ws-reverse
Leave other configurations as default, click save, and then enable the plugin.

After configuration, add the WS reverse address in NapCat's settings. The WS reverse address for Koishi OneBot is ws://127.0.0.1:5140/onebot. Once added, click save.

Configuring NoneBotConfigure NoneBot
Assuming you have installed the OneBot adapter.
By default, NoneBot enables reverse ws. If you encounter a 403 error, it may be due to default configuration issues and requires configuring a token for a normal connection. The specific method is to modify the NoneBot configuration file .env and add ONEBOT_ACCESS_TOKEN=your_token_configured_in_NapCat.
Then, start NoneBot and you will see the port number output by NoneBot, such as 8080.

Configure NapCat
Add the reverse ws address in NapCat settings, the address is ws://127.0.0.1:8080/onebot/v11/ws, where 8080 is the port number output by NoneBot, and /onebot/v11/ws is the default path for NoneBot onebot adapter.
TIP
Always remember: the token configured in NapCat must match the one configured in NoneBot!

Configuring HTTP Service ​
Configuring the HTTP service involves two main aspects: one is the HTTP listening port (to be called by your application), and the other is the HTTP reporting address (to be called by NapCat).
HTTP Listening PortFor example, if the configured port number is 3000, the API address would be http://localhost:3000.
HTTP Reporting AddressWhen NapCat receives messages or other events, it reports them to this address via a POST request.
TIP
The reporting address must start with http://

Configuring WebSocket Service ​
In the OneBot 11 standard, the definitions of "forward WS" and "reverse WS" are somewhat ambiguous. Here's a clear distinction: forward refers to accepting WS connections from the application side, while reverse refers to NapCat actively connecting to the reverse WS address listened by the application side.
Forward WS ConfigurationFor example, if the configured port number is 3001, then the WS address configured on the application side should be ws://localhost:3001.
Reverse WS ConfigurationFor example, if NoneBot2 is configured with a OneBot port of 8080 and a path of /onebot/v11/ws, then the configured reverse WS address is ws://localhost:8080/onebot/v11/ws.


---


## en-US

NapCatQQ

 Skip to content NapCatQQ

 Main Navigation ReferenceDevelopEnglish
简体中文

English
简体中文

Appearance

NapCat
A QQ BOT implemented based on NTQQ
Start
Github

Ready to use
Multiple deployment methods, quick deployment on Win/Linux Docker/Termux and other platforms, no virtualization required, lightweight memory.

Secure and stable
Implemented through Electron’s own mechanism, using NTQQ’s own code for message sending and receiving, can be synchronized with mobile QQ login.

Fast adaptation
Based on the OneBotV11 protocol, plugins can be quickly migrated to the NapCat platform without the need for adaptation efforts.


---
