import http.server
import socketserver

PORT = 8000

# HTML content for the Valentine page
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Be My Valentine?</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background-color: #ffe6f0;
      text-align: center;
      padding-top: 100px;
    }
    h1 {
      color: #d6336c;
      font-size: 2.5em;
    }
    .buttons {
      margin-top: 40px;
    }
    button {
      font-size: 1.2em;
      padding: 10px 20px;
      margin: 10px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      transition: all 0.3s ease;
    }
    #yesBtn {
      background-color: #ff6699;
      color: white;
    }
    #noBtn {
      background-color: #cccccc;
      color: black;
      position: absolute;
    }
  </style>
</head>
<body>
  <h1>Will you be my Valentine?</h1>
  <div class="buttons">
    <button id="yesBtn">Yes 💖</button>
    <button id="noBtn">No 😢</button>
  </div>

  <script>
    const noBtn = document.getElementById('noBtn');
    const yesBtn = document.getElementById('yesBtn');

    noBtn.addEventListener('mouseover', () => {
      const x = Math.random() * (window.innerWidth - noBtn.offsetWidth);
      const y = Math.random() * (window.innerHeight - noBtn.offsetHeight);
      noBtn.style.left = `${x}px`;
      noBtn.style.top = `${y}px`;
    });

    yesBtn.addEventListener('click', () => {
      alert("Yay! Happy Valentine's Day! 💘 You're the sweetest!");
    });
  </script>
</body>
</html>
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving Valentine page at http://localhost:{PORT}")
    httpd.serve_forever()
