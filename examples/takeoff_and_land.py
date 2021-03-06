#!/usr/bin/env python3

import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():

    arm_result, _ = await drone.action.arm()
    print(f"-- Arm result: {arm_result}")

    # We do not need to proceed if the copter did not take off
    if not arm_result:
        return

    takeoff_result, _ = await drone.action.takeoff()
    print(f"-- Takeoff result: {takeoff_result}")

    await asyncio.sleep(5)

    land_result, _ = await drone.action.land()
    print(f"-- Land result: {land_result}")


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
