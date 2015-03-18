import os
import inspect
import time
import sys

from output import turquoise, yellow
from output import EOutput
out = EOutput()

def wytrace():
	if os.getenv("WYDEBUG"):
		stack = inspect.stack()
		for frame in stack:
			filepath_, line_, func_ = frame[1], frame[2], frame[3]
			file_ = os.path.basename(filepath_)
			print "====[(%s)%s:%s %s()]"%(os.getpid(), file_, line_, func_)

def wylog(msg):
	if os.getenv("WYDEBUG"):
		try:
			calling = inspect.stack()[1]
			filepath_, line_, func_ = calling[1], calling[2], calling[3]
			file_ = os.path.basename(filepath_)
		except IndexError, e:
			file_, line_, func_ = ""
		print "==[(%s)%s:%s %s()] %s"%(os.getpid(), file_, line_, func_, msg)

class Lockdir(object):

	def __init__(self, dir_path, name, wait_timeout=60, lock_duration=60):
		"""
		file based lock to protect a portage dir.
		since portage can exit everywhare, lock has a duration
		"""
		self._wait_timeout = wait_timeout
		self._lock_duration = lock_duration
		self._lock = os.path.join(dir_path, name+".LOCK")

	def __delete_lock(self):
		try:
			out.ewarn("Unlocking %s..."%self._lock)
			os.unlink(self._lock)
		except Exception, e:
			sys.stderr.write("!!! Unable to unlink %s: %s"%(self._lock, str(e)))
			sys.exit(1)

	def _get_locked(self):
		if os.path.exists(self._lock):
			ctime = os.path.getctime(self._lock)
			now = time.time()
			wylog("%s exists ctime=%s now=%s"%(self._lock, ctime, now))
			if time.time() - ctime > self._lock_duration:
				wylog("%s timeouted"%(self._lock))
				self.__delete_lock()
				return False
			else:
				f = open(self._lock, 'r')
				pid = f.read()
				f.close()
				return int(pid)
		else:
			wylog("%s does not exists !!"%self._lock)
		return False

	locked = property(_get_locked)

	def lock(self):
		if self.locked:
			return False
		else:
			out.ewarn("Locking %s..."%self._lock)
			f = open(self._lock, 'w')
			f.write("%s"%os.getpid())
			f.close()
			return True

	def unlock(self):
		pid = os.getpid()
		if self.locked == pid:
			self.__delete_lock()

	def waitlock(self):
		loop = 0
		loop_duration = 5
		max_loop = int(self._wait_timeout / loop_duration)
		while loop <= max_loop:
			if self.lock():
				return True
			else:
				if loop == 0:
					out.ewarn("Waiting for %s..."%self._lock)
				wylog("waiting for %s"%self._lock)
				time.sleep(loop_duration)
				loop += 1
		out.ewarn("Waiting too long for %s. exiting."%self._lock)
		return False


