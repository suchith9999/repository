# from pytube import YouTube
# from pathlib import Path

# # URL of the video
# url = input("Enter the YouTube video URL:  ")

# try:
# 	# Create YouTube object
# 	yt = YouTube(url)

# 	# Get the highest resolution stream
# 	stream = yt.streams.get_highest_resolution()

# 	# Download with original video title
# 	# path = r"C:\Users\suchith\Downloads"
# 	download_path = Path("C:/suchith/Downloads")
# 	stream.download(output_path=download_path)  # Leave out 'filename'

# 	print(f"Downloaded: {yt.title}")
# 	print("Download completed!")
# except Exception as e:
# 	print(f"An error occurred: {e}")

# # Optional: Download Only Audio
# # stream = yt.streams.filter(only_audio=True).first()
# # stream.download(output_path="your_download_folder", filename="audio.mp3")


from pytube import YouTube

# def download(link):
#     try:
#         # Create YouTube object
#         yt = YouTube(link)

#         # Get the highest resolution stream
#         stream = yt.streams.get_highest_resolution()

#         # Download with original video title
#         stream.download("../../Desktop/")

#         print(f"Downloaded: {yt.title}")
#         print("Download completed!")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# download('https://www.youtube.com/watch?v=wc_9SlpSJdw')


# with open('C:/Users/suchith/Desktop/test1.txt', 'w') as w:
#     w.write('Hello World')
#     w.write('\n')
#     w.write('This is a test file.')
#     w.write('\n')
#     w.write('Goodbye!')
# with open('../../Desktop/test1.txt', 'r') as r:
#     content = r.read()
#     print(content)


