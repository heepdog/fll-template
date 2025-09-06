# LEGO SPIKE Prime Python Workspace

This workspace demonstrates how to develop and organize Python programs for the LEGO SPIKE Prime hub using the [LEGO SPIKE Prime extension](https://marketplace.visualstudio.com/items?itemName=legoeducation.lego-spike-prime) in Visual Studio Code.

## Features

- **Slot-based Program Importing:**  
  Use the `importslot` function in [`master.py`](master.py) to dynamically import and execute programs from different slots on the SPIKE Prime hub as Python modules. This allows you to modularize your code and call slot programs directly.

- **Master program:**
  importing all the slots into a list that can be iterated over by pressing the left button to start the next program.  Should modify the program to be able to run the program again or skip forwards or backward in the list.  other modifications to the program would be to show the slot that is being run. on the light matrix

- **Stub Files for IntelliSense:**  
  For better code completion and type checking, set the Python analysis extra paths to point to the stub files from [lego-spike-python-v3-docs](https://github.com/jvolkening/lego-spike-python-v3-docs.git).

## Setup

1. **Install the LEGO SPIKE Prime Extension:**  
   In Visual Studio Code, go to Extensions and search for "LEGO SPIKE Prime". Install the official extension.

2. **Clone the SPIKE Python Stubs:**  
   Download or clone the stubs repository:
   ```
   git clone https://github.com/jvolkening/lego-spike-python-v3-docs.git
   ```
   Note the path to the `stubs` directory.

3. **Configure Python Analysis Extra Paths:**  
   In your workspace settings ([.vscode/settings.json](.vscode/settings.json)), add the path to the stubs:
   ```json
   {
       "python.analysis.extraPaths": [
           "<pathto>/lego-spike-python-v3-docs\\stubs"
       ]
   }
   ```
   This enables IntelliSense and type checking for SPIKE Prime modules.

## Using `importslot` to Call Slot Programs

The [`importslot`](mission5.py) function allows you to import and run programs from other slots as modules:

```py
def importslot(slot_number: str):
    return __import__('/flash/program/' + slot_number + '.program').program
```

Example usage in [`mission5.py`](mission5.py):

```py
mission_list = ['02', '03', '10', '04']
mission_imports = {}

for slot in mission_list:
    try:
        pyfile = importslot(slot)
        mission_imports[slot] = pyfile.main
    except Exception as e:
        print(f'Could not import slot {slot}: {e}')

# Run the main function from slot '02'
mission_imports['02']()
```

## Notes

- Make sure each slot program defines a `main()` function to be callable as shown above.
- The workspace is set up for easy experimentation with slot-based modular programming on the SPIKE Prime hub.

---
For more information, see the [LEGO SPIKE Prime Python API documentation](https://github.com/jvolkening/lego-spike-python-v3-docs).
```
