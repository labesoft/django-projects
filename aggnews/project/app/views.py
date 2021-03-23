"""The Views of the News Aggregator Web App
-----------------------------

About this Module
-----------------

The goal of this module is to generate the views of the News AggregatorThis view
function uses modules like requests, bs4 and Django’s shortcuts.

We have imported the model Headline from news.models. Also, we have other
libraries.

The beautiful soup is a library that can extract data from HTML web pages. We
create a soup object where we pass the HTML page. Alongside the HTML page,
we also pass HTML parser as a parameter.

The HTML parser will parse the HTML as a BeautifulSoup object. In this
object, we can access HTML elements and their texts.
"""

__author__ = "Benoit Lapointe"
__date__ = "2021-03-19"
__copyright__ = "Copyright 2021, labesoft"
__version__ = "1.0.0"

from datetime import timedelta
from urllib.parse import urljoin

import requests
from app.models import Headline
from bs4 import BeautifulSoup as BSoup
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.utils import timezone


def generate_news(request):
    """Renders home page with headlines context

    It first removes expired articles and then fetches all articles in the DB
    and add them into the context.

    :param request: the request from the view
    :return: redered home page with the headlines context
    """
    # Remove expired headlines
    expiration_delay = timezone.now() - timedelta(minutes=1)
    Headline.objects.filter(created_at__lt=expiration_delay).delete()
    Headline.objects.filter(created_at__isnull=True).delete()

    # Add remaining headlines
    headlines = Headline.objects.all()[::-1]
    context = {'object_list': headlines}
    return render(request, "home.html", context)


def scrape(request):
    """The scrape() method will scrape the news articles from news urls.

    The first line of the function is a setting for requests framework. These
    settings are necessary. They will prevent the errors to stop the execution of
    the program.

    The first variable is the session object of the requests module. These are
    essential to make a connection to the server. This is the abstraction
    provided by requests framework.

    The session variables have headers as HTTP headers. These headers are used by
    our function to request the webpage. The scrapper acts like a normal http
    client to the news site. The User-Agent key is important here.

    This HTTP header will tell the server information about the client. We are
    using Google bot for that purpose. When our client requests anything on the
    server, the server sees our request coming as a Google bot. You can configure
    it look like a browser User-Agent.

    :param request: the http request
    :return: redirect to the home page
    """
    session = requests.Session()
    session.headers = {
        "User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"
    }
    create_headlines(
        session,
        "https://www.journaldemontreal.com/",
        'div',
        {"class": "item"},
        get_jdem
    )
    create_headlines(
        session,
        "https://www.lapresse.ca/",
        'div',
        {"class": ["homeSectionHeadlinesCard__inner",
                   "editorsChoiceCard__inner"]},
        get_presse
    )
    create_headlines(
        session,
        "https://www.ledevoir.com/",
        'article',
        {"class": "article"},
        get_devoir
    )
    create_headlines(
        session,
        "https://ici.radio-canada.ca/",
        'div',
        {"class": "container-main-card"},
        get_ici
    )
    create_headlines(
        session,
        "https://montrealgazette.com/",
        'div',
        {"class": "article-card__content"},
        get_gazette
    )
    return redirect("../")


def create_headlines(session, url, tag_name, tag_filter, get_func):
    """Get the content of a news site and store it in a Headline

    In the News object, we return the tag of a particular class (tag_filter).
    We selected this class from the webpage inspection. We inspected the
    homepage of the website. Then we select the elements which have the
    information we need.

    :param session: a google bot session
    :param url: the url of the news homepage
    :param tag_name: the tag name of the target section
    :param tag_filter: the classe name which filter which section to pick
    :param get_func: the get function callback for a specific provider
    """
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    news = soup.find_all(tag_name, tag_filter)

    for article in news:
        try:
            image_src, link, title = get_func(article, url)
        except (KeyError, AttributeError, IndexError, TypeError) as e:
            continue
        create_headline(image_src, link, title)


def create_headline(image_src, link, title):
    """Create one Headline and add it to the DB if not already there

    :param title: the title of the article and also the primary key
    :param link: the link of the article
    :param image_src: the image url of the article
    """
    try:
        Headline.objects.create(
            title=title, url=link, image=image_src
        )
    except IntegrityError as err:
        return


def get_devoir(article, url):
    """Get news from ledevoir site

    :param article: the article to inspect
    :param url: the url of the news homepage
    :return: a tuple of the information gathered
    """
    main = article.find_all("a")
    if not main:
        main = [article]
    title = main[0].find("h2")
    if title:
        title = title.get_text().strip("\n ")
    else:
        title = main[1].get_text().strip("\n ")
    link = urljoin(url, main[0]['href'])
    image_src = main[0].find('img')['data-src']
    return image_src, link, title


def get_gazette(article, url):
    """Get news from montrealgazette site

    :param article: the article to inspect
    :param url: the url of the news homepage
    :return: a tuple of the information gathered
    """
    main = article.find_all('a')[1]
    title = main["aria-label"]
    link = urljoin(url, main["href"])
    image_src = article.find_all('img')[0]["src"]
    return image_src, link, title


def get_ici(article, url):
    """Get news from ici radio-canada site

    :param article: the article to inspect
    :param url: the url of the news homepage
    :return: a tuple of the information gathered
    """
    main = article.find_all('a')[0]
    title = main['title'].strip()
    link = urljoin(url, main['href'])
    image_src = article.find_all("img")[0]['src']
    return image_src, link, title


def get_jdem(article, url):
    """Get news from journal de montreal site

    :param article: the article to inspect
    :param url: the url of the news homepage
    :return: a tuple of the information gathered
    """
    main = article.find_all('a')[0]
    title = main.find("h2").contents[0].strip()
    link = main['href']
    image_src = str(main.find('img')['srcset']).split(" ")[0]
    return image_src, link, title


def get_presse(article, url):
    """Get news from lapresse site

    :param article: the article to inspect
    :param url: the url of the news homepage
    :return: a tuple of the information gathered
    """
    main = article.find_all('a')[0]
    title = main['title'].strip()
    link = main['href']
    image_src = main.find('img')['src']
    return image_src, link, title
