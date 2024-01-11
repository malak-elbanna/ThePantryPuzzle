import sqlite3

con = sqlite3.connect("instance/MainDB.db")
cursor = con.cursor()
drop = "drop table Dietry"


# Meat-Based Recipes
meat_queries = [
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Meat Stock', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Homemade Meat Broth', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Crab-Meat-Stuffed Sole', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Turkey Meat Loaf', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Meat Loaf With Bacon', 'Non-Vegetarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Meat Lovers'' Supreme Pizza recipes', 'Non-Vegetarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Meat Loaf', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Harlem Meat Loaf', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Souvlaki', 'Non-Vegetarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Savory Crepes with Meat Filling', 'Non-Vegetarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Favorite Meat Loaf', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Chicken Taco Meat Tacos', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Meat Lovers'' Supreme Pizza', 'Non-Vegetarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Willin Low’s Luncheon Meat Fries With Kaffir Mayo', 'Non-Vegetarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Curried Ground Meat or Keema Matar', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Chipotle Meat Loaf', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Chicken (or Any Other Meat) Stock', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Crab Meat Salad', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('The Best Meat Loaf', 'Omnivorous');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Orange-Ginger Turkey Meat Loaf', 'Omnivorous');"
]

# Fish-Based Recipes
fish_queries = [
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Deep Fried Fish Bones', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Burnt-Scallion Fish', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Curry-Crusted Fish', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Homemade fish fingers', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Gefilte Fish', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Breaded Sicilian Fish', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Fish Stock', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Fish Sticks', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Baked Fish from Iceland', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Fish Curry', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Fried Rock Fish', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Moroccan Fish', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Cod Fish Cakes', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Creamy Fish & Mussel Soup', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Seared and Steamed Fish', 'Pescatarian');",
    "INSERT INTO Dietary (Recipe_Name, preference) VALUES ('Fish Broth', 'Pescatarian');"
]

# Vegetarian
vegetarian_queries = [
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Glazed Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Baby Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Spring Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Steamed Meat Bao with Preserved Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Moo Shu Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Quick-Pickled Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Penne Pasta With Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Spinach Salad with Roasted Vegetables and Apricot recipes', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Mediterranean Marinated Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Warm Artichoke Dip with Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Giardiniera (Italian Pickled Vegetables)', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Oven Roasted Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Nutty Orzo and Vegetables', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Baby Vegetables with Tarragon Nage', 'Vegetarian');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Curried Root Vegetables', 'Vegetarian');"
]

# Vegan
vegan_queries = [
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Glazed Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Baby Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Spring Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Steamed Meat Bao with Preserved Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Moo Shu Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Quick-Pickled Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Penne Pasta With Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Spinach Salad with Roasted Vegetables and Apricot recipes', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Mediterranean Marinated Vegetables', 'Vegan');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Giardiniera (Italian Pickled Vegetables)', 'Vegan');"
]

# Gluten-free
gluten_free_queries = [
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Glazed Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Baby Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Spring Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Saucy Chicken & Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Steamed Meat Bao with Preserved Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Turkey Sandwich With Provolone And Pickled Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Low-key Iridofu Or Scrambled Tofu With Vegetables recipes', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Moo Shu Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Quick-Pickled Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Penne Pasta With Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Spinach Salad with Roasted Vegetables and Apricot recipes', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Mediterranean Marinated Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Warm Artichoke Dip with Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Giardiniera (Italian Pickled Vegetables)', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Oven Roasted Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Nutty Orzo and Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Baby Vegetables with Tarragon Nage', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Hearty Black Bean Stew With Winter Vegetables', 'Gluten-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Curried Root Vegetables', 'Gluten-free');"
]

# Lactose-free
lactose_free_queries = [
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Glazed Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Baby Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Spring Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Saucy Chicken & Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Steamed Meat Bao with Preserved Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Turkey Sandwich With Provolone And Pickled Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Low-key Iridofu Or Scrambled Tofu With Vegetables recipes', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Moo Shu Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Quick-Pickled Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Penne Pasta With Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Spinach Salad with Roasted Vegetables and Apricot recipes', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Mediterranean Marinated Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Warm Artichoke Dip with Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Giardiniera (Italian Pickled Vegetables)', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Oven Roasted Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Nutty Orzo and Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Baby Vegetables with Tarragon Nage', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Hearty Black Bean Stew With Winter Vegetables', 'Lactose-free');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Curried Root Vegetables', 'Lactose-free');"
]

# Keto
keto_queries = [
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Glazed Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Baby Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Spring Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Saucy Chicken & Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roasted Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Steamed Meat Bao with Preserved Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Turkey Sandwich With Provolone And Pickled Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Low-key Iridofu Or Scrambled Tofu With Vegetables recipes', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Quick-Pickled Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Spinach Salad with Roasted Vegetables and Apricot recipes', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Mediterranean Marinated Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Warm Artichoke Dip with Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Giardiniera (Italian Pickled Vegetables)', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Oven Roasted Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Nutty Orzo and Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Baby Vegetables with Tarragon Nage', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Hearty Black Bean Stew With Winter Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Curried Root Vegetables', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Vesuvio', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Paprikash', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Baked Chicken', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Catalan Chicken', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Stew', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Persian Chicken', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Kreplach (Chicken Dumplings)', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken cacciatore', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Roast Chicken', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Crêpes', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Smothered Chicken', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Hash', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Poofs', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Feet Stock', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Soup', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Pie', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Chicken Enchiladas', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Citrus Roasted Chicken', 'Keto');",
    "INSERT INTO Dietary (Recipe_name, preference) VALUES ('Margarita Chicken', 'Keto');"
]


con.commit()
con.close()
