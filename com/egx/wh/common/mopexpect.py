#encoding=utf-8
'''
Created on Jun 24, 2015

@author: lowitty
'''

import os, pexpect

class MoWhApi():
    '''
    classdocs
    '''
    DummyPrompt = "SYSTEMVERIFIERING>"


    def __init__(self, mo_path, java_path, pak_path, password = 'rbs'):
        self.mo_path = unicode( os.path.normpath(mo_path), 'utf8')
        self.java_path = unicode( os.path.normpath(java_path), 'utf8')
        self.pak_path = unicode( os.path.normpath(pak_path), 'utf8')
        self.password = password
        
        if((not os.path.exists(self.mo_path)) or (not os.path.exists(self.java_path)) or (not os.path.exists(self.pak_path))):
            raise Exception("One or more of the paths that you specified is wrong!")
        
        '''
        Constructor
        '''
        
        
    
    def connect(self):
        self.mo_cmd = "%s -v java=%s,set_window_title=0,prompt_highlight=0,show_colors=0,prompt_colors=0,secure_ftp=1 %s" % (self.mo_path, self.java_path, self.pak_path)
        self.session = pexpect.spawn(self.mo_cmd, timeout=180, maxread=50000)
        self.session.expect("QUIT")
        self.session.sendline("p SYSTEMVERIFIERING")
        self.session.expect(self.DummyPrompt)
    
    def close(self):
        self.session.sendline('quit')
        self.session.close()
    
    def sendCmd(self, cmd):
        self.session.sendline(cmd)
        self.session.expect(self.DummyPrompt)
        return self.session.before