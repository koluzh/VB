import os
from src.parcers.betboom_parcer import get_offers_from_betboom
from src.parcers.leon_parcer import get_offers_from_leon
from src.parcers.olimp_parcer import get_offers_from_olimp

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

leon = 'leon'
positive = 'positive'
betboom = 'betboom'
olimp = 'olimp'

utf = 'utf-8'
