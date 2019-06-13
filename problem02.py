s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

start = 0
while True:
    start = s.find('<',start)
    if start==-1:
        break
    end = s.find('>')
    if end!=-1:
        s = s[:start]+s[end+1:]
    else:
        end+=1

print(s)