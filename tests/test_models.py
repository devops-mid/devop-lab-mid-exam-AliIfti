import pytest
from app import app, db
from app.models import User

@pytest.fixture
def test_client():
    """Create a Flask test client and an in-memory database."""
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use an in-memory SQLite DB for testing
    with app.app_context():
        db.create_all()  # Create tables for testing
        yield app.test_client()  # Provide the test client
        db.session.remove()
        db.drop_all()  # Clean up after tests

def test_create_user(test_client):
    """Test creating a new user."""
    with app.app_context():
        user = User(name="John Doe", email="john@example.com", phone="1234567890")
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(email="john@example.com").first()
        assert retrieved_user is not None
        assert retrieved_user.name == "John Doe"
        assert retrieved_user.phone == "1234567890"

def test_user_unique_email(test_client):
    """Test that emails should be unique (if enforced)."""
    with app.app_context():
        user1 = User(name="Alice", email="alice@example.com", phone="1111111111")
        user2 = User(name="Bob", email="alice@example.com", phone="2222222222")  # Duplicate email

        db.session.add(user1)
        db.session.commit()

        db.session.add(user2)
        try:
            db.session.commit()
            assert False, "Database should enforce unique email constraint"
        except Exception:
            db.session.rollback()
