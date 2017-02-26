# Node Js Application

Install Nodejs on your machine "https://nodejs.org/en/download/" or "https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions"

Use the following steps

  -  execute "npm install express express-generator -g"
  -  execute "express ExpressSite -hbs"
  -  execute "cd ExpressSite && npm install"
  -  To test execute "npm start" and open "http://localhost:3000/" in browser  


# Creating Container For the following application

  - pull node image by executing "docker pull node"
  - Now we need to have the ExpressSite Folder to be available to the docker container. 
  - We do this by volume mapping and use following command 
  -     docker run -p 8081:3000 -v $(pwd):/var/www -w "/var/www" node npm start

