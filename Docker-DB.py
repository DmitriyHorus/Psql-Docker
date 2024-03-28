#!/usr/bin/env python3
import os
# Обновление системы
os.system('sudo yum update -y')

# Установка необходимых зависимостей
os.system('sudo yum install -y yum-utils device-mapper-persistent-data lvm2')

# Устанавливаем официальный репозиторий Docker
os.system('sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')

# Устанавливаем Docker
os.system('sudo yum install docker-ce')

# Запускаем сервис Docker
os.system('sudo systemctl start docker')
os.system('sudo systemctl enable docker')
print("Установка Docker и PostgreSQL прошла успешно!")
