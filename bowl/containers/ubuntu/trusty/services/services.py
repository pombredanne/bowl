"""
This module is for all services supported for ubuntu:trusty.

Created on 16 March 2014
@author: Charlie Lewis
"""

class services(object):
    """
    This class is responsible for all available services for ubuntu:trusty.
    """
    def rsyslog(self):
        return {
                'title': "rsyslog",
                'type': "choice_menu",
                'command': "ubuntu:trusty:services:rsyslog",
                'cluster': "no",
                'combine_cmd': "yes",
                'background_cmd': "TODO",
                'tty': "no",
                'interactive': "no"
               }

    def sshd(self):
        return {
                'title': "SSH Server",
                'type': "choice_menu",
                'command': "ubuntu:trusty:services:sshd",
                'cluster': "no",
                'combine_cmd': "yes",
                'background_cmd': "/usr/sbin/sshd",
                'tty': "no",
                'interactive': "no"
               }
