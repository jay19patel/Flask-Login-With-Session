# Flask-Login-With-Session

![Capture](https://user-images.githubusercontent.com/107461719/224716783-560ccb3b-fb44-4c6c-bbbf-656f3f1f6124.PNG)

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

-------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------
![Capture](https://user-images.githubusercontent.com/107461719/224911529-ad298671-2d6d-458c-95b7-1186344c60ba.PNG)

# Flask-Login System  Using JWT
- setup all step .

## add some configrations 
    app.secret_key = 'jaypateltopsecret789654123'
    app.config["JWT_SECRET_KEY"] =    "jaypateltopsecret789654123" 
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=60) 
    jwt = JWTManager(app)


## Login Page :
 - import flask_jwt_extended
 - add token :
    ```
    access_token = create_access_token(identity='Sallubhai')
    res = redirect(url_for('HomePage'))
    set_access_cookies(res, access_token) 
    session['login_user'] = userdata['name']
    return res
- genrate token uisng identity and encrpt them using jwt
- add redirect function as a veriable 
- create session for chekup 
- return redircet veriable  
## Home Page
- when use authentication token then use 
 ``` 
 @jwt_required() 
```
- check session if session is present then name display on home page  other vise name no dispaplay 

## Test Page :
- add @jwt_required()  and access token using 
```
        data = get_jwt_identity()
        name = data['name']
        ```

## logout
 - delete session id and create blank 
 - in home page if session is not define then redirect Login  page 
 - when login then session create and then we use test other vise not use Test page 






 





 
