import yt_dlp
from concurrent.futures import ThreadPoolExecutor, as_completed


def my_hook(d):
    if d['status'] == 'downloading':
        print(f"{d['_percent_str']}", end='\r')
    elif d['status'] == 'finished':
        print("\n下载完成")

def download_single_video(url, output_dir='./output'):
    ydl_opts = {
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'progress_hooks': [my_hook],
        'noplaylist': True,
        'cookiesfrombrowser': ('chrome',),  # 自动读取Chrome cookies
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"\n下载出错: {e}")

def download_videos(url_list, output_dir='./output'):
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(download_single_video, url, output_dir) for url in url_list]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"下载出错: {e}")

def load_urls_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]

if __name__ == '__main__':
    urls = load_urls_from_file('video_urls.txt')
    download_videos(urls) 