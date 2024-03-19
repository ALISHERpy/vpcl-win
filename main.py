import asyncio
from fastapi import FastAPI, Request
import subprocess


async def open1():
    cmd_file_path = 'port1_on.cmd'
    subprocess.call(cmd_file_path, shell=True)


async def close1():
    cmd_file_path = 'port1_off.cmd'
    subprocess.call(cmd_file_path, shell=True)


async def open2():
    cmd_file_path = 'ikkinchi_on.cmd'
    subprocess.call(cmd_file_path, shell=True)


async def close2():
    cmd_file_path = 'ikkinchi_off.cmd'
    subprocess.call(cmd_file_path, shell=True)


async def stop():
    cmd_file_path = 'stop_wdt.cmd'
    subprocess.call(cmd_file_path, shell=True)


app = FastAPI()
gate_status = 0


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    global gate_status
    if data[0]["camera"] == 19:

        if gate_status == 0:
            await open1()
            await asyncio.sleep(15)  ####
            await close1()

            gate_status += 1
        elif gate_status == 1:
            await close1()
            gate_status -= 1

    if data[0]["camera"] == 20:
        if gate_status == 0:
            await open1()
            await asyncio.sleep(15)  ###
            await close1()

            gate_status += 1
        elif gate_status == 1:
            await close1()
            gate_status -= 1

    return {"message": "Okey"}


@app.post("/open")
async def open_button():
    await open1()
    await asyncio.sleep(1)
    await close1()
    return 'its opened'


@app.post("/close")
async def close_button():
    await open2()
    await asyncio.sleep(1)
    await close2()
    return 'its closed'


@app.post("/stop")
async def close_button():
    await stop()
    return 'it has been stop'
