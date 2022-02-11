# Markdown to HTML Interactive Typing Prompt Generator

1. Add a text expansion using [aText](https://www.trankynam.com/atext/)
	- Abbreviation = "imd"
	- Expand: "After typing delimiter ( discard delimiter )"
	- `<span class="interactive-typing-prompt" style="border: 2px solid green">【clipboard】</span>【|】`
2. Then Using typora , or whatever md editor , type document as normal
3. `Ctrl+x` the text you want to be prompted to type
4. Activate text expansion
	- it replaces it with temporary green border around text
4. Run `python3 main.py "/path/to/file.md"`