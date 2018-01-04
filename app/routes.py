from app import app

@app.route("/")
def index():
    return "Hello World"

@app.route("/login", methods=["GET", "POST"])
def login():
    return "Login successful"

@app.route("/scores/<int:level>", methods=["GET", "POST"])
def fetch_scores():
    return ""

@app.route("/user", methods=["PUT", 'DELETE'])
def update_user():
    return ""