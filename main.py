# McB's Attack Nav JSON Parser

# Imports

import json

# Global Variables

FILE_1="json_files\crowdstrike_apt3_results.json"
FILE_2="json_files\crowdstrike_apt29_results.json"
FILE_3="json_files\crowdstrike_carbanak-fin7_results.json"
FILE_4="json_files\crowdstrike_wizard-spider-sandworm_results.json"

FILE_LIST = [FILE_1, FILE_2, FILE_3, FILE_4]

# Functions

def get_techniques(FILE):

    list1 = FILE['Adversaries']
    for dict1 in list1:
        step1 = dict1['Detections_By_Step']['Scenario_1']['Steps']
        step2 = dict1['Detections_By_Step']['Scenario_2']['Steps']
        for step_nums in step1:
            sub_steps = step_nums['Substeps']
            for sub_step in sub_steps:
                detections = sub_step['Detections']
                for detection in detections:
                    detection_type = detection['Detection_Type']
                    detection_note = detection['Detection_Note']
                deets = {
                    "technique": sub_step['Technique']['Technique_Id'],
                    "sub_technique": sub_step['Subtechnique']['Subtechnique_Id'],
                    "detection_type": detection_type,
                    "detection_note": detection_note,
                }
                tech_list.append(deets)
        for step_nums in step2:
            sub_steps = step_nums['Substeps']
            for sub_step in sub_steps:
                detections = sub_step['Detections']
                for detection in detections:
                    detection_type = detection['Detection_Type']
                    detection_note = detection['Detection_Note']
                deets = {
                    "technique": sub_step['Technique']['Technique_Id'],
                    "sub_technique": sub_step['Subtechnique']['Subtechnique_Id'],
                    "detection_type": detection_type,
                    "detection_note": detection_note,
                }
                tech_list.append(deets)


# Start

tech_list = []

for file in FILE_LIST:
	with open(file, "r") as f1:
		data = json.load(f1)

get_techniques(data)

tech_list2 = sorted(tech_list, key=lambda d: d['technique'])

#print(json.dumps(tech_list2, indent=4))
#print(len(tech_list2))

tech_list3 = []

for i in tech_list2:
    if i not in tech_list3:
        tech_list3.append(i)

tech_list4 = sorted(tech_list3, key=lambda d: d['technique'])
print(json.dumps(tech_list4, indent=4))
print(len(tech_list4))

with open('attack_nav_techs.json', 'w') as file:
    json.dump(tech_list4, file)

# End
