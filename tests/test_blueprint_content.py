"""Tests for the homepage Blueprint routes."""

from application.app import app

def test_main_page_content():
    """Test that the main homepage route returns 200 and contains 'Blueprint'."""
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b'Blueprint' in response.data


def test_about_page_content():
    """Test that the about route returns 200 and contains 'Blueprint'."""
    tester = app.test_client()
    response = tester.get('/about')
    assert response.status_code == 200
    assert b'Blueprint' in response.data
