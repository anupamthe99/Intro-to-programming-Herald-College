try:
    with open('datafile.txt','r') as f:
        print(f.read())
except FileNotFoundError:
    print("filed not found")
except PermissionError:
    print("No permission man ")
except Exception as e:
    print(f"failed to run",e)

