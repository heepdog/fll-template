# LEGO slot:5 autostart

from hub import button

# while not button.pressed(button.LEFT):
#     pass

mission_list = ['02', '03', '10', '04']
mission_imports = {}
def importslot(slot_number: str):
    return __import__('/flash/program/' + slot_number+ '.program').program


# current_path = os.getcwd()
# sys.path.append('/flash/program')

# num2 = __import__('02.program').program

for slot in mission_list:
    print(f'adding {slot}')
    try:
        pyfile = importslot(slot)
        try:
            mission_imports[slot] = pyfile.main
        except Exception as e:
            print(f'import {slot} does not contain main(): {e}')
    except Exception as e:
        print(f'Could not import slot {slot}: {e}')


mission_imports[mission_list[0]]()
# print(dir(num2))
# mission_imports(mission_list[1]).run2()

