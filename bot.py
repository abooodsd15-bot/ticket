import discord
from discord.ext import commands
from discord.ui import Select, View

# إعداد البوت واللاحقة (Prefix)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# إنشاء القائمة المنسدلة
class TicketSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="تقديم شكوى",
                description="اضغط هنا لفتح تكت تقديم شكوى",
                emoji="📩",
                value="complaint"
            ),
            discord.SelectOption(
                label="طلب أدمن",
                description="التقديم على إداري في السيرفر",
                emoji="🛡️",
                value="admin_request"
            ),
            discord.SelectOption(
                label="طلب رول",
                description="طلب رتبة خاصة أو معينة",
                emoji="🎭",
                value="role_request"
            ),
            discord.SelectOption(
                label="استفسار عام",
                description="لأي سؤال أو استفسار آخر",
                emoji="❓",
                value="general_inquiry"
            ),
        ]
        super().__init__(
            placeholder="اختر نوع التكت / الخدمة من القائمة...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        # الاستجابة بناءً على خيار المستخدم
        selection = self.values[0]
        
        if selection == "complaint":
            await interaction.response.send_message("تم استلام طلبك: **تقديم شكوى**. سيتم التواصل معك قريباً.", ephemeral=True)
        elif selection == "admin_request":
            await interaction.response.send_message("تم استلام طلبك: **طلب أدمن**. يرجى تجهيز سيرتك الذاتية.", ephemeral=True)
        elif selection == "role_request":
            await interaction.response.send_message("تم استلام طلبك: **طلب رول**. اكتب اسم الرتبة المطلوبة.", ephemeral=True)
        elif selection == "general_inquiry":
            await interaction.response.send_message("تم استلام طلبك: **استفسار عام**. اكتب سؤالك هنا.", ephemeral=True)

# الكلاس الخاص بإضافة القائمة إلى الرسالة
class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None) # يجعل القائمة تعمل دائماً بدون توقف
        self.add_item(TicketSelect())

# أمر لتشغيل قائمة التكت (للأدمن فقط)
@bot.command()
@commands.has_permissions(administrator=True)
async def setup_tickets(ctx):
    embed = discord.Embed(
        title="مركز الدعم والمساعدة 🎫",
        description="مرحباً بك! يرجى اختيار نوع الخدمة المطلوبة من القائمة المنسدلة أدناه للبدء.",
        color=discord.Color.blue()
    )
    embed.set_footer(text="نظام التكت الآلي")
    
    await ctx.send(embed=embed, view=TicketView())

@bot.event
async def on_ready():
    print(f'تم تسجيل الدخول بنجاح باسم: {bot.user}')

# ضع توكن البوت الخاص بك هنا
bot.run("MTU1MzMwNzcyMjk4NjgxNTU0OQ.GuuRCH.H1AiH86PWO26pVSnd0_rv7HP-8DX_RbRMh5cio")
