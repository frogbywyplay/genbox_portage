# portage: Constants
# Copyright 1998-2004 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$


# ===========================================================================
# START OF CONSTANTS -- START OF CONSTANTS -- START OF CONSTANTS -- START OF
# ===========================================================================

import os

VDB_PATH                = "var/db/pkg"
PRIVATE_PATH            = "var/lib/portage"
CACHE_PATH              = "/var/cache/edb"
DEPCACHE_PATH           = CACHE_PATH+"/dep"
SYNCCACHE_PATH          = "/var/cache/sync-cache"

USER_CONFIG_PATH        = "/etc/portage"
MODULES_FILE_PATH       = USER_CONFIG_PATH+"/modules"
CUSTOM_PROFILE_PATH     = USER_CONFIG_PATH+"/profile"

#PORTAGE_BASE_PATH       = "/usr/lib/portage"
PORTAGE_BASE_PATH       = os.path.join(os.sep, os.sep.join(__file__.split(os.sep)[:-2]))
PORTAGE_BIN_PATH        = PORTAGE_BASE_PATH+"/bin"
PORTAGE_PYM_PATH        = PORTAGE_BASE_PATH+"/pym"
PROFILE_PATH            = "/etc/make.profile"
LOCALE_DATA_PATH        = PORTAGE_BASE_PATH+"/locale"

EBUILD_SH_BINARY        = PORTAGE_BIN_PATH+"/ebuild.sh"
MISC_SH_BINARY          = PORTAGE_BIN_PATH + "/misc-functions.sh"
SANDBOX_BINARY          = "/usr/bin/sandbox"
FAKEROOT_BINARY         = "/usr/bin/fakeroot"
BASH_BINARY             = "/bin/bash"
MOVE_BINARY             = "/bin/mv"
PRELINK_BINARY          = "/usr/sbin/prelink"

WORLD_FILE              = PRIVATE_PATH + "/world"
MAKE_CONF_FILE          = "/etc/make.conf"
MAKE_DEFAULTS_FILE      = PROFILE_PATH + "/make.defaults"
DEPRECATED_PROFILE_FILE = PROFILE_PATH+"/deprecated"
USER_VIRTUALS_FILE      = USER_CONFIG_PATH+"/virtuals"
EBUILD_SH_ENV_FILE      = USER_CONFIG_PATH+"/bashrc"
INVALID_ENV_FILE        = "/etc/spork/is/not/valid/profile.env"
CUSTOM_MIRRORS_FILE     = USER_CONFIG_PATH+"/mirrors"
CONFIG_MEMORY_FILE      = PRIVATE_PATH + "/config"
COLOR_MAP_FILE          = USER_CONFIG_PATH + "/color.map"

REPO_NAME_FILE         = "repo_name"
REPO_NAME_LOC          = "profiles" + "/" + REPO_NAME_FILE

INCREMENTALS = ["USE", "USE_EXPAND", "USE_EXPAND_HIDDEN", "FEATURES",
	"ACCEPT_KEYWORDS", "ACCEPT_LICENSE",
	"CONFIG_PROTECT_MASK", "CONFIG_PROTECT",
	"PRELINK_PATH", "PRELINK_PATH_MASK", "PROFILE_ONLY_VARIABLES"]
EBUILD_PHASES           = ["setup", "unpack", "compile", "test", "install",
                          "preinst", "postinst", "prerm", "postrm", "other"]

EAPI = 1

HASHING_BLOCKSIZE        = 32768
MANIFEST1_HASH_FUNCTIONS = ["MD5","SHA256","RMD160"]
MANIFEST2_HASH_FUNCTIONS = ["SHA1","SHA256","RMD160"]

MANIFEST1_REQUIRED_HASH = "MD5"
MANIFEST2_REQUIRED_HASH = "SHA1"

MANIFEST2_IDENTIFIERS = ["AUX","MISC","DIST","EBUILD"]

MAKE_CONF_ALLOW_EXPAND = ['EHG_BASE_URI', 'EGIT_BASE_URI']

WYPLAY_ALCATRAZ_DIRS = ["/chroot", "/lxc", "/redist/chroot", "/redist/lxc"]

# ===========================================================================
# END OF CONSTANTS -- END OF CONSTANTS -- END OF CONSTANTS -- END OF CONSTANT
# ===========================================================================
