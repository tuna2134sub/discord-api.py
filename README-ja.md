# discord-api.py

## 紹介

これはdiscordのbotを簡単に作れるようにしたapiラッパーです。

discord.pyとの大きな違いはuvloopとujsonを使っている違いです。

uvloopは元からある非同期より速いのが特徴です。

ujsonは元からあるjsonより早いのが特徴です。


## 例えば

```python
from discord_api import Client, Command

client = Client(log = False)

client.add_command(Command("ping", "Pong"))

@client.event
async def on_ready():
    print("起動")

@client.event
async def on_interaction(i):
    await i.send("Pong!", True)

client.run("token")
```

## ライセンス

ライセンスは`LICENSE`に書いてあるので、この通りに従ってください。