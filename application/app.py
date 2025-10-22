from flask import Flask
from application.bp.homepage.routes import homepage

def init_app():
    """Factory function that creates and configures the Flask app."""
    # Step 1: Create a Flask app instance
    app = Flask(__name__)

    # Step 2: Register your Blueprint
    app.register_blueprint(homepage)

    # Step 3: Return the configured app
    return app

# Optional: also create a global app instance
app = init_app()

# Step 4: Allow running the app directly
if __name__ == "__main__":
    app.run(debug=True)
