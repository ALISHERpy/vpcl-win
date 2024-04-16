# import asyncio
from fastapi import FastAPI, Request
import subprocess

app = FastAPI()
back_side = ["back", 'Rear']
front_side = ["front"]


async def open():
    cmd_file_path = 'port1_on.cmd'
    subprocess.call(cmd_file_path, shell=True)
    cmd_file_path = 'port1_off.cmd'
    subprocess.call(cmd_file_path, shell=True)


async def close():
    cmd_file_path = 'ikkinchi_on.cmd'
    subprocess.call(cmd_file_path, shell=True)
    cmd_file_path = 'ikkinchi_off.cmd'
    subprocess.call(cmd_file_path, shell=True)


async def stop():
    cmd_file_path = 'stop_wdt.cmd'
    subprocess.call(cmd_file_path, shell=True)


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    orientation_info = data[0]['features']['orientation']
    # print(orientation_info['name'])

    if orientation_info['name'] in front_side:
        await open()
        return {"message": "It has been Opened"}

    elif orientation_info['name'] in back_side:
        await close()
        return {"message": "It has been closed"}
    else:
        return {"message": "Error no thing is clear"}


@app.post("/open")
async def open_button():
    await open()
    return 'its opened'


@app.post("/close")
async def close_button():
    await close()
    return 'its closed'


@app.post("/stop")
async def close_button():
    await stop()
    return 'it has been stop'
