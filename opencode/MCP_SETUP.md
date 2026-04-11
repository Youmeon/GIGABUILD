# Безопасная настройка MCP Figma для opencode

## 1. Создай файл настроек opencode

Создай файл `~/.opencode/mcp.json` (или `~/.config/opencode/mcp.json`):

```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": ["-y", "figma-developer-mcp"],
      "env": {
        "FIGMA_API_KEY": "${FIGMA_API_KEY}"
      }
    }
  }
}
```

## 2. Добавь переменную окружения

В файл `~/.bashrc` или `~/.zshrc` добавь:

```bash
# Figma API Key для opencode MCP
export FIGMA_API_KEY="твой_токен"
```

Затем примени изменения:

```bash
source ~/.bashrc
```

## 3. Запусти opencode из WSL

```bash
opencode
```

---

**Безопасность:**
- Ключ НИКОГДА не сохраняется в файлах репозитория
- Ключ доступен только через переменную окружения
- При запуске `opencode` в WSL - MCP сервер автоматически подхватит `~/.opencode/mcp.json`

Хочешь, проверю работает ли npx figma-developer-mcp в твоей системе?
