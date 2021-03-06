from flask import Flask, render_template, request, session
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy
import os





app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'
#will change because its locally hosted :o
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Rhonda:'+'@localhost:5000/B501596j'
db = SQLAlchemy(app)

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Meats(db.Model):
    __tablename__ = 'Meats'
    upc = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

class Fruits(db.Model):
    __tablename__ = 'Fruits'
    upc = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Vegetables(db.Model):
    __tablename__ = 'Vegetables'
    upc = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Store(db.Model):
    __tablename__ = 'Store'
    storeId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    number = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)


class FruitHolder(db.Model):
    __tablename__ = 'fruitholder'
    id = db.Column(db.Integer, primary_key=True)
    storeId = db.Column(db.Integer, db.ForeignKey('Store.storeId'))
    upc = db.Column(db.Integer, db.ForeignKey('Fruit.upc'))
    price = db.Column(db.Integer, nullable=False)


class MeatHolder(db.Model):
    __tablename__ = 'meattholder'
    id = db.Column(db.Integer, primary_key=True)
    storeId = db.Column(db.Integer, db.ForeignKey('Store.storeId'))
    upc = db.Column(db.Integer, db.ForeignKey('Meat.upc'))
    price = db.Column(db.Integer, nullable=False)

class VegetablHolder(db.Model):
    __tablename__ = 'vegetableholder'
    id = db.Column(db.Integer, primary_key=True)
    storeId = db.Column(db.Integer, db.ForeignKey('Store.storeId'))
    upc = db.Column(db.Integer, db.ForeignKey('Vegetable.upc'))
    price = db.Column(db.Integer, nullable=False)


@app.route('/dbhome/', methods=['POST'])



@app.route('/dbhome/meats/')
def meats():
    data= Meats.query.with_entities(Meats.name, Meats.upc).all()
    return render_template('pages/meats.html', meats=data)



@app.route('/dbhome/meats/search', methods=['POST'])
def search_meats():
    results = Meats.query.filter(Meats.name('%{}%'.format(request.form['search_term']))).all()

    response={
  	    "count": len(results),
        "data": []
    }
    for meats in results:
        response['data'].append({
        "upc": meats.upc,
        "name": meats.name,
    })
    return render_template('pages/search_fruits.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/dbhome/meats/create', methods=['GET'])
def create_meats_form():
  form = MeatsForm()
  return render_template('forms/new_meat.html', form=form)


@app.route('/dbhome/meats/delete', methods=['POST'])
def delete_meats():
    meats_upc = request.form.get('meats_upc')
    deleted_meats = Meats.query.get(meats_upc)
    meatsName = deleted_meats.name
    try:
        db.session.delete(deleted_meats)
        db.session.commit()
        flash('Meats ' + meatsName + ' was successfully deleted!')
    except:
        db.session.rollback()
        flash('please try again. ' + meatsName + ' could not be deleted.')
    finally:
        db.session.close()


@app.route('/dbhome/meats/edit', methods=['GET'])
def edit_meats():
    form = MeatsForm()
    meats_upc = request.args.get('meats_upc')
    meats = Meats.query.get(meats_upc)
    meats_info={
        "upc": meats.upc,
        "name": meats.name,
    }
    return render_template('forms/edit_meats.html', form=form, meats=meats_info)
    # TODO: populate form with fields from artist with ID <artist_id>







@app.route('/dbhome/fruits/')
def fruits():
    data= Fruits.query.with_entities(Fruits.name, Fruits.upc).all()
    return render_template('pages/fruits.html', fruits=data)



@app.route('/dbhome/fruits/search', methods=['POST'])
def search_fruits():
    results = Fruits.query.filter(Fruits.name('%{}%'.format(request.form['search_term']))).all()

    response={
  	    "count": len(results),
        "data": []
    }
    for fruits in results:
        response['data'].append({
        "upc": fruits.upc,
        "name": fruits.name,
    })
    return render_template('pages/search_fruits.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/dbhome/fruits/create', methods=['GET'])
def create_fruits_form():
  form = FruitsForm()
  return render_template('forms/new_fruit.html', form=form)



@app.route('/dbhome/fruits/delete', methods=['POST'])
def delete_fruits():
    fruits_upc = request.form.get('fruits_upc')
    deleted_fruits = Fruits.query.get(fruits_upc)
    fruitsName = deleted_fruits.name
    try:
        db.session.delete(deleted_fruits)
        db.session.commit()
        flash('Fruits ' + fruitsName + ' was successfully deleted!')
    except:
        db.session.rollback()
        flash('please try again. ' + fruitsName + ' could not be deleted.')
    finally:
        db.session.close()


@app.route('/dbhome/fruits/edit', methods=['GET'])
def edit_fruits():
    form = FruitsForm()
    fruits_upc = request.args.get('fruits_upc')
    fruits = Fruits.query.get(fruits_upc)
    fruits_info={
        "upc": fruits.upc,
        "name": fruits.name,
    }
    return render_template('forms/edit_fruits.html', form=form, fruits=fruits_info)
    # TODO: populate form with fields from artist with ID <artist_id>









@app.route('/dbhome/vegetables/')
def vegetables():
    data= Vegetables.query.with_entities(Vegetables.name, Vegetables.upc).all()
    return render_template('pages/vegetables.html', vegetables=data)



@app.route('/dbhome/vegetables/search', methods=['POST'])
def search_vegetables():
    results = Vegetables.query.filter(Vegetables.name('%{}%'.format(request.form['search_term']))).all()

    response={
  	    "count": len(results),
        "data": []
    }
    for vegetables in results:
        response['data'].append({
        "upc": vegetables.upc,
        "name": vegetables.name,
    })
    return render_template('pages/search_vegetables.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/dbhome/vegetable/create', methods=['GET'])
def create_vegetables_form():
  form = VegetablesForm()
  return render_template('forms/new_vegetable.html', form=form)



@app.route('/dbhome/vegetables/delete', methods=['POST'])
def delete_vegetables():
    vegetables_upc = request.form.get('vegetables_upc')
    deleted_vegetables = Vegetables.query.get(vegetables_upc)
    vegetablesName = deleted_vegetables.name
    try:
        db.session.delete(deleted_vegetables)
        db.session.commit()
        flash('Vegetables ' + vegetablesName + ' was successfully deleted!')
    except:
        db.session.rollback()
        flash('please try again. ' + vegetablesName + ' could not be deleted.')
    finally:
        db.session.close()


@app.route('/dbhome/vegetables/edit', methods=['GET'])
def edit_vegetables():
    form = FruitsForm()
    vegetables_upc = request.args.get('vegetables_upc')
    vegetables = Vegetables.query.get(vegetables_upc)
    vegetables_info={
        "upc": vegetables.upc,
        "name": vegetables.name,
    }
    return render_template('forms/edit_vegetables.html', form=form, vegetables=vegetables_info)
    # TODO: populate form with fields from artist with ID <artist_id>







@app.route('/dbhome/fruitholder/')
def fruitholder():
    data= FruitHolder.query.with_entities(FruitHolder.storeId, FruitHolder.upc).all()
    return render_template('pages/fruitholder.html', fruitholder=data)



@app.route('/dbhome/fruitholder/search', methods=['POST'])
def search_fruitholder():
    results = FruitHolder.query.filter(FruitHolder.id('%{}%'.format(request.form['search_term']))).all()

    response={
  	    "count": len(results),
        "data": []
    }
    for fruitholder in results:
        response['data'].append({
        "upc": fruitholder.upc,
        "name": fruitholder.name,
    })
    return render_template('pages/search_fruitholder.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/dbhome/fruitholder/create', methods=['GET'])
def create_fruitholder_form():
  form = FruitholderForm()
  return render_template('forms/new_fruitholder.html', form=form)



@app.route('/dbhome/fruitholder/delete', methods=['POST'])
def delete_fruitholder():
    fruitholder_upc = request.form.get('fruitholder_upc')
    deleted_fruitholder = FruitHolder.query.get(fruitholder_upc)
    fruitholderName = deleted_fruitholder.id
    try:
        db.session.delete(deleted_vegetableholder)
        db.session.commit()
        flash('Holder ' + fruitholderName + ' was successfully deleted!')
    except:
        db.session.rollback()
        flash('please try again. ' + fruitholderName + ' could not be deleted.')
    finally:
        db.session.close()


@app.route('/dbhome/fruitholder/edit', methods=['GET'])
def edit_fruitholder():
    form = FruitHolderForm()
    fruitholder_upc = request.args.get('fruitholder_upc')
    fruitholder = FruitHolder.query.get(fruitholder_upc)
    fruitholder_info={
        "upc": fruitholder.upc,
        "storeId": fruitholder.storeId,
        "price": fruitholder.price
    }
    return render_template('forms/edit_fruitholder.html', form=form, fruitholder=fruitholder_info)
    # TODO: populate form with fields from artist with ID <artist_id>








@app.route('/dbhome/vegetableholder/')
def vegetableholder():
    data= VegetableHolder.query.with_entities(VegetableHolder.storeId, VegetableHolder.upc).all()
    return render_template('dbhome/vegetableholder.html', vegetableholder=data)



@app.route('/dbhome/vegetableholder/search', methods=['POST'])
def search_vegetableholder():
    results = VegetableHolder.query.filter(VegetableHolder.id('%{}%'.format(request.form['search_term']))).all()

    response={
  	    "count": len(results),
        "data": []
    }
    for vegetableholder in results:
        response['data'].append({
        "upc": vegetableholder.upc,
        "name": vegetableholder.name,
    })
    return render_template('dbhome/search_vegetableholder.html', results=response, search_term=request.form.get('search_term', ''))

@app.route('/dbhome/vegetableholder/create', methods=['GET'])
def create_vegetableholder_form():
  form = VegetableholderForm()
  return render_template('forms/new_vegetableholder.html', form=form)

@app.route('/dbhome/vegetableholder/delete', methods=['POST'])
def delete_vegetableholder():
    vegetableholder_upc = request.form.get('vegetableholder_upc')
    deleted_vegetableholder = VegetableHolder.query.get(vegetableholder_upc)
    vegetableholderName = deleted_vegetableholder.id
    try:
        db.session.delete(deleted_vegetableholder)
        db.session.commit()
        flash('Holder ' + vegetableholderName + ' was successfully deleted!')
    except:
        db.session.rollback()
        flash('please try again. ' + vegetableholderName + ' could not be deleted.')
    finally:
        db.session.close()


@app.route('/dbhome/vegetableholder/edit', methods=['GET'])
def edit_vegetableholder():
    form = VegetableHolderForm()
    vegetableholder_upc = request.args.get('Vegetableholder_upc')
    vegetableholder = VegetableHolder.query.get(vegetableholder_upc)
    vegetableholder_info={
        "upc": vegetableholder.upc,
        "storeId": vegetableholder.storeId,
        "price": vegetableholder.price
    }
    return render_template('dbhome/forms/edit_vegetableholder.html', form=form, vegetableholder=vegetableholder_info)
    # TODO: populate form with fields from artist with ID <artist_id>












@app.route('/dbhome/meatholder/')
def meatholder():
    data= MeatHolder.query.with_entities(MeatHolder.storeId, MeatHolder.upc).all()
    return render_template('pages/meatholder.html', meatholder=data)



@app.route('/dbhome/meatholder/search', methods=['POST'])
def search_meatholder():
    results = MeatHolder.query.filter(MeatHolder.id('%{}%'.format(request.form['search_term']))).all()

    response={
  	    "count": len(results),
        "data": []
    }
    for meatholder in results:
        response['data'].append({
        "upc": meatholder.upc,
        "name": meatholder.name,
    })
    return render_template('dbhome/search_meatholder.html', results=response, search_term=request.form.get('search_term', ''))



@app.route('/dbhome/meatholder/create', methods=['GET'])
def create_meatholder_form():
  form = MeatholderForm()
  return render_template('forms/new_meatholder.html', form=form)


@app.route('/dbhome/meatholder/delete', methods=['POST'])
def delete_meatholder():
    meatholder_upc = request.form.get('meatholder_upc')
    deleted_meatholder = MeatHolder.query.get(meatholder_upc)
    meatholderName = deleted_meatholder.id
    try:
        db.session.delete(deleted_meatholder)
        db.session.commit()
        flash('Holder ' + meatholderName + ' was successfully deleted!')
    except:
        db.session.rollback()
        flash('please try again. ' + meatholderName + ' could not be deleted.')
    finally:
        db.session.close()


@app.route('/dbhome/meatholder/edit', methods=['GET'])
def edit_meatholder():
    form = MeatHolderForm()
    meatholder_upc = request.args.get('meatholder_upc')
    meatholder = MeatHolder.query.get(meatholder_upc)
    meatholder_info={
        "upc": meatholder.upc,
        "storeId": meatholder.storeId,
        "price": meatholder.price
    }
    return render_template('dbhome/edit_meatholder.html', form=form, meatholder=meatholder_info)
    # TODO: populate form with fields from artist with ID <artist_id>








@app.route('/dbhome/store/')
def store():
    data= Store.query.with_entities(Store.storeId).all()
    return render_template('dbhome/holder.html', store=data)



@app.route('/dbhome/store/search', methods=['POST'])
def search_store():
    results = Store.query.filter(Store.storeId('%{}%'.format(request.form['search_term']))).all()

    response={
  	    "count": len(results),
        "data": []
    }
    for store in results:
        response['data'].append({
        "storeId": store.storeId,
        "name": store.name,
        "number": store.number,
        "address": store.address
    })
    return render_template('dbhome/search_store.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/dbhome/store/create', methods=['GET'])
def create_store_form():
  form = storeForm()
  return render_template('forms/new_store.html', form=form)



@app.route('/dbhome/store/delete', methods=['POST'])
def delete_store():
    store_storeId = request.form.get('store_storeId')
    deleted_store = Store.query.get(store_storeId)
    StoreName = deleted_store.storeId
    try:
        db.session.delete(deleted_store)
        db.session.commit()
        flash('Store ' + storeName + ' was successfully deleted!')
    except:
        db.session.rollback()
        flash('please try again. ' + storeName + ' could not be deleted.')
    finally:
        db.session.close()


@app.route('/dbhome/store/edit', methods=['GET'])
def edit_store():
    form = StoreForm()
    Store_storeId = request.args.get('store_storeId')
    store = Store.query.get(store_storeId)
    store_info={
        "storeId": store.storeId,
        "name": store.name,
        "number": store.number,
        "address": store.address
    }
    return render_template('dbhome/edit_store.html', form=form, store=store_info)
    # TODO: populate form with fields from artist with ID <artist_id>




if __name__ == '__main__':
    app.run()