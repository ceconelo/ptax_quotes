from datetime import datetime

import argparse

from core.parser_bo_ptax import ParserBoPtax
from core.post_tweet import tweetAboutIt
from core.log import log
from core.utils import countdown


def get_argument():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-t', '--time', help='Set an time (E.g hh:mm)', required=True)
    args = arg_parser.parse_args()
    if args.time:
        return args.time


def main():
    # _request_data = datetime.today().strftime('%d/%m/%Y')
    _request_data = '04/06/2022'  # test
    pbop = ParserBoPtax(request_data=_request_data)

    while True:
        quotes_ptax = pbop.start()

        if quotes_ptax is None:
            log('console').info('There are no quotes for that date.')
        else:
            if quotes_ptax[-1].get('hora') >= get_argument():
                log('console').info('A new quote has been found.')
                tweetAboutIt(quotes_ptax=quotes_ptax)
                break
            else:
                log('console').info('No new quotes found.')
        countdown(300)  # 5 min


if __name__ == '__main__':
    log('console').info('Initializing...')
    main()
