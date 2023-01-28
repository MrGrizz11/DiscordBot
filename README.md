<h2>Bot commands</h2>

<h3 align=center><code>[Translator]</code></h3>

>\>sl - change the language of the source text<br>
```- ex: >sl ru```<br>
```- ex: >sl russian```<br>
<br>

>\>dl - change the destination language<br>
```- ex: >dl ro```<br>
```- ex: >dl romanian```<br>
<br>

>\>lang - displays all available languages<br>
<br>

>\>t - translates the following text<br>
```ex: >t translate this text```<br>

<h3 align=center><code>[Counter]</code></h3>

>\>cnt (number) - counting up to (number)<br>
```- ex: >cnt 69```<br>
<br>

>\>stopcnt - to force stop the counter<br>
<br>


<h2>Installation</h2><br>

1\) <a href="https://discordpy.readthedocs.io/en/stable/discord.html" target="_blank">Create your own Discord Bot</a><br>
2\) <a href="https://github.com/MrGrizz11/DiscordBot/archive/refs/heads/main.zip">Download and extract the repository</a><br>
3\) Open a terminal, go to repository directory and type:

```terminal
pip install -r requirements.txt
```
<br>
<h2>Configure</h2><br>

1\) Open ```const.py``` file in your <b>IDE</b> and put the **TOKEN** of your bot in there
```python
TOKEN = "your token here"
```

<br>
<h2>Other</h2><br>

```css
Warning:
 - googletrans python module has some whims and the only version that works is "googletrans==4.0.0-rc1"
 - this project was made with python 3.10 and pip 21.3.1
 ```
