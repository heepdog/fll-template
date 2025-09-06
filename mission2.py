# LEGO slot:02 autostart

from hub import button
import runloop

def main():
    runloop.run(main2())

async def main2():
    print('running from 2 ')


if __name__ == '__main__':
    main()
    print("running from main")
    