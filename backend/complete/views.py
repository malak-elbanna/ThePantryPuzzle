from flask import Blueprint, render_template, request, url_for, redirect, flash, send_file, Flask
from logging import Formatter, FileHandler
from flask_login import login_required, current_user, logout_user
from backend.controllers.database import pantry_database, shopping_list_database, user_database, favorite_recipe, reviews_database, dietary_prefernces_database, chef_database
import base64
from models.validation import Reviews
from werkzeug.security import generate_password_hash, check_password_hash

views = Blueprint('views', __name__)

database_path = "ThePantryPuzzle/instance/MainDB.db"
user_profile = 'views.userprofile'
Page_Recipes = 'pages/Recipes.html'
home = 'views.home'


@views.route('/')
def home():
    return render_template('pages/HomePage.html',  user=current_user)

@views.route('/FAQs')
def faqs():
    return render_template('pages/FAQs.html',  user=current_user)

@views.route('/Recipes', methods=["POST", "GET"])
def about():
    databasemanager = pantry_database(database_path)
    if request.method == "GET":
        recipes= databasemanager.return_all_recipe_names()
        return render_template(Page_Recipes, recipelist=recipes)
    else:
        rname= request.form.get("recipename")
        #print(rname)
        recipesearch= databasemanager.get_similar_recipes(rname)
        return render_template(Page_Recipes, recipelist=recipesearch)

@views.route('/delete_account/<userid>', methods=["POST"])
def delete_account(userid):
    user_db = user_database(database_path)
    result = user_db.delete_user(userid)

    if result == "User deleted":
        # Log the user out and redirect to the home page
        logout_user()
        return redirect(url_for(home))
    else:
        flash("Error deleting account.")
        return redirect(url_for(user_profile, userid=userid))

@views.route('/change_name/<userid>', methods=["POST"])
def change_name(userid):
    user_db = user_database(database_path)

    if request.method == 'POST':
        new_firstname = request.form.get("new_firstname")
        new_lastname = request.form.get("new_lastname")

        if new_firstname and new_lastname:
            user_db.change_name(userid, new_firstname, new_lastname)
            flash("Name changed successfully.")
        else:
            flash("Both first and last names are required.")

    return redirect(url_for(user_profile, userid=userid))

@views.route('/change_password/<userid>', methods=["POST"])
def change_password(userid):
    user_db = user_database(database_path)

    if request.method == 'POST':
        new_password = request.form.get("new_password")
        password=generate_password_hash(new_password, method='pbkdf2:sha256')

        if new_password:
            user_db.change_password(userid, password)
            flash("Password changed successfully.")
        else:
            flash("New password cannot be empty.")

    return redirect(url_for(user_profile, userid=userid))


@views.route('/add_favorite/<rname>', methods=["GET", "POST"])
def add_favorite(rname):
    user = current_user 
    if request.method == 'POST':
        databasemanager_favorite = favorite_recipe(database_path)
        databasemanager_favorite.add_favorite_recipe(rname, user.id)
        return redirect(url_for(user_profile, userid=user.id))
    else:
        pantry_databasemanager = pantry_database(database_path)
        image_data = pantry_databasemanager.get_recipe_image(rname)
        if image_data:
            image = image_data[0]
            image_data_base64 = base64.b64encode(image).decode('utf-8')
            return render_template(Page_Recipes, image_data_base64=image_data_base64)

@views.route('/remove_favorite/<recipe_name>', methods=["POST"])
def remove_favorite(recipe_name):
    user = current_user
    if request.method == 'POST':
        databasemanager_favorite = favorite_recipe(database_path)
        databasemanager_favorite.remove_favorite_recipe(user.id, recipe_name)

    return redirect(url_for(user_profile, userid=user.id))

@views.route('/get_recipe_image/<rname>', methods=["GET", "POST"])
def get_recipe_image(rname):
    pantry_databasemanager = pantry_database(database_path)
    image_data = pantry_databasemanager.get_recipe_image(rname)

    if image_data:
        image = image_data[0]
        image_data_base64 = base64.b64encode(image).decode('utf-8')
        return render_template(Page_Recipes, image_data_base64=image_data_base64)
    else:
        return 'Image not found', 404
        
@views.route('/RecipeInfo/<rname>/<userid>', methods=["POST", "GET"])
def recipeinfo(rname, userid):
    form = Reviews()
    reviews_db = reviews_database(database_path)
    if form.validate_on_submit():
        review_text = form.review.data
        reviews_db.add_review(userid, review_text, rname)
        return redirect(url_for('views.recipeinfo', rname=rname, userid=userid))

    database_manager = pantry_database(database_path)
    ingredients = database_manager.get_recipe_info(rname)
    image_data = database_manager.get_recipe_image(rname)
    database_manager_chef = chef_database(database_path)
    review_list = reviews_db.display_review(rname)
    image = image_data[0]
    image_data_base64 = base64.b64encode(image).decode('utf-8')

    if database_manager_chef.get_chef_id(rname):
        chef_id = database_manager_chef.get_chef_id(rname)
    else:
        chef_id = None
    return render_template('pages/RecipeInfo.html', ingredientlist=ingredients, Recipe=rname,
                           image_data_base64=image_data_base64, form=form, review_list=review_list, chef_id=chef_id)

@views.route('/chef_profile/<chef_id>/<rating>/<rname>', methods=["GET", "POST"])
def rate_recipe(chef_id, rating, rname):
    form = Reviews()
    reviews_db = reviews_database(database_path)
    chef_db = chef_database(database_path)
    chef_db.add_Rating(chef_id,int(rating))
    database_manager = pantry_database(database_path)
    ingredients = database_manager.get_recipe_info(rname)
    image_data = database_manager.get_recipe_image(rname)
    database_manager_chef = chef_database(database_path)
    review_list = reviews_db.display_review(rname)
    image = image_data[0]
    image_data_base64 = base64.b64encode(image).decode('utf-8')
    if database_manager_chef.get_chef_id(rname):
        chef_id = database_manager_chef.get_chef_id(rname)
    else:
        chef_id = None
    return render_template('pages/RecipeInfo.html', ingredientlist=ingredients, Recipe=rname,
                           image_data_base64=image_data_base64, form=form, review_list=review_list, chef_id=chef_id)

@views.route('/chef_profile/<chef_id>', methods=["GET"])
def chef_profile(chef_id):
    user_db = user_database(database_path)
    chef_db = chef_database(database_path)
    list_recipes = chef_db.get_recipes(chef_id)
    chef_info = user_db.get_user(chef_id)
    if chef_info:
        return render_template('pages/chef_profile.html', chef_info=chef_info, list_recipes=list_recipes)
    else:
        flash("Chef not found", "error")

@views.route('/recipedirections/<rname>', methods=["POST", "GET"])
def recipe_directions(rname):
    recipename = rname
    databasemanager = pantry_database(database_path)
    ingredients=databasemanager.get_recipe_directions(recipename)
    return render_template('pages/recipedirections.html', ingredientlist=ingredients, Recipe=recipename)

@views.route('/userprofile/<userid>')
@login_required
def userprofile(userid):
    databasemanager = user_database(database_path)
    favorite_recipe_instance = favorite_recipe(database_path)
    userinfo= databasemanager.get_user(userid)
    favorite_recipes = favorite_recipe_instance.display_favorite_recipe(userid)
    return render_template('pages/userprofile.html', item=userinfo, favorite_recipes=favorite_recipes)

@views.route('/useredit/<userid>')
@login_required
def useredit(userid):
    databasemanager = user_database(database_path)
    userinfo= databasemanager.get_user(userid)
    return render_template('pages/useredit.html',item=userinfo)

@views.route('/shoplist/<userid>')
@login_required
def shoppinglist(userid):
    databasemanager=shopping_list_database(database_path)
    listofingrients=databasemanager.display_shopping_list(userid)
    databasemanager = user_database(database_path)
    userinfo= databasemanager.get_user(userid)
    return render_template('pages/usershoppinglist.html',item=userinfo, shoplist=listofingrients)

@views.route('/newshoplist/<userid>/<rname>')
@login_required
def generateshoplist(userid, rname):
    databasemanager=pantry_database(database_path)
    ingredientslist=databasemanager.get_recipe_ingredients(rname)
    databasemanager_shop=shopping_list_database(database_path)
    for item in ingredientslist:
        databasemanager_shop.add_item(userid, item)
    return shoppinglist(userid)

@views.route('/removeshoplist/<userid>/<removeingredient>', methods=["POST"])
@login_required
def removeshoplistitem(userid, removeingredient):
    databasemanager=shopping_list_database(database_path)
    databasemanager.remove_item(userid,removeingredient)
    return shoppinglist(userid)

@views.route('/pantry/<userid>', methods=["POST", "GET"])
@login_required
def viewpantry(userid):
    databasemanager = user_database(database_path)
    userinfo= databasemanager.get_user(userid)
    databasemanager = pantry_database(database_path)
    ingredients= databasemanager.display_pantry(userid)
    autofill = databasemanager.ingredient_list()
    return render_template('pages/pantryprofile.html', item= userinfo, pantrylist=ingredients, ingr=autofill)

@views.route('/pantryadd/<userid>/', methods=["POST", "GET"])
@login_required
def addtopantry(userid):
    databasemanager = pantry_database(database_path)
    ingredientt= request.form.get("ing")
    ingredientsinput = ingredientt.split()
    for item in ingredientsinput:
        databasemanager.insert_into_pantry(userid, item)
    return viewpantry(userid)
    
@views.route('/pantrydelete/<userid>/<ingredients>', methods=["POST", "GET"])
@login_required
def remove_from_pantry(userid, ingredients):
        databasemanager= pantry_database(database_path)
        databasemanager.remove_from_pantry(userid,ingredients)
        return viewpantry(userid)

@views.route('/pantrysearch/<useridd>', methods=["POST", "GET"])
@login_required
def pantrysearch(useridd):
        databasemanager= pantry_database(database_path)
        recipes_from_pantry= databasemanager.recommend_recipes(useridd)
        return render_template('pages/pantryRecipes.html',recipelist=recipes_from_pantry, userid = useridd)

@views.route('/keto', methods=['POST', 'GET'])
@login_required
def keto():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Keto")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/lactose_free', methods=['POST', 'GET'])
@login_required
def lactose_free():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Lactose-free")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/omnivorous', methods=['POST', 'GET'])
@login_required
def omnivorous():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Omnivorous")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/pescatarian', methods=['POST', 'GET'])
@login_required
def pescatarian():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Pescatarian")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/non_vegetarian', methods=['POST', 'GET'])
@login_required
def non_vegetarian():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Non-Vegetarian")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/vegetarian', methods=['POST', 'GET'])
@login_required
def vegetarian():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Vegetarian")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/vegan', methods=['POST', 'GET'])
@login_required
def vegan():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Vegan")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/gluten_free', methods=['POST', 'GET'])
@login_required
def gluten_free():
    databasemanager= dietary_prefernces_database(database_path)
    recipes = databasemanager.get_recipes_dietary("Gluten-free")
    return render_template(Page_Recipes, recipelist=recipes)


@views.route('/addrecipe/<userid>', methods=["POST", "GET"])
@login_required
def viewaddrecipe(userid):
    databasemanager = user_database(database_path)
    userinfo= databasemanager.get_user(userid)
    return render_template('pages/addrecipe.html', item=userinfo)

@views.route('/addedrecipe/<userid>', methods=["POST", "GET"])
@login_required
def add_recipe(userid):
    databasemanager = user_database(database_path)
    userinfo= databasemanager.get_user(userid)
    if request.method == 'POST':
        recipe_name = request.form.get("recipe_name")
        databasemanager2=chef_database(database_path)
        databasemanager2.add_recipe_name(userid,recipe_name)
        quantities = request.form.get("quantities")
        instructions = request.form.get("instructions")
        recipeimage = request.files['recipe_image']
        recipeimag2=recipeimage.read()
        recipeimagebase64=base64.b64encode(recipeimag2)
        recipeimagebinary=base64.b64decode(recipeimagebase64)
        databasemanager2.add_recipe_quantites(recipe_name,quantities)
        databasemanager2.add_recipe_instructions(recipe_name,instructions)
        databasemanager2.add_picture(recipe_name,recipeimagebinary)
    return render_template('pages/addrecipe.html', item=userinfo)

if __name__ == '__main__':
    views.run()

