# TEAM PURVI ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "28284695"
    API_HASH = "2fedf2c683513b853cba01854a15d12b"
    #TOKEN = "8253695488:AAHxR9VRkkAxjNvv_hTwC3LzWe6n6qnR5CE"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://Toxicbots:TOXIC0000@cluster0.u5sllsx.mongodb.net/?appName=Cluster0"
    START_PIC = "https://files.catbox.moe/tbk4io.jpg"
    SUDOERS = filters.user(["8299512910"])
