from pytube import YouTube
from pytube.exceptions import RegexMatchError
import sys
import os
import subprocess

DOWNLOAD_FOLDER = '/Users/inikki/Downloads/video'  # constant, DO NOT reassign

# this '&' symbol is used in console to concatenate commands so be aware about when you copy-paste urls from YouTube
def main(argv):
    youtube_url = ''
    is_subs = False
    wait_for_add = False
    is_audio = False
    is_url_given = False

    # parse params
    for param in argv:
        if param == 'audio':
            is_audio = True
            print('Audio would be converted from mp4. Ffmpeg should be preinstalled.')
            continue
        if param == 'subs':
            is_subs = True
            print('English subtitles would be downloaded.')
            continue
        if param == 'url':
            wait_for_add = True
            continue
        if wait_for_add:
            wait_for_add = False
            youtube_url = str(param)
            is_url_given = True
            continue

    # validators
    if not is_url_given:
        print('URL is not found!')
        return

    # main body
    try:
        youtube = YouTube(youtube_url)
    except RegexMatchError:
        print("URL is incorrect!")
        return

    save_subtitles(is_subs, youtube)

    video = youtube.streams.get_highest_resolution()

    print(f"We are going to try to download '{youtube.title}' from url '{youtube_url}' "
          f"in the highest available resolution.")

    path_to_video = video.download(DOWNLOAD_FOLDER)

    print(f"Downloaded into '{path_to_video}'")

    get_audio(is_audio, path_to_video, youtube)


def save_subtitles(is_subs, youtube, language='en'):
    if is_subs:
        en_caption = youtube.captions.get_by_language_code(language)

        en_caption_convert_to_srt = (en_caption.generate_srt_captions())  # get srt content

        # save the caption to a video named files
        output_srt_file = DOWNLOAD_FOLDER + "/" + youtube.title + ".srt"
        print(output_srt_file)
        text_file = open(output_srt_file, "w")
        text_file.write(en_caption_convert_to_srt)
        text_file.close()


# should be executed after we get mp4 from youtube
def get_audio(is_audio, path_to_video, youtube):
    if is_audio:
        # ffmpeg -i 'Dumbbell Nan Kilo Moteru Opening「Onegai Muscle」Full Version.mp4' 'Dumbbell Nan Kilo Moteru Opening「Onegai Muscle」Full Version.mp3'
        subprocess.run([
            'ffmpeg',
            '-i',
            path_to_video,
            os.path.join(DOWNLOAD_FOLDER, youtube.title + ".mp3")
        ])

if __name__ == "__main__":
    main(sys.argv[1:])
