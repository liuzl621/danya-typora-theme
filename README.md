# danya（淡雅）

一个 Typora 主题：低饱和青绿强调色，西文与数字 Times、正文宋体、标题黑体。

<!-- 首屏封面图-->

## 预览

- 导出效果（论文密度）：[samples/danya-sample.pdf](samples/danya-sample.pdf)

<!-- 预览截图 -->

## 安装

1. Typora → 偏好设置 → 外观 → 打开主题文件夹；
2. 拷入 `danya.css`、`danya.user.css` 和 `danya/` 整个目录；
3. 重启 Typora，在「主题」里选 **danya**。

个别 Typora 版本对 `@import` 支持不好时，跑 `python scripts/build.py`，改用 `dist/` 里的单文件版。

## 自定义

配色、字体、字号、间距全部集中在 `danya/variables.css`，改完保存、回 Typora 重点一下当前主题即生效。

## 许可

MIT，见 [LICENSE](LICENSE)。主题只引用系统已装字体名、不打包字体文件；字体遵循各自授权。
