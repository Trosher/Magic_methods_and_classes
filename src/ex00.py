class Key():
    def __len__ (self):
        return 1337
    
    def __getitem__ (self, key):
        return 3 if key == 404 else 0
    
    def __gt__ (self, other):
        return True if other == 9000 else False
    
    def __getattr__ (self, name):
        return "zax2rulez" if name == "passphrase" else ""
    
    def __str__ (self):
        return "GeneralTsoKeycard"
    
def main():
    key = Key()
    if len(key) == 1337:
        print("[SUCCESS] len(key) == 1337")
    else:
        print("[FAILED] len(key) == 1337")
        
    if key[404] == 3:
        print("[SUCCESS] key[404] == 3")
    else:
        print("[FAILED] key[404] == 3")
        
    if key > 9000:
        print("[SUCCESS] key > 9000")
    else:
        print("[FAILED] key > 9000")
        
    if key.passphrase == "zax2rulez":
        print("[SUCCESS] key.passphrase == 'zax2rulez'")
    else:
        print("[FAILED] key.passphrase == 'zax2rulez'")
        
    if str(key) == "GeneralTsoKeycard":
        print("[SUCCESS] str(key) == 'GeneralTsoKeycard'")
    else:
        print("[FAILED] str(key) == 'GeneralTsoKeycard'")

if __name__ == "__main__":
    main()