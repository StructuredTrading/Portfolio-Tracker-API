# <center>Portfolio Tracker API</center>

<br>
<br>
<br>

### Links
**<a href="https://trello.com/b/BpbEW080/portfolio-tracker-api">Trello - development plan</a>**<br>
**<a href="https://github.com/StructuredTrading/Portfolio-Tracker-API">Github - portfolio tracker API app</a>**

<br>

### Pre-requisite's
Must have created a database and user with ownership rights of the database or super user privillages. `.env` file must be created using: `.env.sample` as as template.

<br>

### Installing
Using a terminal, run the following commands:

1. `cd SamOwen_T2A2/src` - Navigate to src folder.
2. `python3 -m venv .venv` - Create a virtual environment.
3. `source .venv/bin/activate` - Activate virtual environment.
4. `pip3 install -r requirements.txt` - Install required packages.
5. `flask run` - Start the flask server.
6. `db create` - Create the tables in the database
7. `db seed` - Seed the tables in the database

<br>

### Testing / Usage
Open insomnia and import the API endpoints using the `ENDPOINTS.json` file or manually add endpoints using the documentation below. Please be sure to follow all instruction's in documentation to ensure correct usage and results.

<br>
<br>
<br>

## R1 Identification of the problem you are trying to solve by building this particular app.

The <b>Portfolio Tracker API</b> for managing investment portfolios is designed to tackle common issues faced by investors, including:

#### Scattered Investments: 
Many investors have their assets spread out across different platforms or investment types, making it hard to see the big picture of their financial health.

#### Time-consuming Portfolio Management: 
Keeping track of and updating various investments manually can be a hassle and prone to mistakes.

#### Need for Up-to-date Information: 
In the fast-moving financial world, investors require the latest data on their investments to make swift, informed choices.

#### Security Worries: 
Given the sensitive nature of financial data, investors are often concerned about the safety and privacy of using third-party tracking services.

### How the App Helps:

#### Brings Everything Together: 
Offers a unified platform for all investment details, simplifying tracking and updates.

#### Delivers Real-time Insights: 
Provides current financial data to help investors make quick, informed decisions.

#### Keeps track of all transactions, asset classes and overal portfolio wealth: 
Includes features for tracking current transactions and grouping assets owned together in one convenient place for quick retreival. Portfolio equity can be also be accessed easily.

#### Customizable and Scalable: 
Can be tailored to fit individual needs and easily handles growing investment portfolios.

#### Prioritizes Security: 
Uses strong security measures to protect users' financial information, offering peace of mind.

This app aims to make investment management more straightforward, informed, and secure, helping investors better achieve their financial goals.

<br>
<br>
<br>

## R2 Why is it a problem that needs solving?

The absence of a centralized and automated investment management system presents several significant challenges for investors, highlighting the necessity for a solution like the described app. Without such a system, investors face the following problems:

#### Scattered Investment Data: 
Investors typically have assets across different accounts, platforms, or asset classes like stocks, bonds, and cryptocurrencies. This dispersion makes it difficult to get a unified view of their financial health, leading to disjointed decision-making and potential oversight of critical portfolio diversification or rebalancing opportunities.

#### Manual Portfolio Updates and Time Consumption: 
Tracking and updating portfolio holdings manually is not only tedious but also prone to errors. Each buy or sell transaction requires manual entry, and keeping tabs on the current market value of diverse assets can be overwhelmingly complex, consuming valuable time that could be better spent on strategic investment analysis.

#### Security and Privacy Concerns: 
Given the sensitive nature of financial data, there's a legitimate concern over the security and privacy of using third-party services. Investors need assurance that their data is protected against unauthorized access and breaches.

#### In summary:
The absence of an efficient investment management system complicates portfolio tracking, exposes investors to the risk of making decisions based on outdated information, and ultimately hampers their ability to achieve optimal financial outcomes. The app addresses these issues by offering a secure, real-time, and user-friendly platform for investors to manage their portfolios more effectively, making it a critical solution for anyone looking to optimize their investment strategy. 

<br>
<br>
<br>

## R3 Why have you chosen this database system. What are the drawbacks compared to others?

Choosing PostgreSQL for a project comes down to its many advantages and powerful features. Here's a straightforward overview of why PostgreSQL is a standout option and its minor limitations compared to other database systems:

### Why Pick PostgreSQL

- **Free and Open-Source**: PostgreSQL is available at no cost, allowing you to use, modify, and distribute it freely. This aspect significantly reduces database management expenses.

- **Packed with Features**: Capable of handling tricky operations and supporting a broad array of advanced data types, PostgreSQL enables extensive data manipulation, making it suitable for diverse projects.

- **Customizable**: It offers the flexibility to introduce custom data types, craft functions, and even employ various programming languages beyond SQL.

- **Follows Standards**: Adhering closely to SQL standards, PostgreSQL ensures your application can seamlessly interface with other database systems as required.

- **Flexible with Data Types**: Supporting both traditional SQL and NoSQL data formats, such as JSON, PostgreSQL is adaptable for various data storage and retrieval needs.

- **Secure**: Equipped with robust built-in security features, including encryption and access control mechanisms, PostgreSQL safeguards your data effectively.

### Limitations

- **Might Be Slower for Some Tasks**: In scenarios requiring extensive data reads, other specialized databases might offer superior performance.

- **Complicated Replication**: Establishing data replication, particularly in tricky configurations, can be more challenging in PostgreSQL than in some alternative databases.

- **Uses More Resources**: PostgreSQL's operation may demand greater memory and processing power compared to more lightweight database options.

- **Handling Large Volumes of Unstructured Data**: When dealing with vast amounts of unstructured data, NoSQL databases could potentially provide better efficiency due to their schema-less nature.

Even with a few downsides, PostgreSQL's wide range of features, strong security, and flexibility make it a great pick for projects that need careful data management and reliable performance. Overall, the benefits of using PostgreSQL far outweigh the few limitations it has, making it ideal for handling complicated data tasks.


<br>
<br>
<br>

## R4 Identify and discuss the key functionalities and benefits of an ORM
 
Object-Relational Mapping (ORM) is a way to use your programming language to interact with a database, so you don't have to write SQL code. It's like having a bridge between the way databases store data and how your application wants to use it. Here's a simpler look at what ORM does and why it's useful:

### Key Functionalities
- **Makes Coding Easier**: ORM lets you work with database data as if they were objects in your code. No need to write SQL directly.
- **Handles CRUD Easily**: Creating, reading, updating, and deleting database entries is simpler because you use your programming language's syntax, not SQL.
- **Converts Data Types**: Automatically changes data from one type to another, like turning SQL dates into the date types your programming language understands.
- **Manages Transactions Safely**: Keeps your data safe by automatically managing database transactions and rolling back changes if something goes wrong.
- **Improves Performance with Lazy Loading**: Loads data only when it's needed, which can make your application faster and use less memory.
- **Uses Caching to Speed Things Up**: Some ORM tools can remember data that's been used before, reducing the need to go back to the database.

### Benefits
- **Saves Time**: Automates routine tasks, so developers can focus on more important stuff, speeding up how fast you can make things.
- **Makes Code Cleaner**: Encourages writing neater, more maintainable code since you're working with high-level concepts, not database specifics.
- **Works Across Different Databases**: Makes your application flexible. You can change databases with minimal fuss because the ORM deals with database-specific details.
- **Keeps Your Data Safe**: Helps prevent common security issues, like SQL injection, by handling data in a safer way.
- **Deals with Complex Data Easily**: Simplifies working with tricky database relationships, turning them into easy-to-understand object properties.

While ORM has many pluses, like making development faster and your code cleaner, there can be downsides, like potentially slower performance for complex queries. However, for many projects, the benefits are worth it, making ORM a favorite for working with databases in web development.


<br>
<br>
<br>

## R5 Document all endpoints for your API

<br>

### **User Management (auth_controller)**

Prefix for all User management API endpoints (auth_controller):

    http://localhost:5000/auth
<br>

<!-- User Registration -->
### **1. User Registration:**
 * **Endpoint:** 'POST' `/auth/register`<br>
   * `http://localhost:5000/auth/register`
 * **Description:** Allows new users to register. Accessible by anyone who isn't logged in.<br>
 * **Request Methods:** `'POST'`
 * **Request Requirements:**
    `All requirements case sensitive`
   * `email` - Email must be a valid string containing all components that make up an email e.g., `example@domain.com`
   * `password` - Passwords have a minimum length requirement of 6 characters and are of type string e.g., `123456`
 * **Request Body Example:**
    ```json
    {
      "email": "test_account@email.com",
      "password": "123456"
    }
    ```
 * **Success Response Example:**
    ```json
    {
      "email": "test_account@email.com",
      "password": "$2b$12$X1HOxFaImXfPxTWbqv4zQOzykzuLVCAlhZZhSRFRHPyCW0av4rGXq",
      "userID": 5
    }
    ```
 * **Error Response Example:**
    ```json
    {
	  "error": "Email address allready in use"
    }
    ```
    ```json
    {
	  "error": "The 'email' field is required"
    }
    ```
    ```json
    {
	  "error": "The 'password' field is required"
    }
    ```
    ```json
    {
	  "error": "{'email': ['Not a valid email address.'], 'password': ['Shorter than minimum length 6.']}"
    }
    ```

 * **Status Codes:**
   * **'201 Created'** if the registration is successful.
   * **'400 Bad Request'** if the input validation fails (e.g., missing email or password, email email allready in use, email or password not valid).

<br>
<br>

<!-- User Login -->
### **2. User Login:**
 * **Endpoint:** 'POST' `/auth/login`<br>
   * `http://localhost:5000/auth/login`
 * **Description:** Authenticates users and returns a token (JWT). Accessible by anyone who isn't logged in with a valid username and password.<br>
 * **Request Methods:** `'POST'`
 * **Request Requirements:**
    `All requirements case sensitive`
   * `email` - Email must be a valid string containing all components that make up an email e.g., `example@domain.com`
   * `password` - Passwords have a minimum length requirement of 6 characters and are of type string e.g., `123456`
 * **Request Body Example:**
    ```json
    {
	"email": "test_account@email.com",
	"password": "123456"
    }
    ```
 * **Success Response Example:**
    ```json
    {
	"email": "test_account@email.com",
	"is_admin": false,
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxMDI5NDY3MCwianRpIjoiOWVjM2RmNzctZDhmMy00YTM2LTk0OWMtMWUyMWY4YWVlYTU2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjUiLCJuYmYiOjE3MTAyOTQ2NzAsImNzcmYiOiI0NzA0NzJjOC1kMGJkLTQ3YmQtODA0Mi05NTAzY2FlYzA2ODkiLCJleHAiOjE3MTAzODEwNzB9.ywr-dRkbhu2vW3K0OqNNjj92nl963yiaExvqP1BVS-Q"
    }
    ```
 * **Error Response Example:**
    ```json
    {
	"error": "Invalid email or password"
    }
    ```
    ```json
    {
	  "error": "{'email': ['Not a valid email address.'], 'password': ['Shorter than minimum length 6.']}"
    }
    ```
 * **Status Codes:**
   * **'200 OK'** if the login is successful.
   * **'401 Unauthorised'** if the email or password is incorrect.
   * **'400 Bad Request'** if the input validation fails (e.g., incorrect email format or password not required minimum length)

<br>
<br>

<!-- Delete User -->
### **3. Delete User** 
 * **Endpoint:** 'DELETE' `/auth/<int:user_id>`<br>
   * `http://localhost:5000/auth/delete/<int:user_id>`
 * **Description:** This endpoint allows for the deletion of a specific user by their user ID. It can be accessed by the user themselves (if the user_id in the URL matches the currently logged-in userID) or by an authenticated user with administrative privileges. This setup enables users to delete their own account or allows administrators to remove user accounts and associated data from the system.<br>
 * **Request Methods:** `'DELETE'`
 * **URL Parameters:** 'user_id' - The unique identifier (integer) of the user to be deleted.
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - The JWT token obtained upon authenticating. The token should either belong to the user being deleted or to an administritive user.
 * **Success Response Example:**
   * If the user is successfully deleted:
        ```json
        {
          "message": "User with userID '<user_id>' successfully deleted."
        }
        ```
 * **Error Response Examples:**
   * The user_id does not match the current user, and the user is not an admin:
        ```json
        {
        "error": "Unauthorized. You do not have permission to perform this action."
        }
        ```
    * If the user to be deleted does not exist:
        ```json
        {
        "error": "User with 'userID' '<user_id>' does not exist."
        }
        ```
 * **Status Codes:**
   * **'200 Ok'** If the user is successfully deleted.
   * **'403 Forbidden'** The user_id does not match, and the user is not an admin.
   * **'404 Not Found'** If the user is not found.

<br>
<br>
<br>

### **Portfolio Management (portfolio_controller)**

Prefix for all portfolio management API endpoints (portfolio_controller):

    http://localhost:5000/portfolios
<br>

<!-- Create Portfolio -->
### **1. Create Portfolio**
 * **Endpoint:** 'POST' `/portfolios/create`<br>
   * `http://localhost:5000/portfolios/create`
 * **Description:** This endpoint enables authenticated users to create a new portfolio. It requires users to be logged in and provide necessary portfolio details through the request body. The newly created portfolio is associated with the user's account based on their authentication token.<br>
 * **Request Methods:** `'POST'`
 * **Request Requirements:**
   * `name` - Name must be a valid string type containing atleast 1 character.
   * `description` - Description must be a valid string type containing atleast 1 character.
 * **Request Body Example:**
   ```json
   {
     "name": "My Investment Portfolio",
     "description": "A diversified portfolio of cryptocurrencies"
   }
   ```
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - The JWT token obtained upon logging in. This token identifies the authenticated user and links the newly created portfolio to their account.
 * **Success Response Example:**
   * If the portfolio is successfully created:
     ```json
     {
      "date": "2024-03-16",
      "description": "My Investment Portfolio",
      "holdings": 0.0,
      "name": "A diversified portfolio of cryptocurrencies",
      "ownedAssets": [],
      "portfolioID": 3,
      "userID": 3
     }
     ```
 * **Error Response Examples:**
   * If the user allready owns a portfolio:
     ```json
     {
      "error": "User '6' is not allowed to create more than one portfolio, user '6' allready has a portfolio called 'My portfolio'."
     }
     ```
   * If required data is missing or invalid in the request body:
     ```json
     {
	    "error": "{'name': ['Not a valid string.'], 'description': ['Not a valid string.']}"
     }
     ```
     ```json
     {
        "error": "{'name': ['Shorter than minimum length 1.'], 'description': ['Shorter than minimum length 1.']}"
     }
     ```
     ```json
     {
      "error": "{'name': ['Not a valid string.'], 'description': ['Not a valid string.']}"
     }
     ```
 * **Status Codes:**
   * **'201 Created'** If the portfolio is successfully created.
   * **'400 Bad Request'** If there is missing or invalid data in the request body.
   * **'403 Forbidden'** If the user allready owns a portfolio.
  
  <br>
  <br>

<!-- Retrieve All Portfolios -->
### **2. Retrieve All Portfolios**
 * **Endpoint:** 'GET' `/portfolios`<br>
   * `http://localhost:5000/portfolios/`
 * **Description:** This endpoint retrieves all portfolios from the database. It is accessible only by an administrator, allowing for a comprehensive view of all user portfolios.<br>
 * **Request Methods:** `'GET'`
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - The JWT token obtained upon logging in. This token should belong to an administrative user.
 * **Success Response Example:**
   * If the request is successful:
     ```json
     [
      {
        "date": "2024-03-16",
        "description": "A Portfolio that is owned by Admin.",
        "holdings": 4604232.317,
        "name": "Admin Portfolio",
        "ownedAssets": [
          {
            "ID": 7,
            "assetID": "litecoin",
            "name": "Litecoin",
            "portfolioID": 1,
            "price": 86.8,
            "quantity": 10,
            "symbol": "LTC"
          },
          {
            "ID": 8,
            "assetID": "bitcoin",
            "name": "Bitcoin",
            "portfolioID": 1,
            "price": 67663.0,
            "quantity": 10,
            "symbol": "BTC"
          }
        ],
        "portfolioID": 1,
        "userID": 1
      },
      {
        "date": "2024-03-16",
        "description": "A diversified portfolio of cryptocurrencies",
        "holdings": 0.0,
        "name": "My Investment Portfolio",
        "ownedAssets": [],
        "portfolioID": 2,
        "userID": 2
      }
     ]
     ```
 * **Error Response Examples:**
   * If the user is not an admin:
     ```json
     {
      "error": "Not authorised to perform this action"
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the request is successful.
   * **'403 Forbidden'** If the user is not authenticated as an admin.
   
<br>
<br>

<!-- Search Portfolio -->
### **3. Search Portfolio**
 * **Endpoint:** 'GET' `/portfolios/<int:portfolio_id>`<br>
   * `http://localhost:5000/portfolios/search/<int:portfolio_id>`
 * **Description:** Displays details of a specific portfolio. This endpoint is accessible by the owner of the portfolio or an administrator, ensuring privacy and administrative oversight.<br>
 * **Request Methods:** `'GET'`
 * **URL Parameters:** '<int:portfolio_id>' - The unique identifier of the portfolio to be retrieved of type 'Integer'.
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - The JWT token obtained upon logging in. The token should either belong to the portfolio's owner or to an administrative user.
 * **Success Response Example:**
   * If the portfolio is found:
     ```json
     {
       "portfolioID": 1,
       "name": "My Investment Portfolio",
       "userID": "<user_id>"
     }
     ```
 * **Error Response Examples:**
   * If the portfolio does not exist or the user does not have permission to view it:
     ```json
     {
       "error": "Not authorised to perform this action"
     }
     ```
     ```json
     {
      "error": "Portfolio with id '16' not found"
     }
 * **Status Codes:**
   * **'200 OK'** If the portfolio is successfully retrieved.
   * **'403 Forbidden'** If the user lacks access.
   * **'404 Not Found'** If the portfolio does not exist.

<br>
<br>   

<!-- Update Portfolio -->
### **4. Update Portfolio**
 * **Endpoint:** 'PATCH' `/portfolios/<int:portfolio_id>`<br>
   * `http://localhost:5000/portfolios/update/<int:portfolio_id>`
 * **Description:** This endpoint allows for the editing of details of a specific portfolio. It ensures that portfolio management is personal and secure by granting access exclusively to the portfolio's owner or to an administrative user. The flexibility to update portfolio details such as its name or description and enables users to maintain accurate and up-to-date information.<br>
 * **Request Methods:** `'PATCH'`
 * **URL Parameters:** '<int:portfolio_id>' - The unique identifier (integer) of the portfolio to be updated.
 * **Request Requirements:**
   * `name` - Name must be a valid string type containing atleast 1 character.
   * `description` - Description must be a valid string type containing atleast 1 character.
 * **Request Body Example:**
   ```json
   {
     "name": "Updated Portfolio Name",
     "description": "New description of the portfolio"
   }
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - The JWT token must be provided in the request header to authenticate. This token verifies the identity of the requester, ensuring that only the portfolio's owner or an administrative user can perform updates.
 * **Success Response Example:**
   * If the portfolio is successfully updated:
     ```json
     {
       "date": "2024-03-16",
       "description": "New description of the portfolio",
       "holdings": 0.0,
       "name": "Updated Portfolio Name",
       "ownedAssets": [],
       "portfolioID": 2,
       "userID": 2
     }
     ```
 * **Error Response Examples:**
   * If the user is not authenticated, the token is invalid, or the user does not have the necessary permissions:
     ```json
     {
       "error": "Not authorised to perform this action"
     }
     ```
   * If the portfolio to be updated does not exist:
     ```json
     {
       "error": "Portfolio with id '65' not found"
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the portfolio is successfully updated.
   * **'400 Bad Request'** If the request body is missing required attributes or contains invalid data.
   * **'403 Forbidden'** If the user lacks the necessary permissions to update the portfolio.
   * **'404 Not Found'** If the specified portfolio does not exist.
  
<br>
<br>

<!-- Delete Portfolio -->
### **5. Delete Portfolio**
 * **Endpoint:** 'DELETE' `/portfolios/<int:portfolio_id>`<br>
   * `http://localhost:5000/portfolios/delete/<int:portfolio_id>`
 * **Description:** This endpoint facilitates the removal of a specific portfolio from the system. It is designed to ensure secure portfolio management by allowing only the portfolio's owner or an administrative user to delete a portfolio. This operation permanently deletes the portfolio and its associated data, underscoring the importance of cautious use.<br>
 * **Request Methods:** `'DELETE'`
 * **URL Parameters:** '<int:portfolio_id>' - The unique identifier (integer) of the portfolio to be deleted.
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - To authenticate the request, a JWT token must be included in the Authorization header. This token serves to identify the requester, confirming whether they are the owner of the portfolio in question or an administrative user with the authority to delete it.
 * **Success Response Example:**
   * If the portfolio is successfully deleted:
     ```json
     {
       "message": "Portfolio 'Updated Portfolio Name' with portfolio ID '2' has successfully been deleted."
     }
     ```
 * **Error Response Examples:**
   * If the user does not have the necessary permissions:
     ```json
     {
       "error": "Only the portfolio owner or an admin can delete the requested portfolio"
     }
     ```
   * If the specified portfolio does not exist:
     ```json
     {
       "error": "Portfolio with ID '101' not found."
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the portfolio is successfully deleted.
   * **'403 Forbidden'** If the user lacks the necessary permissions to delete the portfolio.
   * **'404 Not Found'** If the specified portfolio does not exist.

<br>
<br>
<br>


### Transactions Management (transactions_controller)

Prefix for all transactions management API endpoints (transactions_controller):

    http://localhost:5000/transactions

<br>
<br>

<!-- Create Transaction -->
### **1. Create Transaction**
 * **Endpoint:** 'POST' `/transactions/trade`<br>
   * `http://localhost:5000/transactions/trade`
 * **Description:** This endpoint allows logged-in users to add a new transaction to their account. It automatically associates the created transaction with the userID of the currently logged-in user, enabling users to track their trades or investments in a personal and secure manner. This functionality is essential for maintaining an accurate and up-to-date record of the user's financial activities.<br>
 * **Request Methods:** `'POST'`
 * **Request Requirements:**
   * `transactionType` - Transaction type must be of type string and be one of the following two options (CASE SENSITIVE) `buy` `sell`.
   * `quantity` - Quantity must be of type integer and greater then or equal to 1.
   * `assetID` - Asset id must be of type string and must match one of the available to trade assets (This can be found by using the retrieve all assets endpoint). e.g., `bitcoin` `ethereum` `litecoin`
 * **Request Body Example:**
   ```json
    {
        "transactionType": "buy",
        "quantity": "25",
        "assetID": "bitcoin"
    }
   ```
   ```json
    {
        "transactionType": "sell",
        "quantity": "15",
        "assetID": "ethereum"
    }
   ```
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - The request must include a JWT token in the Authorization header to authenticate the user. This token identifies the currently logged-in user, ensuring that the new transaction is correctly associated with their account.
 * **Success Response Example:**
   * If the transaction is successfully created:
     ```json
     {
        "assetID": "bitcoin",
        "date": "2024-03-13",
        "portfolioID": 1,
        "price": 72025.0,
        "quantity": 25,
        "totalCost": 1800625.0,
        "transactionID": 17,
        "transactionType": "buy"
     }
     ```

 * **Error Response Examples:**
   * If the user does not own a portfolio:
     ```json
     {
      "error": "You must create a portfolio first"
     }
     ```
   * If required data is missing in the request body:
     ```json
     {
      "error": "{'transactionType': ['Missing data for required field.']}"
     }
     ```
     ```json
     {
      "error": "{'quantity': ['Missing data for required field.']}"
     }
     ```
     ```json
     {
      "error": "{'assetID': ['Missing data for required field.']}"
     }
     ```
   * If required data is invalid in the request body:
     ```json
     {
      "error": "{'transactionType': ['Not a valid string.']}"
     }
     ```
     ```json
     {
      "error": "{'quantity': ['Not a valid integer.']}"
     }
     ```
     ```json
     {
      "error": "{'assetID': ['Not a valid string.']}"
     }
     ```
   * If assetID is not found in the db: 
     ```json
     {
       "error": "Asset id not found."
     }
     ```
 * **Status Codes:**
   * **'201 Created'** If the transaction is successfully created.
   * **'400 Bad Request'** If there is missing or invalid data in the request body.
   * **'404 Not Found'** If the assetID is not found in the db.
   * **'403 Forbidden'** If user does not own a portfolio.

<br>
<br>


#### 2. List Transactions
 * **Endpoint:** 'GET' `/transactions`<br>
   * `http://localhost:5000/transactions`
 * **Description:** This endpoint retrieves a list of transactions associated with all portfolios. It is designed to be accessible exclusively by an admin.<br>
 * **Request Methods:** `'GET'`
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - To access this endpoint, a JWT token must be provided in the Authorization header. This token verifies the identity of the requester, confirming that they are in fact an administrator.
 * **Success Response Example:**
   * If the request is successful, a list of transactions is returned:
     ```json
     [
      {
        "assetID": "bitcoin",
        "date": "2024-03-16",
        "portfolioID": 1,
        "price": 68131.0,
        "quantity": 10,
        "totalCost": 681310.0,
        "transactionID": 1,
        "transactionType": "buy"
      },
      {
        "assetID": "ethereum",
        "date": "2024-03-16",
        "portfolioID": 3,
        "price": 3688.41,
        "quantity": 5,
        "totalCost": 18442.05,
        "transactionID": 2,
        "transactionType": "buy"
      },
      {
        "assetID": "litecoin",
        "date": "2024-03-16",
        "portfolioID": 1,
        "price": 89.2,
        "quantity": 30,
        "totalCost": 2676.0,
        "transactionID": 3,
        "transactionType": "buy"
      },
      {
        "assetID": "dogecoin",
        "date": "2024-03-16",
        "portfolioID": 3,
        "price": 0.156731,
        "quantity": 1000,
        "totalCost": 156.73,
        "transactionID": 4,
        "transactionType": "buy"
      },
      {
        "assetID": "binancecoin",
        "date": "2024-03-16",
        "portfolioID": 2,
        "price": 602.14,
        "quantity": 10,
        "totalCost": 6021.4,
        "transactionID": 5,
        "transactionType": "sell"
      },
      {
        "assetID": "binancecoin",
        "date": "2024-03-16",
        "portfolioID": 2,
        "price": 602.14,
        "quantity": 10,
        "totalCost": 6021.4,
        "transactionID": 6,
        "transactionType": "sell"
      },
      {
        "assetID": "binancecoin",
        "date": "2024-03-16",
        "portfolioID": 1,
        "price": 602.14,
        "quantity": 10,
        "totalCost": 6021.4,
        "transactionID": 7,
        "transactionType": "sell"
      }
     ]
     ```

 * **Error Response Examples:**
   * If the user is not authorised:
     ```json
     {
       "error": "Not authorised to perform this action"
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the transactions or assets are successfully retrieved.
   * **'403 Forbidden'** If the user is not authorised (not an admin).

<br>
<br>

<!-- Search for Transaction -->
### **1. Search for Transaction**
 * **Endpoint:** 'GET' `/transactions/search/<int:transaction_id>`<br>
   * `http://localhost:5000/transactions/search/<int:transaction_id>`
 * **Description:** This endpoint is designed to retrieve a specific transaction. It ensures secure access by allowing only the portfolio's owner or an administrative user to retrieve transaction details. This capability is crucial for reviewing individual transactions, auditing, and comprehensive portfolio management.<br>
 * **Request Methods:** `'GET'`
 * **URL Parameters:** 'transaction_id' - The unique identifier (integer) of the transaction which is to be searched for.
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - A JWT token must be included in the Authorization header to authenticate the request. This token identifies the requester, ensuring that only authorized users, such as the portfolio's owner or an admin, can access transaction details.
 * **Success Response Example:**
   * If the transaction is found:
     ```json
     {
      "assetID": "bitcoin",
      "date": "2024-03-19",
      "portfolioID": 1,
      "price": 63265.0,
      "quantity": 10,
      "totalCost": 632650.0,
      "transactionID": 1,
      "transactionType": "buy"
     }
     ```
 * **Error Response Examples:**
   * If the user is not authenticated, does not own the specified transaction, or is not an admin:
     ```json
     {
       "error": "Not Authorised to view transaction"
     }
     ```
   * If the specified transaction does not exist:
     ```json
     {
       "error": "Transaction not found"
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the specific transaction is successfully retrieved.
   * **'403 Forbidden'** If the user lacks the necessary permissions to access the transaction.
   * **'404 Not Found'** If the specified transaction does not exist.


<br>
<br>

### **Owned Assets management (ownedAssets_controller)**

Prefix for all owned assets management API endpoints (ownedAssets_controller):

    http://localhost:5000/assets/owned

### **1. Retrieve all owned Assets**
 * **Endpoint:** 'GET' `/assets/owned`<br>
   * `http://localhost:5000/assets/owned`
 * **Description:** This endpoint is designed to retrieve a comprehensive list of assets owned by all users. This functionality is essential for admins to manage and audit assets across the platform.<br>
 * **Request Methods:** `'GET'`
 * **Requires Headers:**
   * **'Authorization':'Bearer JWT'** - A JWT token must be provided in the Authorization header for authenticating the user. This token determines whether the requester is an admin, accessing a comprehensive list of all assets.
 * **Success Response Example:**
   * If the request is successful, it returns a list of all assets owned by all users:
     ```json
     [
      {
        "ID": 1,
        "assetID": "bitcoin",
        "name": "Bitcoin",
        "portfolioID": 1,
        "price": 63265.0,
        "quantity": 10,
        "symbol": "BTC"
      },
      {
        "ID": 2,
        "assetID": "ethereum",
        "name": "Ethereum",
        "portfolioID": 1,
        "price": 3250.61,
        "quantity": 5,
        "symbol": "ETH"
      },
      {
        "ID": 3,
        "assetID": "litecoin",
        "name": "Litecoin",
        "portfolioID": 1,
        "price": 78.49,
        "quantity": 30,
        "symbol": "LTC"
      },
      {
        "ID": 4,
        "assetID": "cardano",
        "name": "Cardano",
        "portfolioID": 1,
        "price": 0.605016,
        "quantity": 1000,
        "symbol": "ADA"
      }
     ]
     ```
 * **Error Response Examples:**
   * If the user is authorised as an admin:
     ```json
     {
       "error": "Not authorised to perform this action"
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the assets are successfully retrieved.
   * **'403 Forbidden'** If the user is authorised as an admin.<br>

<br>
<br>


### **2. Retrieve Portfolio Assets by Portfolio ID**
 * **Endpoint:** 'GET' /assets/owned/<int:portfolio_id><br>
   * `http://localhost:5000/assets/owned/<int:portfolio_id`
 * **Description:** This endpoint retrieves all assets associated with a specific portfolio ID. It ensures that the requestor has the appropriate authorization, either by being the owner of the portfolio or by possessing administrative privileges. JWT authentication is required to access this endpoint.<br>
 * **Request Methods:** 'GET'
 * **URL Parameters:** '<int:portfolio_id>' - The unique identifier (integer) of the portfolio owned assets to be retrieved.
 * **Requires Headers:**
   * **'Authorization:'Bearer JWT'** - A JWT token is required for authentication, providing proof of the requestor's identity and permissions.
 * **Success Response Example:**
   * If the request is successful and assets exist within the specified portfolio:
      ```json
      [
        {
          "ID": 1,
          "assetID": "bitcoin",
          "name": "Bitcoin",
          "portfolioID": 1,
          "price": 63265.0,
          "quantity": 10,
          "symbol": "BTC"
        },
        {
          "ID": 2,
          "assetID": "ethereum",
          "name": "Ethereum",
          "portfolioID": 1,
          "price": 3250.61,
          "quantity": 5,
          "symbol": "ETH"
        },
        {
          "ID": 3,
          "assetID": "litecoin",
          "name": "Litecoin",
          "portfolioID": 1,
          "price": 78.49,
          "quantity": 30,
          "symbol": "LTC"
        },
        {
          "ID": 4,
          "assetID": "cardano",
          "name": "Cardano",
          "portfolioID": 1,
          "price": 0.605016,
          "quantity": 1000,
          "symbol": "ADA"
        }
      ]
      ```
 * **Error Response Examples:**
   * If the requestor is not authorized to view the assets:
      ```json
      {
        "error": "Not Authorised"
      }
      ```
   * If no assets are found for the specified portfolio ID:
      ```json
      {
        "error": "Assets with portfolioID '2' not found"
      }
      ```
* **Status Codes:**
  * **'200 OK'** If the assets are successfully retrieved.
  * **'403 Forbidden'** If the requestor is neither the portfolio owner nor an admin.
  * **'404 Not Found'** If no assets are found for the specified portfolio ID.

<br>
<br>
<br>

### **Assets management (assets_controller)**

Prefix for all assets management API endpoints (assets_controller):

    http://localhost:5000/assets

### **1. Retrieve all tradeable assets**
 * **Endpoint:** 'GET' `/assets`<br>
   * `http://localhost:5000/assets`
 * **Description:** This endpoint interfaces with the CoinGecko 3rd party API to retrieve a comprehensive list of 250 cryptocurrency assets available on CoinGecko. It is designed to provide users and administrators with up-to-date information about various cryptocurrencies, including names, symbols, current prices, and market data. This functionality is vital for users looking to make informed investment decisions and for admins to monitor cryptocurrency market trends.<br>
 * **Request Methods:** `'GET'`
 * **No Authentication Required:** This endpoint is designed to be publicly accessible since it retrieves general market data without exposing sensitive user information.
 * **Success Response Example:**
   * If the request is successful, it returns a list of cryptocurrency assets:
     ```json
     [
        {
            "assetID": "bitcoin",
            "marketCapPos": 1,
            "name": "Bitcoin",
            "price": 72029.0,
            "symbol": "BTC"
        },
        {
            "assetID": "ethereum",
            "marketCapPos": 2,
            "name": "Ethereum",
            "price": 4041.47,
            "symbol": "ETH"
        },
        {
            "assetID": "tether",
            "marketCapPos": 3,
            "name": "Tether",
            "price": 0.999579,
            "symbol": "USDT"
        },
        {
            "assetID": "binancecoin",
            "marketCapPos": 4,
            "name": "BNB",
            "price": 538.45,
            "symbol": "BNB"
        },
        {
            "assetID": "solana",
            "marketCapPos": 5,
            "name": "Solana",
            "price": 149.28,
            "symbol": "SOL"
        },
        {
            "assetID": "staked-ether",
            "marketCapPos": 6,
            "name": "Lido Staked Ether",
            "price": 4038.12,
            "symbol": "STETH"
        },
        {
            "assetID": "ripple",
            "marketCapPos": 7,
            "name": "XRP",
            "price": 0.696329,
            "symbol": "XRP"
        },
        {
            "assetID": "usd-coin",
            "marketCapPos": 8,
            "name": "USDC",
            "price": 0.999925,
            "symbol": "USDC"
        },
        {
            "assetID": "cardano",
            "marketCapPos": 9,
            "name": "Cardano",
            "price": 0.751814,
            "symbol": "ADA"
        },
        {
            "assetID": "dogecoin",
            "marketCapPos": 10,
            "name": "Dogecoin",
            "price": 0.171544,
            "symbol": "DOGE"
        }
        
     ]
     ```
     
 * **Error Response Examples:**
   * If there is an issue connecting to the CoinGecko API or retrieving data:
     ```json
     {
       "error": "Service Unavailable. Unable to retrieve data from CoinGecko at this time."
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the cryptocurrency asset data is successfully retrieved.
   * **'503 Service Unavailable'** If there is an issue connecting to the CoinGecko API or retrieving data.

<br>
<br>

#### **2. Retrieve Information of a Single Asset**
 * **Endpoint:** 'GET' `/assets/search/<string:asset_id>`<br>
    * `http://localhost:5000/assets/search/<string:asset_id>`
 * **Description:** This endpoint is specifically designed to retrieve updated general market data about a single cryptocurrency asset.<br>
 * **Request Methods:** `'GET'`
 * **URL Parameters:** '<string:asset_id>' - The unique identifier (string) of the asset to be retrieved.
 * **No Authentication Required:** This endpoint is publicly accessible, considering it provides general market data that does not involve sensitive personal information.
 * **Success Response Example:**
   * If the request is successful, it returns general information about the asset:
     ```json
     {
        "assetID": "litecoin",
        "marketCapPos": 22,
        "name": "Litecoin",
        "price": 98.05,
        "symbol": "LTC"
     }
     ```
 * **Error Response Examples:**
   * If the specified asset is not found or there is an issue with the request:
     ```json
     {
       "error": "Asset with asset id '{asset_id}' not found"
     }
     ```
 * **Status Codes:**
   * **'200 OK'** If the asset information is successfully retrieved.
   * **'404 Not Found'** If the specified asset could not be found or does not exist.



<br>
<br>
<br>

## R6 An ERD for your app

<br>

### **Users model:**
* **Table name:** `users`
* **Attributes:**
  * `userID`: Primary key (PK), Integer. Uniquely identifies each user in the table.
  * `email`: String, Email address used to create an account. Unique to each user in 'users' table as this is used as a username to log in.
  * `password`: String minimum 6 characters in length, used with 'email' attribute to verify ownership of an account.
  * `is_admin`: Boolean value, indicates whether the 'user' is a administrator or not.
* **Association:**
  * `One-to-One` with `portfolios` table, each user can own one portfolio and a user must be present for a portfolio to exist.

<br>

### **Portfolios model:**
* **Table name:** `portfolios`
* **Attributes:**
  * `portfolioID`: Primary key (PK), Integer. Uniquely identifies each portfolio in the portfolios table.
  * `userID`: Foreign key (FK), Integer. Links to the `users` table.
  * `name`: String minimum 1 characters in length. Identifies the portfolio with a more easily identifiable name.
  * `description`: String minimum 1 characters in length. Used to describe the contents of the portfolio or who it may belong to.
  * `Holdings`: Float. Used to display current holdings (portfolio value) of the portfolio.
  * `date`: Date. The date the portfolio was created.
* **Association:**
  * `One-to-One` with `users` table, each portfolio belongs to one user in the users table.
  * `One-to-Many` with `ownedAssets` table, each portfolio can own many assets in ownedAssets table.
  * `One-to-Many` with `transactions` table, each portfolio can have many transactions.

<br>

### **OwnedAssets model:**
* **Table name:** `ownedAssets`
* **Attributes:**
  * `ID`: Primary key (PK), Integer. Uniquely identifies each ownedAsset in ownedAssets table.
  * `assetID`: Foreign key (FK), String. Links to the `assets` table.
  * `portfolioID`: Foreign key (PK), Integer. Links to the `portfolios` table.
  * `symbol`: String. Used to more easily identify the id of the asset.
  * `name`: String. The name of the asset that is owned.
  * `quantity`: Integer. Used to showcase the amount of the asset which is owned.
  * `price`: Float. The AVG price the asset was aquired for.
* **Association:**
  * `Many-to-One` with `portfolios` table, each ownedAsset can belong to one portfolio in the portfolios table.
  * `Many-to-One` with `assets` table, many ownedAssets can belong to one asset.

<br>

### **Transactions model:**
* **Table name:** `transactions`
* **Attributes:**
  * `TransactionID`: Primary key (PK), Integer. Uniquely identifies each transaction in transactions table.
  * `portfolioID`: Foreign key (PK), Integer. Links to the `portfolios` table.
  * `assetID`: Foreign key (FK), String. Links to the `assets` table.
  * `transactionType`: String ('buy', 'sell'). Used to identify whether the transaction that occured 'bought' or 'sold' an asset.
  * `quantity`: Integer. Used to showcase the amount of the asset which has been transacted.
  * `price`: Float. The price the asset was aquired or sold for.
  * `totalCost`: Float. The total cost of the transaction or Sum of.
  * `date`: Date. The date that the transaction was made.
* **Association:**
  * `Many-to-One` with `portfolios` table, many transactions can belong to one user in the users table.
  * `Many-to-One` with `assets` table, many transactions can belong to the one asset in assets table.

<br>

### **Assets model:**
* **Table name:** `assets`
* **Attributes:**
  * `assetID`: Primary key (PK), String. Uniquely identifies each asset in assets table.
  * `marketCapPos`: Integer. identifies the current market cap position or rank in the table denoted by market dominance.
  * `symbol`: String. Used to more easily identify the id of the asset.
  * `name`: String. The name of the asset in assets table.
  * `price`: Float. The price the asset was aquired or sold for.
* **Association:**
  * `One-to-Many` with `ownedAssets` table, one asset can belong to many ownedAssets in the ownedAssets table.
  * `One-to-Many` with `transactions` table, one asset can belong to many transactions in transactions table.

<br>

### **Description**
The described Entity-Relationship Diagram (ERD) outlines a database schema for managing investment portfolios, describing the relationships between users, their investment portfolio, the assets within those portfolios, and the transactions associated to those assets. Here's a overview:

<img src="./docs/Images/Portfolio-Tracker-API_ERD.png"></img>

<br>
<br>
<br>

## R7 Detail any third party services that your app will use


### PyCoinGecko
**Package:** pycoingecko==3.1.0<br>
**Service:** CoinGecko<br>
**Description:** CoinGecko gives you data about cryptocurrency prices, how much they're being traded, and their market value. The pycoingecko package lets your app get this data straight from CoinGecko.<br>
**Use Cases:** the portfolio tracker app uses it to show live cryptocurrency prices, how they rank in the market, and their symbols. It also helps retrieve a list of the top 250 cryptocurrencies to update the assets table.

### Flask & Flask-Extensions
**Package:** Flask==3.0.2, Flask-Bcrypt==1.0.1, Flask-JWT-Extended==4.6.0, Flask-SQLAlchemy==3.1.1, flask-marshmallow==1.2.0<br>
**Service:** Flask<br>
**Description:** Flask is an easy-to-use web framework for Python. With Flask-Extensions, you can do things like hash passwords (Flask-Bcrypt), manage login tokens (Flask-JWT-Extended), work with databases more easily (Flask-SQLAlchemy), and convert data between formats (flask-marshmallow).<br>
**Use Cases:** These tools help build and manage portfolio Tracker to handle logins, interact with the database, and work with data easily.

### SQLAlchemy & psycopg2-binary
**Package:** SQLAlchemy==2.0.27, psycopg2-binary==2.9.9<br>
**Service:** PostgreSQL<br>
**Description:** SQLAlchemy is a toolkit that makes it easier to talk to databases using Python, and psycopg2-binary lets you connect specifically to PostgreSQL databases.<br>
**Use Cases:** Together, they help to create database models, run queries, and connect to the PostgreSQL database reliably.

### bcrypt & PyJWT
**Package:** bcrypt==4.1.2, PyJWT==2.8.0<br>
**Service:** Security and Authentication<br>
**Description:** bcrypt helps securely hash passwords, so they're safely stored. PyJWT lets you create, check, and use JWT tokens for logging in and keeping information secure.<br>
**Use Cases:** bcrypt is used to make sure user passwords are safe. PyJWT helps to manage user logins and keep things secure with tokens.

### marshmallow
**Package:** marshmallow==3.21.0<br>
**Service:** Data Serialization/Deserialization<br>
**Description:** marshmallow is a tool that helps you convert complex data like objects into simpler Python data types and back.<br>
**Use Cases:** It's used to check data and convert it to and from JSON format, making it easier to handle API data in the portfolio tracker app.

### requests
**Package:** requests==2.31.0<br>
**Service:** HTTP Requests<br>
**Description:** The requests package makes it straightforward to send HTTP requests to websites or APIs.<br>
**Use Cases:** It is used to talk to web services or APIs, apart from CoinGecko, or for communication within the app if needed.


<br>
<br>
<br>

## R8 Describe your projects models in terms of the relationships they have with each other

<!-- The project's models represent a financial portfolio tracking system with entities such as users, portfolios, transactions, owned assets, and assets. The relationships between these entities are crucial for organizing how data is linked and managed within the system. Here's an overview of the models and their relationships:

### User model and Portfolio model
- **One-to-One Relationship**: Each `User` is linked to a single `Portfolio`, and vice versa. This connection is made possible by the `portfolio` attribute in the `User` model and the `user` attribute in the `Portfolio` model. A `ForeignKey` on `userID` within the `Portfolio` model ensures this relationship's uniqueness.
- The `cascade="all, delete"` setting on the `User` model's `portfolio` relationship specifies that deleting a `User` will also remove their associated `Portfolio`.

### Portfolio model and Transaction model
- **One-to-Many Relationship**: A `Portfolio` can contain many `Transactions`, yet each `Transaction` is associated with only one `Portfolio`. This relationship is represented by the `transaction` attribute in the `Portfolio` model and the `portfolio` attribute in the `Transaction` model, linked by a `ForeignKey` on `portfolioID` in the `Transaction` model.
- The `cascade="all, delete"` option means that removing a `Portfolio` also deletes all related `Transactions`.

### Portfolio model and OwnedAsset model
- **One-to-Many Relationship**: A `Portfolio` may also contain multiple `OwnedAssets`, but each `OwnedAsset` relates to a single `Portfolio`. This is managed via the `ownedAssets` relationship in the `Portfolio` model and the `portfolio` relationship in the `OwnedAsset` model, connected by a `ForeignKey` on `portfolioID` in the `OwnedAsset` model.
- The `cascade="all, delete"` setting ensures the deletion of a `Portfolio` results in the removal of all its `OwnedAssets`.

### Asset, Transaction, and OwnedAsset
- **One-to-Many Relationship**: An `Asset` is linked to multiple `Transactions` and `OwnedAssets`, though each `Transaction` and `OwnedAsset` corresponds to only one `Asset`. These connections are denoted by the `transaction` and `ownedAssets` attributes in the `Asset` model, and the `asset` attributes in both the `Transaction` and `OwnedAsset` models. `ForeignKey` constraints on `assetID` in the `Transaction` and `OwnedAsset` models facilitate these links.
- The `cascade="all, delete"` directives for these relationships indicate that erasing an `Asset` also eliminates all associated `Transactions` and `OwnedAssets`.

The relational structure of these models offers a systematic way to manage portfolios, where users own portfolios that include transactions and assets, and assets may be part of transactions or categorized as owned assets. The inclusion of cascading delete options aids in maintaining data integrity and streamlines the management of interconnected data. -->

In the portfolio tracker API , relationships are defined between models using SQLAlchemy, an ORM (Object-Relational Mapping) framework. These relationships are crucial for organizing and managing data within the application. Here's a breakdown of the models and their relationships:

### User Model:
```python
class User(db.Model):
    # Table Name
    __tablename__ = "users"

    # Table Attributes
    userID = db.Column(db.Integer, primary_key=True)  # Primary Key
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Relationships between Tables
    portfolio = db.relationship("Portfolio", back_populates="user", uselist=False, cascade="all, delete")
```

The User model represents users of the system.
It has a one-to-one relationship with the `Portfolio model`, established through a `ForeignKey` relationship in portfolios table. 
```python
userID = db.Column(db.Integer, db.ForeignKey("users.userID"), unique=True, nullable=False)
```
This signifies that each user owns a single portfolio.
Additionally, the User model serves as the parent in a parent-child relationship with the Portfolio model.
```python
portfolio = db.relationship("Portfolio", back_populates="user", uselist=False, cascade="all, delete")
```
<br>

### Portfolio Model:
```python
class Portfolio(db.Model):
    # Table Name
    __tablename__ = "portfolios"

    # Table Attributes
    portfolioID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    holdings = db.Column(db.Float, default=0, nullable=False)
    date = db.Column(db.Date, nullable=False)

    # Foreign Keys
    userID = db.Column(db.Integer, db.ForeignKey("users.userID"), unique=True, nullable=False)

    # Relationships between Tables
    user = db.relationship("User", back_populates="portfolio")
    transaction = db.relationship("Transaction", back_populates="portfolio", cascade="all, delete")
    ownedAssets = db.relationship("OwnedAsset", back_populates="portfolio", cascade="all, delete")
```
The Portfolio model represents portfolios owned by users.
It has a one-to-one relationship with the User model, established through the ForeignKey relationship. 
```python
userID = db.Column(db.Integer, db.ForeignKey("users.userID"), unique=True, nullable=False)
```
This signifies that each portfolio belongs to a single user.
Furthermore, the Portfolio model has one-to-many relationships with the Transaction and OwnedAsset models. This means that a portfolio can have multiple transactions and owned assets associated with it.
The Portfolio model acts as the child in the parent-child relationship with the User model.
```python
user = db.relationship("User", back_populates="portfolio")
```

<br>

### Transaction Model:
```python
class Transaction(db.Model):
    # Table Name
    __tablename__ = "transactions"

    # Table Attributes
    transactionID = db.Column(db.Integer, primary_key=True)  # Primary Key
    transactionType = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    totalCost = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)

    # Foreign Keys
    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolios.portfolioID"))
    assetID = db.Column(db.String, db.ForeignKey("assets.assetID"))

    # Relationships between Tables
    portfolio = db.relationship("Portfolio", back_populates="transaction")
    asset = db.relationship("Asset", back_populates="transaction")
```
The Transaction model represents financial transactions within a portfolio.
It has one-to-many relationships with the Portfolio and Asset models, indicating that each transaction is associated with a single portfolio and a single asset.
The cascade="all, delete" option is utilized to ensure that deleting a portfolio or an asset also deletes associated transactions, maintaining data integrity.

Sets `Transaction model` to child of parent `Portfolio Model`:
```python
# Child Relationship Setup in Transaction Model
portfolio = db.relationship("Portfolio", back_populates="transaction")
```
```python
# Parent Relationship Setup in Portfolio Model
transaction = db.relationship("Transaction", back_populates="portfolio", cascade="all, delete")
```

Sets `Transaction model` to child of parent `Asset Model`:
```python
asset = db.relationship("Asset", back_populates="transaction")
```
```python
transaction = db.relationship("Transaction", back_populates="asset", cascade="all, delete")
```

<br>

### OwnedAsset Model:
```python
class OwnedAsset(db.Model):
    # Table Name
    __tablename__ = "ownedAssets"

    # Table Attributes
    ID = db.Column(db.Integer, primary_key=True)  # Primary Key
    symbol = db.Column(db.String, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Foreign Keys
    assetID = db.Column(db.String, db.ForeignKey("assets.assetID"), nullable=False)
    portfolioID = db.Column(db.Integer, db.ForeignKey("portfolios.portfolioID"), nullable=False)

    # Relationships between Tables
    asset = db.relationship("Asset", back_populates="ownedAssets")
    portfolio = db.relationship("Portfolio", back_populates="ownedAssets")
```
The OwnedAsset model represents assets owned within portfolios.
It has many-to-one relationships with the Portfolio and Asset models, indicating that each owned asset is associated with a single portfolio and a single asset.
The cascade="all, delete" option ensures that deleting a portfolio or an asset also deletes associated owned assets, maintaining data integrity.

Sets `OwnedAsset model` to child of parent `Portfolio Model`:
```python
# Child Relationship Setup in Portfolio Model
ownedAssets = db.relationship("OwnedAsset", back_populates="portfolio", cascade="all, delete")
```
```python
# Parent Relationship Setup in OwnedAsset Model
portfolio = db.relationship("Portfolio", back_populates="ownedAssets")
```

Sets `OwnedAssets model` to child of parent `Assets Model`:
```python
# Child Relationship Setup in Asset Model
ownedAssets = db.relationship("OwnedAsset", back_populates="asset", cascade="all,delete")
```
```python
# Parent Relationship Setup in OwnedAsset Model
asset = db.relationship("Asset", back_populates="ownedAssets")
```

<br>


### Asset Model:
```python
class Asset(db.Model):
    # Table Name
    __tablename__ = "assets"

    # Table Attributes
    assetID = db.Column(db.String, primary_key=True)
    marketCapPos = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Relationships between Tables
    transaction = db.relationship("Transaction", back_populates="asset", cascade="all, delete")
    ownedAssets = db.relationship("OwnedAsset", back_populates="asset", cascade="all,delete")
```
The Asset model represents assets available for trading.
It has one-to-many relationships with the Transaction and OwnedAsset models, indicating that each asset can be involved in multiple transactions and owned by multiple portfolios.
The cascade="all, delete" option ensures that deleting an asset also deletes associated transactions and owned assets, maintaining data integrity.

Sets `Assets model` to parent of child `Transactions`:
```python
# Child Relationship Setup in Assets Model
transaction = db.relationship("Transaction", back_populates="asset", cascade="all, delete")
```
```python
# Parent Relationship Setup in Transactions Model
asset = db.relationship("Asset", back_populates="transaction")
```

Sets `Assets model` to parent of child `Transactions`:
```python
# Child Relationship Setup in Assets Model
ownedAssets = db.relationship("OwnedAsset", back_populates="asset", cascade="all,delete")
```
```python
# Parent Relationship Setup in OwnedAssets Model
asset = db.relationship("Asset", back_populates="ownedAssets")
```
<br>

##### Summary
In summary, the app utilize's `ForeignKey` relationships to establish associations between models, representing `one-to-one` and `one-to-many` relationships. The same method may be used differently on different models based on the specific nature of the relationships. Additionally, `parent-child` relationships are established to denote hierarchical associations, where one model acts as the `parent` and another as the `child`. These relationships are essential for organizing and managing financial data within the application.


<br>
<br>
<br>

## R9 Discuss the database relations to be implemented in your application


#### Entity-Relationship Diagram (ERD) Overview:
The ERD illustrates the structure of the portfolio tracker database, depicting the entities (tables) and their relationships between each other.

#### Users Table:
* **Attributes:** 
  * userID (primary key, String) 
  * email 
  * password 
  * is_admin
* **Relationships:**
  * One-to-One with Portfolios: Illustrated in the ERD, each user can only have a single portfolio. This relationship is established by the foreign key userID in the portfolios table, referencing the primary key userID in the Users table.

<br>

#### Portfolios Table:
* **Attributes:** 
  * portfolioID (primary key)
  * userID (foreign key) 
  * name
  * description 
  * holdings 
  * date
* **Relationships:**
  * One-to-One with Users: As depicted in the ERD, each portfolio belongs to a single user. This relationship is represented by the foreign key userID in the portfolios table, linking to the primary key userID in the Users table.
  * One-to-Many with OwnedAssets: The ERD illustrates that each portfolio can have multiple owned assets. This relationship is established by the foreign key portfolioID in the ownedAssets table, referencing the primary key portfolioID in the Portfolios table.
  * One-to-Many with Transactions: As shown in the ERD, each portfolio can have multiple transactions. This relationship is indicated by the foreign key portfolioID in the transactions table, linking to the primary key portfolioID in the Portfolios table.

<br>

#### OwnedAssets Table:
* **Attributes:** 
  * ID (primary key) 
  * assetID (foreign key) 
  * portfolioID (foreign key) 
  * symbol 
  * name 
  * quantity 
  * price
* **Relationships:**
  * Many-to-One with Portfolios: As visualized in the ERD, each owned asset belongs to a single portfolio. This relationship is represented by the foreign key portfolioID in the ownedAssets table, referencing the primary key portfolioID in the Portfolios table.
  * Many-to-One with Assets: As shown in the ERD, each owned asset can only belong to one Asset. This relationship is indicated by the foreign key assetID in the ownedAssets table, linking to the primary key assetID in the Assets table.

<br>

#### Transactions Table:
* **Attributes:** transactionsID (primary key), portfolioID (foreign key), assetID (foreign key), transactionType, quantity, price, totalCost, date.
* **Relationships:**
  * Many-to-One with Portfolios: The ERD illustrates that each transaction belongs to a single portfolio. This relationship is indicated by the foreign key portfolioID in the transactions table, linking to the primary key portfolioID in the Portfolios table.
  * Many-to-One with Assets: As depicted in the ERD, each transaction involves a single asset. This relationship is established by the foreign key assetID in the transactions table, referencing the primary key assetID in the Assets table.

<br>

#### Assets Table:
* **Attributes:** assetID (primary key), marketCapPos, symbol, name, price.
* **Relationships:**
  * One-to-Many with Transactions: Visualized in the ERD, each asset can be involved in multiple transactions. This relationship is indicated by the foreign key assetID in the transactions table, linking to the primary key assetID in the Assets table.
  * One-to-Many with OwnedAssets: As shown in the ERD, each asset can be owned by multiple portfolios. This relationship is established by the foreign key assetID in the ownedAssets table, referencing the primary key assetID in the Assets table.

<br>

#### Discussion:

The ERD visually represents the connections between tables in the portfolio tracker database schema. Each relationship depicted in the ERD corresponds to a foreign key constraint in the database tables, ensuring data integrity and coherence.

For example, the ERD illustrates the one-to-many relationship between Portfolios and ownedAssets tables, with the foreign key portfolioID in the ownedAssets table referencing the primary key portfolioID in the Portfolios table. Similarly, the ERD depicts the many-to-one relationship between Transactions and Portfolios, where the foreign key portfolioID in the Transactions table links to the primary key portfolioID in the Portfolios table.

Overall, the ERD serves as a blueprint for designing and understanding the database relations implemented in the portfolio tracker API application, facilitating effective data management and query operations.

<br>
<br>
<br>

## R10 Describe the way tasks are allocated and tracked in your project

In the <b>Portfolio tracker API</b> project, task allocation and tracking are streamlined through the use of Trello, a project management tool that facilitates clear visualization of the project timeline and responsibilities. Here's how it's structured:

#### Trello Board Setup: 
<img src="./">
I have set up a Trello board specifically for this project, divided into three lists that correspond to the three weeks of the project timeline. Each list represents a week, ensuring tasks are organized according to the timeframe in which they need to be completed.

#### Weekly Lists and Daily Cards: 
Within each weekly list, I have created cards that represent specific tasks or activities to be undertaken on particular days. These cards detail what needs to be done, and any relevant deadlines. This structure allows for a day-by-day breakdown of the project's progress.

#### Tracking Progress: 
Task's are sorted directly on Trello by using checklist's on cards with status's from "To Do" to "In Progress" and finally to "Done" as I complete their activities. This visual progression allows me to monitor the project's advancement in real-time and identify any areas that may require additional focus.

#### Adapting to Changes: 
Given the tight timeline, flexibility is crucial. The Trello board is reviewed and updated to reflect any changes in priorities or task allocations. This agile approach enables me to respond quickly to unforeseen challenges or adjustments in the project scope.

#### Summary:
By utilizing Trello in this structured yet flexible manner, I maintain a clear overview of the project's progress, ensure tasks are completed efficiently. This methodical approach to task alocation and tracking is instrumental in keeping the project on track within the constrained three-week timeframe.