from datetime import datetime
from time import sleep
import argparse

from core.parser_bo_ptax import ParserBoPtax
from core.post_tweet import tweetAboutIt
from core.log import log


def get_argument():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-t', '--time', help='Set an time (E.g hh:mm)', required=True)
    args = arg_parser.parse_args()
    if args.time:
        return args.time


def main():
    # _request_data = datetime.today().strftime('%d/%m/%Y')
    _request_data = '03/06/2022'  # test
    pbop = ParserBoPtax(request_data=_request_data)

    control = True
    while control:
        quotes_ptax = pbop.start()

        if quotes_ptax is None:
            log('console').info('There are no quotes for that date.')
        else:
            if quotes_ptax[-1].get('hora') >= get_argument():
                log('console').info('A new quote has been found.')
                tweetAboutIt(quotes_ptax=quotes_ptax)
                control = False
            else:
                log('console').info('No new quotes found.')
            sleep(10)


if __name__ == '__main__':
    log('console').info('Initializing...')
    main()
