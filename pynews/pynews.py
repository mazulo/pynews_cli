"""Script to gather news from HackerNews."""
import argparse
import multiprocessing
import sys

import requests as req

from .utils import get_stories, create_list_stories, create_menu


DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        prog='PyNews-CLI',
        description='Your news collector inside your terminal! Tell me, what\'s\
                      cooler than that?',
        usage="""
        PyNews-CLI - News Collector from HackerNews API
        Usage: pynews [-t/--top-stories number_of_stories]
                      [-n/--news-stories number_of_stories]

        If the number of stories is not supplied, will be showed 200 from the
        500 stories.

        Examples:
        - Get Top Stories:
            $ pynews -t 10 # or
            $ pynews --top-stories 10
            This will show the 10 first top stories from the list of 500.

        - Get New Stories:
            $ pynews -n 10 # or
            $ pynews --news-stories
            This will show the 10 first new stories from the list of 500.

        Get basic options and Help, use: -h\--help

        """,
    )
    parser.add_argument(
        '-t',
        '--top-stories',
        nargs='?',
        const=200,
        type=int,
        help='Get the top N stories from HackerNews API'
    )

    parser.add_argument(
        '-n',
        '--news-stories',
        nargs='?',
        const=200,
        type=int,
        help='Get the N new stories from HackerNews API'
    )

    parser.add_argument(
        '-s',
        '--shuffle',
        nargs='?',
        const=False,
        type=bool,
        help='Get the N new stories from HackerNews API'
    )

    parser.add_argument(
        '-T',
        '--threads',
        nargs='?',
        const=DEFAULT_THREADS_NUMBER,
        type=int,
        help='Determine the number max of threads'
    )

    options = parser.parse_args()

    if options.top_stories:
        param = options.top_stories, 'top'
    else:
        param = options.news_stories, 'news'

    list_data = None

    try:
        list_data = get_stories(param[1])
    except req.ConnectionError:
        print('A connection problem occurred.')
    except req.Timeout:
        print('A timeout problem occurred.')
    except req.TooManyRedirects:
        print('The request exceeds the configured number\
            of maximum redirections.')

    if not list_data:
        return

    max_threads = (
        options.threads if options.threads or 0 > 0 else DEFAULT_THREADS_NUMBER
    )

    list_dict_stories = create_list_stories(
        list_data,
        param[0],
        options.shuffle,
        max_threads
    )

    menu = create_menu(list_dict_stories, param[1])
    menu.show()


if __name__ == '__main__':
    sys.exit(main())
