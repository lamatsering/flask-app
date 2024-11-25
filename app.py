from flask import Flask  # Import the Flask class

app = Flask(__name__)  # Create an instance of the Flask class

@app.route("/")  # Define the route for the homepage
def home():
    return "<h1> WElcome to my first Flask App!</hi>"  # Return a response when the route is accessed

if __name__ == "__main__":  # Run the application
    app.run(host="0.0.0.0", port=5000)
