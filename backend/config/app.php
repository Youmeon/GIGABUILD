<?php

declare(strict_types=1);

// Вспомогательная функция для получения переменных окружения
function env(string $key, $default = null)
{
    // Проверяем в разных местах
    $value = $_ENV[$key] ?? $_SERVER[$key] ?? getenv($key);
    
    // Если значение найдено, возвращаем его
    if ($value !== false && $value !== null) {
        return $value;
    }
    
    // Иначе возвращаем значение по умолчанию
    return $default;
}

return [

    'name' => env('APP_NAME', 'GIGABUILD'),

    'env' => env('APP_ENV', 'local'),

    'debug' => filter_var(env('APP_DEBUG', false), FILTER_VALIDATE_BOOLEAN),

    'url' => env('APP_URL', 'http://localhost'),

    'timezone' => env('TIMEZONE', 'Europe/Riga'),

];