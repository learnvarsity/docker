
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
