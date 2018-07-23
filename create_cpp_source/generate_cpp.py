import json
from pprint import pprint
import glob
import re

def main():
	json_list = glob.glob("json/*.json")
	my_remotes = {}
	for element in json_list:
		with open(element) as f:
			data = json.load(f)
		my_remotes[element] = data
	for remote in my_remotes:
		for value in my_remotes[remote]:
			for remote_name in my_remotes[remote][value]:
				remote_name_adj = re.sub(r'\s+', '_', remote_name)
				file = open("generated_cpp/" + remote_name_adj + ".cpp","w+")
				file.write("#include <" + remote_name_adj +".h" +">\n\n\n")
				file_h = open("generated_cpp/" + remote_name_adj + ".h","w+")
				for action in my_remotes[remote][value][remote_name]:
					function_name = re.sub(r'\s+|\/', '_', action)
					function_name = function_name.lower()
					file_h.write("void " + function_name + "();\n\n")
					file.write("void " + function_name + "()"+"{")
					file.write("\n")
					for x in range(0, len(my_remotes[remote][value][remote_name][action]["off"])):
						file.write("	delayMicroseconds("+my_remotes[remote][value][remote_name][action]["off"][x]+");\n")
						file.write("	pulseIR("+my_remotes[remote][value][remote_name][action]["on"][x]+");\n")
					file.write("}\n\n\n")
				

if __name__ == "__main__":
	main()


