<?php

declare(strict_types=1);

namespace App\Http;

final class JsonResponse
{
    public static function success(
        array $data = [],
        int $status = 200
    ): void {
        http_response_code($status);

        header('Content-Type: application/json; charset=utf-8');

        echo json_encode(
            [
                'success' => true,
                'data' => $data
            ],
            JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
        );
    }

    public static function error(
        string $message,
        int $status = 400,
        array $errors = []
    ): void {
        http_response_code($status);

        header('Content-Type: application/json; charset=utf-8');

        echo json_encode(
            [
                'success' => false,
                'message' => $message,
                'errors' => $errors
            ],
            JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE
        );
    }
}

