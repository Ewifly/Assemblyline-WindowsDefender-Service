FROM cccs/assemblyline-v4-service-base:latest

ENV SERVICE_PATH windowsdefender.WindowsDefender

USER root

RUN dpkg --add-architecture i386 && apt-get update && apt-get -y install libc6-dev-i386 gcc-multilib cabextract libimage-exiftool-perl
COPY requirements.txt .

RUN pip3 install -r requirements.txt 

# Switch to assemblyline user
USER assemblyline

# Copy ResultSample service code
WORKDIR /opt/al_service
COPY . .



