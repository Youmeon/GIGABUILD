<?php

declare(strict_types=1);

return [

    'driver' => 'mysql',

    'host' => env('DB_HOST'),

    'port' => env('DB_PORT'),

    'database' => env('DB_DATABASE'),

    'username' => env('DB_USERNAME'),

    'password' => env('DB_PASSWORD'),

    'charset' => 'utf8mb4',

];
