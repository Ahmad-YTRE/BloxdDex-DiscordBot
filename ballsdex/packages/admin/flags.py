import discord
from discord.ext.commands import FlagConverter, Range, flag

from ballsdex.core.utils.transformers import BallTransform, EconomyTransform, RegimeTransform, SpecialTransform
from settings.models import settings


class StatusFlags(FlagConverter):
    status: discord.Status | None = flag(description="The status you want to set")
    name: str | None = flag(description="Title of the activity, if not custom")
    state: str | None = flag(description="Custom status or subtitle of the activity")
    activity_type: discord.ActivityType | None = flag(
        description="The type of activity", default=discord.ActivityType.custom
    )


class RarityFlags(FlagConverter):
    chunked: bool = flag(default=True, description="Group together blocks with the same rarity.")
    include_disabled: bool = flag(
        default=False, description="Include the blocks that are disabled or with a rarity of 0."
    )


class SpawnFlags(FlagConverter):
    block: BallTransform | None = flag(
        description="The block you want to spawn. Random according to rarities if not specified."
    )
    channel: discord.TextChannel | None = flag(
        description="The channel you want to spawn the block in. Current channel if not specified.", default=None
    )
    n: Range[int, 1, 100] = flag(
        description="The number of blocks to spawn. If no block was specified, it's random every time.",
        default=1,
    )
    special: SpecialTransform | None = flag(
        description="Force the block to have a special attribute when mined."
    )
    atk_bonus: int | None = flag(description="Force the block to have a specific attack bonus when mined.")
    hp_bonus: int | None = flag(description="Force the block to have a specific health bonus when mined.")


class GiveBallFlags(FlagConverter):
    block: BallTransform = flag(positional=True, description="The block you want to give")
    special: SpecialTransform | None = flag(description="A special event to set to this card")
    health_bonus: int | None = flag(description="Force a specific health bonus percentage")
    attack_bonus: int | None = flag(description="Force a specific attack bonus percentage")


class BallsCountFlags(FlagConverter):
    user: discord.User | None = flag(description="The player whose blocks you are counting")
    block: BallTransform | None = flag(description="Restrict countring to a specific block")
    special: SpecialTransform | None = flag(description="Restrict counting to a special event")
    deleted: bool = flag(default=False, description="Count the deleted blocks too")


class TradeHistoryFlags(FlagConverter):
    sort_oldest: bool = flag(description='"yes" to have oldest trades first', default=False)
    days: int | None = flag(description="Retrieve entries from the last n days")
    if settings.currency_enabled:
        currency: bool = flag(default=False, description=f"Only show trades that included {settings.currency_plural}")


class UserTradeHistoryFlags(TradeHistoryFlags):
    block: BallTransform | None = flag(description="The block you want to filter the history by")
    user2: discord.User | None = flag(description="The second user you want to check the history of")
    special: SpecialTransform | None = flag(description="The special you want to filter the history by")


class CreateFlags(FlagConverter):
    name: Range[str, None, 48] = flag(description="The name of the block", aliases=["country"])
    health: int = flag(description="The health of the block")
    attack: int = flag(description="The attack of the block")
    rarity: float = flag(description="The rarity of the block, if enabled")
    emoji_id: Range[str, 17, 21] = flag(description="Emoji ID of this block.")
    credits: Range[str, None, 64] = flag(description="Authors of wild card and collection card")
    capacity_name: Range[str, None, 64] = flag(description="Name of the block's capacity")
    capacity_description: Range[str, None, 256] = flag(description="Description of the block's capacity")
    enabled: bool = flag(description="Type 'no' if you don't want this block to spawn.", default=True)
    tradeable: bool = flag(
        description="Type 'no' if you don't want this block to be traded with others.", default=True
    )
    regime: RegimeTransform = flag(description="Political regime of this block")
    economy: EconomyTransform | None = flag(description="Economical regime of this block", default=None)
