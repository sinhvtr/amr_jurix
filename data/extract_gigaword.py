import json
import sys

num_instances = sys.argv[1]
print("Number of instances to be extracted: ", num_instances)
num_instances = int(num_instances)
with open("gigaword/2m.json", "rU") as f:
    all_instances = json.load(f)
print("All instances loaded")
with open("gigaword/"+str(num_instances)+".json", "w") as f:
    json.dump(all_instances[:num_instances], f, indent=2)
