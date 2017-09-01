# encoding:utf-8
import client


class command_handler:
    def __init__(self, sys_args):
        self.sys_args = sys_args
        if len(self.sys_args) < 2:
            exit(self.help_msg())
        self.command_allowcator()

    def command_allowcator(self):
        print self.sys_args[1]

        if hasattr(self, self.sys_args[1]):
            func = getattr(self, self.sys_args[1])
            return func
        else:
            print 'command does not exist!'
            self.help_msg()

    def help_msg(self):
        valid_commands = '''
    	start start monitor client
    	stop stop monitor client
    	'''
        exit(valid_commands)

    def start(self):
        print 'going to start the monitor client'

        Client = client.ClientHandle()
        Client.forever_run()

    def stop(self):
        print 'stopping the monitory client'
