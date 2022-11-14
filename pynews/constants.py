import multiprocessing

DEFAULT_THREADS_NUMBER = multiprocessing.cpu_count()

URL_NEWS_STORIES = "https://hacker-news.firebaseio.com/v0/newstories.json"

URL_TOP_STORIES = "https://hacker-news.firebaseio.com/v0/topstories.json"

URL_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"

URLS = {"top": URL_TOP_STORIES, "news": URL_NEWS_STORIES, "item": URL_ITEM}
