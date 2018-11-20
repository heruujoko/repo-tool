import urllib, json
import subprocess
import time
from pprint import pprint

#commit
# url = "https://jsonplaceholder.typicode.com/posts"
# response = urllib.urlopen(url)
# data = json.loads(response.read())
# print data[0]['body']

# tag the commit
# subprocess.call(["ls", "-l"])

# bump version
def bump_version():
    with open('package.json') as data_file:
        data = json.load(data_file)
    version = data['version']
    version_arr = version.split('.')
    new_version = version_arr[0] +"."+ str(int(version_arr[1]) +1) +"."+ version_arr[2]

    # Safely read the input filename using 'with'
    filename = 'package.json'
    with open(filename) as f:
        s = f.read()
        if version not in s:
            print '"{version}" not found in {filename}.'.format(**locals())
            return
        else:
            print '"{version}" found in {filename}.'.format(**locals())
            # Safely write the changed content, if found in the file
            with open(filename, 'w') as f:
                print 'Bumping version "{version}" to "{new_version}" in {filename}'.format(**locals())
                s = s.replace(version, new_version)
                f.write(s)
        
        time.sleep(1)
        tag_new_version(new_version)    


def tag_new_version(new_version):
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "#bump version"])
    subprocess.call(["git", "tag", "v"+str(new_version)])

bump_version()