#!/usr/bin/env python3
import os
# Обновление системы
os.system('sudo yum update -y')

# Установка необходимых зависимостей
os.system('sudo yum install -y yum-utils device-mapper-persistent-data lvm2')

# Устанавливаем официальный репозиторий Docker
os.system('sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')

# Устанавливаем Docker
os.system('sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin')

# Запускаем сервис Docker
os.system('sudo systemctl start docker')
os.system('sudo systemctl enable docker')

# Создание сети
os.system('docker network create --subnet 172.20.0.0/16 --ip-range 172.20.240.0/20 postgres')

# Запуск docker-postgres:14
os.system('sudo docker-compose up -d')

print("Установка Docker и PostgreSQL прошла успешно!")
