# Importing the Sanic class from the sanic package to create a web server
# Importing the json function to send JSON responses
from sanic import Sanic
from sanic.response import json

# Creating an instance of the Sanic application named "MyApp"
app = Sanic("MyApp")

# Defining a route "/hello" which will trigger the 'test' function when accessed via HTTP GET
@app.route("/hello")
async def test(request):
    # When a request is made to "/hello", the server responds with a JSON message
    # The response contains a dictionary with a key "message" and value "Hello, PLP May 2024 Cohort"
    return json({"message": "Hello, PLP May 2024 Cohort"})

# This block ensures that the Sanic application runs only if this file is executed directly
# The application will run on host 0.0.0.0 (accessible on the local network) and port 8000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
