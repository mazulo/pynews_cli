import argparse

from .constants import DEFAULT_THREADS_NUMBER


def get_parser_options() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="PyNews-CLI",
        description="Your news collector inside your terminal! Tell me, what's\
                          cooler than that?",
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
        "-t",
        "--top-stories",
        nargs="?",
        const=200,
        type=int,
        help="Get the top N stories from HackerNews API",
    )

    parser.add_argument(
        "-n",
        "--news-stories",
        nargs="?",
        const=200,
        type=int,
        help="Get the N new stories from HackerNews API",
    )

    parser.add_argument(
        "-s",
        "--shuffle",
        nargs="?",
        const=False,
        type=bool,
        help="Get the N new stories from HackerNews API",
    )

    parser.add_argument(
        "-T",
        "--threads",
        nargs="?",
        const=DEFAULT_THREADS_NUMBER,
        type=int,
        help="Determine the number max of threads",
    )

    options = parser.parse_args()
    return options
