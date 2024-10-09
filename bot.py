from telethon import TelegramClient, events, Button
import asyncio
import random
import datetime
import pytz  # Adicionada a importação para lidar com fuso horário
import os

# Credenciais do Telegram (carregadas de variáveis de ambiente para maior segurança)
api_id = '23741041'
api_hash = '30000ace726d11d9bbcdb6415f340709'
bot_token = '7279073071:AAFQ4Gl03XZkOXWhjUcw7Hat-6R4lqWyKjc'

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# ID do chat (substitua pelo seu chat ID real)
chat_id = -1002179015837  # Certifique-se de que está correto

# Função para enviar a pré-mensagem
async def send_pre_message():
    try:
        await client.send_file(
            chat_id,
            'botpy.img1.jpg',  # Certifique-se de que a imagem está no mesmo diretório que o script
            caption="**🚨 HACKEANDO O ALGORITMO COM ROBOTOPS! 🤖🚨**\n🔍Buscando oportunidades...\n\nQuer Saber mais sobre Hack de Entradas?\nAperte aqui (https://t.me/HackEntradas) ↩️\n\n**🤚 AGUARDE A CONFIRMAÇÃO!👇**"
        )
    except Exception as e:
        print(f"Erro ao enviar pré-mensagem: {e}")

# Função para gerar horários dinâmicos com timezone
def generate_times(base_time):
    times = [(base_time + datetime.timedelta(minutes=12 + i * 14)).strftime("%H:%M") for i in range(6)]
    line1 = ' | '.join([f"⏰ {times[i]}" for i in range(3)])  # Primeira linha de horários
    line2 = ' | '.join([f"⏰ {times[i]}" for i in range(3, 6)])  # Segunda linha de horários
    return f"{line1}\n{line2}"

# Função para gerar a mensagem principal
async def send_main_message(base_time):
    try:
        versions = [
            ("**🐂 Fortune Ox 🐂**", 9, 7),
            ("**🐯 Fortune Tiger 🐯**", 12, 4),
            ("**🐰 Fortune Rabbit 🐰**", 6, 11),
            ("**🐭 Fortune Mouse 🐭**", 15, 3),
            ("**🐲 Fortune Dragon 🐲**", 8, 9)
        ]

        random.shuffle(versions)
        game, normal, turbo = random.choice(versions)

        message = f"""
**🎮JOGO:** {game}
{generate_times(base_time)} 
**📅 VÁLIDO ATÉ:** {datetime.datetime.now().strftime('%d/%m/%Y')}

{game}
✅ {normal}**X Normal**
🔄 **Alternando** 
⚡️ {turbo}**X Turbo**

**🚨 FUNCIONA APENAS NESTA PLATAFORMA ⬇️**
🎰 𝗣𝗹𝗮𝘁𝗮𝗳𝗼𝗿𝗺𝗮: https://abrir.ai/PlataformaOfc
**⚠️ NÃO TENTE EM OUTRO SITE! ⬆️**

**👇 HACK DE ENTRADAS 👇**
📲 https://abrir.ai/RobosTOP 📲
"""
        buttons = [
            [Button.url("🚨 JOGUE AQUI 🚨", "https://abrir.ai/PlataformaOfc")],
            [Button.url("👩‍💻 HACK DE ENTRADAS 👩‍💻", "https://t.me/HackEntradas")]
        ]

        await client.send_message(chat_id, message, buttons=buttons, file='botpy.img2.jpg')
    except Exception as e:
        print(f"Erro ao enviar mensagem principal: {e}")

# Função para gerar nomes e valores de vencedores
def generate_winners():
    names = ["Michele", "Gisele", "Natalia", "Anderson", "Graça", "Evelyn", "Cynthia", "Carlos", "Lara", "Larissa", "Marina", "Eugênio", "Luana", "Renan", "Mariana", "Tiago", "Raquel", "Claudio", "Zélia", "Wagner", "Juliana", "Noemi", "Rosângela", "Cecília", "Laís", "Marjorie", "Bianca", "Aline", "Cíntia", "André", "Vanessa", "Thiago", "Nathália", "Juliano", "Glauco", "Ellen", "Renato", "Gustavo", "Tatiane", "Hugo", "Milena", "Joaquim", "Soraya", "Clara", "Ariana", "Kelly", "Viviane", "Natália", "Lucas", "Karina", "Roger", "Letícia", "Juliana", "Lívia", "Elaine", "Tânia", "Rodrigo", "César", "Paulo", "Ricardo", "Lorenzo", "Julio", "Luiz", "Neiva", "Gilberto", "Luiza", "Gabriel", "Otávio", "Cristina", "Marcel", "Vinícius", "Evelyn", "Fernanda", "Marcelo", "Alice", "Sérgio", "Fernando", "Iago", "Fátima", "Sérgio", "Viviane", "Hélio", "Maria", "Eduardo", "Josiane", "Nina", "Priscila", "Cássia", "Ney", "Mariana", "Carlos", "João", "Alberto", "Daniel", "Jaime", "Fernando", "Fábia", "Diego", "Elaine", "Lucas", "Sérgio", "Patrícia", "Tiago", "Léo", "Jéssica", "Sabrina", "Patrícia", "Thiago", "Roberto", "Renato", "Joaquim", "Manuela", "Breno", "Rosa", "Roberta", "Giovana", "Fernando", "Denise", "Paula", "Alan", "Nivaldo", "Fábio", "Roberto", "Giovanna", "Cristina", "João Paulo", "Karla", "Vinícius", "Paulo", "Mariana", "Simone", "Félix", "Thiago", "Douglas", "Marcio", "Elaine", "Márcia", "Rafael", "Eliane", "Rogério", "Rosana", "Geraldo", "Karin", "Rafael", "Patrícia", "Paulo", "Viviane", "Bruno", "Tatiane", "Erick", "Jéssica", "Alice", "Gustavo", "Marina", "Fernanda", "Alessandra", "Felipe", "Thiago", "Zita", "Rafaela", "Nélio", "Roberto", "Adriana", "Fernando", "Eduarda", "Elias", "Rafaela", "Marcio", "Isabela", "Diana", "Pedro", "Edna", "Alana", "Rui", "Alice", "Ana Carolina", "Luiz", "Carmen", "Bruna", "Lucia", "Natália", "Matheus", "Bruno", "Ricardo", "Samuel", "Mônica", "Guilherme", "Miriam", "Rogério", "Leandro", "Eliane", "Kelly", "Larissa", "Soraya", "Edson", "Hugo"]
    random.shuffle(names)
    values = sorted(random.sample(range(200, 1201), len(names)), reverse=True)
    winners = [f"{i+1}º: {names[i]} R$ {values[i]:,.2f}".replace(",", ".") for i in range(8)]
    return f"**🏆VITÓRIA PARA {random.randint(70, 98)}% DOS APOSTADORES🏆**\n\n" + "\n".join(winners) + "\n\n**🎰🔎 BUSCANDO NOVAS BRECHAS**"

# Função para enviar a mensagem de vencedores
async def send_winners_message():
    try:
        await client.send_message(chat_id, generate_winners())
    except Exception as e:
        print(f"Erro ao enviar mensagem de vencedores: {e}")

# Função principal que controla o envio das mensagens
async def main():
    while True:  # Loop infinito
        await send_pre_message()
        await asyncio.sleep(120)  # Aguarda 2 minutos antes de enviar a mensagem principal
        base_time = datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
        await send_main_message(base_time)
        await asyncio.sleep(3300)  # Aguarda 55 minutos antes de enviar a mensagem dos vencedores
        await send_winners_message()
        await asyncio.sleep(180)  # Aguarda 3 minutos antes de reiniciar o ciclo

with client:
    client.loop.run_until_complete(main())