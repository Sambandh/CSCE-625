from constraint import *

mission_type = {}
m_type =[]
pilot_names = []
pilot_preferences =[]
modelsname = []
pilot_mapping = []
missions = []
models = []
outputfile1=open("op2.txt",'w')
inputfile = open("test2.txt", 'r')
lines = inputfile.readlines()
for line in lines:
    words = line.split()
    a = words[0]
    if (a == 'MT'):
        m_type = words[1]
        possible_models = words[2]
        mission_type[m_type] = possible_models
    elif (a == 'P'):
        pilot_names.append(words[1])
        pilot_mapping.append(words[2])
        pilot_preferences.append(words[3])
    elif (a == 'NUAS'):
        no = words[1]
    elif (a == 'M'):
        missions.append(words[2])
    else:
        models.append(a)

uasset = []
for i in range(len(models)):
    for j in range(int(no[i])):
        uasset.append(models[i]+'_'+str(j))

uasnumber = {}
for i in range(len(uasset)):
    uasnumber[i] = uasset[i]

pilotnumber = {}
for i in range(len(pilot_names)):
    pilotnumber[i] = pilot_names[i]


pilot_uas_map = []
for mapping in pilot_mapping:
    part=[]
    for j in range(len(models)):
        for k in range((int(no[j]))):
            part.append(int(mapping[j]))
    pilot_uas_map.append(part)

pilot_pref_new = []
for pref in pilot_preferences:
    part = []
    for j in range(len(models)):
        for k in range((int(no[j]))):
            part.append(int(pref[j]))
    pilot_pref_new.append(part)

print(pilot_pref_new)

mission_uas_map = {}
for key in mission_type:
    part = []
    for j in range(len(models)):
        for k in range((int(no[j]))):
            part.append(int(mission_type[key][j]))
    mission_uas_map[key] = part

problem = Problem()
for i in range(len(missions)):
    problem.addVariable("uas%d" % i, range(len(uasnumber)))
    problem.addVariable("pilot%d" % i, range(len(pilotnumber)))
    problem.addVariable("mission%d" % i, [i])

for i in range(len(missions)):
    problem.addConstraint(lambda u, p: pilot_uas_map[p][u] == 1, ("uas%d"%i, "pilot%d"%i))

all_pilot = []
for i in range(len(missions)):
    all_pilot.append("pilot%d" % i)

for i in range(len(pilotnumber)):
    problem.addConstraint(SomeNotInSetConstraint([i], len(missions) - 3), all_pilot)


def checker(pilot, pilotnext, uav, uavnext):
    if ((pilot == pilotnext and uav == uavnext) or (pilot != pilotnext and uav != uavnext)):
        return 1
    else:
        return 0


for i in range(len(missions)):
    for j in range(i + 1, len(missions)):
        problem.addConstraint(lambda pilot, pilotnext, uav, uavnext: checker(pilot, pilotnext, uav, uavnext) == 1,
                              ("pilot%d" % i, "pilot%d" % j, "uas%d" % i, "uas%d" % j))

for i in range(len(missions)):
    problem.addConstraint(lambda u, m: mission_uas_map[missions[m]][u] == 1, ("uas%d"%i, "mission%d"%i))

ans = problem.getSolution()

for i in range(len(missions)):
    if(pilot_pref_new[ans["pilot%d" % i]][ans["uas%d" % i]] == "1"):
        match = 'Yes'
    else:
        match = 'No'

    outputfile1.write('M' + str(ans["mission%d" % i]) +'\t'+ str(uasnumber[ans["uas%d"%i]].split('_')[0])+'\t'+str(pilotnumber[ans["pilot%d" % i]])+'\t'+str(match)+'\n')
outputfile1.close()

