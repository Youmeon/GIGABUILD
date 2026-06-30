<?php

declare(strict_types=1);

namespace App\Core;

final class Router
{
    private array $routes = [];

    public function __construct(
        private readonly Container $container
    ) {
    }

    public function get(string $uri, array $action): void
    {
        $this->routes['GET'][$uri] = $action;
    }

    public function post(string $uri, array $action): void
    {
        $this->routes['POST'][$uri] = $action;
    }

    public function dispatch(string $method, string $uri): void
    {
        $route = $this->routes[$method][$uri] ?? null;

        if ($route === null) {

            http_response_code(404);

            echo json_encode([
                'success' => false,
                'message' => 'Route not found'
            ]);

            return;
        }

        [$controller, $action] = $route;

        $instance = $this->container->get($controller);

        $instance->$action();
    }
}