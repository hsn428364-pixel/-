import discord
from discord.ext import commands
from discord import app_commands
import datetime

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # أمر Ping
    @app_commands.command(name='ping', description='معرفة سرعة البوت')
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="🏓 Ping",
            description=f"**Latency:** {latency}ms",
            color=discord.Color.blue()
        )
        await interaction.response.send_message(embed=embed)
    
    # أمر Hello
    @app_commands.command(name='hello', description='تحية من البوت')
    async def hello(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="👋 مرحبا!",
            description=f"مرحبا {interaction.user.mention}!",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)
    
    # أمر معلومات المستخدم
    @app_commands.command(name='user', description='معلومات المستخدم')
    async def user_info(self, interaction: discord.Interaction, user: discord.User = None):
        if user is None:
            user = interaction.user
        
        embed = discord.Embed(
            title=f"👤 معلومات {user.name}",
            color=discord.Color.purple(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.add_field(name="🔢 ID", value=user.id, inline=False)
        embed.add_field(name="📅 تاريخ الإنشاء", value=user.created_at.strftime('%Y-%m-%d'), inline=False)
        embed.add_field(name="🤖 بوت", value="نعم" if user.bot else "لا", inline=False)
        embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
        
        await interaction.response.send_message(embed=embed)
    
    # أمر معلومات السيرفر
    @app_commands.command(name='serverinfo', description='معلومات السيرفر')
    async def server_info(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title=f"🏢 {guild.name}",
            color=discord.Color.orange()
        )
        embed.add_field(name="🔢 ID", value=guild.id, inline=False)
        embed.add_field(name="👥 عدد الأعضاء", value=guild.member_count, inline=False)
        embed.add_field(name="📅 تاريخ الإنشاء", value=guild.created_at.strftime('%Y-%m-%d'), inline=False)
        embed.add_field(name="👑 المالك", value=guild.owner.mention if guild.owner else "غير معروف", inline=False)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Utility(bot))