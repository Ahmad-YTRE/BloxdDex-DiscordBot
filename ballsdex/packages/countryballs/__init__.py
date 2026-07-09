from typing import TYPE_CHECKING

from .cog import BlocksSpawner

if TYPE_CHECKING:
    from ballsdex.core.bot import BloxdDexBot


async def setup(bot: "BloxdDexBot"):
    cog = BlocksSpawner(bot)
    await bot.add_cog(cog)
    await cog.load_cache()
