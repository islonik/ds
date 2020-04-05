from pytube import YouTube
import sys


def main(argv):
    youtube_url = ''
    wait_for_add = False
    for param in argv:
        if param == 'url':
            wait_for_add = True
            continue
        if wait_for_add:
            wait_for_add = False
            youtube_url = str(param)
            continue

    youtube = YouTube(youtube_url)

    video = youtube.streams.get_highest_resolution()

    print(f"We are going to try to download '{youtube.title}' from url '{youtube_url}' "
          f"in the highest available resolution.")

    path_to_video = video.download('/Users/inikki/Downloads/video')

    print(f"Downloaded into '{path_to_video}'")


if __name__ == "__main__":
    main(sys.argv[1:])