from time import sleep
import pygame.mixer
import serial 
import subprocess

import threading

#serialFromArduino = serial.Serial("/dev/ttyUSB1", 115200)
serialFromArduino = serial.Serial("/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_A900aepy-if00-port0", 115200)
serialFromArduino.flush()

pygame.mixer.quit()
pygame.mixer.init(48000, -16, 2, 1024)
warning = False

cws = pygame.mixer.Sound("cws.wav")
cws.set_volume(0.2)
cwsC = pygame.mixer.Channel(1)
thirteenSound = pygame.mixer.Sound("11event.wav") # O2 Fan w/Explosion

teiPushed = 0
spsPushed = 0
suitCompPushed = 0
abortArmed = 0
lightningStruck = 0
sceRestored = False
sceAux = False
cwsPower = False
thirteen = False

locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3','/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']

def lightningStrike():
	global lightningStruck
	global sceAux

	while True:
		if (lightningStruck == 1):
			if not sceAux:
				serialFromArduino.write(b'1,4,4,1,1\n') # Illuminated Hatch 
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(2)
			if not sceAux:		
				serialFromArduino.write(b'1,4,4,2,5\n') # Illuminated Suit Comp
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(2)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,5,0\n') # Illuminated CO2 PP HI
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,3,5\n') # Illuminated SM RCS D
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,0,3\n') # Illuminated SPS Rough ECO
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(2) 
			if not sceAux:
				serialFromArduino.write(b'1,4,4,3,1\n') # Illuminated Picth GMBL 1
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,5,3\n') # Illuminated CM RCS 2
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,1,4\n') # Illuminated Crew Alert
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,3,3\n') # Illuminated Glycol Temp Low
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,0,5\n') # Illuminated FC Bus Discnnct
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,3,0\n') # Illuminated B Mag 1 Temp
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,1,3\n') # Illuminated AC Bus 1 Overload
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
				sleep(1)
			if not sceAux:
				serialFromArduino.write(b'1,4,4,5,2\n') # Illuminated Cryo Press.
				sleep(0.1)
				serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
				cwsC.play(cws)
			lightningStruck = 0
			sleep(1)

def sceRestore():
	global sceRestored
	
	while True:
		if sceRestored:
			cwsC.stop()
			serialFromArduino.write(b'0,4,4,1,1\n') # Delumminate Hatch
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,2,5\n') # Delumminate Suit Comp.
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,5,0\n') # Delumminate CO2 PP HI
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,3,5\n') # Delumminate SM RCS D
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,0,3\n') # Delumminate SPS Rough ECO
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,3,1\n') # Delumminate Pitch Gmbl 1
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,5,3\n') # Delumminate CM RCS 2
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,1,4\n') # Delumminate Crew Alert
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,3,3\n') # Delumminate Glycol Temp Low
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,0,5\n') # Delumminate FC Bus Discnnct
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,3,0\n') # Delumminate B Mag 1 Temp
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,1,3\n') # Delumminate AC Bus 1 Overload
			sleep(0.1)
			serialFromArduino.write(b'0,4,4,5,2\n') # Delumminate Cryo Press
			sceRestored = False
		sleep(0.5)

def thirteenEvent():
	global thirteen
	global thirteenSound
	global cwsC
	global cws
	
	while True:
		if thirteen:
			serialFromArduino.write(b'1,4,4,4,7\n') # Light next to switch (O2 Fan)
			offbit = 0
			thirteenSound.play()
			sleep(4.5)
			serialFromArduino.write(b'1,4,4,1,5\n') # Illuminated Ox flow high
			sleep(0.1)
			serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
			cwsC.play(cws)
			sleep(0.1)
		#	serialFromArduino.write(b'2,11,0,0,0\n')
		#	sleep(1)
		#	serialFromArduino.write(b'2,10,0,0,0\n')
		#	sleep(1)
			serialFromArduino.write(b'2,9,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,9,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,8,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,8,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'1,4,4,2,3\n')	# Illuminated Main Bus B Undervolt
			sleep(0.1)
			serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
			cwsC.play(cws)
			sleep(0.5)
	
			serialFromArduino.write(b'2,7,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,7,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,6,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,6,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,5,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,5,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,4,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,4,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,3,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,3,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,2,0,0,0\n') # Delumminate O2 Press (bar graph) 
			sleep(0.5)
			serialFromArduino.write(b'2,2,6,0,0\n') # Delumminate O2 Qty (bar graph) 
			sleep(0.5)
			thirteen = False
		sleep(0.1)



def mainLoop():

	global teiPushed
	global spsPushed
	global suitCompPushed
	global abortArmed
	global lightningStruck
	global sceAux
	global sceRestored
	global airComp
	global cws
	global cwsPower
	global thirteen
	
	tliPushed = 0
	sicPushed = 0
	siiPushed = 0
	sivbPushed = 0
	miPushed = 0
	miiPushed = 0
	miiiPushed = 0
	glycolPushed = 0

	sequenceC = pygame.mixer.Channel(2)
	
	aborted = pygame.mixer.Sound("aborted.wav") # Abort Pushbutton
	liftoff = pygame.mixer.Sound("liftoff.wav") # Blast Off Pushbutton
	stagetwo = pygame.mixer.Sound("stagetwo.wav") # Stage Two Pushbutton
	stagethree = pygame.mixer.Sound("stagethree.wav") # Stage Three Pushbutton
	switchorbits = pygame.mixer.Sound("switchorbits.wav") # Switch Orbits Pushbutton
	tde = pygame.mixer.Sound("tde.wav") # TDE Pushbutton
	landeva = pygame.mixer.Sound("landeva.wav") # Land Eva Pushbutton
	headhome = pygame.mixer.Sound("headhome.wav") # Head Home Pushbutton
	reentry = pygame.mixer.Sound("reentry.wav") # ReEntry Pushbutton
	splashdown = pygame.mixer.Sound("splashdown.wav") # Splashdown Pushbutton
	poll = pygame.mixer.Sound("poll.wav") # Go For Launch Pushbutton
	
	shortexp = pygame.mixer.Sound("shortexp.wav")  # exp = explosion??
	medexp = pygame.mixer.Sound("medexp.wav")
	les = pygame.mixer.Sound("les.wav") # LES Motor Fire Switch
	pexp = pygame.mixer.Sound("pexp.wav")
	hiexp = pygame.mixer.Sound("hiexp.wav")
	drogue = pygame.mixer.Sound("drogue.wav") # Drogue Deploy Switch
	main = pygame.mixer.Sound("main.wav") # Main Deploy Switch
	fpump = pygame.mixer.Sound("fpump.wav") # Pumps Switch
	fpump.set_volume(0.7)
	fan = pygame.mixer.Sound("fan.wav") # H2 Fan
	heat = pygame.mixer.Sound("heat.wav") # Heat Switch
	sps = pygame.mixer.Sound("sps.wav") # SPS Pushbutton
	tei = pygame.mixer.Sound("tei.wav") # TEI Pushbutton
	tli = pygame.mixer.Sound("tli.wav") # TLI Pushbutton
	sic = pygame.mixer.Sound("sic.wav") # SIC Pushbutton
	sii = pygame.mixer.Sound("sii.wav") # SII Pushbutton
	sivb = pygame.mixer.Sound("sivb.wav") # SIVB Pushbutton
	mi = pygame.mixer.Sound("mi.wav") # MI Pushbutton
	mii = pygame.mixer.Sound("mii.wav") # MII Pushbutton
	miii = pygame.mixer.Sound("miii.wav") # MIII Pushbutton
	flush = pygame.mixer.Sound("flush.wav") # Waste Dump Switch
	aircomp = pygame.mixer.Sound("aircomp.wav") # Suit Compression Rocker Switch
	aircomp.set_volume(0.5)
	dieselpump = pygame.mixer.Sound("dieselpump.wav") # Glycol Pump Switch
	dieselpump.set_volume(0.7)
	extend = pygame.mixer.Sound("extend.wav") # Extend Dock Probe Switch
	retract = pygame.mixer.Sound("retract.wav") # Retract Dock Probe Switch
	qin = pygame.mixer.Sound("qin.wav") # PTT Pushbutton (Initiate)
	qin.set_volume(0.3)
	qout = pygame.mixer.Sound("qout.wav") # PTT Pushbutton (Release)
	qout.set_volume(0.3)
	hflow = pygame.mixer.Sound("lantern.wav") # H2O Flow Rocker Switch
	cfan = pygame.mixer.Sound("cfan.wav") # Cabin Fan Rocker Switch
	cfan.set_volume(0.3)	

	serialFromArduino.write(b'0,4,4,6,0\n') # Deluminate Go For Launch Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,6,1\n') # Deluminate Blast Off Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,6,2\n') # Deluminate Stage Two Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,6,3\n') # Deluminate Stage Three Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,6,4\n') # Deluminate Switch Orbits Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,7,0\n') # Deluminate TDE Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,7,1\n') # Deluminate Land EVA Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,7,2\n') # Deluminate Head Home Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,7,3\n') # Deluminate ReEntry Pushbutton
	sleep(0.1)
	serialFromArduino.write(b'0,4,4,7,4\n') # Deluminate Splash Down Pushbutton


	print "Sampler Ready."

	# Loop while waiting for a keypress
	while True:
		try:
			digit = ord(serialFromArduino.read())
			offBit = 0
			if (digit > 128):
				digit = digit - 128
				offBit = 1
		#####		
			if (digit == 6):
				if (offBit):
					offBit = 0
					medexp.play()

			elif (digit == 21): # Abort button
				if (offBit):
					offBit = 0
				else:
					if abortArmed:
						aborted.play()
						serialFromArduino.write(b'0,4,4,7,5\n') # Deluminate Abort Button
						subprocess.call("halt", shell=True)

			elif (digit == 46): # Master Alarm button
				if (offBit):
					offBit = 0
				else:
					cwsC.stop()
					serialFromArduino.write(b'0,4,4,1,7\n') # Deluminated Master Alarm Pushbutton
					warning = False

			elif (digit == 19): # Power Switch on C&WS Panel
				if (offBit):
					offBit = 0
					cwsPower = True
					serialFromArduino.write(b'0,4,4,2,4\n') # Deluminate C/W
					cwsC.stop()
				else:
					cwsPower = False
					serialFromArduino.write(b'1,4,4,2,4\n') # Illuminated C/W
					sleep(0.1)
					cwsC.play(cws)
					serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton

                # Initiate Apollo 12 Lightning Strike
                #####
			elif (digit == 16): # CSM/CM switch or Ack pushbutton
				if (offBit):
					offBit = 0
				else:
					if not cwsPower:
						if not lightningStruck:
							if not sceAux:
								lightningStruck = 1

			elif (digit == 0): # Switch Orbits Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(switchorbits)
					serialFromArduino.write(b'1,4,4,6,4\n') # Illuminated Switch Orbits Pushbutton
					
			elif (digit == 1): # Stage Three Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(stagethree)
					serialFromArduino.write(b'1,4,4,6,3\n') # Illuminated Stage Three Pushbutton
					
			elif (digit == 5): # Blast Off Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(liftoff)
					serialFromArduino.write(b'1,4,4,6,1\n') # Illuminated Blast Off Pushbutton
					
			elif (digit == 4): # Stage Two Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(stagetwo)
					serialFromArduino.write(b'1,4,4,6,2\n') # Illuminated Stage Two Pushbutton
					
			elif (digit == 41): # Splash Down Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(splashdown)
					serialFromArduino.write(b'1,4,4,7,4\n') # Illuminated Splash Down Pushbutton
					
			elif (digit == 42): # ReEntry Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(reentry)
					serialFromArduino.write(b'1,4,4,7,3\n') # Illuminated Splash Down Pushbutton
					
			elif (digit == 43): # Head Home Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(headhome)
					serialFromArduino.write(b'1,4,4,7,2\n') # Illuminated Head Home Pushbutton
					
			elif (digit == 44): # Land Eva Pushbutton
				if (offBit): 
					offBit = 0
				else:					 
					sequenceC.play(landeva)
					serialFromArduino.write(b'1,4,4,7,1\n') # Illuminated Land Eva Pushbutton
					
			elif (digit == 45): # TDE Pushbutton
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(tde)
					serialFromArduino.write(b'1,4,4,7,0\n') # Illuminated TDE Pushbutton
		#####			
			elif (digit == 3):
				if (offBit):
					offBit = 0
					hiexp.play()
					
			elif (digit == 2): # Main Deploy (Pyro Panel Switch)
				if (offBit):
					offBit = 0
				else:
					main.play()
					serialFromArduino.write(b'1,4,4,0,1\n') # Illuminate Main Chute
					
			if (digit == 7): # LES Motor Fire Switch
				if (offBit):
					offBit = 0
				else:
					les.play()
					
			elif (digit == 8): # Go For Launch Pushbutton	 
				if (offBit):
					offBit = 0
				else:
					sequenceC.play(poll)
					serialFromArduino.write(b'1,4,4,6,0\n') # Illuminated Go For Launch Pushbutton
					
			elif (digit == 9): # Drogue Deploy Switch
				if (offBit):
					offBit = 0
				else:
					drogue.play()
					serialFromArduino.write(b'1,4,4,0,0\n') # Illuminated Drogue Chute
		#####			
			if (digit == 10):
				if (offBit):
					offBit = 0
					pexp.play()
		#####			
			elif (digit == 11):
				if (offBit):
					offBit = 0
					shortexp.play()

		# Apollo 13 explosion
			elif (digit == 12): # O2 Fan Switch	
				if (offBit):
					thirteen = True
				else:
					serialFromArduino.write(b'0,4,4,4,7\n') # Deluminate O2 Fan
					sleep(0.1)
					serialFromArduino.write(b'2,9,0,0,0\n') # Illumminate O2 Press (bar graph)
					sleep(0.1)
					serialFromArduino.write(b'2,9,6,0,0\n') # Illumminate O2 Qty (bar graph)
					sleep(0.1)
					serialFromArduino.write(b'0,4,4,1,5\n') # Deluminate Ox flow high
					sleep(0.1)
					serialFromArduino.write(b'0,4,4,2,3\n')	# Deluminate Main Bus B Undervolt
                
			elif (digit == 13): # H2 Fan Switch
				if (offBit):
					serialFromArduino.write(b'1,4,4,5,7\n') # Illuminate H2 Fan
					offbit = 0
					fan.play()
				else:
					serialFromArduino.write(b'0,4,4,5,7\n') # Deluminate H2 Fan
					fan.fadeout(1000)
					
			elif (digit == 14): # Pumps Switch
				if (offBit):
					serialFromArduino.write(b'1,4,4,6,7\n') # Illuminate Pumps
					offbit = 0
					fpump.play()
				else:
					serialFromArduino.write(b'0,4,4,6,7\n') # Deluminate Pumps
					fpump.fadeout(1000)
					
			elif (digit == 15): # Heat Switch
				if (offBit):
					serialFromArduino.write(b'1,4,4,7,7\n') # Illuminate Heat
					offbit = 0
					heat.play()
				else:
					serialFromArduino.write(b'0,4,4,7,7\n') # Deluminate Heat
					heat.fadeout(500)
					
			elif (digit == 24): # TEI Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					tei.play()	
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					sleep(0.1)
					teiPushed = teiPushed + 1
					
					if teiPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,4,1\n') # Illuminate B Mag 2 Temp
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 25): # SPS Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					sps.play()	
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					sleep(0.1)
					spsPushed = spsPushed + 1
					
					if (spsPushed % 10) == 0:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,0,4\n') # Illuminate SPS FLNG Temp Hi
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
					if spsPushed == 5:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,0,2\n') # Illuminate SPS Press
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
					if spsPushed == 25:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,0,3\n') # Illuminate SPS Rough ECO
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 26): # MIII Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					miii.play()	 
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					sleep(0.1)
					miiiPushed = miiiPushed + 1
					
					if miiiPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,0,4\n') # Illuminate SPS FLNG Temp Hi
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)

			elif (digit == 27): # SIVB Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					sivb.play()	 
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					sivbPushed = sivbPushed + 1
					
					if sivbPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,0,5\n') # Illuminate FC Bus Discnnct
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 28): # SII Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					sii.play()	
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					siiPushed = siiPushed + 1
					
					if siiPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,4,0\n') # Illuminate B Mag 2 Temp
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 29): # SIC Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					sic.play()	
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					sicPushed = sicPushed + 1
					
					if sicPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,3,1\n') # Illuminate Pitch Gmbl 1
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 30): # MI Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					mi.play()  
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					miPushed = miPushed + 1
					
					if miPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,3,2\n') # Illuminate Pitch Gmbl 2
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 31): # MII Pushbutton
				if (offBit): 
					offBit = 0
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					mii.play()	
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					miiPushed = miiPushed + 1
					
					if miiPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,4,2\n') # Illuminate YAW Gmbl 2
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 47): # TLI Pushbutton
				if (offBit):
					offBit = 0 
					serialFromArduino.write(b'0,4,4,2,0\n') # Deluminate Thrust
				else:
					tli.play()
					serialFromArduino.write(b'1,4,4,2,0\n') # Illuminate Thrust
					tliPushed = tliPushed + 1
					
					if tliPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,5,0\n') # Illuminate CO2 PP HI
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 22): # ARM Switch (Abort Panel) 
				if (offBit):
					serialFromArduino.write(b'1,4,4,7,5\n') # Illuminate Abort Button
					offbit = 0
					abortArmed = 1
				else:
					serialFromArduino.write(b'0,4,4,7,5\n') # Deluminate Abort Button
					abortArmed = 0
					
			elif (digit == 23):
				if (offBit):
					serialFromArduino.write(b'1,4,4,7,6\n')
					offbit = 0
					flush.play()
				else:
					serialFromArduino.write(b'0,4,4,7,6\n')
					flush.fadeout(2000)
					
			elif (digit == 20):
				if (offBit):
					serialFromArduino.write(b'0,4,4,6,5\n')
					offBit = 0
					qout.play()
				else:
					serialFromArduino.write(b'1,4,4,6,5\n')
					qin.play()
					
			elif (digit == 32):
				if (offBit):
					serialFromArduino.write(b'0,4,4,3,6\n')
					aircomp.fadeout(2000)
					offBit = 0
				else:
					serialFromArduino.write(b'1,4,4,3,6\n')
					aircomp.play()
					suitCompPushed = suitCompPushed + 1
					sleep(0.1)
					
					if (suitCompPushed % 5) == 0:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,2,5\n')
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
						
			elif (digit == 33):
				if (offBit):
					offbit = 0
					serialFromArduino.write(b'0,4,4,2,6\n')
				else:
					serialFromArduino.write(b'1,4,4,2,6\n')
					
			elif (digit == 34):
				if (offBit):
					offbit = 0
					serialFromArduino.write(b'1,4,4,6,6\n')
					sceAux = True
					if lightningStruck:
						sceRestored = True
				else:
					serialFromArduino.write(b'0,4,4,6,6\n')
					sceAux = False
					
			elif (digit == 35):
				if (offBit):
					serialFromArduino.write(b'1,4,4,5,6\n')
					offbit = 0
					dieselpump.play()
					glycolPushed = glycolPushed + 1
					
					if glycolPushed == 6:
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,3,3\n')
						sleep(0.1)
						serialFromArduino.write(b'1,4,4,1,7\n') # Illuminated Master Alarm Pushbutton
						cwsC.play(cws)
				else:
					serialFromArduino.write(b'0,4,4,5,6\n')
					dieselpump.fadeout(1000)
					
			elif (digit == 36):
				if (offBit):
					serialFromArduino.write(b'0,4,4,4,6\n')
					retract.stop()
					offBit = 0
				else:
					serialFromArduino.write(b'1,4,4,4,6\n')
					retract.play()
					
			elif (digit == 37):
				if (offBit):
					serialFromArduino.write(b'0,4,4,4,6\n')
					extend.stop()
					offBit = 0
				else:
					serialFromArduino.write(b'1,4,4,4,6\n')
					extend.play()
					
			elif (digit == 38):
				if (offBit):   
					serialFromArduino.write(b'0,4,4,0,6\n')
					cfan.fadeout(2000)
					offBit = 0
				else:
					serialFromArduino.write(b'1,4,4,0,6\n')
					cfan.play()
					
			elif (digit == 39):
				if (offBit):
					serialFromArduino.write(b'0,4,4,1,6\n')
					hflow.fadeout(500)
					offBit = 0
				else:
					serialFromArduino.write(b'1,4,4,1,6\n')
					hflow.play()

			sleep(0.01)
		except KeyboardInterrupt:
			exit()

thread1 = threading.Thread(target = mainLoop)
thread2 = threading.Thread(target = lightningStrike)
thread3 = threading.Thread(target = sceRestore)
thread13 = threading.Thread(target = thirteenEvent)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread13.start()
print "Exiting Main Thread"

