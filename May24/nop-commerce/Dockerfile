FROM mcr.microsoft.com/dotnet/aspnet:8.0
LABEL AUTHOR="shaikkhajaibrahim"
# installing unzip
RUN mkdir /app
WORKDIR /app
COPY app/ /app
EXPOSE 5000
CMD ["dotnet", "Nop.Web.dll", "--urls", "http://0.0.0.0:5000" ]
