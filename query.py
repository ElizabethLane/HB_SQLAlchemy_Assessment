"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *
from collections import defaultdict
#Imported defaultdict for Part 2 (sub-section Part 2, number 2).  Henry
#explained this in dig deeper and it proved to be useful!

init_app()
#Hey Katie - what does init_app() do?

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

# Brand.query.get(8)

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.

# Model.query.filter(Model.brand_name == 'Chevrolet', 
#     Model.name == 'Corvette').all()

# # Get all models that are older than 1960.

# Model.query.filter(Model.year < 1960).all()

# # Get all brands that were founded after 1920.

# Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor".
# Model.query.filter(Model.name.like('Cor%')).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
# Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded 
# # before 1950.
# Brand.query.filter( (Brand.founded < 1950) | (Brand.discontinued != None)).all()

# # Get any model whose brand_name is not Chevrolet.

# Model.query.filter(Model.brand_name == 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''


    model = Model.query.options(db.joinedload('brands')).filter(Model.year == 
            year).all()

    for m in model:
        for brands in m.brands:
            print m.name, m.brand_name, brands.headquarters

    #Hey Katie, quick question.  So I tried, at first, simply to do
    #one for loop, then write, "m.brands.headquarters".  I would see this:
    # error: >>> m.brands.headquarters
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # AttributeError: 'list' object has no attribute 'brands'
    #I understand the error, but is there a quicker way to access
    #the attribute without the extra for loop?
    #Thank you!

    

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models = Model.query.all()
    d = defaultdict(set)
    for model in models:
        key = model.brand_name
        d[key].add(model.name)


    cars = d.items()

    for car in cars:
        print car[0] + ":"
        for brand_name in car[1]:
            print "\t" + brand_name


    #Defaultdic made this one much quicker to hash out!


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#The returned value is an ORM-level SQL construction object.
#What that means is a query object generated from SQL syntax.


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
#An association table is a table has no meaningful data besides
#the data which correlates two tables. This is a many to many type of
#relationship.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()
    return brands
    
def get_models_between(start_year, end_year):

    models = Model.query.filter(Brand.founded >= start_year, Brand.
        discontinued < end_year).all()
    return models
