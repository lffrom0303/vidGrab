# 多平台视频批量下载脚本

本项目是一个基于 Python 的多线程视频下载工具，支持 YouTube、Bilibili、Twitter 等主流平台，自动获取 Chrome 浏览器 cookies，无需手动导出 cookies.txt。

## 功能特性

- 支持 YouTube、Bilibili、Twitter 等主流视频网站的视频下载
- 多线程并发下载，提升下载效率
- 自动获取 Chrome 浏览器 cookies，支持需要登录的视频下载
- 终端显示简洁进度条

## 依赖安装

1. 安装 Python 3.7 及以上版本
2. 安装依赖包：

```bash
pip install -r requirements.txt
```

## 使用方法

1. **手动创建 `video_urls.txt` 文件，并将你要下载的视频链接（支持多平台）填入该文件，每行一个链接**：

```
https://www.youtube.com/watch?v=xxxxxxx
https://www.bilibili.com/video/BV1xxxxxxx
https://twitter.com/i/status/xxxxxxxxxx
```

> **注意：** `video_urls.txt` 文件需要你自己手动创建和维护，主程序会自动读取该文件中的所有链接进行批量下载，无需再在代码中手动维护 `urls` 列表。

2. 运行脚本：

```bash
python youtube_downloader.py
```

3. 下载的视频会保存在 `./output` 文件夹下。

## 自动获取浏览器 cookies

- 本脚本会自动从本机 Chrome 浏览器读取 cookies，无需手动导出 cookies.txt。
- 只需确保你已在 Chrome 浏览器中登录目标网站（如 Bilibili、Twitter、YouTube），即可下载需要登录的视频。
- 如果遇到 `browser-cookie3` 相关报错，请先安装依赖：

```bash
pip install browser-cookie3
```

- 如需支持其他浏览器（如 Edge、Firefox），可在脚本中将 `'chrome'` 替换为对应浏览器名。

## 常见问题

1. **下载报错 `fragment not found; Skipping fragment`**

   - 可能是网络不稳定、分片丢失或被限流。建议切换网络、降低分辨率或重试。

2. **需要 cookies 才能下载**

   - 本脚本已自动获取 Chrome cookies。若依赖未安装，按提示安装 `browser-cookie3`。

3. **如何更换下载目录？**

   - 修改 `download_single_video` 函数的 `output_dir` 参数即可。

4. **支持哪些平台？**
   - 只要 yt-dlp 支持的平台（YouTube、Bilibili、Twitter、抖音、Vimeo 等）都可以直接用。

## 参考

- [yt-dlp 官方文档](https://github.com/yt-dlp/yt-dlp)
- [browser-cookie3 文档](https://github.com/borisbabic/browser-cookie3)

---

如有更多需求或问题，欢迎反馈！

---
