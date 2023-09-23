from http import HTTPStatus
from typing import TYPE_CHECKING

import pytest
from django.test import Client
from django.urls import reverse

from server.apps.identity.models import User

if TYPE_CHECKING:
    from plugins.identity.user import (
        RegistrationData,
        UserAssertion,
        UserData,
    )


@pytest.mark.django_db()
def test_user_update(
    as_user: User,
	auth_client: Client,
	user_data: 'UserData',
	assert_correct_user: 'UserAssertion',
) -> None:
	"""Test that registration works with correct user data."""
	response = auth_client.post(
		reverse('identity:user_update'),
		data=user_data,
	)

	assert response.status_code == HTTPStatus.FOUND
	assert response.get('Location') == reverse('identity:user_update')
	assert_correct_user(as_user.email , user_data)
