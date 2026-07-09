from typing import TYPE_CHECKING

from .cog import Config

if TYPE_CHECKING:
    from ballsdex.core.bot import BloxdDexBot


async def setup(bot: "BloxdDexBot"):
    await bot.add_cog(Config(bot))
