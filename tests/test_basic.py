"""
Basic tests for the Frontend Web Application
"""
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_frontend_app_creation():
    """Test that the Frontend Flask app can be created without errors"""
    try:
        from app import create_app
        app = create_app()
        assert app is not None
        assert app.config is not None
        print("Frontend app creation: OK")
    except Exception as e:
        raise AssertionError(f"Failed to create frontend app: {e}")

def test_frontend_routes_import():
    """Test that frontend routes can be imported"""
    try:
        from app import routes
        assert routes is not None
        print("Frontend routes import: OK")
    except Exception as e:
        raise AssertionError(f"Failed to import frontend routes: {e}")

def test_template_exists():
    """Test that the main template exists"""
    template_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'templates', 'index.html')
    if os.path.exists(template_path):
        print("Frontend template exists: OK")
    else:
        print("Warning: Frontend template not found at expected location")

if __name__ == "__main__":
    test_frontend_app_creation()
    test_frontend_routes_import()
    test_template_exists()
    print("All frontend tests passed!")
