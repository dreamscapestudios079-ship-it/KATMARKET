# ── Python 3.13 audioop compatibility shim ──────────────────────────────────
import sys as _sys
if _sys.version_info >= (3, 13):
    try:
        import audioop
    except ModuleNotFoundError:
        try:
            import importlib as _il
            _audioop = _il.import_module("audioop_lts")
            _sys.modules.setdefault("audioop", _audioop)
        except ModuleNotFoundError:
            from types import ModuleType as _MT
            _stub = _MT("audioop")
            for _fn in (
                "add", "adpcm2lin", "alaw2lin", "avg", "avgpp", "bias",
                "byteswap", "cross", "findfactor", "findfit", "findmax",
                "getsample", "lin2adpcm", "lin2alaw", "lin2lin", "lin2ulaw",
                "max", "maxpp", "minmax", "mul", "ratecv", "reverse", "rms",
                "tomono", "tostereo", "ulaw2lin",
            ):
                setattr(_stub, _fn, lambda *a, **k: b"")
            _sys.modules["audioop"] = _stub
# ─────────────────────────────────────────────────────────────────────────────

import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.ui import View, Button, Modal, TextInput, Select
import os, json, asyncio, time, random, uuid
from datetime import datetime, timedelta, timezone
import re
import aiohttp

# --- INSERT ALL YOUR COMMANDS, VIEWS, AND MODALS HERE ---

# ─────────────────────────────────────────────
#  RUN
# ─────────────────────────────────────────────
if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ DISCORD_TOKEN environment variable is not set.")
    else:
        bot.run(TOKEN)
