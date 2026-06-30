<?php

declare(strict_types=1);

use App\Core\Router;
use App\Controllers\HealthController;
use App\Controllers\DatabaseController;
use App\Controllers\RequestController;

/** @var Router $router */

// Проверка API
$router->get(
    '/api/health',
    [HealthController::class, 'index']
);

// Проверка подключения к БД
$router->get(
    '/api/database',
    [DatabaseController::class, 'test']
);

// Отправка формы заявки
$router->post(
    '/api/send-form',
    [RequestController::class, 'store']
);