import discord
from discord.ext import commands
from discord import app_commands
import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # أمر Kick (طرد عضو)
    @app_commands.command(name='kick', description='طرد عضو من السيرفر')
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if member == interaction.user:
            await interaction.response.send_message("❌ لا يمكنك طرد نفسك!", ephemeral=True)
            return
        
        if member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("❌ لا يمكنك طرد هذا العضو!", ephemeral=True)
            return
        
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="✅ تم الطرد",
            description=f"{member.mention} تم طرده من السيرفر",
            color=discord.Color.red()
        )
        if reason:
            embed.add_field(name="السبب", value=reason, inline=False)
        await interaction.response.send_message(embed=embed)
    
    # أمر Ban (حظر عضو)
    @app_commands.command(name='ban', description='حظر عضو من السيرفر')
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        if member == interaction.user:
            await interaction.response.send_message("❌ لا يمكنك حظر نفسك!", ephemeral=True)
            return
        
        if member.top_role >= interaction.user.top_role:
            await interaction.response.send_message("❌ لا يمكنك حظر هذا العضو!", ephemeral=True)
            return
        
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="✅ تم الحظر",
            description=f"{member.mention} تم حظره من السيرفر",
            color=discord.Color.red()
        )
        if reason:
            embed.add_field(name="السبب", value=reason, inline=False)
        await interaction.response.send_message(embed=embed)
    
    # أمر Warn (إنذار عضو)
    @app_commands.command(name='warn', description='إنذار عضو')
    @app_commands.checks.has_permissions(moderate_members=True)
    async def warn(self, interaction: discord.Interaction, member: discord.Member, reason: str = None):
        embed = discord.Embed(
            title="⚠️ تحذير",
            description=f"{member.mention} تم تحذيره",
            color=discord.Color.yellow()
        )
        if reason:
            embed.add_field(name="السبب", value=reason, inline=False)
        
        await interaction.response.send_message(embed=embed)
        await member.send(f"⚠️ تم تحذيرك في {interaction.guild.name}\nالسبب: {reason if reason else 'لم يتم تحديده'}")
    
    # أمر Mute (إسكات عضو)
    @app_commands.command(name='mute', description='إسكات عضو')
    @app_commands.checks.has_permissions(moderate_members=True)
    async def mute(self, interaction: discord.Interaction, member: discord.Member, duration: int = None):
        if duration:
            duration_td = datetime.timedelta(minutes=duration)
            await member.edit(timed_out_until=datetime.datetime.now(datetime.timezone.utc) + duration_td)
        
        embed = discord.Embed(
            title="🔇 تم الإسكات",
            description=f"{member.mention} تم إسكاته",
            color=discord.Color.blue()
        )
        if duration:
            embed.add_field(name="المدة", value=f"{duration} دقيقة", inline=False)
        
        await interaction.response.send_message(embed=embed)
    
    # أمر Clear (حذف الرسائل)
    @app_commands.command(name='clear', description='حذف عدد من الرسائل')
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        if amount > 100:
            await interaction.response.send_message("❌ لا يمكن حذف أكثر من 100 رسالة", ephemeral=True)
            return
        
        deleted = await interaction.channel.purge(limit=amount)
        embed = discord.Embed(
            title="✅ تم الحذف",
            description=f"تم حذف {len(deleted)} رسالة",
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Moderation(bot))