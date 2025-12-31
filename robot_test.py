from flask import Flask, request, render_template_string
from gpiozero import Motor

# Motors setup (update pins if needed)
motor_left = Motor(forward=17, backward=18)
motor_right = Motor(forward=22, backward=23)

# Flask server
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
    dir = request.args.get('dir')
    if dir == 'forward':
        motor_left.forward(0.6)
        motor_right.forward(0.6)
    elif dir == 'backward':
        motor_left.backward(0.6)
        motor_right.backward(0.6)
    elif dir == 'left':
        motor_left.forward(0.6)
        motor_right.stop()
    elif dir == 'right':
        motor_left.stop()
        motor_right.forward(0.6)
    elif dir == 'stop':
        motor_left.stop()
        motor_right.stop()
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
