from src.parcers import get_offers_from_olimp, get_offers_from_betboom, get_offers_from_leon
from src.parcers.classes import TimeOut, NoMarkets
from time import time


class Parser(object):
    _instance = None
    default_timeout_secs = 5
    timeouts = {}
    parsers = [get_offers_from_olimp, get_offers_from_betboom, get_offers_from_leon]

    def __init__(self):
        raise RuntimeError('Call instance() instead')


    def get_parcer_data(self, parser: callable):
        timeout = self.timeouts.get(parser.__name__)
        data = []
        if timeout and time() <= timeout:
            return []
        else:
            try:
                # print(f'parsing {parser.__name__}')
                temp = parser()
                if temp is None or len(temp) == 0:
                    print(f"{parser.__name__} no data")
                if __name__ == '__main__' and parser.__name__ == "get_offers_from_olimp":
                    print(f"olimp: {temp}")
                data += temp
                # print(data)
            except TimeOut:
                print(f'{parser.__name__}: timeout')
                self.timeouts[parser.__name__] = time() + self.default_timeout_secs
            except NoMarkets:
                print(f'{parser.__name__}: no markets')
                data = []
            except Exception as e:
                print(f"{parser.__name__} fucked up: {e}")
        return data

    def get_offers(self):
        offers = []
        for p in self.parsers:
            offers += self.get_parcer_data(p)
        return offers

    def get_data(self):
        offers = self.get_offers()
        data = []
        for o in offers:
            data.append(o.get_dict())
        return data

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    parser = Parser.instance()
    # print(parser.get_offers())
    # print(parser.get_data())
    print(f"main olimp: {parser.get_data()}")

