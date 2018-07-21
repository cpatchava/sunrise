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
		print()
		print(remote)
		for value in my_remotes[remote]:
			print(value)
			for remote_name in my_remotes[remote][value]:
				remote_name_adj = re.sub(r'\s+', '_', remote_name)
				print("remote_name: " + remote_name_adj)
				file = open("generated_cpp/" + remote_name_adj + ".cpp")
				for actions in my_remotes[remote][value][remote_name]:
					for x in range(0, len(actions["off"])):
						print(actions[x])
					
				
				
				#print(len(my_remotes["json/white_remote.json"]["remote"]["white remote"]))

if __name__ == "__main__":
	main()


