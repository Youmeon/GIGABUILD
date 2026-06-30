<?php

declare(strict_types=1);

namespace App\Controllers;

use App\Core\Controller;
use App\Http\Request;

final class HealthController extends Controller
{
    public function index(): void
    {
        $request = new Request();

        $this->success([
            'status' => 'ok',
            'app' => 'GIGABUILD',
            'version' => '1.0.0',
            'method' => $request->method(),
            'uri' => $request->uri(),
            'ip' => $request->ip(),
        ]);
    }
}