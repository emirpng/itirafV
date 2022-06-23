#################################
# Etiraf Club Bot #
#################################
# Repo Sahibi - aykhan_s
# Telegram - t.me/aykhan_s
# Support - t.me/RoBotlarimTg
# GitHub - aykhan026
#################################
#################################
# Bu repo sıfırdan yığılıb
# Başka github hesabına yükləməy olmaz
# Reponu öz adına çıxaran peysərdi...!!!
#################################
#################################
#
import os
import heroku3
from telethon import TelegramClient, events
#
# Buranı qurdalama
# Yalnız deploy buttonuyla botunu yarat
# 
api_id = int(os.environ.get("17650375"))
api_hash = os.environ.get("107850a23a8b730c39db315b5cd1c64c")
bot_token = os.environ.get("5454472706:AAFq_qben9Gq0kIw2ryUO2x2jmySC_ylrBE")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
admin_qrup = int(os.environ.get("-1001757412983"))
etiraf_qrup = int(os.environ.get("-1001757412983"))
kanal = os.environ.get("kanal")
log_qrup = int(os.environ.get("-1001757412983"))
botad = os.environ.get("@MajesteitirafXBot")
etirafmsg = os.environ.get("itirafınız nasıl paylaşılsın?")
startmesaj = os.environ.get("**Merhaba** __hoşgeldin Kimseye söyleyemediğin itirafları bana söyleyebilirsin__ 🤭")
etirafyaz = os.environ.get("**Buraya bir itiraf yaz daha sonra açık mı yoksa anonim mi diye soracağım** 😍")
qrupstart = os.environ.get("**Aktifim itiraf yazmak için bana özelden yazın**.")
gonderildi = os.environ.get("✅ **İtirafınız gönderildi Adminler tarafından onaylandıktan sonra @Majesteitiraf kanalında paylaşılacaktır**")
support = os.environ.get("majesteler")
sahib = os.environ.get("majestesahip")
#
# RoBotlarimTg
# RoBotlarimTg
# RoBotlarimTg






