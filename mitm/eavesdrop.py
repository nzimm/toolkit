#!/usr/bin/env python3
import subprocess
proc = subprocess.Popen(['tshark', '-i', 'lo', '-T', 'fields', '-e', 'data'], stdout=subprocess.PIPE)
try:
    outs, errs = proc.communicate(timeout=1)
except subprocess.TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()
