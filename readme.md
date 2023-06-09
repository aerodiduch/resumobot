
# ResumoBot

Un pequeño bot que conecta Discord con OpenAI pensado para generar un resumen de las conversaciones que ocurren en los canales de un servidor.

# Prerequisitos
Actualmente este bot no está hosteado en ninguna plataforma, por lo cual para 
agregarlo a cualquier servidor, debe ser buildeado en origen y cumplir con las siguientes condiciones:

- API KEY de OpenAI (servicio de pago) **[DOCUMENTACION PENDIENTE]**
- API KEY de Discord (servicio gratuito) **[DOCUMENTACION PENDIENTE]**

# Instalación

Una obtenida ambas API KEYs, podemos ejecutar iniciarlizar el bot de forma local.
Este proyecto utiliza **entorno virtual de venv** para aislar el bot de las demas dependencias del sistema. 

## Linux
```bash
git clone https://github.com/aerodiduch/ResumoBot.git && cd $_
python3 -m venv venv
source venv/bin/activate && pip install -r requirements.txt
```

Luego, ejecutamos nuestro editor de texto favorito para popular los campos `TOKEN` y `openai.api_key`. Hecho esto, ejecutamos el bot.

```
python3 main.py
```

Output:

```sh
❯ python main.py
2023-06-08 23:15:24 INFO     discord.client logging in using static token
2023-06-08 23:15:26 INFO     discord.gateway Shard ID None has connected to Gateway (Session ID: XXXX).
MiBotCool#XXXX has connected to Discord!
```

# Utilización

Para poder darle uso a este bot, simplemente tenemos que etiquetarlo en el canal que deseamos generar un resumen. Luego de unos segundos cuando sea satisfcatoria la llamada a OpenAI, obtendremos el resumen.


# WIP
Este proyecto es un Work In Progress, por lo cual estará sujeto a modificaciones constantes con el objetivo de mejorar la experiencia del usuario

Futuro:
- Dockerizacion del proyecto
- Documentacion de generación de llaves de Discord (tutorial de bot)
- Documentación de generación de llaves de OpenAI