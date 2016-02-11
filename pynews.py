"""Script to gather news from HackerNews."""
import argparse
import sys

URL_NEWS_STORIES = 'https://hacker-news.firebaseio.com/v0/newstories.json'

URL_TOP_STORIES = 'https://hacker-news.firebaseio.com/v0/topstories.json'

URL_ITEM = 'https://hacker-news.firebaseio.com/v0/item/{}.json'


def get_top_stories(url):
    """Return a list of ids of the 500 top stories."""
    pass


def get_new_stories(url):
    """Return a list of ids of the 500 new stories."""
    pass


def show_stories(list_stories):
    """Show in a formatted way the stories for each item of the list."""
    pass


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
        - Get Lyrics:
            $ pynews -t 10 # or
            $ pynews --top-stories 10
            This will show the 10 first top stories from the list of 500.

        - Get Discography:
            $ pynews -n 10 # or
            $ pynews --news-stories
            This will show the 10 first new stories from the list of 500.

        Get basic options and Help, use: -h\--help

        """
    )
    parser.add_argument(
        '-t',
        '--top-stories',
        type=int,
        help='Get the top N stories from HackerNews API'
    )
    parser.add_argument(
        '-n',
        '--news-stories',
        type=int,
        help='Get the N new stories from HackerNews API'
    )
    options = parser.parse_args()
    print(options)

if __name__ == '__main__':
    sys.exit(main())
