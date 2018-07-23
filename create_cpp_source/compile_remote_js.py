import json
import glob
import re
import pprint

def main():
    my_list = glob.glob("remote_codes/*.txt")
    
    for element in my_list:
        curr_dict = {}
        curr_remote_file =  open(element)
        action_array_set = None #if we are too lazy and dont wanna specify each button
        for line in curr_remote_file:
            if 'remote' not in curr_dict and re.search("REMOTE" , line): #keyword for remote
                remote_name = line.split(':')[1].rstrip().lstrip()
                remote_data = {remote_name : {}}
                curr_dict['remote'] = remote_data
    #        if re.search("ACTION_ARRAY", line): #keyword for a whole row, too lazy to name all colors
     #           action_array_name = line.split(":")[1].rstrip().lstrip()
      #          action_array_data = {action_array_name : {}}
       #         curr_dict['remote'][remote_name]['action_grid_list'] = action_array_data
        #        action_array_set = True
            elif re.search("ACTION", line): #keyword for action
                on_off = {'off' : [], 'on' : []}
                action_name = line.split(":")[1].rstrip().lstrip()
                curr_dict['remote'][remote_name][action_name] = on_off
                action_array_set = None
#            if re.search("_row", line): #we are in the first set of row
 #               on_off = {'off' : [], 'on' : []}
  #              row_name = line.split("_")[1].rstrip().lstrip()
   #             curr_dict['remote'][remote_name]['action_grid_list'][row_name] = on_off
            if re.search('usec', line):#keyword for IR off/on values
                re.sub(r'\s+', '', line)
                line = line.rstrip("usec").lstrip()
                line = line.lstrip()
                off = line.split(",")[0].rstrip("usec")
                on = line.split(",")[1].rstrip().rstrip("usec")
                if action_array_set :
                    curr_dict['remote'][remote_name]['action_grid_list'][row_name]['off'].append(off)
                    curr_dict['remote'][remote_name]['action_grid_list'][row_name]['on'].append(on)
                else:    
                    curr_dict['remote'][remote_name][action_name]['off'].append(off)
                    curr_dict['remote'][remote_name][action_name]['on'].append(on)
        r = json.dumps(curr_dict)
        parsed = json.loads(r)
        
        with open('json/'+re.sub(r'\s+','_', remote_name)+'.json', 'w+') as handle:
            json.dump(parsed, handle, indent=4, sort_keys=True)

if __name__ == "__main__":
    main()
