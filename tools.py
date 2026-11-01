from livekit.agents import RunContext, function_tool
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_FROM_NUMBER,
    EMERGENCY_CONTACT
)

# -------- SYSTEM IMPORTS -------- #
import os
import cv2
import pyautogui
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


# =========================================================
# 🚨 EMERGENCY CALL (YOUR CODE - CLEANED)
# =========================================================
@function_tool
async def Emergency_Call(context: RunContext, query: str) -> str:
    """
    Trigger an emergency call using Twilio API.
    """
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = """
        Emergency detected at home.
        Location link has been sent to your phone.
        I repeat, emergency detected.
        """

        response = VoiceResponse()
        response.say(message, voice='alice')

        client.calls.create(
            to=EMERGENCY_CONTACT,
            from_=TWILIO_FROM_NUMBER,
            twiml=str(response),
            timeout=20,
        )

        return "🚨 Emergency call initiated successfully."

    except Exception as e:
        return f"Emergency call failed: {str(e)}"


# =========================================================
# 🖥️ SYSTEM CONTROL TOOLS
# =========================================================

# -------- OPEN APP -------- #
@function_tool
async def Open_App(context: RunContext, app_name: str) -> str:
    apps = {
     "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "command prompt": "cmd.exe",
    "powershell": "powershell.exe",
    "file explorer": "explorer.exe",
    "task manager": "taskmgr.exe",
    "control panel": "control.exe",
    "registry editor": "regedit.exe",
    "snipping tool": "snippingtool.exe",
     "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    }

    app_name = app_name.lower()

    if app_name in apps:
        os.startfile(apps[app_name])
        return f"{app_name} opened"

    return "App not found"


# -------- CAMERA -------- #
@function_tool
async def Take_Photo(context: RunContext) -> str:
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()

    if ret:
        cv2.imwrite("photo.jpg", frame)
        cam.release()
        return "📸 Photo captured and saved"

    return "Camera error"


# -------- VOLUME CONTROL -------- #
@function_tool
async def Set_Volume(context: RunContext, level: int) -> str:
    try:
        level = max(0, min(level, 100))
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        volume.SetMasterVolumeLevelScalar(level / 100, None)

        return f"🔊 Volume set to {level}%"

    except Exception as e:
        return f"Volume error: {str(e)}"


# -------- SHUTDOWN -------- #
@function_tool
async def Shutdown_System(context: RunContext) -> str:
    os.system("shutdown /s /t 5")
    return "⚠️ System will shutdown in 5 seconds"


# -------- RESTART -------- #
@function_tool
async def Restart_System(context: RunContext) -> str:
    os.system("shutdown /r /t 5")
    return "🔄 System will restart in 5 seconds"


# -------- KEYBOARD -------- #
@function_tool
async def Type_Text(context: RunContext, text: str) -> str:
    pyautogui.write(text)
    return "⌨️ Typed successfully"


# -------- MOUSE -------- #
@function_tool
async def Move_Mouse(context: RunContext, x: int, y: int) -> str:
    pyautogui.moveTo(x, y)
    return f"🖱️ Mouse moved to {x}, {y}"
