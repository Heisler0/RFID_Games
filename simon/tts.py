import subprocess,os

FNULL = open(os.devnull, 'w')

def speak(output):
  subprocess.call(["/usr/bin/say", output], stdout=FNULL, stderr=subprocess.STDOUT)

