import os
import re
import time

from idaapi import *
from idc import *
from idautils import *

SYM_TOKEN = "_SYM"

sym_reg = re.compile(SYM_TOKEN)
call_reg = re.compile("^call")

mbase = idaapi.get_imagebase()

def AllSyms():
	ea = ScreenEA()	
	syms = []
	for funcea in Functions(SegStart(ea), SegEnd(ea)):
		funcname = GetFunctionName(funcea)
		if sym_reg.search(funcname):
			syms.extend(Syms(funcea))
	
	return syms

def GetReturnSyms(func_name, block):
	syms = []
	func_addr = GetFunctionAttr(block.startEA, FUNCATTR_START)
	for head in Heads(block.startEA, block.endEA):
			dasm = GetDisasm(head)
			if call_reg.search(dasm):
				ret_addr = NextHead(head, BADADDR);
				s = { 'start' : (ret_addr - mbase), 'name' : func_name, 'offset' : (ret_addr - func_addr) }
				syms.append(s)
	return syms
				

def Syms(addr = ScreenEA()):
	syms = []	
	func_addr = idaapi.get_func(addr)
	start_addr = GetFunctionAttr(addr, FUNCATTR_START)	
	fname = GetFunctionName(ScreenEA())
	func_name = re.sub(SYM_TOKEN, "", fname)	
	for block in idaapi.FlowChart(func_addr):
		s = { 'start' : (block.startEA - mbase), 'name' : func_name, 'offset' : (block.startEA - start_addr) }
		syms.append(s)
		syms.extend(GetReturnSyms(func_name, block))
		
	return syms
	
def SaveSyms(syms, out = None):	
	moduleName = idc.GetInputFile()
	moduleShortName = re.sub(r'\.[^.]*$','', moduleName)
	fname = "%s.sym" % moduleShortName
	if out == None: out = fname
	f = open(out,"w")	
	for s in syms:
		str = "%0.8X,%s + 0x%0.4X ( 0x%0.8X )" % (s['start'], s['name'], s['offset'], s['start'])
		#print str
		f.write( str + '\n')
		
	f.closed
	print "\n>> %i syms written to %s\\%s" % (len(syms), os.getcwd(),out)