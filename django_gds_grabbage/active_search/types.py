from typing import Any, Protocol


class SelectableObject(Protocol):
    """An object with a primary key (pk) which is stringable."""

    pk: Any

    def __str__(self) -> str:
        ...
