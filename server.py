import subprocess
from flask import Flask, request
import page.work
import page.sound
app = Flask(__name__)
port = 3000
@app.route('/api/frame/<int:id>')
def get_frame(id):
    try:
        a = page.work.load(int(id))
        if id == 0:
            page.sound.play()
        return str(a)
    except subprocess.CalledProcessError as e:
        return e.stderr.decode()
if __name__ == '__main__':
    app.run(port=port)