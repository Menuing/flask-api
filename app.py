from flask import Flask

app = Flask(__name__)

# This method will return the probability of a user liking a recipe
@app.route("/recipe_prob")
def calculate_recipe():
    # request.args.get('rating')
    # request.args.get('list')
    return "YEAH!"


if __name__ == '__main__':
    app.run(debug=True)