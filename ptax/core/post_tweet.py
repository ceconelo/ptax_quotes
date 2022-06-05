from tweepy.errors import Unauthorized

from core.log import log
import api.twitter_api as twitter_api


def format_content_post(quotes_ptax):
    """
    We take the dictionary that contains the ptax quotes and transform it into text. This is the text ready
    for posting on twitter.
    """
    log('console').info('Formatting the data.')
    txt = 'BRL USD exchange rate\nPTAX: cotação de compra\n'
    for r in quotes_ptax:
        hora = r['hora']
        compra = r['compra']
        txt += hora + 'h ' + compra + '\n'
    return txt


def tweetAboutIt(quotes_ptax):
    """
    Method responsible for starting the twitter posting process.
    """
    tweettopublish = format_content_post(quotes_ptax)
    query_ptax = 'BRL USD exchange rate  -is:retweet'

    try:
        log('console').info('Preparing to post a new tweet.')
        response = twitter_api.tweet_to_publish(tweettopublish, query_ptax)
        if response is not None:
            log('console').info('Successfully tweeted')
            log('root').info(f'Tweet ID: {response.data["id"]}')
    except Unauthorized as err:
        log('console').error('Put your keys in the settings.ini file.')
        log('console').error('Error: {}'.format(err))
    except BaseException as err:
        log('console').error('Error: {}'.format(err))
