<?php

declare(strict_types=1);

namespace App\Validators;

final class RequestValidator
{
    public function validate(array $data): array
    {
        $errors = [];

        // Имя
        if (empty($data['full_name'])) {
            $errors['full_name'] = 'Введите имя';
        } elseif (mb_strlen(trim($data['full_name'])) < 2) {
            $errors['full_name'] = 'Имя слишком короткое';
        }

        // Телефон
        if (empty($data['phone'])) {

            $errors['phone'] = 'Введите телефон';

        } else {

            $phone = preg_replace('/\D/', '', $data['phone']);

            if (strlen($phone) < 10) {
                $errors['phone'] = 'Некорректный телефон';
            }
        }

        // Email
        if (!empty($data['email'])) {

            if (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
                $errors['email'] = 'Некорректный Email';
            }

        }

        return $errors;
    }
}