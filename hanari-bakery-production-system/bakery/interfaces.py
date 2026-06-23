from abc import ABC, abstractmethod


class Bakeable(ABC):
    """Interface standar proses pemanggangan (baking)."""

    @abstractmethod
    def baking(self) -> str:
        ...


class Packageable(ABC):
    """Interface standar proses pengemasan (packaging)."""

    @abstractmethod
    def packaging(self) -> str:
        ...


class Labelable(ABC):
    """Interface standar proses pelabelan (labeling)."""

    @abstractmethod
    def labeling(self) -> str:
        ...


class Proofable(ABC):
    """Interface untuk produk yang memiliki proses pengembangan (proofing)."""

    @abstractmethod
    def pengembangan(self) -> str:
        ...


class Toppable(ABC):
    """Interface untuk produk yang memiliki proses topping."""

    @abstractmethod
    def topping(self) -> str:
        ...
