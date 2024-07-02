# tests/test_app.py
import sys
import os

# Ensure the app module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import hello

def test_hello():
    assert hello() == "Hello, GitHub Actions!"
    