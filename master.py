# LEGO slot:5 autostart

from hub import button
import asyncio

mission_list = ['02', '19', '15']
mission_imports = {}

def importslot(slot_number: str):
    return __import__('/flash/program/' + slot_number+ '.program').program


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


async def run_mission(slot_number: str):
    if slot_number in mission_imports:
        print(f'Starting mission {slot_number}')
        try:
            # await mission_imports[slot_number]()
            mission_imports[slot_number]()
        except Exception as e:
            print(f'Error running mission {slot_number}: {e}')
    else:
        print(f'Mission {slot_number} not found')

async def run_next_mission(event, delay):
    for slot in mission_list:
        try:
            await asyncio.wait_for(event.wait(), timeout=delay)
            print('Button pressed, skipping wait.')
            event.clear()
        except asyncio.TimeoutError:
            pass

        await run_mission(slot)
        print(f'Waiting {delay} seconds before next mission...')

    print('All missions completed, exiting.')

async def get_button_press(event):
    while True:
        while not button.pressed(button.LEFT):
            await asyncio.sleep(0.1)
        event.set()
        while button.pressed(button.LEFT):
            await asyncio.sleep(0.1)

async def main():
    event = asyncio.Event()
    print('creating tasks')
    tasks = [
        asyncio.create_task(run_next_mission(event, 100)),
        asyncio.create_task(get_button_press(event))
    ]
    await asyncio.gather(tasks[0])
    

if __name__ == "__main__":
    print('Starting mission runner\n')
    asyncio.run(main())

