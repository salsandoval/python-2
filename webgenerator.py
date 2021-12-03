import webbrowser

f = open('Staytunedforouramazingsummersale.html', 'w')

message = """<html>
<head></head>
<body><p>Stay tuned for our amazing summer sale!</p></body>
</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab('Staytunedforouramazingsummersale.html')
