from .interfaces import Proofable
from .produk import Produk


class RotiManis(Produk, Proofable):
    def __init__(
        self,
        nama: str = "Roti Manis",
        kode: str = "RM-01",
        bahan_baku=None,
        biaya_produksi: float = 18000,
        harga_jual: float = 36000,
        pcs_per_batch: int = 12,
    ) -> None:
        if bahan_baku is None:
            bahan_baku = {
                "Tepung terigu protein tinggi": "250 g",
                "Gula pasir": "50 g",
                "Ragi instan": "5 g",
                "Susu bubuk": "15 g",
                "Telur": "1 butir",
                "Mentega": "30 g",
                "Air": "125 ml",
                "Garam": "3 g",
            }
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual, pcs_per_batch)

    def pengadonan(self) -> str:
        return "Pengadonan: mencampur tepung, ragi, gula, susu, telur, lalu menguleni hingga kalis elastis."

    def pengembangan(self) -> str:
        return "Pengembangan: fermentasi ~60 menit hingga mengembang 2x, lalu proofing kedua ~30 menit."

    def pemanggangan(self) -> str:
        return "Pemanggangan: panggang pada 180C selama ~15 menit hingga keemasan."
