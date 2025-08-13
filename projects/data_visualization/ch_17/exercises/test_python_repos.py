import pytest

from python_repos import get_github_token, make_request, response_to_dict

@pytest.fixture
def response():
    token = get_github_token()
    return make_request(token)

def test_status_code(response):
    """Test if status code is 200."""
    status_code = response.status_code
    assert status_code == 200

def test_repo_count(response):
    """Test if the number of repos returned is as expected."""
    res_dict = response_to_dict(response)
    repo_count = len(res_dict['items'])
    assert repo_count > 10
