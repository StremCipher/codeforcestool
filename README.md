# all about flask api and deploying ml model with flask api on heroku
- this is flask project to host ml model on heroku and i am using this app for 
- this is fully workin app to featch ml model as api 
codeforcestool project
*how to create flask project*
- for ubuntu
  - first install virtualenv using command pip install virtualenv you can run this command on simply opening terminal anytwhere

  - then create the project folder then open terminal there and run command virtualenv env then a new folder will auto created
  - now install flask at the same directory using pip install flask
  - now cd to  env ->bin in newly created folder
  - run command source activate to deactivate just run deactivate
  - activate simply start a virtual server as like in django python manage.py runserver do
  thats it
  - now cd to folder where app.py is present to start the app run touch app_name.py
  then flask run
- this is tutorial program how to create a flask  app and how to use flas to deploy a machine learning model on heroku
- now to deploy flask app on heroku you need to add requirments.txt Procfile
  - procfile contains : web: gunicorn my_webapp:flask_app --log-file=- where my_webapp is the default app that we want to run on heruko as main function and flask_app is the name that we give in my_webapp.py flask_app=Flask(__name__)
