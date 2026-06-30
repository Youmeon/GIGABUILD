<?php

declare(strict_types=1);

namespace App\Controllers;

use App\Database\Database;
use App\Http\JsonResponse;

final class DatabaseController
{
    public function test(): void
    {
        Database::connection();

        JsonResponse::success([
            'database' => 'connected'
        ]);
    }
}
