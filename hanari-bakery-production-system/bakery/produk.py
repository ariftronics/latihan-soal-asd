from abc import ABC, abstractmethod
from typing import Dict, List

from .interfaces import Bakeable, Labelable, Packageable


class Produk(Bakeable, Packageable, Labelable, ABC):
    """Kelas induk abstrak untuk seluruh produk Hanari Bakery."""

    def __init__(
        self,
        nama: str,
        kode: str,
        bahan_baku: Dict[str, str],
        biaya_produksi: float,
        harga_jual: float,
        pcs_per_batch: int,
    ) -> None:
        self.nama = nama
        self.kode = kode
        self.bahan_baku = bahan_baku
        self.biaya_produksi = float(biaya_produksi)
        self.harga_jual = float(harga_jual)
        self.pcs_per_batch = int(pcs_per_batch)

    # ---------- Perhitungan ekonomi ----------
    @property
    def biaya_per_pcs(self) -> float:
        return self.biaya_produksi / self.pcs_per_batch

    @property
    def harga_per_pcs(self) -> float:
        return self.harga_jual / self.pcs_per_batch

    @property
    def profit_per_pcs(self) -> float:
        return self.harga_per_pcs - self.biaya_per_pcs

    def estimasi_profit(self, jumlah_pcs: int) -> dict:
        if jumlah_pcs <= 0:
            raise ValueError("Jumlah pcs harus lebih dari 0.")
        total_modal = self.biaya_per_pcs * jumlah_pcs
        total_pendapatan = self.harga_per_pcs * jumlah_pcs
        total_profit = total_pendapatan - total_modal
        margin = (total_profit / total_pendapatan * 100) if total_pendapatan else 0
        return {
            "jumlah_pcs": jumlah_pcs,
            "total_modal": total_modal,
            "total_pendapatan": total_pendapatan,
            "total_profit": total_profit,
            "margin_persen": margin,
        }

    # ---------- Proses produksi (ABSTRACT) ----------
    @abstractmethod
    def pengadonan(self) -> str:
        ...

    @abstractmethod
    def pemanggangan(self) -> str:
        ...

    # ---------- Implementasi interface umum ----------
    def baking(self) -> str:
        return self.pemanggangan()

    def packaging(self) -> str:
        return f"Mengemas {self.nama} ke dalam box/paper bag berlogo Hanari Bakery."

    def labeling(self) -> str:
        return (
            f"Menempel label: {self.nama} | Kode {self.kode} | "
            f"Rp{self.harga_per_pcs:,.0f}/pcs."
        )

    # ---------- Utilitas ----------
    def urutan_proses(self) -> List[str]:
        from .interfaces import Proofable, Toppable

        langkah = [self.pengadonan()]
        if isinstance(self, Proofable):
            langkah.append(self.pengembangan())
        langkah.append(self.pemanggangan())
        if isinstance(self, Toppable):
            langkah.append(self.topping())
        langkah.append(self.packaging())
        langkah.append(self.labeling())
        return langkah

    def simulasi_produksi(self) -> str:
        baris = [f"=== Simulasi Produksi: {self.nama} ({self.kode}) ==="]
        for i, step in enumerate(self.urutan_proses(), start=1):
            baris.append(f"{i}. {step}")
        return "\n".join(baris)

    def info(self) -> str:
        bahan = "\n".join(f"   - {n}: {j}" for n, j in self.bahan_baku.items())
        return (
            f"[{self.kode}] {self.nama} ({type(self).__name__})\n"
            f" Bahan baku (per {self.pcs_per_batch} pcs):\n{bahan}\n"
            f" Biaya produksi : Rp{self.biaya_produksi:,.0f} / {self.pcs_per_batch} pcs "
            f"(Rp{self.biaya_per_pcs:,.0f}/pcs)\n"
            f" Harga jual     : Rp{self.harga_jual:,.0f} / {self.pcs_per_batch} pcs "
            f"(Rp{self.harga_per_pcs:,.0f}/pcs)\n"
            f" Profit/pcs     : Rp{self.profit_per_pcs:,.0f}"
        )
