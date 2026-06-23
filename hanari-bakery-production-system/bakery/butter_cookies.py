from .kue_kering import KueKering


class ButterCookies(KueKering):
    def __init__(
        self,
        nama: str = "Butter Cookies",
        kode: str = "BC-01",
        bahan_baku=None,
        biaya_produksi: float = 20000,
        harga_jual: float = 45000,
        pcs_per_batch: int = 30,
    ) -> None:
        if bahan_baku is None:
            bahan_baku = {
                "Tepung terigu protein rendah": "200 g",
                "Mentega/butter": "150 g",
                "Gula halus": "75 g",
                "Kuning telur": "2 butir",
                "Vanili": "2 g",
            }
        super().__init__(nama, kode, bahan_baku, biaya_produksi, harga_jual, pcs_per_batch)

    def pengadonan(self) -> str:
        return "Pengadonan: kocok butter + gula halus, masukkan kuning telur, campur tepung hingga jadi adonan."

    def pemanggangan(self) -> str:
        return "Pemanggangan: panggang pada 150C selama ~20 menit hingga matang merata."

    def topping(self) -> str:
        return "Topping: hias dengan choco chip / selai / taburan gula sebelum dipanggang."
