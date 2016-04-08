from tqdm import tqdm
from cursesmenu import CursesMenu
from cursesmenu.items import FunctionItem
from webbrowser import open as url_open

from concurrent.futures import as_completed, ThreadPoolExecutor
import requests as req
import random


URL_NEWS_STORIES = 'https://hacker-news.firebaseio.com/v0/newstories.json'

URL_TOP_STORIES = 'https://hacker-news.firebaseio.com/v0/topstories.json'

URL_ITEM = 'https://hacker-news.firebaseio.com/v0/item/{}.json'

URLS = {
    'top': URL_TOP_STORIES,
    'news': URL_NEWS_STORIES,
    'item': URL_ITEM
}


def show(arg):
    print(arg)
    return


def get_stories(type_url):
    """Return a list of ids of the 500 top stories."""
    data = req.get(URLS[type_url])
    return data.json()


def get_story(new):
    """Return a story of the given ID."""
    url = URLS['item'].format(new)
    try:
        data = req.get(url)
    except req.ConnectionError:
        raise
    except req.Timeout:
        raise req.Timeout('A timeout problem occurred.')
    except req.TooManyRedirects:
        raise req.TooManyRedirects('The request exceeds the configured number\
            of maximum redirections.')
    else:
        return data.json()


def create_list_stories(list_id_stories, number_of_stories, shuffle):
    """Show in a formatted way the stories for each item of the list."""

    list_stories = []
    with ThreadPoolExecutor(max_workers=8) as executor:
        waits = {
            executor.submit(get_story, new)
            for new in list_id_stories[:number_of_stories]
        }
        for future in tqdm(
            as_completed(waits),
            desc='Getting results',
            unit=' news',
        ):
            list_stories.append(future.result())
    if shuffle:
        random.shuffle(list_stories)
    return list_stories


def create_menu(list_dict_stories, type_new):
    title = 'Pynews - {} stories'.format(type_new.capitalize())
    menu = CursesMenu(title, 'Select the new and press enter')
    for story in list_dict_stories:
        if 'url' in story:
            item = FunctionItem(story['title'], url_open, args=[story['url']])
        else:
            msg = 'This new does not have an URL'
            item = FunctionItem(story['title'], show, args=[msg])
        menu.append_item(item)
    return menu
