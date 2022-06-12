FROM mcr.microsoft.com/dotnet/aspnet:6.0-focal AS base
WORKDIR /app
EXPOSE 8000

ENV ASPNETCORE_URLS=http://+:8000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-dotnet-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

FROM mcr.microsoft.com/dotnet/sdk:6.0-focal AS build
WORKDIR /src
COPY ["microservices/pySigmaService/pySigmaService.csproj", "microservices/pySigmaService/"]
RUN dotnet restore "microservices/pySigmaService/pySigmaService.csproj"
COPY . .
WORKDIR "/src/microservices/pySigmaService"
RUN dotnet build "pySigmaService.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "pySigmaService.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "pySigmaService.dll"]
