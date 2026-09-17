# install.ps1 — 一键安装 danya 主题到 Typora（Windows）
# README 一行指令：irm https://raw.githubusercontent.com/liuzl621/danya-typora-theme/main/install.ps1 | iex
# 注意：irm|iex 会直接执行远程脚本，用户需自行信任。
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

$repo   = 'liuzl621/danya-typora-theme'
$branch = 'main'
$theme  = 'danya'

# 1. Typora 主题目录（没有就建）
$themesDir = Join-Path $env:APPDATA 'Typora\themes'
New-Item -ItemType Directory -Path $themesDir -Force | Out-Null

# 2. 下载仓库 zip 并解压到临时目录（比逐个 raw 稳，文件增减不用改脚本）
$tmp = Join-Path $env:TEMP 'danya-install'
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory -Path $tmp -Force | Out-Null
$zip = Join-Path $tmp 'repo.zip'
Invoke-WebRequest -Uri "https://github.com/$repo/archive/refs/heads/$branch.zip" -OutFile $zip
Expand-Archive -Path $zip -DestinationPath $tmp -Force
$src = Join-Path $tmp "$($repo.Split('/')[1])-$branch"

# 3. 复制主题：入口 css + danya/ 模块目录；user.css 是个人微调层，仅在不存在时复制，防止重装覆盖
Copy-Item (Join-Path $src "$theme.css") $themesDir -Force
Copy-Item (Join-Path $src $theme) $themesDir -Recurse -Force
if (-not (Test-Path (Join-Path $themesDir "$theme.user.css"))) {
    Copy-Item (Join-Path $src "$theme.user.css") $themesDir -Force
}

Remove-Item $tmp -Recurse -Force
Write-Host "安装完成：重启 Typora，在 主题 菜单选择 $theme"
