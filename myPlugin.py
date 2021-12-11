from datetime import datetime as dt

class cf(GenericCommand):
  """Toggle Carry Flag"""
  _cmdline_ = "cf"
  _syntax_  = "{:s}".format(_cmdline_)
  @only_if_gdb_running
  def do_invoke(self, argv):
    if ((get_register("$eflags") & 0x1) == 0x1):
    	print("Set Carry Flag to 0")
    else:
    	print("Set Carry Flag to 1")
    gdb.execute('set $eflags ^= 0x1')
    return    
    
class pf(GenericCommand):
  """Toggle Parity Flag"""
  _cmdline_ = "pf"
  _syntax_  = "{:s}".format(_cmdline_)
  @only_if_gdb_running
  def do_invoke(self, argv):
    if ((get_register("$eflags") & 0x4) == 0x4):
    	print("Set Parity Flag to 0")
    else:
    	print("Set Parity Flag to 1")
    gdb.execute('set $eflags ^= 0x4')
    return    

class af(GenericCommand):
  """Toggle Auxiliary Carry Flag"""
  _cmdline_ = "af"
  _syntax_  = "{:s}".format(_cmdline_)
  @only_if_gdb_running
  def do_invoke(self, argv):
    if ((get_register("$eflags") & 0x10) == 0x10):
    	print("Set Auxiliary Carry Flag to 0")
    else:
    	print("Set Auxiliary Carry Flag to 1")
    gdb.execute('set $eflags ^= 0x10')
    return    
    
class zf(GenericCommand):
  """Toggle Zero Flag"""
  _cmdline_ = "zf"
  _syntax_  = "{:s}".format(_cmdline_)
  @only_if_gdb_running
  def do_invoke(self, argv):
    if ((get_register("$eflags") & 0x40) == 0x40):
    	print("Set Zero Flag to 0")
    else:
    	print("Set Zero Flag to 1")
    gdb.execute('set $eflags ^= 0x40')
    return    
    
class sf(GenericCommand):
  """Toggle Sign Flag"""
  _cmdline_ = "sf"
  _syntax_  = "{:s}".format(_cmdline_)
  @only_if_gdb_running
  def do_invoke(self, argv):
    if ((get_register("$eflags") & 0x80) == 0x80):
    	print("Set Sign Flag to 0")
    else:
    	print("Set Sign Flag to 1")
    gdb.execute('set $eflags ^= 0x80')
    return    

class of(GenericCommand):
  """Toggle Overflow Flag"""
  _cmdline_ = "of"
  _syntax_  = "{:s}".format(_cmdline_)
  @only_if_gdb_running
  def do_invoke(self, argv):
    if ((get_register("$eflags") & 0x800) == 0x800):
    	print("Set Overflow Flag to 0")
    else:
    	print("Set Overflow Flag to 1")
    gdb.execute('set $eflags ^= 0x800')
    return    

class testZero(GenericCommand):
  """Set register rax to 0, alternative way to bypass test rax, rax"""
  _cmdline_ = "tz"
  _syntax_  = "{:s}".format(_cmdline_)
  @only_if_gdb_running
  def do_invoke(self, argv):
    gdb.execute('set $rax = 0')
    print("Set RAX to 0")
    return
        
def findptrace(event):
  try:
    result = gdb.execute("info address ptrace", to_string=True)
    if 'Symbol "ptrace" is at' in result:
      print("ptrace found! Setting up a temporary breakpoint for you.")
      gdb.execute("tb ptrace")
    gdb.events.cont.disconnect(findptrace)
    return
  except Exception:
    pass

def customizedLogging(event):
  time = str(dt.now().strftime('%m-%d_%H:%M:%S'))
  cmd = 'set logging file ' + time + '.txt'
  gdb.execute(cmd)
  gdb.execute("set logging on")
  gdb.events.cont.disconnect(customizedLogging)
  return
  
def reg_changed(event):
  print("Frame: " + str(event.frame))
  return
  
def mem_changed(event):
  print("Start at: " + str(hex(event.address)) + " Length: " + str(event.length) + " bytes")
  return

def bp(event):
  gdb.execute("info breakpoints")
  return
  
if __name__ == '__main__':
  register_external_command(cf())
  register_external_command(pf())
  register_external_command(af())
  register_external_command(zf())
  register_external_command(sf())
  register_external_command(of())
  register_external_command(testZero())
  gdb.events.cont.connect(findptrace)
  gdb.events.cont.connect(customizedLogging)
  gdb.events.register_changed.connect(reg_changed)
  gdb.events.memory_changed.connect(mem_changed)
  gdb.events.breakpoint_created.connect(bp)
  gdb.events.breakpoint_modified.connect(bp)
  gdb.events.breakpoint_deleted.connect(bp)
