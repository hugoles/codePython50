import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    source = re.search('src="([^"]+)"', s)
    if source and 'youtube.com' in source.group(1):
        video_id = source.group(1).split('/')[-1]
        url = f"https://youtu.be/{video_id}"
        return url
    else:
        return "None"

if __name__ == "__main__":
    main()
