import discord
from discord.ext import commands

from ballsdex.core.bot import BloxdDexBot
from ballsdex.core.utils import checks


@commands.hybrid_group()
@checks.has_permissions("admincmd.logs")
async def logs(ctx: commands.Context[BloxdDexBot]):
    """
    Bot logs management
    """
    await ctx.send_help(ctx.command)


@logs.command(name="mininglogs")
@checks.has_permissions("admincmd.logs")
async def logs_add(ctx: commands.Context[BloxdDexBot], user: discord.User):
    """
    Add or remove a user from mining logs.

    Parameters
    ----------
    user: discord.User
        The user you want to add or remove to the logs.
    """
    if user.id in ctx.bot.catch_log:
        ctx.bot.catch_log.remove(user.id)
        await ctx.send(f"{user} removed from mining logs.", ephemeral=True)
    else:
        ctx.bot.catch_log.add(user.id)
        await ctx.send(f"{user} added to mining logs.", ephemeral=True)


@logs.command(name="commandlogs")
@checks.has_permissions("admincmd.logs")
async def commandlogs_add(ctx: commands.Context[BloxdDexBot], user: discord.User):
    """
    Add or remove a user from command logs.

    Parameters
    ----------
    user: discord.User
        The user you want to add or remove to the logs.
    """
    if user.id in ctx.bot.command_log:
        ctx.bot.command_log.remove(user.id)
        await ctx.send(f"{user} removed from command logs.", ephemeral=True)
    else:
        ctx.bot.command_log.add(user.id)
        await ctx.send(f"{user} added to command logs.", ephemeral=True)
