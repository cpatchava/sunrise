import requests
import argparse
import sys
from particle import Particle


def main():
	parser = argparse.ArgumentParser(description="Sunrise emulator")
	parser.add_argument('-s' , dest="func_call" , type=str, help="This is the type of led lighting you wish to do")
	args = parser.parse_args()
	bedroom = Particle("29003d000b47353137323334", "d3445998cd1cf79e2fe49700ce395d7c56afff52")
	
	if len(sys.argv[1:]) != 0:
		#we wannado something specific
		print("doing " + args.func_call )
		bedroom.post("led", "arg", args.func_call)
	#bedroom.turn_on()


if __name__ == '__main__':
	main()
