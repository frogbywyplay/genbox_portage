import sys, os
from unittest import TestCase
import portage
import shutil
import tarfile
from portage_const import INCREMENTALS
from portage_util import LazyItemsDict
from portage import _global_updates


class WyplayUpdateTestCase(TestCase):

    def __init__(self, methodName='runTest'):
        TestCase.__init__(self, methodName)
        self.path = os.path.realpath(os.path.dirname(sys.modules[__name__].__file__))
        self.tgt = '%s/data/update' % self.path
        self.tgt_root = '%s/root/' % self.tgt
        
    def create_trees(self):
        config = self.config
        trees = {}
        
        settings = config
        settings.lock()
        
        myroots = [(settings["ROOT"], settings)]
        for myroot, mysettings in myroots:
            trees[myroot] = LazyItemsDict(trees.get(myroot, None))
            trees[myroot].addLazySingleton("virtuals", mysettings.getvirtuals, myroot)
            trees[myroot].addLazySingleton(
                "vartree", portage.vartree, myroot, categories=mysettings.categories,
                settings=mysettings)
            trees[myroot].addLazySingleton("porttree",
                                           portage.portagetree, myroot, settings=mysettings)
            trees[myroot].addLazySingleton("bintree",
                                           portage.binarytree, myroot, mysettings["PKGDIR"], settings=mysettings)
            
        #settings = trees["/"]["vartree"].settings
                
        for myroot in trees:
            trees[myroot]["porttree"].dbapi.freeze()
            if myroot != "/":
                settings = trees[myroot]["vartree"].settings
                break
            
        return trees

    def setUp(self):
        if not os.path.isfile('%s.tar.gz' % self.tgt):
            self.fail('Target tarball is missing')
        tar = tarfile.open('%s.tar.gz' % self.tgt, 'r:gz')
        tar.extractall('%s/../' % self.tgt)
        # initialize portage configuration
        self.config = portage.config(clone=None,
                                     mycpv=None,
                                     config_profile_path=None,
                                     config_incrementals=INCREMENTALS,
                                     config_root=self.tgt_root,
                                     target_root=self.tgt_root,
                                     local_config=True)
        self.trees = self.create_trees()
        self.vartree = self.trees[self.tgt_root]['vartree']
        self.bintree = self.trees[self.tgt_root]['bintree']
        self.porttree = self.trees[self.tgt_root]['porttree']
        
    def tearDown(self):
        shutil.rmtree(self.tgt)
        del self.config
        
    def testPortdirUpdate(self):
        self.assertEqual(1, len(self.vartree.getnode('test-update/a')))
        self.assertEqual(0, len(self.vartree.getnode('test-update/aa')))
        # root argument is only available through patch
        _global_updates(self.trees, {}, self.tgt_root)
        
        self.assertEqual(0, len(self.vartree.getnode('test-update/a')))
        self.assertEqual(1, len(self.vartree.getnode('test-update/aa')))

    def testOverlayUpdate(self):
        self.assertEqual(1, len(self.vartree.getnode('test-update/b')))
        self.assertEqual(0, len(self.vartree.getnode('test-update/e')))

        # root argument is only available through patch
        _global_updates(self.trees, {}, self.tgt_root)

        self.assertEqual(0, len(self.vartree.getnode('test-update/b')))
        self.assertEqual(1, len(self.vartree.getnode('test-update/e')))

    def testProfileUpdate(self):
        self.assertEqual(1, len(self.vartree.getnode('test-update/c')))
        self.assertEqual(1, len(self.vartree.getnode('test-update/d')))
        self.assertEqual(0, len(self.vartree.getnode('test-update/cc')))
        self.assertEqual(0, len(self.vartree.getnode('test-update/dd')))

        # root argument is only available through patch
        _global_updates(self.trees, {}, self.tgt_root)

        self.assertEqual(0, len(self.vartree.getnode('test-update/c')))
        self.assertEqual(0, len(self.vartree.getnode('test-update/d')))
        self.assertEqual(1, len(self.vartree.getnode('test-update/cc')))
        self.assertEqual(1, len(self.vartree.getnode('test-update/dd')))
        
