 
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Simple Flask App</title>
<h2>Simple Flask Input App</h2>
<form method="post">
  <input type="text" name="message" placeholder="Type something" required>
  <button type="submit">Submit</button>
</form>

{% if msg %}
  <p><b>You entered:</b> {{ msg }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    msg = None
    if request.method == "POST":
        msg = request.form.get("message")
    return render_template_string(HTML, msg=msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
