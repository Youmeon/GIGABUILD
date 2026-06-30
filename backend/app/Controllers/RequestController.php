<?php

declare(strict_types=1);

namespace App\Controllers;

use App\Http\JsonResponse;
use App\Http\Request;
use App\Services\EmailService;
use App\Services\RequestService;
use App\Validators\RequestValidator;

final class RequestController
{
    private RequestValidator $validator;
    private RequestService $service;
    private EmailService $email;

    public function __construct()
    {
        $this->validator = new RequestValidator();
        $this->service = new RequestService();
        $this->email = new EmailService();
    }

    public function store(): void
    {
        $request = new Request();

        $data = $request->json();

        $errors = $this->validator->validate($data);

        if (!empty($errors)) {

            JsonResponse::error(
                'Ошибка валидации',
                422,
                $errors
            );

            return;
        }

        // Сохраняем заявку в БД
        $id = $this->service->create($data);

        // Отправляем письмо
        $mailSent = $this->email->send($data);

        JsonResponse::success([
            'message' => 'Заявка успешно отправлена',
            'id' => $id,
            'email_sent' => $mailSent
        ]);
    }
}