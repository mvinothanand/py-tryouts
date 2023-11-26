import json
from pathlib import Path

def main():
  input_file = Path("/home/vinoth/git-repositories/conman-dev/db/projects.json")
  if input_file.exists():
    with open(input_file, "r") as fp:
      input_data = json.load(fp)
  else:
    print("Input file doesn't exist")
  
  transformed_data = []
  for item in input_data:
    if not item["title"] == "Project - A":
      continue

    activities = item["activities"]
    for activity in activities:
      pid, billing, description, plannedSchedule, actualSchedule, pcntCompl, projectedStart, projectedEnd = ( 
        activity["id"], 
        activity["billing"], 
        activity["description"], 
        activity["plannedSchedule"], 
        activity["actualSchedule"],
        activity["completionPercent"],
        activity["projectedSchedule"]["projectedStart"],
        activity["projectedSchedule"]["projectedEnd"]
      )

      transformed_data.append({
        "id": pid,
        "bill": billing,
        "description": description,
        "earlyStart": plannedSchedule["earlyStart"],
        "earlyEnd": plannedSchedule["earlyEnd"],
        "lateStart": plannedSchedule["lateStart"],
        "lateEnd": plannedSchedule["lateEnd"],
        "actualStart": actualSchedule["actualStart"],
        "actualEnd": actualSchedule["actualEnd"],
        "pcntCompl": pcntCompl,
        "projectedStart": projectedStart,
        "projectedEnd": projectedEnd
      })

  #print(transformed_data)
  output_file = Path("/home/vinoth/git-repositories/conman-dev/db/activities.json")
  with open(output_file, "w") as fp:
    fp.write(json.dumps(transformed_data, indent=2))


if __name__ == "__main__":
  main()