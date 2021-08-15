import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Combine audio and GIF files to create loops with unique audio effects.')
    parser.add_argument('audio_file', type=str,
                        help='the audio file to be looped')
    parser.add_argument('video_file', type=str,
                        help='the video file to be looped')
    args = parser.parse_args()

    audio_file: str = args.audio_file
    video_file: str = args.video_file
