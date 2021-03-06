import os, time
from portage_data import portage_uid, portage_gid
from portage_util import ensure_dirs

def process(mysettings, cpv, logentries, fulltext):
	cpv_path = cpv.replace("/", ":")

	if mysettings["PORT_LOGDIR"] != "":
		elogdir = os.path.join(mysettings["PORT_LOGDIR"], "elog")
	else:
		elogdir = os.path.join(os.sep, "var", "log", "portage", "elog")
	ensure_dirs(elogdir, uid=portage_uid, gid=portage_gid, mode=02770)

	elogfilename = elogdir+"/"+cpv_path+":"+time.strftime("%Y%m%d-%H%M%S", time.gmtime(time.time()))+".log"
	elogfile = open(elogfilename, "w")
	elogfile.write(fulltext)
	elogfile.close()

	return elogfilename
