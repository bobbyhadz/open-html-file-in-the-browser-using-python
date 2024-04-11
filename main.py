# How to open an HTML file in the Browser using Python 

import webbrowser

file_path = 'index.html'

html_string = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
  </head>
  <body>
    <h2>bobbyhadz.com</h2>

    <h2 style="background-color: lime;">google.com</h2>
  </body>
</html>
"""

with open(file_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html_string)

webbrowser.open_new_tab(file_path)
