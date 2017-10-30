#!/usr/bin/python
import sys
import jobschedule

def write_stdout(s):
    sys.stdout.write(s)
    sys.stdout.flush()

def write_stderr(s):
    sys.stderr.write(s)
    sys.stderr.flush()

def main(args):

    while True:
        write_stdout('READY\n') # transition from ACKNOWLEDGED to READY

        line = sys.stdin.readline() # wait for event

        # Some debug info
        write_stderr(line) # print it out to stderr
        headers = dict([ x.split(':') for x in line.split() ])
        data = sys.stdin.read(int(headers['len'])) # read the event payload
        write_stderr(data)

        # Run tasks
        jobschedule.schedule.run_pending()

        write_stdout('RESULT 2\nOK') # transition from READY to ACKNOWLEDGED

if __name__ == '__main__':
    main(sys.argv[1:])

