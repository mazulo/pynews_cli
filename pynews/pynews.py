"""
Script to gather news from HackerNews.
"""
import sys

import requests as req

from .constants import DEFAULT_THREADS_NUMBER
from .parser import get_parser_options
from .utils import create_list_stories, create_menu, get_stories


def main():
    """Main entry point for the script."""
    options = get_parser_options()

    if options.top_stories:
        param = options.top_stories, "top"
    else:
        param = options.news_stories, "news"

    list_data = None

    try:
        list_data = get_stories(param[1])
    except req.ConnectionError:
        print("A connection problem occurred.")
    except req.Timeout:
        print("A timeout problem occurred.")
    except req.TooManyRedirects:
        print(
            "The request exceeds the configured number\
            of maximum redirections."
        )

    if not list_data:
        return

    max_threads = (
        options.threads if options.threads or 0 > 0 else DEFAULT_THREADS_NUMBER
    )

    list_dict_stories = create_list_stories(
        list_data, param[0], options.shuffle, max_threads
    )

    menu = create_menu(list_dict_stories, param[1])
    menu.show()


if __name__ == "__main__":
    sys.exit(main())
