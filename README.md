# EC-1307-Data-communication-and-networking

## Lets run the code first:
- Install all dependencies:
    
    > pip install -r requirements.txt

## Running Different part of code

Open Command prompt or terminal in the Parent Directory 

###### For HTTP Server
run the file using the following command 
    > python HTTP_server/main.py
    Go to any of your browser and type url "http://localhost:3000/{filename}" where filename is the name of json file inside "JSON_data" directory for which you want to perform the GET request

    Ex. python server.py
        http://localhost:3000/pet_names

###### For FTP Server
    The directory is used to imitate some remote server and client is used to imitate a client system
    Run two different instances of command prompt
    In one of them move to the server directory and run "python server.py"
    In other one move to client directory and execute command in following manner
        python client.py "path of file to be uploaded relative to client" "path where file has to be uploaded relative to server" u
        this will upload the file from client to server

        python client.py "path of file to be downloaded" "path where file has to be downloaded" d
        this will download file from server to client
    
    Example
        python client.py ./uploads/pet_names ./new_file d
        this will download pet_names file in /server/uploads with name "new_file" to client

###### For SMTP Server:
    Again run two different ionstances of command prompt and run server in one of them
    Now if you want to send mail from your gmail account run following command
        python client.py your_mail_id your_password recepients_mail_id subject_of_mail body_of_mail
        For this to work make sure to enable "Access for less secure apps" on your google account
    Or you can send mail to our custom server by following command
        python client.py your_mail_id recepients_mail_id subject_of_mail body_of_mail
        and you will be able to see recieved mail in command prompt where server is running

###### For SNTP Server
    Simply run client.py and it will return synchronized time
 10:44 05-07-2020

###### For DNS
    run following command
    python main.py websitename
    website name can be the url of any website

