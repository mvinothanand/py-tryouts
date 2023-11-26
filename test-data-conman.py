from datetime import date, timedelta
import json

def form_data_set(start_date, end_date, duration):
  # dataset = [{ "date": str(start_date), "percentCompletion": 0.00 }]
  dataset = []
  for i in range(duration + 1):
    item = { 
            "date": (start_date + timedelta(days=i)).strftime("%Y-%m-%d"),
            "percentCompletion": round(i/duration * 100, 2)
          }
    dataset.append(item)
  return dataset

def main():
  duration_days = 60
  duration_td = timedelta(days=duration_days)
  early_start_date_str = "2023-11-01"
  # early_start_date_obj = date(*early_start_date_str.split("-"))
  early_start_date_obj = date.fromisoformat(early_start_date_str) 
  late_start_date_str = "2023-11-10"
  late_start_date_obj = date.fromisoformat(late_start_date_str)

  early_end_date = early_start_date_obj + duration_td
  print(f"early_end_date: {early_end_date}")
  late_end_date = late_start_date_obj + duration_td
  print(f"late end date: {late_end_date}") 

  dataset = form_data_set(late_start_date_obj, late_end_date, duration_days)
  #print(dataset)

  output_file = "./conman_data.json"
  with open(output_file, "w") as fp:
    fp.write(json.dumps(dataset, indent=2,ensure_ascii=False))


if __name__ == "__main__":
  main()