from telethon import TelegramClient, sync, events

INPUT_CHANNEL = ['@if_bonds', "@tinkoff_invest_official", "@DayCapital", "@WinniePooh11", "@testchannel_19",
                 "@testchannel_561", "@investnique", "@div_invest"]
OUTPUT_CHANNEL = '@scan_news_make_money'
# ключевые фразы по которым будем парсить новости из каналов
TAGS = ['новости','финансы', 'акции', ' облигации', 'рост', 'падение', 'прогноз', 'анализ',
        'деньги', 'средства', 'аналитика', 'рынок', 'Китая', 'США','выгода', 'дефолт', 'прибыль',
        'финансовый отчет','дивиденды', 'фонд', 'фонды', 'анализ', 'СБЕР', 'технический']

api_id = 23336816
api_hash = 'bbf67b75e7d89dfb76eb8c187c070181'

client = TelegramClient('testing', api_id, api_hash)
for channel in INPUT_CHANNEL:
    @client.on(events.NewMessage(chats=(channel)))
    async def normal_handler(event):
        for tag in TAGS:
            if tag in str(event.message):
                await client.send_message(OUTPUT_CHANNEL, event.message)
                break

client.start()
client.run_until_disconnected()
