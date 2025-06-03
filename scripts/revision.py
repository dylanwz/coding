#!/usr/bin/env python3

import sys
import json
from datetime import datetime, timedelta

FILE = "revision.json"
TODAY = datetime.today().date()

def load():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)

def check():
    data = load()
    print("📚 Problems to review today:")
    due = False
    for prob, meta in data.items():
        next_review = datetime.strptime(meta["next_review"], "%Y-%m-%d").date()
        if TODAY >= next_review:
            print(f" - {prob}")
            due = True
    if not due:
        print("🎉 You're all caught up!")

def due():
    data = load()
    for prob, meta in data.items():
        next_review = datetime.strptime(meta["next_review"], "%Y-%m-%d").date()
        if TODAY >= next_review:
            print(f"{prob}: due today or earlier (next_review = {meta['next_review']})")

def update(problem, quality):
    data = load()
    if problem not in data:
        print(f"❌ Problem '{problem}' not found.")
        return

    quality = int(quality)
    if not (0 <= quality <= 5):
        print("❌ Quality must be between 0 and 5.")
        return

    item = data[problem]
    repetition = item.get("repetition", 0)
    interval = item.get("interval", 1)
    ef = item.get("ef", 2.5)

    if quality >= 3:
        if repetition == 0:
            interval = 1
        elif repetition == 1:
            interval = 6
        else:
            interval = round(interval * ef)
        repetition += 1
    else:
        interval = 1
        repetition = 0

    # Update EF (easiness factor)
    ef = ef + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    ef = max(1.3, ef)

    item["last_reviewed"] = TODAY.strftime("%Y-%m-%d")
    item["next_review"] = (TODAY + timedelta(days=interval)).strftime("%Y-%m-%d")
    item["interval"] = interval
    item["repetition"] = repetition
    item["ef"] = round(ef, 2)

    save(data)
    print(f"✅ Updated '{problem}' with quality={quality}. Next review: {item['next_review']}")

def add(problem, quality=None):
    data = load()
    if problem in data:
        print("⚠️ Already exists.")
        return
    data[problem] = {
        "last_reviewed": TODAY.strftime("%Y-%m-%d"),
        "next_review": TODAY.strftime("%Y-%m-%d"),
        "interval": 0,
        "repetition": 0,
        "ef": 2.5
    }
    save(data)
    if quality:
        update(problem, quality)
    else:
        print(f"✅ Added '{problem}' to schedule.")

def remove(problem):
    data = load()
    if problem not in data:
        print(f"❌ Problem '{problem}' not found.")
        return
    del data[problem]
    save(data)
    print(f"🗑️ Removed '{problem}' from schedule.")

def purge():
    confirm = input("⚠️ Are you sure you want to delete all tracked problems? (yes/no): ").strip().lower()
    if confirm == "yes":
        save({})
        print("🧼 All problems have been purged.")
    else:
        print("❌ Purge cancelled.")


def list_all():
    data = load()
    if not data:
        print("No problems are currently being tracked.")
        return
    print("📋 All tracked problems:")
    for prob, meta in data.items():
        print(f"{prob:25} next: {meta['next_review']} | ef: {meta['ef']} | interval: {meta['interval']}d")

def help():
    print("Usage:")
    print("  revise check                     # See what’s due today")
    print("  revise due                       # See overdue problems")
    print("  revise add <problem>             # Start tracking a new problem")
    print("  revise update <problem> <0–5>    # Log a review with quality")
    print("  revise list                      # View all tracked problems")
    print("  revise remove <problem>          # Delete a problem")
    print("  revise purge                     # Delete all problems")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        help()
    elif args[0] == "check":
        check()
    elif args[0] == "due":
        due()
    elif args[0] == "update" and len(args) == 3:
        update(args[1], args[2])
    elif args[0] == "add" and len(args) == 2:
        add(args[1])
    elif args[0] == "remove" and len(args) == 2:
        remove(args[1])
    elif args[0] == "purge":
        purge()
    elif args[0] == "list":
        list_all()
    else:
        help()
