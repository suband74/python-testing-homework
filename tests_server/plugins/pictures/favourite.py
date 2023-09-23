from typing import Protocol, TypedDict, final


@final
class FavouritePictureData(TypedDict, total=False):
    """Represent the simplified favourite picture data."""

    foreign_id: int
    url: str


class FavouritePictureDataFactory(Protocol):
    """Protocol for FavouritePictureData data factory."""

    def __call__(
        self,
        **fields: 'FavouritePictureData',
    ) -> FavouritePictureData:
        """Favourite picture data factory protocol."""
