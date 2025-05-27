import json 

with open("/Users/ninofischer/workflows-app-trial-stripe/Spec3/spec3.json") as f:
    spec3 = json.load(f)


CREATE_PATHS = {}
LIST_PATHS = {}
RETRIEVE_PATHS = {}
DELETE_PATHS = {}
UPDATE_PATHS = {}
CUSTOM_PATHS = {}


CREATE_OBJECTS_TYPES = []
LIST_OBJECTS_TYPES = []
RETRIEVE_OBJECTS_TYPES = []
DELETE_OBJECTS_TYPES = []
UPDATE_OBJECTS_TYPES = []
CUSTOM_OBJECTS_TYPES = []

paths = spec3.get("paths")
for path, actions in paths.items():
    for action, params in actions.items():
        
       
        summary = params.get("summary")
        if "Create" in str(summary):
            actions ={}
            actions[action] = params
            CREATE_PATHS[path]=actions 
        elif "List" in str(summary):
            actions ={}
            actions[action] = params
            LIST_PATHS[path]=actions
        elif "Retrieve" in str(summary):
            actions ={}
            actions[action] = params
            RETRIEVE_PATHS[path]=actions
        elif "Delete" in str(summary):
            actions ={}
            actions[action] = params
            DELETE_PATHS[path]=actions  

        elif "Update" in str(summary):
            actions ={}
            actions[action] = params
            UPDATE_PATHS[path]=actions
        else:
            actions ={}
            actions[action] = params
            CUSTOM_PATHS[path]=actions


            
        
        # elif "List" in str(summary):
        #     LIST_PATHS.append(path)
        # elif "Retrieve" in str(summary):
        #     RETRIEVE_PATHS.append(path)
        # elif "Delete" in str(summary):
        #     DELETE_PATHS.append(path)
        # elif "Update" in str(summary):
        #     UPDATE_PATHS.append(path)
        # else:
        #     CUSTOM_PATHS.append(path)



# CREATE_OBJECTS_TYPES = [ path.split("/")[2] for path in CREATE_PATHS]
# LIST_OBJECTS_TYPES = [ path.split("/")[2] for path in LIST_PATHS]
# RETRIEVE_OBJECTS_TYPES = [ path.split("/")[2] for path in RETRIEVE_PATHS]
# DELETE_OBJECTS_TYPES = [ path.split("/")[2] for path in DELETE_PATHS]
# UPDATE_OBJECTS_TYPES = [ path.split("/")[2] for path in UPDATE_PATHS]
# CUSTOM_OBJECTS_TYPES = [ path.split("/")[2] for path in CUSTOM_PATHS]



# print(CREATE_OBJECTS_TYPES)
# print(LIST_OBJECTS_TYPES)
# print(RETRIEVE_OBJECTS_TYPES)
# print(DELETE_OBJECTS_TYPES)
# print(UPDATE_OBJECTS_TYPES)
# print(CUSTOM_OBJECTS_TYPES)

# print(f"CREATE_PATHS: {CREATE_PATHS}")
# print(f"LIST_PATHS: {LIST_PATHS}")
# print(f"RETRIEVE_PATHS: {RETRIEVE_PATHS}")
# print(f"DELETE_PATHS: {DELETE_PATHS}")
# print(f"UPDATE_PATHS: {UPDATE_PATHS}")
# print(f"CUSTOM_PATHS: {CUSTOM_PATHS}")


# for path in CREATE_PATHS:
#     print(path)

for paths,actions in LIST_PATHS.items():
   for action,params in actions.items():
      print("Parameters: ",params.get("parameters"),"\n\n\n")
      print("Request Body: ",params.get("requestBody"),"\n\n\n")
      
n_obj_c=0
for obj in CREATE_OBJECTS_TYPES:
    n_obj_c+=1
   
print(n_obj_c)




    









