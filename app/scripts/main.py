import hvac
import os

# Получаем путь до файла с токеном из env (APPROLE_UNWRAPPEN_TOKEN_FILE)
token_file = os.getenv('APPROLE_UNWRAPPEN_TOKEN_FILE')
# Читаем файл и записываем в переменную t
t=open(token_file, "r").read()

# Получаем url vault из env (APPROLE_VAULT_ADDR)
u=os.getenv('APPROLE_VAULT_ADDR')

# Получаем mount_point секрета из env (APPROLE_SECRET_MOUNT_POINT)
mp=os.getenv('APPROLE_SECRET_MOUNT_POINT')

# Получаем path секрета из env (APPROLE_SECRET_PATH)
p=os.getenv('APPROLE_SECRET_PATH')

client = hvac.Client(
  url=u,
  token=t
)

result=client.secrets.kv.v2.read_secret_version(
  mount_point=mp,
  path=p
)

print(result["data"]["data"]["responseText"])