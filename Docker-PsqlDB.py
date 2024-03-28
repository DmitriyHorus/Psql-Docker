#!/usr/bin/env python3

# Импортируем необходимые модули
import subprocess
import time

# Обновляем список пакетов
subprocess.run(["sudo", "yum", "update"])

# Устанавливаем Docker
subprocess.run(["sudo", "yum", "install", "docker"])

# Запускаем Docker
subprocess.run(["sudo", "systemctl", "start", "docker"])

# Скачиваем образ PostgreSQL
subprocess.run(["docker", "pull", "postgres"])

# Запускаем контейнер PostgreSQL
subprocess.run(["docker", "run", "-d", "-p", "5432:5432", "postgres"])

# Ждем, пока PostgreSQL запустится
time.sleep(5)

# Создаем пользователя postgres
subprocess.run(["docker", "exec", "-it", "postgres", "psql", "-c", "CREATE USER postgres WITH PASSWORD 'postgres';"])

# Создаем базу данных my_database
subprocess.run(["docker", "exec", "-it", "postgres", "psql", "-c", "CREATE DATABASE my_database;"])

# Подключаемся к базе данных my_database
subprocess.run(["docker", "exec", "-it", "postgres", "psql", "-U", "postgres", "-d", "my_database"])

# Выводим информацию о базе данных
subprocess.run(["docker", "exec", "-it", "postgres", "psql", "-U", "postgres", "-d", "my_database", "-c", "\d"])

# Закрываем соединение с базой данных
subprocess.run(["docker", "exec", "-it", "postgres", "psql", "-U", "postgres", "-d", "my_database", "-c", "\q"])

# Останавливаем контейнер PostgreSQL
#subprocess.run(["docker", "stop", "postgres"])

# Удаляем контейнер PostgreSQL
#subprocess.run(["docker", "rm", "postgres"])

# Выводим сообщение об успешном завершении
print("Установка Docker и PostgreSQL прошла успешно!")
