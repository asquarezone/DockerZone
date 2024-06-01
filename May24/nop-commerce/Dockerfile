FROM mcr.microsoft.com/dotnet/sdk:8.0
LABEL AUTHOR="shaikkhajaibrahim"
# installing unzip
RUN apt update 
RUN apt install unzip -y 
RUN mkdir /app
WORKDIR /app
ARG DOWNLOAD_URL="https://github.com/nopSolutions/nopCommerce/releases/download/release-4.70.1/nopCommerce_4.70.1_NoSource_linux_x64.zip"
# Downloading a file from internet
ADD ${DOWNLOAD_URL} /app/
EXPOSE 5000
# unzip the file and add bin and logs folder
RUN unzip nopCommerce_4.70.1_NoSource_linux_x64.zip && mkdir bin && mkdir logs
CMD ["dotnet", "Nop.Web.dll", "--urls", "http://0.0.0.0:5000" ]
