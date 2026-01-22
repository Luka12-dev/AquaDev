# AquaDev

```
    ___                        ____             
   /   |  ____ ___  ______ _  / __ \___  _   __
  / /| | / __ `/ / / / __ `/ / / / / _ \| | / /
 / ___ |/ /_/ / /_/ / /_/ / / /_/ /  __/| |/ / 
/_/  |_|\__, /\__,_/\__,_/ /_____/\___/ |___/  
          /_/                                  
```

**100% Local | 100% Private | Open Source**

AI Development Agent powered by Ollama - Your personal coding assistant that runs entirely on your machine.

## Features

- **100% Local & Private** - All processing happens on your machine
- **Ollama Integration** - Use any model you have installed
- **File Operations** - Read, write, create, delete files
- **Real-time Streaming** - See AI responses as they generate
- **Permission System** - Full control over what AquaDev can do
- **Beautiful ASCII Interface** - Clean, modern terminal UI
- **Command System** - Powerful commands for quick actions

## Installation

1. **Install Ollama** (if not already installed):
   - Visit https://ollama.ai and download for your platform

2. **Pull a model**:
   ```bash
   ollama pull llama2
   # or
   ollama pull codellama
   # or any other model
   ```

3. **Install AquaDev dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run AquaDev**:
   ```bash
   python aquadev.py
   ```

## Global Command (Windows)

You can run AquaDev from anywhere by adding it to your PATH:

1. **Add to PATH:**
   - Press `Win + S` and search "Environment Variables"
   - Click "Edit the system environment variables"
   - Click "Environment Variables" button
   - Under "User variables", select "Path" and click "Edit"
   - Click "New" and add the path to your AquaDev folder (e.g., `C:\path\to\AquaDev`)
   - Click OK on all windows

2. **Now run from anywhere:**
   ```bash
   aquadev
   ```

3. **Files will be created in your current working directory**, not the AquaDev installation folder.

## Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all available commands |
| `/version` | Show version information |
| `/models` | List and select Ollama models |
| `/model` | Show current model |
| `/clear` | Clear the screen |
| `/status` | Show agent status and permissions |
| `/files` | List files in current directory |
| `/pwd` | Show current working directory |
| `/cd <path>` | Change working directory |
| `/read <file>` | Read a file |
| `/reset` | Reset conversation context |
| `/quit` | Exit AquaDev |

## Configuration

Edit `Agree.yaml` to customize:

- **Permissions** - Enable/disable file operations
- **Ollama Settings** - Host, timeout, streaming
- **Safety Settings** - Confirm deletes, restricted paths

## First Run

On first run, AquaDev will ask for your permission to operate. 
After agreeing, the `new_user` flag in `Agree.yaml` is set to `False`.

## Disclaimer

**Developer Luka is NOT responsible for:**
- Deleted files
- Modified content  
- Lost data
- System changes

**ALL ACTIONS ARE PERFORMED AT YOUR OWN RISK.**

## Links

- **GitHub**: https://github.com/Luka12-dev/AquaDev
- **YouTube**: https://www.youtube.com/@LukaCyber-s4b7o

## License

Open Source - MIT License

---

Made with care by Luka
