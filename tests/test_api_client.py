from unittest.mock import Mock, patch 
from frontend.utils.api_client import get_population

@patch("frontend.utils.api_client.requests.get")
def test_get_population_returns_json(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {"country_name": "Denmark"}
    mock_get.return_value = mock_response
    
    result = get_population("Denmark")
    
    mock_get.assert_called_once_with(
        "http://backend:8000/population?country=Denmark"
    )
    assert result == {"country_name": "Denmark"}
    
    '''
    This is a real unit test because you isolate one function:
get_population("Denmark")
and test it without making a real HTTP request.
@patch(...)
Replaces requests.get with a fake version during the test.
That means:
- no real backend call
- no network dependency
- fast and predictable test
mock_response.json.return_value = ...
Makes the fake HTTP response behave like a real requests response.
mock_get.assert_called_once_with(...)
Checks that your function builds the correct URL.
assert result == ...
Checks that your function returns the expected JSON.
This is especially good because it shows you understand mocking, which is strong for the exam.
    '''