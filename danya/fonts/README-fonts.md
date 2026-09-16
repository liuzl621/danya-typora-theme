# 字体目录

把要随主题分发的字体文件放这里，路径与 `../fonts.css` 里的 `fonts/xxx` 对应。

步骤：放文件 → 取消 `fonts.css` 里对应模板的注释并核对文件名 →
到 `../variables.css` 把字体名加进 `--font-text` / `--font-code` 的栈里。

默认做法是只写系统字体名（不放进这个目录），那样不涉及任何字体授权问题。
只有把字体文件随主题分发时才需要看授权：思源宋体 / 思源黑体 / 霞鹜文楷（SIL OFL）、
JetBrains Mono、Cascadia Code 都可以自由再分发；Windows 自带的宋体、楷体、微软雅黑
授权只随系统，拷进主题分发会侵权。
