# Discord Bot 🤖

بوت Discord متكامل مع أوامر مختلفة (Utility, Moderation, Fun)

## المتطلبات
- Python 3.8+
- discord.py 2.0+

## التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/hsn428364-pixel/discord-bot.git
cd discord-bot
```

2. ثبت المتطلبات:
```bash
pip install -r requirements.txt
```

3. أنشئ ملف `.env` وأضف التوكن:
```
DISCORD_TOKEN=your_token_here
```

4. شغل البوت:
```bash
python main.py
```

## الأوامر المتاحة

### Utility (الأدوات)
- `/ping` - معرفة سرعة البوت
- `/hello` - تحية من البوت
- `/user` - معلومات المستخدم
- `/serverinfo` - معلومات السيرفر

### Moderation (الإدارة)
- `/kick` - طرد عضو
- `/ban` - حظر عضو
- `/warn` - إنذار عضو
- `/mute` - إسكات عضو
- `/clear` - حذف الرسائل

### Fun (التسلية)
- `/8ball` - الكرة الثمانية
- `/dice` - رمي النرد
- `/coin` - رمي العملة
- `/random` - رقم عشوائي
- `/avatar` - صورة البروفايل

## الترخيص
MIT License
