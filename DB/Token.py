import json

def Token():
    with open("DB/Config.json", "r") as f:
        data = json.load(f)
    return data["Token"]

def New_token():
    print("\nSieht so aus als würde der Token nicht funktionieren.\n")
    text: str = input("Möchtest du einen neuen Token hinzufügen? (Ja/Nein) >> ")
    match text.lower().replace(" ", ""):
        case "ja":
            print('\nDu kannst es immer mit "c", "cancel", "abbrechen" oder "stop" abbrechen')
            text: str = input("Gebe den neuen Token hier an >> ")
            match text:
                case text if text.lower().replace(" ", "") in ["c", "cancel", "abbrechen", "stop"]:
                    print("\nIch hab es abgebrochen")
                case _:
                    with open("DB/Config.json", "r") as f:
                        data = json.load(f)
                        data["Token"] = text
                    with open("DB/Config.json", "w") as f:
                        json.dump(data, f, indent=4)
                        print(f'\n"{text}" wurde gespeichert')
                        print("\nWenn es nun funktioniert, werden Sie diese Nachricht nicht mehr sehen")
        case "nein":
            print("\nIch werde es abbrechen")
