"""Script to gather news from HackerNews."""
from tqdm import tqdm

from new_curses_menu import NewCursesMenu
from cursesmenu.items import FunctionItem
from webbrowser import open as url_open

import argparse
from concurrent.futures import as_completed, ThreadPoolExecutor
import requests as req
import sys

URL_NEWS_STORIES = 'https://hacker-news.firebaseio.com/v0/newstories.json'

URL_TOP_STORIES = 'https://hacker-news.firebaseio.com/v0/topstories.json'

URL_ITEM = 'https://hacker-news.firebaseio.com/v0/item/{}.json'


def get_stories(url):
    """Return a list of ids of the 500 top stories."""
    try:
        data = req.get(url)
    except req.ConnectionError:
        print('A network problem occurred.')
    except req.Timeout:
        print('A timeout problem occurred.')
    except req.TooManyRedirects:
        print('The request exceeds the configured number of maximum \
            redirections.')
    return data.json()


def get_story(new):
    """Return a story of the given ID."""
    url = URL_ITEM.format(new)
    try:
        data = req.get(url)
    except req.ConnectionError:
        print('A network problem occurred.')
    except req.Timeout:
        print('A timeout problem occurred.')
    except req.TooManyRedirects:
        print('The request exceeds the configured number of maximum \
            redirections.')
    return data.json()


def create_list_stories(list_id_stories, number_of_stories):
    """Show in a formatted way the stories for each item of the list."""

    list_stories = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        waits = {
            executor.submit(get_story, new)
            for new in list_id_stories[:number_of_stories]
        }
        for future in tqdm(as_completed(waits), unit='s'):
            list_stories.append(future.result())
    return list_stories


def create_menu(list_dict_stories):
    menu = NewCursesMenu('PyNews', 'Select the new and press enter')
    for story in list_dict_stories:
        if 'url' in story:
            item = FunctionItem(story['title'], url_open, args=[story['url']])
        else:
            msg = 'This new does not have an URL'
            item = FunctionItem(story['title'], print, args=[msg])
        menu.append_item(item)
    return menu


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        prog='PyNews-CLI',
        description='Your news collector inside your terminal! Tell me, what\'s\
                      cooler than that?',
        usage="""
        PyNews-CLI – News Collector from HackerNews API
        Usage: pynews [-t/--top-stories number_of_stories]
                      [-n/--news-stories number_of_stories]

        If the number of stories is not supplied, will be showed all the
        500 stories from the list.

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
        const=499,
        type=int,
        help='Get the top N stories from HackerNews API'
    )
    parser.add_argument(
        '-n',
        '--news-stories',
        nargs='?',
        const=499,
        type=int,
        help='Get the N new stories from HackerNews API'
    )
    options = parser.parse_args()
    if options.top_stories:
        list_dict_stories = create_list_stories(
            get_stories(URL_TOP_STORIES), options.top_stories
        )

    elif options.news_stories:
        list_dict_stories = create_list_stories(
            get_stories(URL_NEWS_STORIES), options.news_stories
        )

    menu = create_menu(list_dict_stories)
    menu.show()

if __name__ == '__main__':
    sys.exit(main())
