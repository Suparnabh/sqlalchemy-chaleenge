import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import json
from decimal import Decimal

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/chinook.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Create references to the invoices and invoice_items tables called Invoices and Items
Invoices = Base.classes.invoices
Items = Base.classes.invoice_items

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/countries<br/>"
        f"/api/v1.0/USA/invoice_totals<br/>"
        f"/api/v1.0/USA/invoice_items_totals<br/>"
    )


# add route decorator

@app.route("/api/v1.0/countries")
def countries():

    """Return a list of all billing countries"""
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all billing countries
    results = session.query(Invoices.BillingCountry).distinct().all()

   
    # close the active session
    session.close()

    # Convert list of tuples into normal list
    all_countries = list(np.ravel(results))

    
    # return jsonified list of countries
    return jsonify(all_countries)

# add route decorator

@app.route("/api/v1.0/<country>/invoice_totals")

def country_inv_total(country):

    """Return invoice totals for the country specified"""
    # Create our session (link) from Python to the DB
    session = Session(engine)


    # Query all invoice totals for specified country
    
    results = session.query(Invoices.Total).filter(Invoices.BillingCountry == country).all()
    
    totals = [str(row[0]) for row in results]
    

    # close the active session
    
    session.close()
    
    # Convert list of tuples into normal list
    all_totals = list(np.ravel(totals))
    # return jsonified result with country and list of invoice totals for the country
    return jsonify(all_totals)

# add route decorator
@app.route("/api/v1.0/<country>/item_totals")

def country_inv_items_total(country):

    for country in all_countries:

    """Return invoice items totals for the country specified"""
    # Create our session (link) from Python to the DB

    session = Session(engine)

    # Query 
    session.query()

    results = session.query(Invoices.BillingCountry,Items.UnitPrice,Items.Quantity).filter(Invoices.InvoiceId == Items.Invoice_Id).filter(Invoices.BillingCountry == country)).all()

    total = 0   
    for i,result in enumerate(results):        
        total = total + (result[i]*result[i+1])
        
    return jsonify(total)

    # close the active session
    

    # Convert list of tuples into normal list

    
    # return jsonified result with country and a list of dictionaries. 
    # each dictionary in the list represents an invoice and contains invoice id and total of all items in that invoice.


if __name__ == '__main__':
    app.run(debug=True)
