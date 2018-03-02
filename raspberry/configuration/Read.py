#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    #print "Ctrl+C captured, ending read."
    continue_reading = False
    #GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
#print "Welcome to the MFRC522 data read example"
#print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    #If a card is found
    #If status == MIFAREReader.MI_OK:
       #print "Card detected"
    
    #Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    
    input_state_shutdown = GPIO.input(pinShutdown)
    input_state_testPin = GPIO.input(pinTestButton)
    if input_state_shutdown == False:
        print('pressed Shutdown')
        os.system("shutdown -h now")
    elif input_state_testPin == False:
        print('pressed Test')
    else:
    	sleep(0.2)
    if status == MIFAREReader.MI_OK:

        #Print UID
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
		card=str(str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3]))
		print card
		
		isValid = False
		#POROVNANIE CARD ID S DB
		#AK SPRAVNE isValid > True
		#INAK isValid > False 
		if isValid:
			print "KARTA ROZOZNANA"
			#ZAPNUt KAMERU
			#UROBIT FOTO
			
			isRecognized = False
			print "NIECO"
			#VOLAT AWS A UROBIT POROVNANIE FOTO
			#AK ROZOZNANIE USPESNE isRecognized > True
			
			if isRecognized:
				print "ZAPIS DO DB USPESNE"
				#ZAPIS DO DB OVERENIE USPESNE
				
			else:
				print "ZAPIS DO DB NEUSPESNE"
				#ZAPIS DO DB NEUSPESNE
				
		else:
			print "ZAPIS DO DB NEUSPESNE ZLA KARTA"
			#ZAPIS DO DB NEUSPESNE ZLA KARTA
		
	
		sleep(1)
	#break

        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        #else:
            #print "Authentication error"

