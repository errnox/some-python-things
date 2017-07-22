import subprocess
import os

class Sub(object):
    def __init__(self):
        pass

    def subprocessTest(self):
        cmd = ['ls', '-l', ]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        for line in process.stdout:
            print line
        process.wait()
        print process.returncode

    def subprocessTest1(self):
        subprocess.call(["ls", "-l", "$HOME"])

    def osTest(self):
        os.system('echo -e "\033[0;32mThis is a test.\033[m"')

    def subprocessTest2(self):
        print subprocess.Popen("ls -l $HOME", stdout=subprocess.PIPE, shell=True).stdout.read()

    def osTest1(self):
        output = os.popen("ls -l $HOME") # File-like object
        for line in output:              # Operations on the file-like object
            print line.rstrip()


if __name__ == '__main__':
    sub = Sub()
    # sub.subprocessTest()
    # sub.subprocessTest1()
    # sub.subprocessTest2()
    # sub.osTest()
    # sub.osTest1()
