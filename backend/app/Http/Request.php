<?php

declare(strict_types=1);

namespace App\Http;

final class Request
{
    public function method(): string
    {
        return $_SERVER['REQUEST_METHOD'];
    }

    public function uri(): string
    {
        return parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
    }

    public function input(string $key, mixed $default = null): mixed
    {
        return $_POST[$key]
            ?? $_GET[$key]
            ?? $default;
    }

    public function all(): array
    {
        return array_merge($_GET, $_POST);
    }

    public function json(): array
    {
        $content = file_get_contents('php://input');

        if ($content === false || $content === '') {
            return [];
        }

        return json_decode($content, true) ?? [];
    }

    public function ip(): string
    {
        return $_SERVER['REMOTE_ADDR'] ?? '';
    }

    public function userAgent(): string
    {
        return $_SERVER['HTTP_USER_AGENT'] ?? '';
    }
}