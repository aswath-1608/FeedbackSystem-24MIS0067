from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
feedback_list = []

@app.route("/")
def home():
    return render_template("index.html", feedback=feedback_list)

@app.route("/submit", methods=["POST"])
def submit():
    entry = {
        "name": request.form.get("name", "").strip(),
        "rating": request.form.get("rating", ""),
        "comments": request.form.get("comments", "").strip()
    }

    if entry["name"] and entry["rating"] and entry["comments"]:
        feedback_list.append(entry)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)