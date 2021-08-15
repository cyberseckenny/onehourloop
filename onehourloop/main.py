import argparse

from os.path import exists

from colorama import Fore, init
init()


def main(audio_file: str, gif_file: str):
    has_errors: bool = False

    if not exists(audio_file):
        message(
            f'{Fore.LIGHTRED_EX}Could not find audio file {audio_file}, did you specify the wrong file name?')
        has_errors = True
    elif not audio_file.endswith('.mp3'):
        message(
            f'{Fore.LIGHTRED_EX}Only audio files with the mp3 file format are supported.')
        has_errors = True

    if not exists(gif_file):
        message(
            f'{Fore.LIGHTRED_EX}Could not find gif file {gif_file}, did you specify the wrong file name?')
        has_errors = True
    elif not gif_file.endswith('.gif'):
        message(
            f'{Fore.LIGHTRED_EX}You must specify a valid gif file.')
        has_errors = True

    if has_errors:
        return


def message(message: str):
    print(f'{Fore.RESET}{message}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Combine audio and GIF files to create loops with unique audio effects.')
    parser.add_argument('audio_file', type=str,
                        help='the audio file to be looped')
    parser.add_argument('gif_file', type=str,
                        help='the video file to be looped')
    args = parser.parse_args()

    audio_file: str = args.audio_file
    gif_file: str = args.video_file
