import os, signal
from Logging import logging as log

def kill(pid:int):
    """Terminate a running process"""
    os.kill(pid, signal.SIGSTOP)
    log.info('Kill process {0}'.format(pid))

def sleep(pid:int):
    """Tell a process to sleep"""
    os.waitpid(pid, os.WSTOPPED)
    log.info('Wait process {0}'.format(pid))

def wake(pid:int):
    """Continue a stopped process"""
    os.kill(pid, signal.SIGCONT)
    log.info('Continue process {0}'.format(pid))

def pid() -> int:
    """Get the Process PID"""
    return os.getpid()

def parent_pid() -> int:
    """Get the Parent PID"""
    return os.getppid()

def fork():
    """Create a Child Process"""
    return os.fork()

def sid():
    """Return Session ID"""
    return os.getsid(pid) 
