# Проект магазин на FastAPI

# Генерация приватного секретного ключа

>

    openssl genrsa -out jwt-private.pem 2048

# Генерация открытого секретного ключа

>

    openssl rsa -in jwt-private.pem -pubout -out jwt-public.pem
