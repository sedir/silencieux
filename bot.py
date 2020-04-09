from environs import Env
from telethon import TelegramClient, events, sync

# Lendo variáveis de ambiente do arquivo .env
env = Env()
env.read_env('.env')

api_id = env('TELEGRAM_API_ID')
api_hash = env('TELEGRAM_API_HASH')

client = TelegramClient('session_name', api_id, api_hash)
client.start()

with client:

    # for dialog in client.iter_dialogs(archived=False):
    #     if dialog.name == 'Teste bot':
    #         print(dialog)

    # Obter mensagens um chat (arg0) originadas por um usuário específico (from_user)
    messages = client.get_messages(427777832, from_user=335653242)

    # Remover mensagens do chat (arg0) somente para o usuário (revoke=False)
    client.delete_messages(427777832, messages, revoke=False)
