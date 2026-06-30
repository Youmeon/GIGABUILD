<?php

declare(strict_types=1);

namespace App\Core;

use App\Http\JsonResponse;

abstract class Controller
{
    protected function success(array $data = [], int $status = 200): void
    {
        JsonResponse::success($data, $status);
    }

    protected function error(
        string $message,
        int $status = 400,
        array $errors = []
    ): void {
        JsonResponse::error($message, $status, $errors);
    }
}
