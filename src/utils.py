import discord
import logging
import os

logger = logging.getLogger(__name__)
APPROVED_FILE = "./data/approved.txt"
os.makedirs(os.path.dirname(APPROVED_FILE), exist_ok=True)

try:
    with open(APPROVED_FILE, "r") as f:
        approved_users = {line.strip() for line in f if line.strip()}
except FileNotFoundError:
    approved_users = set()


def is_user_approved(user_id: str) -> bool:
    return user_id in approved_users


def whitelist_user(user_id: str) -> bool:
    if is_user_approved(user_id):
        return False

    with open(APPROVED_FILE, "a") as f:
        f.write(f"{user_id}\n")

    approved_users.add(user_id)

    return True


def remove_whitelisted_user(user_id: str) -> bool:
    if not is_user_approved(user_id):
        return False

    approved_users.discard(user_id)

    with open(APPROVED_FILE, "w") as f:
        for user in approved_users:
            f.write(f"{user}\n")

    return True


def create_media_embed(user: discord.User, caption: str | None, url: str):
    embed = discord.Embed(
        color=discord.Color.from_rgb(85, 125, 135),
        title=caption,
        description=f"> _Original by_ : <@{user.id}>\n> _Source_:||{url}||",
    )
    return embed
