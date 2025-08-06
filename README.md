<h1 align="center"> Search-And-Rescue-Dashboard </h1>
<p align="center"> Grazioso Salvare </p>

<p align="center">
<img alt="image" src="Grazioso Salvare Logo.png" />
</p>


## Table of Contents
- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
- [The Dashboard](#the-dashboard)
- [Filtering](#filtering)
- [Specific Filtering](#specific-filters)
- [Tools](#tools)
  * [Description of drivers](#description-of-drivers)
  * [Attributes](#attributes)


## About the project
Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. When trained, these dogs are able to find and help to rescue humans or other animals, often in life-threatening conditions.

## Getting Started
To get a local copy up and running, follow these simple example steps.

1. Clone the repository with the following command:
   - `https://github.com/FinnishArmy/Search-And-Rescue-Dashboard.git`

2. Within CRUD.py, edit the connection variables accordingly to access your own database and user.
   - `USER = 'aacuser'`
   - `PASS = 'SNHU1234'`
   - `HOST = 'nv-desktop-services.apporto.com'`
   - `PORT = 34419`
   - `DB   = 'AAC'`
   - `COL  = 'animals'`
  
3. To test the module, run `python crud_test_script.ipynb`.

4. Then run the `Valtonen-Ronny-ProjectTwoDashboard.ipynb`.
If ran correctly you should see the following message:
<img width="651" height="93" alt="image" src="https://github.com/user-attachments/assets/d88dc617-b520-4455-ab05-1cbd54860554" />

## The Dashboard
If everything works correctly, and the MongoDB database was imported properly, you should be able to navigate to `http://127.0.0.1:12043/` (or on the port you are on). You should see this after the website loads:
<img width="3698" height="1664" alt="image" src="https://github.com/user-attachments/assets/93bfe0f4-4a00-44f0-95b2-6f432e8d7c05" />


This is the initial screen. You will notice a table that displays every animal in the animals database. You can filter by each column as desired, or use the dropdown menu for a specific type of Search and Rescue dog; by default it will only display non-mix breeds unless the 'Include Mixes' is checked.

When you scroll down you will see two widgets:
<img width="3091" height="894" alt="image" src="https://github.com/user-attachments/assets/05767116-bc1b-437b-95b9-cbec85e3c8ea" />

The left sunburst widget will display the type of animal on the inner ring, then the breed of animal on the outer ring. The right will display a geo-location map of the selected animal from the table mentioned earlier.

## Filtering
If you want to filter by specific Search and Rescue dogs, you can use the drop down to select from:
  - Water Rescue
  - Mountain/Wilderness
  - Disaster Recovery
  - Scent Tracking
<img width="3617" height="1037" alt="image" src="https://github.com/user-attachments/assets/6055e70b-d0e3-4111-91f8-7b0a13c6a0d9" />

Once selected you will see the following will update:

1. Table will only show dog breeds that pertain to the specific Search & Rescue type
<img width="3620" height="787" alt="image" src="https://github.com/user-attachments/assets/f2565743-93cf-42a5-872b-9e76007d466b" />

2. Sunburst will only show dogs and the breeds for the selected Search & Rescue Type
<img width="3092" height="888" alt="image" src="https://github.com/user-attachments/assets/39a206a3-db2d-4135-994c-99eb94c0670a" />


If desired, you may also select 'Include Mixes' to include the specified breeds which are also mixed, the table and sunburst will update accordingly:
<img width="1017" height="780" alt="image" src="https://github.com/user-attachments/assets/1b2eef30-1982-48df-b9df-46c49404f1eb" />

<img width="1066" height="794" alt="image" src="https://github.com/user-attachments/assets/f1f80f31-e084-4fdb-982c-8352a3226ac9" />

## Specific Filters
If you want further refinement, you can type in the specific breed into the column directly on the table:

For example you can type "Adoption" into the 'outcome_type' column and you will only get these outcomes:
<img width="2456" height="644" alt="image" src="https://github.com/user-attachments/assets/0b962fb9-3bcd-42ce-9371-e0c7425fef0c" />

## Tools
### Description of drivers
* Python 3.7 or later
   + You must use this as the runtime for the CRUD module and test scripts.
* PyMongo
   + Python Driver for MongoDB to execute CRUD operations on the database.
* Git
   + To close the repo from Github.
* Jupyter Notebook
   + This is to run the test script(s). However you may use your own IDE.
 
### Attributes
In the CRUD.py python library, I have created the following functionality that aligns with the fundamental elements of "CRUD."

* C - Create: Making a new entry in the database.
* R - Read: Given a specific query, return the details in a list.
* U - Update: Given a specific query, update the details of that entry.
* D - Delete: Remove an entry.


