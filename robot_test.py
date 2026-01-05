from flask import Flask, request, render_template_string
from gpiozero import CamJamKitRobot

# Robot set up 
robot = CamJamKitRobot()

app = Flask(__name__)

HTML = """
<html>
<head>
<title>CamJam Robot Control</title>
<style>
body { font-family: sans-serif; text-align: center; }
button { width: 100px; height: 100px; margin: 10px; font-size: 20px; border-radius: 20px; }
.grid { display: grid; grid-template-columns: 120px 120px 120px; justify-content: center; align-items: center; }
</style>
<script>
function send(dir) { fetch('/action?dir=' + dir); }
</script>
</head>
<body>
<h2>CamJam Robot Control</h2>
<div class="grid">
  <div></div><button onclick="send('forward')">up</button><div></div>
  <button onclick="send('left')">left</button>
  <button onclick="send('stop')">stop</button>
  <button onclick="send('right')">right</button>
  <div></div><button onclick="send('backward')">back</button><div></div>
</div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/action')
def action():
    direction = request.args.get('dir')
    speed = 0.6

    if direction == 'forward':
        robot.forward(speed)
    elif direction == 'backward':
        robot.backward(speed)
    elif direction == 'left':
        robot.left(speed)
    elif direction == 'right':
        robot.right(speed)
    elif direction == 'stop':
        robot.stop()

    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
