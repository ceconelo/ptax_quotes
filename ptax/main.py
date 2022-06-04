from datetime import datetime

from core.parser_bo_ptax import ParserBoPtax
from core.post_tweet import tweetAboutIt
from core.log import log


def main():
    # _request_data = datetime.today().strftime('%d/%m/%Y')
    _request_data = '03/06/2022' # test

    pbop = ParserBoPtax(request_data=_request_data)
    quotes_ptax = pbop.start()
    tweetAboutIt(quotes_ptax=quotes_ptax)


if __name__ == '__main__':
    log('console').info('Initializing...')
    main()
