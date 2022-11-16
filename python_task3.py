import sys
from pathlib import Path

PATH_LOGS = Path('./' + sys.argv[1])

def extract_logs(path_to_logs_file: Path) -> list[str]:
    return path_to_logs_file.read_text().splitlines()

def get_user_agents(logs: list[str]) -> dict:
    agents_dict = {}
    for line in logs:
        agent = line.split("\"")[5]
        if agent is "-":
            continue

        if agent in agents_dict:
            agents_dict[agent] += 1
        else:
            agents_dict[agent] = 1 
    return agents_dict

logs = extract_logs(PATH_LOGS)
agents_dict = get_user_agents(logs)
            
print(f'Number of agents: {len(agents_dict)}')

for key, value in agents_dict.items():
    print(f'Occurences: {value}\t| Agent: {key}')