# Generar llaves de OpenAI

En primer lugar debemos tener una cuenta creada para poder acceder a la [plataforma de OpenAI](https://platform.openai.com/account/billing/payment-methods) donde configuraremos una **opcion de pago**, ya que para utilizar la api key necesitamos tener un medio de pago habilitado.

Luego de esto, podemos ir al [panel de las api keys](https://platform.openai.com/account/api-keys) para generar una nueva clave que comenzará con `sk-...`. 

**Esta es la clave que deberemos colocar en el archivo `docker-compose.yaml` como variable de entorno.**