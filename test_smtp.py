import asyncio
from email.message import EmailMessage
from aiosmtplib import SMTP

async def test_smtp():
    msg = EmailMessage()
    msg["Subject"] = "Тестовое письмо"
    msg["From"] = "gamunkul2270@mail.ru"
    msg["To"] = "gamunkul2270@mail.ru"
    msg.set_content("Это тестовое письмо.")

    smtp_client = SMTP(
        hostname="smtp.mail.ru",
        port=465,
        username="gamunkul2270@mail.ru",
        password="Faterra205",
        use_tls=True,
    )
    await smtp_client.connect()
    await smtp_client.send_message(msg)
    await smtp_client.quit()

asyncio.run(test_smtp())