from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from grocery_app.models import GroceryStore, GroceryItem

# Import app and db from events_app package so that we can run app
from grocery_app import app, db
from grocery_app.models import GroceryStore, GroceryItem
from grocery_app.forms import GroceryItemForm, GroceryStoreForm

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    all_stores = GroceryStore.query.all()
    print(all_stores)
    return render_template('home.html', all_stores=all_stores)

@main.route('/new_store', methods=['GET', 'POST'])
def new_store():
    """Create new grocery store"""
    form = GroceryStoreForm()
    if form.validate_on_submit():
        new_store = GroceryStore(
            title = form.title.data, 
            address=form.address.data
        )
        db.session.add(new_store)
        db.session.commit()
        flash("New store added successfully.")
        return redirect(url_for("main.store_detail", store_id = new_store.id))
    return render_template("new_store.html", form = form)

@main.route('/new_item', methods=['GET', 'POST'])
def new_item():
    """Create new grocery item"""
    form = GroceryItemForm()
    if form.validate_on_submit():
        new_item = GroceryItem(
            name = form.name.data,
            price = form.price.data,
            category = form.category.data,
            photo_url = form.photo_url.data,
            store_id = form.store.data.id
        )
        db.session.add(new_item)
        db.session.commit()
        flash("New item added successfully.")
        return redirect(url_for("main.item_detail", item_id = new_item.id))
    return render_template("new_item.html", form = form)

@main.route('/store/<store_id>', methods=['GET', 'POST'])
def store_detail(store_id):
    """Display store details and edit form"""
    store = GroceryStore.query.get(store_id)
    form = GroceryStoreForm(obj=store)
    if form.validate_on_submit():
        store.title = form.title.data
        store.address = form.address.data
        db.session.commit()
        flash("Store edited successfully.")
        return redirect(url_for("main.store_detail", store_id = store.id))
    store = GroceryStore.query.get(store_id)
    return render_template("store_detail.html", store = store, form = form)

@main.route('/item/<item_id>', methods=['GET', 'POST'])
def item_detail(item_id):
    item = GroceryItem.query.get(item_id)
    # TODO: Create a GroceryItemForm and pass in `obj=item`

    # TODO: If form was submitted and was valid:
    # - update the GroceryItem object and save it to the database,
    # - flash a success message, and
    # - redirect the user to the item detail page.

    # TODO: Send the form to the template and use it to render the form fields
    item = GroceryItem.query.get(item_id)
    return render_template('item_detail.html', item=item)

