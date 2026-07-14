import discord
from discord.ext import commands
from discord import app_commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # أمر 8ball (الكرة الثمانية)
    @app_commands.command(name='8ball', description='اسأل الكرة الثمانية')
    async def eight_ball(self, interaction: discord.Interaction, question: str):
        responses = [
            "نعم بالتأكيد 🎉",
            "لا على الإطلاق 🚫",
            "ربما... 🤔",
            "بالتأكيد! ✅",
            "لا أعتقد ذلك ❌",
            "يبدو جيدا 👍",
            "لا فرصة 😔",
            "يقول لا... 🎱"
        ]
        
        embed = discord.Embed(
            title="🎱 الكرة الثمانية",
            description=f"**السؤال:** {question}\n**الإجابة:** {random.choice(responses)}",
            color=discord.Color.purple()
        )
        await interaction.response.send_message(embed=embed)
    
    # أمر Dice (رمي النرد)
    @app_commands.command(name='dice', description='رمي النرد')
    async def dice(self, interaction: discord.Interaction):
        result = random.randint(1, 6)
        embed = discord.Embed(
            title="🎲 النرد",
            description=f"النتيجة: **{result}**",
            color=discord.Color.gold()
        )
        await interaction.response.send_message(embed=embed)
    
    # أمر Coin (رمي العملة)
    @app_commands.command(name='coin', description='رمي العملة')
    async def coin(self, interaction: discord.Interaction):
        result = random.choice(["صورة 🪙", "كتابة 📄"])
        embed = discord.Embed(
            title="🪙 العملة",
            description=f"النتيجة: **{result}**",
            color=discord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)
    
    # أمر Random (رقم عشوائي)
    @app_commands.command(name='random', description='رقم عشوائي')
    async def random_number(self, interaction: discord.Interaction, min_num: int = 1, max_num: int = 100):
        result = random.randint(min_num, max_num)
        embed = discord.Embed(
            title="🎰 رقم عشوائي",
            description=f"بين {min_num} و {max_num}\n**النتيجة: {result}**",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)
    
    # أمر Avatar (صورة البروفايل)
    @app_commands.command(name='avatar', description='عرض صورة البروفايل')
    async def avatar(self, interaction: discord.Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user
        
        embed = discord.Embed(
            title=f"Avatar - {user.name}",
            color=discord.Color.blue()
        )
        embed.set_image(url=user.avatar.url if user.avatar else None)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))