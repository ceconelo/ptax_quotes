from tweepy.errors import Unauthorized

from ptax.core.log import log
import ptax.api.twitter_api as twitter_api


def format_content_post(quotes_ptax):
    log('console').info('Formatting the data.')
    txt = 'BRL USD exchange rate\nPTAX: cotação de compra\n'
    for r in quotes_ptax:
        hora = r['hora']
        compra = r['compra']
        txt += hora + 'h ' + compra + '\n'
    return txt


def tweetAboutIt(quotes_ptax):
    tweettopublish = format_content_post(quotes_ptax)
    query_ptax = 'BRL USD exchange rate  -is:retweet'

    try:
        log('console').info('Preparing to post a new tweet.')
        response = twitter_api.tweet_to_publish(tweettopublish, query_ptax)
        if response is not None:
            log('console').info('Successfully tweeted')
            log('root').info(f'Tweet ID: {response.data["id"]}')
            print(tweettopublish)
            log('root').info(str(tweettopublish))
    except Unauthorized as err:
        log('console').error('Put your keys in the settings.ini file.')
        log('console').error('Error: {}'.format(err))
    except BaseException as err:
        log('console').error('Error: {}'.format(err))

