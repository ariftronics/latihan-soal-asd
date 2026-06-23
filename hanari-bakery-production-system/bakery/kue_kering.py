from abc import ABC

from .interfaces import Toppable
from .produk import Produk


class KueKering(Produk, Toppable, ABC):
    """Kategori kue kering. Semua kue kering memiliki proses topping."""

    def topping(self) -> str:
        return f"Memberi topping standar pada {self.nama}."
