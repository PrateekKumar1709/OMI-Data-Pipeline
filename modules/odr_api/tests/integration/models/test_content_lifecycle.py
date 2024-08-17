from base_integration_test import BaseIntegrationTest, random_string
import json
from odr_api.logger import log_api_request, get_logger
import pytest
from odr_core.crud.content import create_content, get_content, update_content
from odr_core.schemas.content import (
    ContentCreate,
    ContentUpdate,
    Content,
    ContentSourceCreate,
    ContentSourceType,
)

logger = get_logger(__name__)


class TestContentLifecycle(BaseIntegrationTest):
    def test_create_content(self):
        content_data = {
            "name": f"test_content_{random_string()}",
            "type": "image",
            "hash": f"hash_{random_string()}",
            "phash": f"phash_{random_string()}",
            "format": "png",
            "size": 1024,
            "license": "CC0",
            "sources": [
                {
                    "type": "path",
                    "value": "./test_assets/omi_logo.png",
                    "source_metadata": {"source": "test"},
                }
            ],
        }
        response = self.client.post(
            "/content/", json=content_data, headers=self.get_session_auth_headers()
        )
        logger.info(f"Response: {response}")
        log_api_request(
            self.logger,
            "POST",
            "/content/",
            response.status_code,
            content_data,
            response.json(),
        )
        assert (
            response.status_code == 200
        ), f"Failed to create content: {response.status_code}\nResponse body: {response.text}"
        created_content = response.json()
        self.logger.info(f"Created content: {created_content['id']}")
        return created_content

    def test_get_content(self):
        created_content = self.test_create_content()
        content_id = created_content["id"]
        response = self.client.get(
            f"/content/{content_id}", headers=self.get_session_auth_headers()
        )
        log_api_request(
            self.logger,
            "GET",
            f"/content/{content_id}",
            response.status_code,
            None,
            response.json(),
        )
        assert (
            response.status_code == 200
        ), f"Failed to get content: {response.status_code}"
        fetched_content = response.json()
        assert fetched_content["id"] == content_id
        self.logger.info(f"Retrieved content: {content_id}")

    def test_update_content(self):
        created_content = self.test_create_content()
        content_id = created_content["id"]
        update_data = {
            "name": f"updated_content_{random_string()}",
            "meta": {"description": "Updated test content"},
        }
        response = self.client.put(
            f"/content/{content_id}",
            json=update_data,
            headers=self.get_session_auth_headers(),
        )
        log_api_request(
            self.logger,
            "PUT",
            f"/content/{content_id}",
            response.status_code,
            update_data,
            response.json(),
        )
        assert (
            response.status_code == 200
        ), f"Failed to update content: {response.status_code}\nResponse body: {response.text}"
        updated_content = response.json()
        assert updated_content["name"] == update_data["name"]
        assert (
            updated_content["meta"]["description"] == update_data["meta"]["description"]
        )
        self.logger.info(f"Updated content: {content_id}")

    def test_delete_content(self):
        created_content = self.test_create_content()
        content_id = created_content["id"]
        response = self.client.delete(
            f"/content/{content_id}", headers=self.get_session_auth_headers()
        )
        log_api_request(
            self.logger,
            "DELETE",
            f"/content/{content_id}",
            response.status_code,
            None,
            response.json(),
        )
        assert (
            response.status_code == 200
        ), f"Failed to delete content: {response.status_code}\nResponse body: {response.text}"
        self.logger.info(f"Deleted content: {content_id}")

        # Verify deletion
        response = self.client.get(
            f"/content/{content_id}", headers=self.get_session_auth_headers()
        )
        log_api_request(
            self.logger,
            "GET",
            f"/content/{content_id}",
            response.status_code,
            None,
            response.text,
        )
        assert (
            response.status_code == 404
        ), f"Failed to verify deletion of content: {response.status_code}\nResponse body: {response.text}"
        self.logger.info(f"Verified deletion of content: {content_id}")


@pytest.fixture(scope="module")
def content_lifecycle_test(request):
    base_url = request.config.getoption("--api-base-url")
    from odr_core.database import SessionLocal

    db = SessionLocal()
    test = TestContentLifecycle()
    TestContentLifecycle.setup_class(base_url, db, test.logger)
    yield test
    TestContentLifecycle.teardown_class()


def test_content_lifecycle(content_lifecycle_test):
    test = content_lifecycle_test
    test.test_create_content()
    test.test_get_content()
    test.test_update_content()
    test.test_delete_content()
