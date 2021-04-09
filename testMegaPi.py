  
from megapi import *

def onRead(level):
	rps = float(level)/60
	print("Encoder motor speed Value:%f" %rps);
def getPos(pos):
	value = pos / 6;
	print("Encoder motor position Value:%i" %value);


bot = MegaPi()
bot.start()

bot.encoderMotorPosition(1,getPos);
bot.encoderMotorSetCurPosZero(1);
bot.encoderMotorRun(1,60);
bot.encoderMotorPosition(1,getPos);
#bot.encoderMotorSpeed(1,onRead);
#bot.encoderMotorPosition(1,getPos);
bot.encoderMotorPosition(1,getPos);
sleep(1);
bot.encoderMotorPosition(1,getPos);
bot.encoderMotorRun(1,0);
sleep(2);
bot.encoderMotorPosition(1,getPos);

sleep(1),
bot.encoderMotorSetCurPosZero(1);
while True:
	bot.encoderMotorPosition(1,getPos);
	sleep(0.1);
