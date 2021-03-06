# EC-1307-Data-communication-and-networking

## Lets run the code first:
- Install all dependencies:
    
    > pip install -r requirements.txt

## Running Different part of code

Open Command prompt or terminal in the Parent Directory 

### For HTTP Server
*Run the file using the following command*

    python HTTP_server/main.py
    
Go to any of your browser and type url http://localhost:3000/{filename} where filename is the name of json file inside "JSON_data" directory for which you want to perform the GET request
    
    Ex. http://localhost:3000/team_members.json

### For FTP Server
This is used to imitate some remote server and client is used to imitate a client system

*Run two different instances of command prompt*
- In one of them run

    > python FTP/server/server.py

- In other one execute command in following manner 
  - For uploading
        
        python FTP/client/client.py "path of file to be uploaded relative to client" "path where file has to be uploaded relative to server" u
        this will upload the file from client to server
    Example
        
    > python FTP/client/client.py "./JSON_data/team_members.json" "./FTP/server/uploads/uploadedFile.json" u
    
    this will upload team_members file in /FTP/server/uploads with name "uploadedFile.json"
   
  - For Downloading
  
        python FTP/client/client.py "path of file to be downloaded" "path where file has to be downloaded" d
        this will download file from server to client
    
    Example
        
    > python FTP/client/client.py "./JSON_data/team_members.json" "./FTP/client/downloads/downloadedFile.json" d
    
     this will download team_members file in /FTP/client/downloads with name "downloadedFile.json" 

### For SMTP Server:
*Run two different instances of command prompt*
- In one of them run

    > python SMTP/server.py
    
- In other one Execute the following Command
    
        python client.py your_mail_id recepients_mail_id subject_of_mail body_of_mail
        this will send message from one end to another

    Example
    
   > python SMTP/client.py "sender@text.com" "reciever@test.com" "TEXT" "THIS IS A DUMMY TEXT"

### For SNTP Server
*Simply run following command*

   > python SNTP/main.py        

It will return synchronized time

### For SNMP
First Enable the device to follow SNMP protocols, then

*Simply run the following command*

If on a public network run
        
        python SNMP/main.py 
        
   Example
   
   > python SNMP/main.py 


If on a password protected network run
        
        python SNMP/main.py "password"
        
   Example
   
   > python SNMP/main.py "THIS IS A DUMMY PASSWORD"


### For DNS
*Run following command*
    
    python DNS/main.py "websitename"
    website name can be the url of any website
  
   Example
   
   > python DNS/main.py "www.youtube.com"
