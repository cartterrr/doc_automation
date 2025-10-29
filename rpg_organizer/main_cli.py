from .commands import RPGManager

def print_help():
    print("Команды:")
    print("  help")
    print("  chars                    - список персонажей")
    print("  char add <name>          - добавить персонажа")
    print("  char rm <id>             - удалить персонажа")
    print("  items                    - список предметов")
    print("  item add <name>          - добавить предмет")
    print("  quests                   - список квестов")
    print("  quest add <title>        - добавить квест")
    print("  give <char_id> <item_id> - дать предмет персонажу")
    print("  exit / quit              - выйти")

def main():
    mgr = RPGManager()
    print("RPG Organizer CLI v0.1")
    print_help()
    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print('\\nВыход')
            break
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0] == "help":
            print_help()
        elif parts[0] == "chars":
            for c in mgr.list_characters():
                print(f"{c['id']}: {c['name']} (Lv {c.get('level',1)})")
        elif parts[0] == "char" and len(parts) >= 2:
            if parts[1] == "add":
                name = " ".join(parts[2:]) or "Unnamed"
                c = mgr.add_character(name)
                print("Created:", c.id, c.name)
            elif parts[1] == "rm" and len(parts) >= 3:
                cid = parts[2]
                ok = mgr.remove_character(cid)
                print("Removed" if ok else "Not found")
            else:
                print("Unknown char command")
        elif parts[0] == "items":
            for it in mgr.list_items():
                print(f"{it['id']}: {it['name']} ({it.get('type')})")
        elif parts[0] == "item" and len(parts) >= 2 and parts[1] == "add":
            name = " ".join(parts[2:]) or "Unnamed Item"
            it = mgr.add_item(name)
            print("Created item:", it.id, it.name)
        elif parts[0] == "quests":
            for q in mgr.list_quests():
                print(f"{q['id']}: {q['title']} [{q.get('status')}]")
        elif parts[0] == "quest" and len(parts) >= 2 and parts[1] == "add":
            title = " ".join(parts[2:]) or "Untitled"
            q = mgr.add_quest(title)
            print("Created quest:", q.id, q.title)
        elif parts[0] == "give" and len(parts) == 3:
            cid, iid = parts[1], parts[2]
            try:
                mgr.give_item_to_character(cid, iid)
                print("Given")
            except Exception as e:
                print("Error:", e)
        elif parts[0] in ("exit", "quit"):
            print("Bye")
            break
        else:
            print("Unknown command. Type 'help'.")

if __name__ == "__main__":
    main()
