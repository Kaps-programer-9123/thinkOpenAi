import pytest
import json
from django.urls import reverse
from django.test import Client
from chunking.views import fixSize, validator
from unittest.mock import Mock

@pytest.fixture
def text():
    return "Lena was a curious girl who loved exploring the woods behind her house every afternoon she would pack a small bag with snacks a notebook and her favorite compass one day she discovered a trail she had never seen before it led her to a hidden pond with crystal clear water and colorful fish swimming near the surface excited she began sketching what she saw in her notebook suddenly a small turtle climbed out of the water and looked at her as if it wanted to say something she laughed and said hello little one this became her secret spot a magical place she would return to again and again."

# Test for the validator function
def test_validator_valid_request():
    # Simulate a POST request with valid JSON data
    request_data = {
        "text": "Some test text",
        "size": 100,
        "overlap": 10,
        "separators": ","
    }
    
    # Mock request object for validator function
    request = Mock()
    request.body = json.dumps(request_data).encode('utf-8')
    request.method = 'POST'
    request.GET = {}

    # Call validator function directly
    result, input_text, size, overlap, separators = validator(request)
    
    # Assert the results
    assert result == "No_error"
    assert input_text == "Some test text"
    assert size == 100
    assert overlap == 10
    assert separators == ","

# Test for the fixSize function using Django test client
@pytest.mark.django_db
def test_fixSize(client):
    url = reverse('fixsize')  # Or use '/fixsize/' if reverse isn't configured
    request_data = {
        "text": "Some test text that needs to be chunked",
        "size": 10,
        "overlap": 2,
        "separators": ","
    }

    response = client.post(url, data=json.dumps(request_data), content_type='application/json')
    
    assert response.status_code == 200
    data = response.json()
    assert "chunk data" in data
    assert data["size"] == 10
