from flask import Flask, render_template, request

app = Flask(__name__, template_folder=".")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        message = f"You entered: {user_input}"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

