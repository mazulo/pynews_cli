"""Script to gather news from HackerNews."""
import sys

URL_NEWS_STORIES = 'https://hacker-news.firebaseio.com/v0/newstories.json'

URL_TOP_STORIES = 'https://hacker-news.firebaseio.com/v0/topstories.json'

URL_ITEM = 'https://hacker-news.firebaseio.com/v0/item/{}.json'


def get_top_stories():
    """Return a list of ids of the 500 top stories."""
    pass


def get_new_stories():
    """Return a list of ids of the 500 new stories."""
    pass


def show_stories(list_stories):
    """Show in a formatted way the stories for each item of the list."""
    pass


def main():
    """Main entry point for the script."""
    pass

if __name__ == '__main__':
    sys.exit(main())
