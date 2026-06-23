from .interfaces import Proofable
from .produk import Produk


class Croissant(Produk, Proofable):
    def __init__(
        self,
        nama: str = "Croissant",
        kode: str = "CR-01",
        bahan_baku=None,
        biaya_produksi: float = 27000,
        harga_jual: float = 54000,
        pcs_per_batch: int = 9,
    ) -> None:
        if bahan_baku is None:
            bahan_baku = {
                "Tepung terigu protein tinggi": "250 g",
                "Butter (lipatan)": "150 g",
                "Gula pasir": "30 g",
                "Ragi instan": "5 g",
                "Susu cair": "130 ml",
                "Garam": "5 g",
            }
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual, pcs_per_batch)

    def pengadonan(self) -> str:
        return "Pengadonan: membuat detrempe lalu melaminasi adonan dengan butter (3x single fold)."

    def pengembangan(self) -> str:
        return "Pengembangan: proofing suhu ruang ~2 jam hingga adonan mengembang dan berlapis."

    def pemanggangan(self) -> str:
        return "Pemanggangan: panggang pada 200C selama ~18 menit hingga renyah berlapis."
