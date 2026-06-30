<?php

declare(strict_types=1);

namespace App\Services;

use PHPMailer\PHPMailer\Exception;
use PHPMailer\PHPMailer\PHPMailer;

final class EmailService
{
    public function send(array $data): bool
    {
        $config = require __DIR__ . '/../../config/mail.php';

        $mail = new PHPMailer(true);

        try {

            $mail->isSMTP();

            $mail->Host = $config['host'];

            $mail->SMTPAuth = true;

            $mail->Username = $config['username'];

            $mail->Password = $config['password'];

            $mail->SMTPSecure = $config['encryption'];

            $mail->Port = $config['port'];

            $mail->CharSet = 'UTF-8';

            $mail->setFrom(
                $config['from'],
                $config['from_name']
            );

            $mail->addAddress($config['to']);

            $mail->isHTML(true);

            $mail->Subject = 'Новая заявка с сайта';

            $mail->Body = $date = date('d.m.Y H:i');

						$mail->Body = "
						<html>
							<head>
    						<meta charset='UTF-8'>
									</head>
										<body style='font-family:Arial,sans-serif;background:#f5f5f5;padding:30px;'>

											<div style='max-width:650px;margin:auto;background:#ffffff;border-radius:10px;padding:30px;'>

											<h2 style='margin-top:0;color:#2563eb;'>
											Новая заявка с сайта GIGABUILD
											</h2>

											<hr>

											<p><strong>👤 Имя:</strong><br>{$data['full_name']}</p>

											<p><strong>📞 Телефон:</strong><br>{$data['phone']}</p>

											<p><strong>📧 Email:</strong><br>".($data['email'] ?: 'Не указан')."</p>

											<p><strong>🌐 Источник:</strong><br>Сайт GIGABUILD</p>

											<p><strong>🕒 Дата:</strong><br>{$date}</p>

											<p><strong>🌍 IP:</strong><br>".($_SERVER['REMOTE_ADDR'] ?? '-')."</p>

										<hr>

											<p style='font-size:12px;color:#777'>
											Это письмо отправлено автоматически с сайта SKDIONIS.
											</p>

										</div>

									</body>
								</html>";
            $mail->send();

            return true;

        } catch (Exception) {

            return false;

        }
    }
}