from datetime import date
from typing import Protocol, TypedDict, Unpack, final, Callable, TypeAlias
import pytest


class UserData(TypedDict, total=False):
    """
    Represent the simplified user data that is required to create a new user.
    It does not include ``password``, because it is very special in django.
    Importing this type is only allowed under ``if TYPE_CHECKING`` in tests.
    """
    email: str
    first_name: str
    last_name: str
    date_of_birth: date
    address: str
    job_title: str
    phone: str
    phone_type: int


@final
class RegistrationData(UserData, total=False):
    """
    Represent the registration data that is required to create a new user.
    Importing this type is only allowed under ``if TYPE_CHECKING`` in tests.
    """
    password1: str
    password2: str


@final
class RegistrationDataFactory(Protocol):
    """Protocol for registration data factory."""
    def __call__(self, **fields: Unpack[RegistrationData],) -> RegistrationData:
        """User data factory protocol."""


UserAssertion: TypeAlias = Callable[[str, UserData], None]


@pytest.fixture()
def registration_data(registration_data_factory: RegistrationDataFactory,) -> RegistrationData:
    """Returns fake random data for regitration."""
    return registration_data_factory()
