
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

feedback_list = []


@app.route("/")
def home():
    search_name = request.args.get("name", "").strip().lower()
    rating_filter = request.args.get("rating", "")
    sort_order = request.args.get("sort", "newest")

    filtered_feedback = []

    for index, item in enumerate(feedback_list):
        if search_name and search_name not in item["name"].lower():
            continue

        if rating_filter and item["rating"] != rating_filter:
            continue

        filtered_feedback.append({
            **item,
            "id": index + 1,
            "position": index
        })

    if sort_order == "rating_high":
        filtered_feedback.sort(
            key=lambda item: int(item["rating"]), reverse=True
        )
    elif sort_order == "rating_low":
        filtered_feedback.sort(
            key=lambda item: int(item["rating"])
        )
    else:
        filtered_feedback.sort(
            key=lambda item: item["position"], reverse=True
        )

    return render_template(
        "index.html",
        feedback=filtered_feedback,
        search_name=search_name,
        rating_filter=rating_filter,
        sort_order=sort_order
    )


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name", "").strip()
    rating = request.form.get("rating", "")
    comments = request.form.get("comments", "").strip()

    if name and rating in {"1", "2", "3", "4", "5"} and comments:
        feedback_list.append({
            "name": name,
            "rating": rating,
            "comments": comments
        })

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
