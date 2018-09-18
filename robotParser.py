from urllib.parse import urlparse

file = open("robots.txt")


def canCrawl(url, agentname):
    obj = urlparse(url)
    print(url)

    if agentname not in agents:
        agentname = "*"

    if "Allow" not in agents[agentname] and "Disallow" not in agents[agentname]:
        return True
    else:
        if "Allow" in agents[agentname]:
            for entry in agents[agentname]["Allow"]:
                isstartingwith = obj.path.startswith(entry)
                if isstartingwith:
                    return True
        if "Disallow" in agents[agentname]:
            for entry in agents[agentname]["Disallow"]:
                isstartingwith = obj.path.startswith(entry)
                if isstartingwith:
                    return False
    return True



rows = file.readlines()
agents = {}
cur_agent = ""

for i in rows:
    splitter = i.split(':')

    if splitter[0] == "User-agent":
        agent_name = " ".join(splitter[1].replace("\n", "").split())

        if any(agent_name == name for name in agents):
            pass
            #print("already has it")
        else:
            agents[agent_name] = {}

        cur_agent = agent_name

    elif splitter[0] == "Allow" or splitter[0] == "Disallow":
        #print(splitter[0])
        rule = " ".join(splitter[1].replace("\n", "").split())
        ruleset = agents[cur_agent]
        if any(splitter[0] == cur_ruleset for cur_ruleset in ruleset):
            ruleset[splitter[0]].append(rule)
        else:
            ruleset[splitter[0]] = [rule]

print(agents["*"])

print(canCrawl("https://docs.python.org/3/library/urllib.parse.html", "*"))
print(canCrawl("https://docs.python.org/3/library/urllib.parse.html", "Google"))
