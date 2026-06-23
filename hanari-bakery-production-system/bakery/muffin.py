from .interfaces import Proofable
from .kue_kering import KueKering


class Muffin(KueKering, Proofable):
    def __init__(
        self,
        nama: str = "Muffin",
        kode: str = "MF-01",
        bahan_baku=None,
        biaya_produksi: float = 22000,
        harga_jual: float = 48000,
        pcs_per_batch: int = 12,
    ) -> None:
        if bahan_baku is None:
            bahan_baku = {
                "Tepung terigu serbaguna": "200 g",
                "Gula pasir": "150 g",
                "Baking powder": "10 g",
                "Telur": "2 butir",
                "Susu cair": "120 ml",
                "Minyak/mentega cair": "80 g",
                "Choco chips (topping)": "100 g",
            }
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual, pcs_per_batch)

    def pengadonan(self) -> str:
        return "Pengadonan: mencampur bahan kering dan basah secukupnya (jangan over-mix)."

    def pengembangan(self) -> str:
        return "Pengembangan: diamkan adonan ~15 menit agar baking powder aktif & muffin mengembang tinggi."

    def pemanggangan(self) -> str:
        return "Pemanggangan: panggang pada 180C selama ~22 menit hingga matang."

    def topping(self) -> str:
        return "Topping: taburkan choco chips / streusel di atas adonan sebelum dipanggang."
