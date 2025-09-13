# LEGO slot:19 autostart

from hub import light_matrix
import runloop
broadcast_up = ''
print('setting up')

async def sleepfor():
    global broadcast_up
    await runloop.sleep_ms(1000)
    broadcast_up = 'broadcast_up'
    await runloop.sleep_ms(1)
    print("runloop sleep for")
    await runloop.sleep_ms(2000)
    broadcast_up = 'broadcast_up'
    await runloop.sleep_ms(5000)
    broadcast_up = 'exit'

async def runto():
    print("runto") 
    await runloop.sleep_ms(5000) 
    print("next runto")

def main():
    runloop.run(maina())
    print('done with main')

async def maina():
   # write your code here
   await light_matrix.write("Hi!")
   runloop.run(sleepfor(),runto(),listenforbroadcast())
   print('done with asyncs')
   future = runto()


async def listenforbroadcast():
    global broadcast_up
    while True:
        await runloop.sleep_ms(1)
        if broadcast_up == 'broadcast_up':
            print('sending up')
            broadcast_up = ''

        if broadcast_up == 'exit':
            break




if __name__ == "__main__":
    main()
    # runloop.run(main())
    # print("exit code")
