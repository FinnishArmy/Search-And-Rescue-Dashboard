<h1 align="center"> Search-And-Rescue-Dashboard </h1>
<p align="center"> Grazioso Salvare </p>

<p align="center">
<img alt="image" src="Grazioso Salvare Logo.png" />
</p>


## Table of Contents
- [About the Project](#about-the-project)
- [Why MongoDB?](#why-mongodb)
- [Getting Started](#getting-started)
- [Import The Database](#import-database)
   * [Import](#import-the-database)
   * [Login](#set-login-details)
   * [MongoDB](#setup-mongodb-interface)
   * [User ACC](#create-a-new-user-account)
- [Tests](#tests)
- [The Dashboard](#the-dashboard)
- [Filtering](#filtering)
- [Specific Filtering](#specific-filters)
- [Tools](#tools)
  * [Description of drivers](#description-of-drivers)
  * [Attributes](#attributes)
- [Challenges](#challenges)
  * [Sunburst](#sunburst)
  * [Styling](#styling)
  * [Logo](#logo)
- [Q&A](#q--a)

## About the project
Grazioso Salvare identifies dogs that are good candidates for search-and-rescue training. When trained, these dogs are able to find and help to rescue humans or other animals, often in life-threatening conditions.

## Why MongoDB?
MongoDB provides great flexibility and scalability of JSON data formats. On top of this it makes it easy to implement Python functionality directly.

## Getting Started
To get a local copy up and running, follow these simple example steps.

1. Clone the repository with the following command:
   - `git clone https://github.com/FinnishArmy/Search-And-Rescue-Dashboard.git`

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
<p align="center">
<img width="651" height="93" alt="image" src="https://github.com/user-attachments/assets/d88dc617-b520-4455-ab05-1cbd54860554" />
</p>

## The Dashboard
If everything works correctly, and the MongoDB database was imported properly, you should be able to navigate to `http://127.0.0.1:12043/` (or on the port you are on). You should see this after the website loads:
<p align="center">
<img width="3698" height="1664" alt="image" src="https://github.com/user-attachments/assets/93bfe0f4-4a00-44f0-95b2-6f432e8d7c05" />
</p>


This is the initial screen. You will notice a table that displays every animal in the animals database. You can filter by each column as desired, or use the dropdown menu for a specific type of Search and Rescue dog; by default it will only display non-mix breeds unless the 'Include Mixes' is checked.

When you scroll down you will see two widgets:
<p align="center">
<img width="3091" height="894" alt="image" src="https://github.com/user-attachments/assets/05767116-bc1b-437b-95b9-cbec85e3c8ea" />
</p>

The left sunburst widget will display the type of animal on the inner ring, then the breed of animal on the outer ring. The right will display a geo-location map of the selected animal from the table mentioned earlier.
- Source for creating Sunburst Charts in Dash can be found [here](https://plotly.com/python/sunburst-charts/)

## Filtering
If you want to filter by specific Search and Rescue dogs, you can use the drop down to select from:
  - Water Rescue
  - Mountain/Wilderness
  - Disaster Recovery
  - Scent Tracking
Note: The dog breeds for each topic were sourced with Google AI overview. If you wish to edit the catagories, you can edit "BREED_MAP."
<p align="center">
<img width="3617" height="1037" alt="image" src="https://github.com/user-attachments/assets/6055e70b-d0e3-4111-91f8-7b0a13c6a0d9" />
</p>

Once selected you will see the following will update:

1. Table will only show dog breeds that pertain to the specific Search & Rescue type
<p align="center">
<img width="3620" height="787" alt="image" src="https://github.com/user-attachments/assets/f2565743-93cf-42a5-872b-9e76007d466b" />
</p>

3. Sunburst will only show dogs and the breeds for the selected Search & Rescue Type
<p align="center">
<img width="3092" height="888" alt="image" src="https://github.com/user-attachments/assets/39a206a3-db2d-4135-994c-99eb94c0670a" />
</p>


If desired, you may also select 'Include Mixes' to include the specified breeds which are also mixed, the table and sunburst will update accordingly:
<p align="center">
<img width="1017" height="780" alt="image" src="https://github.com/user-attachments/assets/1b2eef30-1982-48df-b9df-46c49404f1eb" />
</p>
<p align="center">
<img width="1066" height="794" alt="image" src="https://github.com/user-attachments/assets/f1f80f31-e084-4fdb-982c-8352a3226ac9" />
</p>

Lastly, you can filter by age range, simply select the range on the slider for the animals between a certain age
<p align="center">
<img width="3616" height="1086" alt="image" src="https://github.com/user-attachments/assets/59007af3-ac79-4a45-9db6-19496d6bafd8" />
</p>

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
* DASH Framework
  + [https://dash.plotly.com/](https://dash.plotly.com/installation)
  + The Dash Python framework builds data reactive web applications follows the Model-View-Controller and allows you to program the View layout in pure Python with HTML elements. You then use "Callbacks" to send information to the Controller layer.
 
### Attributes
In the CRUD.py python library, I have created the following functionality that aligns with the fundamental elements of "CRUD."

* C - Create: Making a new entry in the database.
* R - Read: Given a specific query, return the details in a list.
* U - Update: Given a specific query, update the details of that entry.
* D - Delete: Remove an entry.
    * You can find the library [here](https://github.com/FinnishArmy/CRUD/tree/main)
 
## Challenges
### Sunburst
Designing the interactive sunburst chart was perhaps the most difficult part of the UX/UI design. If you don't use the correct callback, the sunburst does not get the up-to-date data from the table based on the specific filter attributes. At first I had a speerate function for update_sunburst which used a callback from `derived_virtual_Data` which never updates and is empty when you first boot. To fix this, I update the sunburst at the same time as the table using the output of `data` instead.
- Information can be found [here](https://plotly.com/python/sunburst-charts/)

### Styling
I wanted to create darkmode for the entire webpage, a lot of the elements cannot be directly in-line styled with HTML, such as the table itself. To overcome this, I setup a CSS `/assets/` folder with custom CSS stylign. When the website loaded, I simply used inspect element to find the elements and stlying them. This is also specific to that table, so if one wanted to add a new table, you can change that table stlying if so desired, based on the id of the table.

### Logo
I was having trouble figuring out what link to use for the img source. So what I ended up doing is importing the .png file into the `/assets/` folder. So now it's a direct source directory to grab it from.

## Import Database
## Usage
Follow these code examples to help run the scripts.

### Code Examples
#### Import the database
<img width="1087" height="360" alt="image" src="https://github.com/user-attachments/assets/b388e8d4-6bcd-4129-9567-e53e8132f06a" />

#### Set login details
<img width="1089" height="179" alt="image" src="https://github.com/user-attachments/assets/19aca942-e2e9-4763-8b4a-cb76afe015b2" />

#### Setup MongoDB Interface
<img width="1089" height="441" alt="image" src="https://github.com/user-attachments/assets/e01a55d8-bb34-41a4-87e8-07002bf8c3f8" />

#### Create a new user account
<img width="1088" height="283" alt="image" src="https://github.com/user-attachments/assets/592940b0-f8c8-4aee-aff2-7f9f854e9e31" />

#### You can now use the new user in a new window
* Note that you will need to change the port and host according to your own interface.
<img width="1094" height="608" alt="image" src="https://github.com/user-attachments/assets/acba5aa2-4d41-41e1-a161-b73b402c62f2" />


#### When running the test script, you should be able to add a new entry and receive this output
<img width="1086" height="176" alt="image" src="https://github.com/user-attachments/assets/0a8d01ea-9778-430c-826f-9ebe537b19f5" />

### Tests
#### Check to ensure you can read all documents
<img width="895" height="223" alt="image" src="https://github.com/user-attachments/assets/84f60bcc-c027-4fc3-ab6a-c4615cfbc243" />

#### CRUD Functionality Test Execution
Below shows the test for creation, reading, updating and deletion. If this does not complete, you will receive an Exception flag.
<img width="1729" height="1082" alt="image" src="https://github.com/user-attachments/assets/7d055ebf-a61b-43c6-801a-3912d745fcfb" />

#### Check that you can access MongoDB and list the database using both the admin and self-created user
<img width="831" height="440" alt="image" src="https://github.com/user-attachments/assets/8d7a249e-2e6a-4dc8-8dd8-def2f01887f4" />

<img width="828" height="521" alt="image" src="https://github.com/user-attachments/assets/8043404a-6e7a-45a1-aa0f-de9b34a4bc14" />

## Q & A
### How do you write programs that are maintainable, readable, and adaptable?
By ensuring that your code follows the basic rules of programming (ACID):
* A - Atomicity: ensure that every action works, if one single transaction fails the entire transaction must be rolled back.
* C - Consistency: every transaction must bring the database from one valid state to another valid state. Any data written to the database must adhere to the integrity requirements.
* I - Isolation: When multiple transaction take place, they must appear to run one-by-one without interfering with each other.
* D - Durability: When a transaction complete successfuly, the changes must be storred permanantly, even in a system failure.

### What were the advantages of working in this way?
When you follow the ACID principles when programming in databases, you ensure you will create a reliable and maintainable program.

### How else could you use this CRUD Python module in the future?
Using the knowledge gained from creating the CRUD Python module, I can now have more confidence in making bigger programs that utilize more than just one script. Creating an actual module to drive speific parts of the program as a whole makes the overall program more readable and easier to maintain.

### How do you approach a problem as a computer scientist?
If I have a problem, I begin by writing down the path at which I took to get to that problem. Instead of trying to go straight to finding a programmable solution, you slow down to think of why the problem occurred in the first place, then you can take steps to find solutions.

### How did your approach to this project differ from previous assignments in other courses?
In previous assignments and courses, you really only had to worry about one file at a time, when working with databases and this final project, you had to write a module that then another program would utilize to drive specific features. This means there a lot more moving parts, but means in the end, the project is easier to maintain. You prevent having spaghetti code by seperating bigger functionalities. Similar to having a function for each feature, having a module for bigger tasks is the way to go. Especially if you want multiple scripts to be able to utilize the same feature, you prevent yourself from having re-write it multiple times.

### What do computer scientists do, and why does it matter?
In the end, a coder converts requests in normal language into something a computer will understand. Further, a computer scientist will ensure this computer language is efficient, reliable and easy to understand for other computer scientists while also adhering to regulations and rules.
