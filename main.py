# import asyncio
from fastapi import FastAPI, Request
import subprocess

app = FastAPI()
gate_status = 0


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
    global gate_status

    # data = await request.json()
    # if data[0]["camera"] == 19:
    if gate_status == 0:
        await open()
        gate_status += 1

    elif gate_status == 1:
        await close()
        gate_status -= 1

    return {"message": "Okey"}


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
