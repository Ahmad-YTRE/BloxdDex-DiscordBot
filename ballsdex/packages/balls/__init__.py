from typing import TYPE_CHECKING

from .cog import Balls

if TYPE_CHECKING:
    from ballsdex.core.bot import BloxdDexBot


async def setup(bot: "BloxdDexBot"):
    await bot.add_cog(Balls(bot))
