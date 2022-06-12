FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY pySigmaService.csproj .
RUN dotnet restore
COPY . .
RUN dotnet publish -c release -o /app

FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build /app .
ENV ASPNETCORE_URLS=http://+:80
ENTRYPOINT ["dotnet", "pySigmaService.dll"]
EXPOSE 80
