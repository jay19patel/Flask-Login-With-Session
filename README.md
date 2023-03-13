# Flask-Login-With-Session


# Flask-Login System 
- First install flask and all setup

## connection with flask and mongodb
    client = MongoClient('localhost', 27017) 
    db = client.API # create table
    myapis = db.apis # triger

## Create simple routes for all pages
```
   @app.post('/')
    def Home():
        return "Home page
```
## Cretae html pages 
 - Home 
 - Login 
 - Register Page

## Registration  Page :
 - In Registrtaion function , get data to Registration.html page

    ```data=request.form['data']```

- set data in a variable  
- set some function like password not match or sort or simple psw ...blaa blaa blaa....
- create dabase connection and insert data in to database 
    ``senddata = regapi.insert_one({data})```  

## Login Page :
 - in Login function , get data to Login.html page
    ```data=request.form['data']```
- find data in database using email
    ```userdata=regapi.find_one({'email':email})```
- match password 
- if match then fetch all data to the data base and save in session 

## Home Page
- create simple home page and pass the data and display in home page 







 
