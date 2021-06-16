FROM cccs/assemblyline-v4-service-base:latest

ENV SERVICE_PATH windowsdefender.WindowsDefender

USER root

RUN dpkg --add-architecture i386 && apt-get update && apt-get -y install libc6-dev-i386 gcc-multilib cabextract libimage-exiftool-perl && rm -rf /var/lib/apt/lists/*

RUN pip3 install tqdm beautifulsoup4 utils

USER assemblyline

WORKDIR /opt/al_service
COPY . .



