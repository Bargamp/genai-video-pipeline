import json
import os
import time

def save_run(data, output_dir, run_id: str):
    os.makedirs(output_dir, exist_ok=True)

    data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
    data["run_id"] = run_id
    with open(os.path.join(output_dir, f"run_{run_id}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)