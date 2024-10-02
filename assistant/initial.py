# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying Darky Userbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About Darky**

🧿 Darky is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@Elite_kirito**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/Elite_kirito)
-> [Keeping Custom Addons Repo](https://t.me/Elite_kirito)
-> [Disabling Deploy message](https://t.me/Elite_kirito)
-> [Setting up TimeZone](https://t.me/Elite_kirito)
-> [About Inline PmPermit](https://t.me/Elite_kirito)
-> [About Dual Mode](https://t.me/Elite_kirito)
-> [Custom Thumbnail](https://t.me/Elite_kirito)
-> [About FullSudo](https://t.me/Elite_kirito)
-> [Setting Up PmBot](https://t.me/Elite_kirito)
-> [Also Check](https://t.me/Elite_kirito)

**• To Know About Updates**
  - Join @botzz_x_hub.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@botzz_x_hub**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
