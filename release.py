import urllib, json
import subprocess
import time
import sys, getopt
import argparse

#commit
# url = "https://jsonplaceholder.typicode.com/posts"
# response = urllib.urlopen(url)
# data = json.loads(response.read())
# print data[0]['body']

# tag the commit
# subprocess.call(["ls", "-l"])

# bump version
def bump_version(type):
    with open('package.json') as data_file:
        data = json.load(data_file)
    version = data['version']
    version_arr = version.split('.')
    if type == 'minor':
        new_version = version_arr[0] +"."+ str(int(version_arr[1]) +1) +"."+ version_arr[2]
    else:
        new_version = str(int(version_arr[0])+1) + "." + version_arr[1] + "." + version_arr[2]

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

def parse_args():
   releasetype = 'minor'
   parser = argparse.ArgumentParser()
   parser.add_argument('-major', '--major', dest='major', action='store_true')
   parser.add_argument('-minor', '--minor', dest='minor', action='store_true')
   args = parser.parse_args()

   if args.major:
       releasetype = 'major'
   elif args.minor:
       releasetype = 'minor'

   print "releasing in "+releasetype+" release..."
   bump_version(releasetype)

if __name__ == "__main__":
   parse_args()


