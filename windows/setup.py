
# run docker on windows

# open power shell and run the following command lines


# first time installation

# Install-Module -Name DockerMsftProvider -Repository PSGallery -Force
# Install-Package -Name docker -ProviderName DockerMsftProvider
# Restart-Computer -Force
# Get-Package -Name Docker -ProviderName DockerMsftProvider


# steps docker for future docker software uprades

# Install-Package -Name Docker -ProviderName DockerMsftProvider -Update -Force
# Start-Service Docker



# references

# original link - https://computingforgeeks.com/how-to-run-docker-containers-on-windows-server-2019/


# install docker compose
# Start-BitsTransfer -Source "https://github.com/docker/compose/releases/download/v2.16.0/docker-compose-Windows-x86_64.exe" -Destination $Env:ProgramFiles\Docker\docker-compose.exe
# docker-compose version
