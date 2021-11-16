# This is a Githb Repo for the APIs of the Terms and Consitions Project

## For this API to run you have to setup Django and Django Rest Framework environment in your system

### To run this project first clone this project to your local directory from my github account by typing
  `git clone https://github.com/Juned-the-programmer/Terms-API.git`
  
 ### After cloning the project the first thing you have to do is that setup environemnt and install everything required to run the project
    pip3 install -r requirements.txt
    
 ### The one thing is required to run this project is that you have to setup the **tessaract** in your system
    sudo dnf install tessaract
    
 ### After that run the Django project by typing the
    python3 manage.py runserver
    
### When you will run this project the base URL will show you the error because we have not setuped the base URL in this project instead of that we have used
  `/api/text_extract/`    To Extract the text from the image 
  `/api/text_process/`    To Process the text to generate the output
  
  
# You can visit that site from [here](https://termsconditionsapi.herokuapp.com/)
> When you visit this URL you will get the error page after loading that

`/api/text_extract` [Here To Extract text](https://termsconditionsapi.herokuapp.com/api/text_extract/)

### When you visit this URL you have to give input as the image and the request for this is POST

`api/text_process/` [Here To Process text](https://termsconditionsapi.herokuapp.com/api/text_process/)

### When you visit this URL you have to give the text as a input and it will generate the output
