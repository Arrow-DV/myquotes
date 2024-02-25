# Made By Arrow-Dev | Ali Hany
# visit us https://arrowdev.pythonanywhere.com | https://arrow-dev.rf.gd

# Import Needed Libraries
from flask import Flask, redirect, request, render_template
import datetime
import json

app = Flask(__name__)
quotes = {}

# Load existing data from data.json
with open('data.json', 'r') as file:
    try:
        quotes = json.load(file)
    except:
        pass
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        author = request.form["author"].title()
        quote = request.form["quote"].title()

        # Check if author and quote are valid
        if not (author.isalpha() and quote.replace(" ", "").isalpha()):
            return render_template("error.html")

        # Add new quote to the quotes dictionary
        quotes[author] = {
            "quote": quote,
            "date": datetime.datetime.now().strftime("%m-%d-%Y")
        }

        # Save the updated quotes dictionary to data.json
        with open('data.json', 'w') as file:
            json.dump(quotes, file, indent=2)

        return redirect("/")
    else:
        return render_template("index.html", quotes=quotes.items())


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
