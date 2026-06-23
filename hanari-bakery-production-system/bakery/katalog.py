from typing import List

from .butter_cookies import ButterCookies
from .croissant import Croissant
from .muffin import Muffin
from .produk import Produk
from .roti_manis import RotiManis


def katalog_default() -> List[Produk]:
    """Mengembalikan daftar produk awal Hanari Bakery."""
    return [RotiManis(), Croissant(), ButterCookies(), Muffin()]
