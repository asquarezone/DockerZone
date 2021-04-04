FROM ubuntu:20.04 as builder
RUN apt update && apt install unzip -y
ADD https://github.com/nopSolutions/nopCommerce/releases/download/release-4.40.2/nopCommerce_4.40.2_NoSource_linux_x64.zip /nop/nopCommerce_4.40.2_NoSource_linux_x64.zip
RUN cd nop && unzip nopCommerce_4.40.2_NoSource_linux_x64.zip && rm nopCommerce_4.40.2_NoSource_linux_x64.zip

FROM mcr.microsoft.com/dotnet/aspnet:5.0
LABEL author="Khaja Ibrahim"
LABEL organization="qualitythought"
COPY --from=builder /nop /nop-bin
WORKDIR /nop-bin
EXPOSE 80
CMD [ "dotnet", "/nop-bin/Nop.Web.dll" ]