from PIL import Image

obj = Image.open("little_pig.jpg")

obj.thumbnail((127, 127), Image.BILINEAR)  # 可调整大小 #极小的东西
obj.save("little_pig.ico")
print(obj.size)

import subprocess

res = subprocess.getoutput("ls -l")

res = subprocess.Popen("ls -l", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
res.stdout.read().decode(encoding="utf-8")
res.stdout.close()