# -*- coding: utf-8 -*-

"""Console script for grips."""
import argparse
import sys

from InstagramAPI import InstagramAPI


def main():
    """Console script for grips."""
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help="Instagram username")
    parser.add_argument('password', help="Instagram password")
    args = parser.parse_args()

    api = InstagramAPI(args.username, args.password)

    api.login()

    # currently not working due to Instagram
    photo_path = 'C:\\Users\\goali\\Downloads\\www.reddit.com_r_science_.jpg'
    caption = "Interesting"
    api.uploadPhoto(photo_path, caption=caption)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
