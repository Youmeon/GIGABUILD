<?php

declare(strict_types=1);

use App\Core\Router;
use Dotenv\Dotenv;
use App\Core\Container;

ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);

require_once __DIR__ . '/../vendor/autoload.php';

/*
|--------------------------------------------------------------------------
| Environment
|--------------------------------------------------------------------------
*/

$dotenv = Dotenv::createImmutable(__DIR__ . '/../');
$dotenv->load();

foreach ($_ENV as $key => $value) {
    putenv("$key=$value");
}

/*
|--------------------------------------------------------------------------
| Configuration
|--------------------------------------------------------------------------
*/

$config = require __DIR__ . '/../config/app.php';

date_default_timezone_set($config['timezone']);

// Устанавливаем CORS заголовки (разрешаем запросы с фронтенда)
$frontendUrl = env('FRONTEND_URL', 'http://localhost:5173');
header("Access-Control-Allow-Origin: {$frontendUrl}");
header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With');
header('Access-Control-Allow-Credentials: true');
header('Content-Type: application/json; charset=utf-8');

// Обработка Preflight-запроса от браузера
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

/*
|--------------------------------------------------------------------------
| Router
|--------------------------------------------------------------------------
*/

$container = new Container();

$router = new Router($container);

require_once __DIR__ . '/../routes/api.php';

/*
|--------------------------------------------------------------------------
| Dispatch request
|--------------------------------------------------------------------------
*/

$router->dispatch(
    $_SERVER['REQUEST_METHOD'],
    parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH)
);