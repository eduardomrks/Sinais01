import random
import datetime
import pytz
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Configurações do bot
api_token = '8280555598:AAFhLXQ_JMsPH3oEOLSv9o_3TZDd38wxHzQ'  # Substitua pelo seu token
chat_id = '-1002179015837'  # Substitua pelo ID do grupo ou canal

# Inicializando o bot
bot = Bot(token=api_token)

# Fuso horário de Brasília
brasilia_tz = pytz.timezone('America/Sao_Paulo')

# Função para gerar horários com intervalo de 10 a 15 minutos
def gerar_horarios():
    now = datetime.datetime.now(brasilia_tz)
    base_time = (now + datetime.timedelta(minutes=(5 - now.minute % 5))).replace(second=0, microsecond=0)
    horarios = [base_time]
    for i in range(5):
        intervalo = 10 if i % 2 == 0 else 15
        next_time = horarios[-1] + datetime.timedelta(minutes=intervalo)
        horarios.append(next_time)
    return horarios

# Função para formatar horários
def formatar_horarios(horarios):
    linha1 = ' | '.join([h.strftime('%H:%M') for h in horarios[:3]])
    linha2 = ' | '.join([h.strftime('%H:%M') for h in horarios[3:]])
    return f"⏰  {linha1}\n⏰  {linha2}"

# Função para enviar sinais
async def enviar_sinais(jogo, data_valida):
    horarios = gerar_horarios()
    msg_sinais = f"""
🤑 NOVA OPORTUNIDADE!

🎮 JOGO: {jogo}
{formatar_horarios(horarios)}
📅 VÁLIDO ATÉ: {data_valida}

🚨 PLATAFORMA REGULARIZADA ⬇️
🎰 Plataforma: https://abrir.ai/News
⚠️ NÃO TENTE EM OUTRO SITE ⬆️

👇 APLICATIVO DOS SLOTS 👇
📲https://t.me/HackEntradas 📲
🔞 Jogue com responsabilidade!
"""
    # Criar botões
    keyboard = [[InlineKeyboardButton("🚨JOGUE AQUI🚨", url="https://abrir.ai/News")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        with open('botpy.img2.jpg', 'rb') as image:
            await bot.send_photo(chat_id=chat_id, photo=image, caption=msg_sinais, reply_markup=reply_markup)
        print(f"Mensagem de sinais enviada para {jogo}.")
    except Exception as e:
        print(f"Erro ao enviar mensagem de sinais: {e}")

# Função para enviar mensagem de finalização
async def enviar_finalizacao():
    msg_finalizacao = """
⌛️ MINUTOS FINALIZADOS ⌛️
✅✅✅ VITÓRIA ✅✅✅
"""
    keyboard = [[InlineKeyboardButton("🎁CADASTRE-SE🎁", url="https://abrir.ai/News")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    try:
        await bot.send_message(chat_id=chat_id, text=msg_finalizacao, reply_markup=reply_markup)
        print("Mensagem de finalização enviada.")
    except Exception as e:
        print(f"Erro ao enviar mensagem de finalização: {e}")

# Função principal
async def main_loop():
    jogos = [
        "🐯 Fortune Tiger 🐯",
        "🐭 Fortune Mouse 🐭",
        "🐂 Fortune OX 🐂",
        "🐲 Fortune Dragon 🐲",
        "🐰 Fortune Rabbit 🐰"
    ]
    while True:
        data_valida = (datetime.datetime.now(brasilia_tz) + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        for jogo in jogos:
            await enviar_sinais(jogo, data_valida)
            await asyncio.sleep(55 * 60)  # Espera 55 minutos
            await enviar_finalizacao()
            await asyncio.sleep(5 * 60)  # Espera 5 minutos

# Iniciar o script
if __name__ == "__main__":
    asyncio.run(main_loop())

