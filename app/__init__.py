from flask import Flask, request, Response
import RecipePredictionController as rpcm

app = Flask(__name__)
rpc = rpcm.RecipePredictionController("logreg.joblib")

# This method will return the probability of a user liking a recipe
# /recipe_prob?rating=4.2&numIngUser=3&listIngRecipe=dried%20fruit&listIngRecipe=dill&listIngRecipe=dallas&listIngRecipe=curry
@app.route("/recipe_prob")
def calculate_recipe():
    return rpc.predict(request)

@app.route("/")
def welcome():
    return "Call /recipe_prob with params ?rating : The mean rate of a recipe, ?numIngUser : number of ingredients a user likes, ?listIngRecipe : for each ingredient a recipe has"


if __name__ == '__main__':
    app.run(debug=True)