# Chinook Database Analysis

* In this activity, you will complete some exploratory analysis of the [chinook](https://chinookdatabase.codeplex.com/wikipage?title=Chinook_Schema&referringTitle=Home) database.

## Instructions

* Create a SQLAlchemy engine to the database `chinook.sqlite`.

* Use `automap_base` to reflect the database tables.

* Create references to the `invoices` and `invoice_items` tables called `Invoices` and `Items`.

* Create a SQLALchemy ORM session object.

* Create routes and functions for each of the following (your API must return results in JSON format. There is already a home/index page route and function added to the starter file app.py which lists all the possible routes):

    1. All of the billing countries found in the invoices table. (The relevant column in `invoices` table is `BillingCountry`)

    2. The invoices totals for a specific billing country with the totals sorted in descending order. The result should be jsonified and contain the country name and a list of invoice totals for that country. (The relevant columns in `invoices` table are `BillingCountry` and `Total`)

## Hint

* For question 2. above you will run into an error while converting the totals into JSON (as they are returned by SQLAlchemy in Decimal format which is not serializable). Convert the invoice totals returned from the database into string values like below before converting to json,

    `totals =  [str(row[0]) for row in results]`

## Bonus - 

* Add a function and route for the following (in JSON format):

    3. The Item Totals **sum(UnitPrice \* Quantity)** for a specific billing country.The results should be jsonified and contain the country and a list of dictionaries. Each dictionary in the list represents an invoice and contains the invoice id and total of all items in that invoice. (The relevant columns in `invoices` table are `InvoiceId` and `BillingCountry` and those in `invoice_items` table are `InvoiceId`, `UnitPrice` and `Quantity`)
