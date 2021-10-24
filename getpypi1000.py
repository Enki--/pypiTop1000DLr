import subprocess
import json

curlCmd = ['curl', 'https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.min.json', '-o' '/tmp/pypi-packages.json']
subprocess.run(curlCmd)

with open("/tmp/pypi-packages.json", "r") as packages:
    data= json.load(packages)
    #print(data)
    for row in data['rows']:
        pipDLCmd = ['pip', 'download', '-d', '/var/www/packages', '--progress-bar', 'pretty', row["project"]]
        subprocess.run(pipDLCmd)
        print(row["project"])
