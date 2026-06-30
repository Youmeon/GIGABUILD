<?php

declare(strict_types=1);

require_once __DIR__ . '/../vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__ . '/../');
$dotenv->load();

$mail = new PHPMailer\PHPMailer\PHPMailer(true);

try {

    $mail->isSMTP();

    $mail->Host = $_ENV['MAIL_HOST'];

    $mail->SMTPAuth = true;

    $mail->Username = $_ENV['MAIL_USERNAME'];

    $mail->Password = $_ENV['MAIL_PASSWORD'];

    $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_SMTPS;

    $mail->Port = (int)$_ENV['MAIL_PORT'];

    $mail->CharSet = 'UTF-8';

    $mail->setFrom(
        $_ENV['MAIL_FROM'],
        $_ENV['MAIL_FROM_NAME']
    );

    $mail->addAddress($_ENV['MAIL_TO']);

    $mail->Subject = 'Тест GIGABUILD';

    $mail->Body = 'Если вы получили это письмо, SMTP работает.';

    $mail->send();

    echo 'Письмо успешно отправлено ✅';

} catch (Exception $e) {

    echo $e->getMessage();

}