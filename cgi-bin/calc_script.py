import cgi

HTML_PAGE = """Content-type: text/html charset=utf-8\n\n
<html>
<head> <meta charset="utf-8"></head>
<style>
input.button4 {{
  position: relative;
  display: inline-block;
  font-family: Arial,Helvetica,FreeSans,"Liberation Sans","Nimbus Sans L",sans-serif;
  font-size: 1.5em;
  font-weight: 700;
  color: rgb(245,245,245);
  text-shadow: 0 -1px rgba(0,0,0,.1);
  text-decoration: none;
  user-select: none;
  padding: .3em 1em;
  outline: none;
  border: none;
  border-radius: 3px;
  background: #0c9c0d linear-gradient(#82d18d, #0c9c0d);
  box-shadow: inset #72de26 0 -1px 1px, inset 0 1px 1px #98ff98, #3caa3c 0 0 0 1px, rgba(0,0,0,.3) 0 2px 5px;
  -webkit-animation: pulsate 1.2s linear infinite;
  animation: pulsate 1.2s linear infinite;
}}
input.button4:hover {{
  -webkit-animation-play-state: paused;
  animation-play-state: paused;
  cursor: pointer;
}}
input.button4:active {{
  top: 1px;
  color: #fff;
  text-shadow: 0 -1px rgba(0,0,0,.3), 0 0 5px #ffd, 0 0 8px #fff;
  box-shadow: 0 -1px 3px rgba(0,0,0,.3), 0 1px 1px #fff, inset 0 1px 2px rgba(0,0,0,.8), inset 0 -1px 0 rgba(0,0,0,.05);
}}
@-webkit-keyframes pulsate {{
  50% {{color: #fff; text-shadow: 0 -1px rgba(0,0,0,.3), 0 0 5px #ffd, 0 0 8px #fff;}}
}}
@keyframes pulsate {{
  50% {{color: #fff; text-shadow: 0 -1px rgba(0,0,0,.3), 0 0 5px #ffd, 0 0 8px #fff;}}
}}</style>
<style>
  body {{
    background: url(../images/image_toys.jpg) no-repeat;
    -webkit-background-size: 100%;
   }}
</style>
	<title>Магазин іграшок</title>
	<body>
	<form method=POST action="http://localhost:8000/cgi-bin/show_toys.py">
		<center><input type="submit" class="button4" value="{}"></center>
	</form>
	<form method=POST action="http://localhost:8000/cgi-bin/add_toy.py">
		<center><input type="submit" class="button4" value="{}"></center>
	</form>
	{}
	</body>
</html>
"""

print(HTML_PAGE)
