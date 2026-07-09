from typing import TYPE_CHECKING

from .cog import Player

if TYPE_CHECKING:
    from ballsdex.core.bot import BloxdDexBot


async def setup(bot: "BloxdDexBot"):
    await bot.add_cog(Player(bot))
