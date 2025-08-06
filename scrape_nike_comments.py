from youtube_comment_downloader import YoutubeCommentDownloader
import pandas as pd

video_url = "https://www.youtube.com/watch?v=OYAtKHrt6YA"

downloader = YoutubeCommentDownloader()
comments_list = []

print("📥 Downloading comments...")

for comment in downloader.get_comments_from_url(video_url, sort_by=0):  # fixed line here
    comments_list.append(comment["text"])

df = pd.DataFrame(comments_list, columns=["comment"])
df.to_csv("nike_youtube_comments.csv", index=False)

print(f"✅ Done! {len(comments_list)} comments saved to 'nike_youtube_comments.csv'")
