FROM mcr.microsoft.com/dotnet/aspnet:8.0
LABEL AUTHOR="shaikkhajaibrahim"
RUN useradd -d /app -m -s /bin/bash  nop
USER nop
WORKDIR /app
COPY --chown=nop:nop app/ /app
EXPOSE 5000
CMD ["dotnet", "Nop.Web.dll", "--urls", "http://0.0.0.0:5000" ]
