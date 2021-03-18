FROM cccs/assemblyline-v4-service-base:latest

ENV SERVICE_PATH windowsdefender.WindowsDefender

USER root

RUN dpkg --add-architecture i386 && apt-get update && apt-get -y install libc6-dev-i386 gcc-multilib cabextract libimage-exiftool-perl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip3 install --no-cache-dir --user -r requirements.txt && rm -rf ~/.cache/pip

USER assemblyline

WORKDIR /opt/al_service
COPY . .



