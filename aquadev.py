"""
AquaDev - AI Development Agent powered by Ollama
100% Local | 100% Private | Open Source

GitHub: https://github.com/Luka12-dev/AquaDev
YouTube: https://www.youtube.com/@LukaCyber-s4b7o

Developer: Luka
DISCLAIMER: Developer Luka is not responsible for any file deletions or modifications.
All actions are performed at your own risk.
"""

import os
import sys
import yaml
import json
import shutil
import requests
from datetime import datetime
from pathlib import Path

# Version info
VERSION = "1.0.0"
CODENAME = "Aqua"

class Colors:
    # ANSI color codes for terminal output
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

class AquaDevUI:
    # Handle all UI elements and ASCII art
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_banner():
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
    ___                        ____             
   /   |  ____ ___  ______ _  / __ \\___ _   __
  / /| | / __ `/ / / / __ `/ / / / / _ \\ | / /
 / ___ |/ /_/ / /_/ / /_/ / / /_/ /  __/ |/ / 
/_/  |_|\\__, /\\__,_/\\__,_/ /_____/\\___/|___/  
          /_/                                  
{Colors.RESET}
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
{Colors.WHITE}  100% Local  |  100% Private  |  Open Source{Colors.RESET}
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
{Colors.CYAN}  GitHub:{Colors.RESET}  https://github.com/Luka12-dev/AquaDev
{Colors.CYAN}  YouTube:{Colors.RESET} https://www.youtube.com/@LukaCyber-s4b7o
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
{Colors.YELLOW}  Version: {VERSION} ({CODENAME}){Colors.RESET}
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
"""
        print(banner)
    
    @staticmethod
    def print_welcome():
        welcome = f"""
{Colors.GREEN}{Colors.BOLD}
  +--------------------------------------------------+
  |                                                  |
  |    Welcome to AquaDev - Your AI Dev Assistant    |
  |                                                  |
  |    Type /help to see all available commands      |
  |    Type /models to select an Ollama model        |
  |    Type 'exit' or /quit to leave                 |
  |                                                  |
  +--------------------------------------------------+
{Colors.RESET}"""
        print(welcome)
    
    @staticmethod
    def print_agreement():
        agreement = f"""
{Colors.YELLOW}{Colors.BOLD}
  +============================================================+
  |                                                            |
  |                    PERMISSION AGREEMENT                    |
  |                                                            |
  +============================================================+
{Colors.RESET}
{Colors.WHITE}  AquaDev requires your permission to operate.
  
  This AI agent can:
{Colors.CYAN}    [*] Read files from your system
    [*] Write and create new files
    [*] Delete files (with confirmation)
    [*] Modify existing files
    [*] Create and manage directories
    [*] Execute Python code
{Colors.RESET}
{Colors.RED}{Colors.BOLD}
  DISCLAIMER:
  -----------
  Developer Luka is NOT responsible for any:
    - Deleted files
    - Modified content
    - Lost data
    - System changes
  
  ALL ACTIONS ARE PERFORMED AT YOUR OWN RISK.
{Colors.RESET}
{Colors.YELLOW}
  Your data stays 100% LOCAL on your machine.
  No data is sent to external servers.
  Powered by Ollama - running locally.
{Colors.RESET}
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
"""
        print(agreement)
    
    @staticmethod
    def print_commands():
        commands = f"""
{Colors.BLUE}{Colors.BOLD}
  +--------------------------------------------------+
  |              AVAILABLE COMMANDS                  |
  +--------------------------------------------------+
{Colors.RESET}
{Colors.BLUE}  /help, help{Colors.RESET}        - Show this help message
{Colors.BLUE}  /version, version{Colors.RESET}  - Show AquaDev version info
{Colors.BLUE}  /models{Colors.RESET}            - List and select Ollama models
{Colors.BLUE}  /model{Colors.RESET}             - Show current model
{Colors.BLUE}  /clear, clear{Colors.RESET}      - Clear the screen
{Colors.BLUE}  /status{Colors.RESET}            - Show agent status and permissions
{Colors.BLUE}  /permissions{Colors.RESET}       - View/modify permissions
{Colors.BLUE}  /history{Colors.RESET}           - Show chat history
{Colors.BLUE}  /save{Colors.RESET}              - Save current session
{Colors.BLUE}  /reset{Colors.RESET}             - Reset conversation context
{Colors.BLUE}  /files{Colors.RESET}             - List files in current directory
{Colors.BLUE}  /pwd{Colors.RESET}               - Show current working directory
{Colors.BLUE}  /cd <path>{Colors.RESET}         - Change working directory
{Colors.BLUE}  /read <file>{Colors.RESET}       - Read a file
{Colors.BLUE}  /quit, exit{Colors.RESET}        - Exit AquaDev

{Colors.DIM}------------------------------------------------------------{Colors.RESET}
{Colors.CYAN}  Just type naturally to chat with the AI!{Colors.RESET}
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
"""
        print(commands)
    
    @staticmethod
    def print_version():
        version_info = f"""
{Colors.CYAN}{Colors.BOLD}
  +--------------------------------------------------+
  |                 AquaDev Version                  |
  +--------------------------------------------------+
{Colors.RESET}
{Colors.WHITE}  Name:{Colors.RESET}      AquaDev
{Colors.WHITE}  Version:{Colors.RESET}   {VERSION}
{Colors.WHITE}  Codename:{Colors.RESET}  {CODENAME}
{Colors.WHITE}  Python:{Colors.RESET}    {sys.version.split()[0]}
{Colors.WHITE}  Platform:{Colors.RESET}  {sys.platform}

{Colors.CYAN}  Developer:{Colors.RESET} Luka
{Colors.CYAN}  GitHub:{Colors.RESET}    https://github.com/Luka12-dev/AquaDev
{Colors.CYAN}  YouTube:{Colors.RESET}   https://www.youtube.com/@LukaCyber-s4b7o

{Colors.GREEN}  Status:{Colors.RESET}    100% Local | 100% Private | Open Source
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
"""
        print(version_info)


class ConfigManager:
    """Manage Agree.yaml configuration"""
    
    def __init__(self, config_path="Agree.yaml"):
        self.config_path = config_path
        self.config = self.load_config()
    
    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        return self.create_default_config()
    
    def save_config(self):
        with open(self.config_path, 'w') as f:
            yaml.dump(self.config, f, default_flow_style=False, sort_keys=False)
    
    def create_default_config(self):
        default = {
            'new_user': True,
            'user_agreed': False,
            'permissions': {
                'file_read': True,
                'file_write': True,
                'file_delete': True,
                'file_modify': True,
                'dir_create': True,
                'dir_delete': True,
                'dir_list': True,
                'execute_python': True,
                'execute_shell': False,
                'network_local': True,
                'network_external': False
            },
            'ollama': {
                'host': 'http://localhost:11434',
                'default_model': '',
                'timeout': 120,
                'stream': True
            },
            'agent': {
                'name': 'AquaDev',
                'version': VERSION,
                'max_context_length': 8192,
                'save_history': True,
                'history_file': 'chat_history.json'
            },
            'safety': {
                'confirm_delete': True,
                'backup_before_modify': False,
                'auto_execute_file_ops': True,
                'restricted_paths': ['/etc', '/sys', '/boot', 'C:\\Windows']
            }
        }
        with open(self.config_path, 'w') as f:
            yaml.dump(default, f, default_flow_style=False)
        return default
    
    def is_new_user(self):
        return self.config.get('new_user', True)
    
    def set_user_agreed(self):
        self.config['new_user'] = False
        self.config['user_agreed'] = True
        self.save_config()
    
    def get_permission(self, perm):
        return self.config.get('permissions', {}).get(perm, False)
    
    def set_default_model(self, model):
        self.config['ollama']['default_model'] = model
        self.save_config()
    
    def get_default_model(self):
        return self.config.get('ollama', {}).get('default_model', '')


class OllamaClient:
    """Handle Ollama API interactions"""
    
    def __init__(self, host="http://localhost:11434"):
        self.host = host
        self.current_model = None
        self.messages = []  # Store conversation history for chat API
    
    def is_running(self):
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_models(self):
        try:
            response = requests.get(f"{self.host}/api/tags", timeout=10)
            if response.status_code == 200:
                data = response.json()
                return [model['name'] for model in data.get('models', [])]
        except Exception as e:
            print(f"{Colors.RED}Error fetching models: {e}{Colors.RESET}")
        return []
    
    def set_model(self, model):
        self.current_model = model
    
    def reset_conversation(self):
        """Clear conversation history"""
        self.messages = []
    
    def chat(self, user_message, system_prompt=None, stream=True):
        """Send message using Ollama chat API with proper message format"""
        if not self.current_model:
            return "Error: No model selected. Use /models to select one."
        
        # Add user message to history
        self.messages.append({
            "role": "user",
            "content": user_message
        })
        
        # Build payload for chat API
        payload = {
            "model": self.current_model,
            "messages": self.messages,
            "stream": stream
        }
        
        # Add system prompt if provided and not already in messages
        if system_prompt:
            payload["messages"] = [{"role": "system", "content": system_prompt}] + self.messages
        
        try:
            response = requests.post(
                f"{self.host}/api/chat",
                json=payload,
                stream=stream,
                timeout=120
            )
            
            if stream:
                full_response = ""
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line)
                        message = data.get('message', {})
                        chunk = message.get('content', '')
                        full_response += chunk
                        print(chunk, end='', flush=True)
                        if data.get('done', False):
                            break
                print()
                
                # Add assistant response to history
                self.messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                
                return full_response
            else:
                data = response.json()
                assistant_message = data.get('message', {}).get('content', '')
                
                # Add assistant response to history
                self.messages.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
                return assistant_message
        except Exception as e:
            # Remove the failed user message from history
            if self.messages and self.messages[-1]["role"] == "user":
                self.messages.pop()
            return f"Error: {e}"


class FileOperations:
    """Handle all file operations with permission checks"""
    
    def __init__(self, config_manager):
        self.config = config_manager
    
    def check_permission(self, perm):
        if not self.config.get_permission(perm):
            print(f"{Colors.RED}Permission denied: {perm} is disabled{Colors.RESET}")
            return False
        return True
    
    def read_file(self, filepath):
        if not self.check_permission('file_read'):
            return None
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"{Colors.RED}Error reading file: {e}{Colors.RESET}")
            return None
    
    def write_file(self, filepath, content):
        if not self.check_permission('file_write'):
            return False
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"{Colors.GREEN}File written: {filepath}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.RED}Error writing file: {e}{Colors.RESET}")
            return False
    
    def delete_file(self, filepath):
        if not self.check_permission('file_delete'):
            return False
        
        if self.config.config.get('safety', {}).get('confirm_delete', True):
            confirm = input(f"{Colors.YELLOW}Delete '{filepath}'? (yes/no): {Colors.RESET}")
            if confirm.lower() not in ['yes', 'y']:
                print(f"{Colors.YELLOW}Deletion cancelled.{Colors.RESET}")
                return False
        
        try:
            os.remove(filepath)
            print(f"{Colors.GREEN}File deleted: {filepath}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.RED}Error deleting file: {e}{Colors.RESET}")
            return False
    
    def create_directory(self, dirpath):
        if not self.check_permission('dir_create'):
            return False
        try:
            os.makedirs(dirpath, exist_ok=True)
            print(f"{Colors.GREEN}Directory created: {dirpath}{Colors.RESET}")
            return True
        except Exception as e:
            print(f"{Colors.RED}Error creating directory: {e}{Colors.RESET}")
            return False
    
    def list_directory(self, dirpath="."):
        if not self.check_permission('dir_list'):
            return []
        try:
            items = os.listdir(dirpath)
            return items
        except Exception as e:
            print(f"{Colors.RED}Error listing directory: {e}{Colors.RESET}")
            return []

class AquaDev:
    """Main AquaDev Agent class"""
    
    def __init__(self):
        # Directory where aquadev.py is located (for config files)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Stay in current working directory (where user runs the command)
        # Do NOT change directory - this allows working in any project folder
        
        self.ui = AquaDevUI()
        self.config = ConfigManager(os.path.join(self.base_dir, "Agree.yaml"))
        self.ollama = OllamaClient(self.config.config.get('ollama', {}).get('host', 'http://localhost:11434'))
        self.file_ops = FileOperations(self.config)
        self.conversation_history = []
        self.working_dir = os.getcwd()
        
        self.system_prompt = """You are AquaDev, an AI development assistant that creates files automatically.

RULES:
1. Use FULL PATH in backticks: `folder/filename.py`
2. Include complete code in a python code block
3. When user says "folder X and add file Y" - path is `X/Y`
4. NO shell commands (no mkdir, touch, cd)
5. Brief explanation, then code

Example response format:
Creating `Code/Calculator.py` with basic functions:

[then a python code block with the actual code]

The code block is required to create the file."""
    
    def setup_first_run(self):
        """Handle first-time user agreement"""
        self.ui.clear_screen()
        self.ui.print_banner()
        self.ui.print_agreement()
        
        while True:
            response = input(f"{Colors.CYAN}Do you agree and want to give permission to AquaDev? (yes/no): {Colors.RESET}")
            if response.lower() in ['yes', 'y']:
                self.config.set_user_agreed()
                print(f"\n{Colors.GREEN}Thank you! Permissions granted. Starting AquaDev...{Colors.RESET}\n")
                return True
            elif response.lower() in ['no', 'n']:
                print(f"\n{Colors.YELLOW}Permission denied. AquaDev cannot operate without your consent.{Colors.RESET}")
                print(f"{Colors.YELLOW}Exiting...{Colors.RESET}\n")
                return False
            else:
                print(f"{Colors.RED}Please enter 'yes' or 'no'{Colors.RESET}")
    
    def select_model(self):
        """Display and select from available Ollama models"""
        print(f"\n{Colors.CYAN}Fetching available models from Ollama...{Colors.RESET}\n")
        
        if not self.ollama.is_running():
            print(f"{Colors.RED}Error: Ollama is not running!{Colors.RESET}")
            print(f"{Colors.YELLOW}Please start Ollama first: 'ollama serve'{Colors.RESET}\n")
            return False
        
        models = self.ollama.get_models()
        
        if not models:
            print(f"{Colors.RED}No models found!{Colors.RESET}")
            print(f"{Colors.YELLOW}Pull a model first: 'ollama pull <model>'{Colors.RESET}")
            print(f"{Colors.YELLOW}Example: 'ollama pull llama2' or 'ollama pull codellama'{Colors.RESET}\n")
            return False
        
        print(f"{Colors.BLUE}{Colors.BOLD}")
        print("  +--------------------------------------------------+")
        print("  |              AVAILABLE OLLAMA MODELS             |")
        print("  +--------------------------------------------------+")
        print(f"{Colors.RESET}")
        
        for i, model in enumerate(models, 1):
            print(f"{Colors.CYAN}  [{i}]{Colors.RESET} {model}")
        
        print(f"\n{Colors.DIM}------------------------------------------------------------{Colors.RESET}")
        
        while True:
            try:
                choice = input(f"\n{Colors.CYAN}Select model number (1-{len(models)}): {Colors.RESET}")
                idx = int(choice) - 1
                if 0 <= idx < len(models):
                    selected = models[idx]
                    self.ollama.set_model(selected)
                    self.config.set_default_model(selected)
                    print(f"\n{Colors.GREEN}Model selected: {selected}{Colors.RESET}\n")
                    return True
                else:
                    print(f"{Colors.RED}Invalid selection. Try again.{Colors.RESET}")
            except ValueError:
                print(f"{Colors.RED}Please enter a number.{Colors.RESET}")
    
    def show_status(self):
        """Show current agent status"""
        ollama_status = "Running" if self.ollama.is_running() else "Not Running"
        status_color = Colors.GREEN if self.ollama.is_running() else Colors.RED
        
        print(f"""
{Colors.CYAN}{Colors.BOLD}
  +--------------------------------------------------+
  |                  AGENT STATUS                    |
  +--------------------------------------------------+
{Colors.RESET}
{Colors.WHITE}  Agent:{Colors.RESET}        AquaDev v{VERSION}
{Colors.WHITE}  Ollama:{Colors.RESET}       {status_color}{ollama_status}{Colors.RESET}
{Colors.WHITE}  Model:{Colors.RESET}        {self.ollama.current_model or 'Not selected'}
{Colors.WHITE}  Working Dir:{Colors.RESET}  {self.working_dir}

{Colors.CYAN}  Permissions:{Colors.RESET}
    File Read:    {Colors.GREEN if self.config.get_permission('file_read') else Colors.RED}{'Enabled' if self.config.get_permission('file_read') else 'Disabled'}{Colors.RESET}
    File Write:   {Colors.GREEN if self.config.get_permission('file_write') else Colors.RED}{'Enabled' if self.config.get_permission('file_write') else 'Disabled'}{Colors.RESET}
    File Delete:  {Colors.GREEN if self.config.get_permission('file_delete') else Colors.RED}{'Enabled' if self.config.get_permission('file_delete') else 'Disabled'}{Colors.RESET}
    Dir Create:   {Colors.GREEN if self.config.get_permission('dir_create') else Colors.RED}{'Enabled' if self.config.get_permission('dir_create') else 'Disabled'}{Colors.RESET}
    Execute Py:   {Colors.GREEN if self.config.get_permission('execute_python') else Colors.RED}{'Enabled' if self.config.get_permission('execute_python') else 'Disabled'}{Colors.RESET}
{Colors.DIM}------------------------------------------------------------{Colors.RESET}
""")
    
    def handle_command(self, cmd):
        """Process user commands"""
        cmd = cmd.strip().lower()
        parts = cmd.split(maxsplit=1)
        base_cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        
        if base_cmd in ['/help', 'help', '/?']:
            self.ui.print_commands()
            return True
        
        elif base_cmd in ['/version', 'version']:
            self.ui.print_version()
            return True
        
        elif base_cmd == '/models':
            self.select_model()
            return True
        
        elif base_cmd == '/model':
            model = self.ollama.current_model or "Not selected"
            print(f"\n{Colors.CYAN}Current model:{Colors.RESET} {model}\n")
            return True
        
        elif base_cmd in ['/clear', 'clear']:
            self.ui.clear_screen()
            self.ui.print_banner()
            return True
        
        elif base_cmd == '/status':
            self.show_status()
            return True
        
        elif base_cmd == '/permissions':
            self.show_status()
            return True
        
        elif base_cmd == '/reset':
            self.conversation_history = []
            self.ollama.reset_conversation()
            print(f"\n{Colors.GREEN}Conversation context reset.{Colors.RESET}\n")
            return True
        
        elif base_cmd == '/files':
            files = self.file_ops.list_directory(self.working_dir)
            if files:
                print(f"\n{Colors.CYAN}Files in {self.working_dir}:{Colors.RESET}\n")
                for f in sorted(files):
                    if os.path.isdir(os.path.join(self.working_dir, f)):
                        print(f"  {Colors.BLUE}[DIR]{Colors.RESET}  {f}")
                    else:
                        print(f"  {Colors.WHITE}[FILE]{Colors.RESET} {f}")
                print()
            return True
        
        elif base_cmd == '/pwd':
            print(f"\n{Colors.CYAN}Current directory:{Colors.RESET} {self.working_dir}\n")
            return True
        
        elif base_cmd == '/cd':
            if args:
                new_path = os.path.abspath(os.path.join(self.working_dir, args))
                if os.path.isdir(new_path):
                    self.working_dir = new_path
                    print(f"\n{Colors.GREEN}Changed to:{Colors.RESET} {self.working_dir}\n")
                else:
                    print(f"\n{Colors.RED}Directory not found:{Colors.RESET} {new_path}\n")
            else:
                print(f"\n{Colors.YELLOW}Usage: /cd <path>{Colors.RESET}\n")
            return True
        
        elif base_cmd == '/read':
            if args:
                filepath = os.path.join(self.working_dir, args)
                content = self.file_ops.read_file(filepath)
                if content:
                    print(f"\n{Colors.CYAN}Content of {args}:{Colors.RESET}\n")
                    print(f"{Colors.DIM}------------------------------------------------------------{Colors.RESET}")
                    print(content)
                    print(f"{Colors.DIM}------------------------------------------------------------{Colors.RESET}\n")
            else:
                print(f"\n{Colors.YELLOW}Usage: /read <filename>{Colors.RESET}\n")
            return True
        
        elif base_cmd in ['/quit', '/exit', 'exit', 'quit']:
            return False
        
        elif base_cmd == '/':
            self.ui.print_commands()
            return True
        
        return None
    
    def handle_delete_operation(self, user_input):
        """Handle file/directory deletion requests"""
        import re
        
        # Valid file extensions
        valid_extensions = ['py', 'js', 'ts', 'jsx', 'tsx', 'html', 'css', 'scss', 
                           'json', 'yaml', 'yml', 'md', 'txt', 'c', 'cpp', 'h', 
                           'java', 'rb', 'go', 'rs', 'php', 'swift', 'kt', 'xml', 'sql']
        ext_pattern = '|'.join(valid_extensions)
        
        # Look for file path in user input
        # Match full paths like Code/file.py or just file.py
        path_match = re.search(rf'([A-Za-z0-9_\-]+/)?([A-Za-z0-9_\-]+\.(?:{ext_pattern}))', user_input, re.IGNORECASE)
        
        if path_match:
            # Construct the path
            if path_match.group(1):
                file_path = path_match.group(1) + path_match.group(2)
            else:
                file_path = path_match.group(2)
            
            full_path = os.path.join(self.working_dir, file_path)
            
            # Check if file exists
            if os.path.exists(full_path):
                # Use the file_ops delete which respects confirm_delete setting
                if self.file_ops.delete_file(full_path):
                    print(f"{Colors.GREEN}Deleted: {file_path}{Colors.RESET}")
                # If delete returns False, the user cancelled or it failed
            else:
                print(f"{Colors.YELLOW}File not found: {file_path}{Colors.RESET}")
                # Try to find similar files
                dir_to_check = os.path.dirname(full_path) or self.working_dir
                if os.path.exists(dir_to_check):
                    files = os.listdir(dir_to_check)
                    similar = [f for f in files if path_match.group(2).lower() in f.lower()]
                    if similar:
                        print(f"{Colors.CYAN}Did you mean one of these?{Colors.RESET}")
                        for f in similar[:5]:
                            print(f"  - {f}")
        else:
            # Look for directory deletion
            dir_match = re.search(r'(?:delete|remove)\s+(?:folder|directory|dir)?\s*([A-Za-z0-9_\-/]+)/?', user_input, re.IGNORECASE)
            if dir_match:
                dir_path = dir_match.group(1).rstrip('/')
                full_path = os.path.join(self.working_dir, dir_path)
                
                if os.path.exists(full_path) and os.path.isdir(full_path):
                    confirm = input(f"{Colors.YELLOW}Delete directory '{dir_path}' and all contents? (yes/no): {Colors.RESET}")
                    if confirm.lower() in ['yes', 'y']:
                        import shutil
                        shutil.rmtree(full_path)
                        print(f"{Colors.GREEN}Deleted directory: {dir_path}{Colors.RESET}")
                    else:
                        print(f"{Colors.YELLOW}Deletion cancelled.{Colors.RESET}")
                else:
                    print(f"{Colors.YELLOW}Directory not found: {dir_path}{Colors.RESET}")
            else:
                print(f"{Colors.YELLOW}Could not determine what to delete. Please specify a file or directory.{Colors.RESET}")

    def extract_code_blocks(self, response):
        """Extract all code blocks with their language hints from response"""
        import re
        blocks = []
        # Match ```language\ncode\n``` pattern
        pattern = r'```(\w*)\n(.*?)```'
        matches = re.findall(pattern, response, re.DOTALL)
        
        # Languages to skip (shell commands are not file content)
        skip_languages = ['bash', 'shell', 'sh', 'cmd', 'powershell', 'ps1', 'terminal', 'console']
        
        for lang, code in matches:
            lang = lang.strip().lower()
            # Skip shell/command blocks - they're instructions, not file content
            if lang in skip_languages:
                continue
            # Skip very short blocks (likely just commands)
            if len(code.strip()) < 20:
                continue
            # Skip blocks that look like shell commands
            if code.strip().startswith(('cd ', 'mkdir ', 'touch ', 'rm ', 'ls ', 'dir ', 'cat ')):
                continue
            blocks.append({'language': lang, 'code': code.strip()})
        return blocks
    
    def extract_file_paths(self, response, user_input):
        """Extract file paths - PRIORITIZE user input over AI response"""
        import re
        
        # Valid file extensions
        valid_extensions = ['py', 'js', 'ts', 'jsx', 'tsx', 'html', 'css', 'scss', 
                           'json', 'yaml', 'yml', 'md', 'txt', 'c', 'cpp', 'h', 
                           'java', 'rb', 'go', 'rs', 'php', 'swift', 'kt', 'xml', 'sql']
        ext_pattern = '|'.join(valid_extensions)
        
        # FIRST: Look for FULL PATH in user input (like Code/HelloWorld.py)
        full_path_match = re.search(rf'([A-Za-z0-9_\-]+/[A-Za-z0-9_\-]+\.(?:{ext_pattern}))', user_input, re.IGNORECASE)
        if full_path_match:
            return [full_path_match.group(1)]
        
        # SECOND: Look for "folder X" + "add Y.py" pattern
        folder_match = re.search(r'(?:folder|directory|dir)\s+([A-Za-z0-9_\-]+)/?', user_input, re.IGNORECASE)
        folder_name = folder_match.group(1) if folder_match else None
        
        # Look for filename in user input
        file_match = re.search(rf'(?:add|create|make)\s+([A-Za-z0-9_\-]+\.(?:{ext_pattern}))', user_input, re.IGNORECASE)
        if not file_match:
            file_match = re.search(rf'([A-Za-z0-9_\-]+\.(?:{ext_pattern}))', user_input, re.IGNORECASE)
        
        # If user specified both folder and file, combine them
        if folder_name and file_match:
            return [f"{folder_name}/{file_match.group(1)}"]
        
        # If only file specified in user input (no folder)
        if file_match:
            return [file_match.group(1)]
        
        # FALLBACK: If nothing found in user input, try AI response backticks
        backtick_pattern = rf'`([A-Za-z0-9_\-./]+\.(?:{ext_pattern}))`'
        matches = re.findall(backtick_pattern, response, re.IGNORECASE)
        
        if matches:
            return [matches[0]]
        
        return []
    
    def process_ai_response(self, response, user_input):
        """Process AI response and handle file operations automatically"""
        import re
        
        user_lower = user_input.lower()
        
        # CHECK FOR DELETE OPERATION FIRST
        if any(word in user_lower for word in ['delete', 'remove', 'del ']):
            self.handle_delete_operation(user_input)
            return
        
        # Extract code blocks and file paths for create operations
        code_blocks = self.extract_code_blocks(response)
        file_paths = self.extract_file_paths(response, user_input)
        
        # Extract directories ONLY from the file paths we found
        directories_to_create = []
        for fp in file_paths:
            if '/' in fp:
                dir_part = os.path.dirname(fp)
                if dir_part and dir_part not in directories_to_create:
                    directories_to_create.append(dir_part)
        
        # If we found code blocks and file paths, offer to create them
        if code_blocks and file_paths:
            # Try to match code blocks to file paths based on extension/language
            ext_to_lang = {
                'py': ['python', 'py', ''],
                'js': ['javascript', 'js', ''],
                'ts': ['typescript', 'ts', ''],
                'html': ['html', ''],
                'css': ['css', ''],
                'json': ['json', ''],
                'yaml': ['yaml', 'yml', ''],
                'yml': ['yaml', 'yml', ''],
                'md': ['markdown', 'md', ''],
                'sh': ['bash', 'shell', 'sh', ''],
                'bat': ['batch', 'bat', ''],
            }
            
            files_to_create = []
            used_blocks = set()
            
            for fp in file_paths:
                ext = fp.split('.')[-1].lower() if '.' in fp else ''
                valid_langs = ext_to_lang.get(ext, [''])
                
                # Find matching code block
                for i, block in enumerate(code_blocks):
                    if i not in used_blocks:
                        if block['language'].lower() in valid_langs or not block['language']:
                            files_to_create.append({'path': fp, 'content': block['code']})
                            used_blocks.add(i)
                            break
            
            # If we have files to create
            if files_to_create or directories_to_create:
                # Check if auto-execute is enabled
                auto_execute = self.config.config.get('safety', {}).get('auto_execute_file_ops', False)
                
                if not auto_execute:
                    # Show what we detected and ask for confirmation
                    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
                    print(f"{Colors.YELLOW}AquaDev detected file operations:{Colors.RESET}\n")
                    
                    if directories_to_create:
                        print(f"{Colors.BLUE}  Directories to create:{Colors.RESET}")
                        for d in directories_to_create:
                            print(f"    - {d}/")
                    
                    if files_to_create:
                        print(f"{Colors.BLUE}  Files to create:{Colors.RESET}")
                        for f in files_to_create:
                            print(f"    - {f['path']}")
                    
                    print(f"\n{Colors.CYAN}{'='*60}{Colors.RESET}")
                    
                    confirm = input(f"\n{Colors.CYAN}Execute these operations? (yes/no/select): {Colors.RESET}")
                else:
                    confirm = 'yes'  # Auto-execute
                
                if confirm.lower() in ['yes', 'y']:
                    # Create directories first
                    for d in directories_to_create:
                        dir_path = os.path.join(self.working_dir, d)
                        self.file_ops.create_directory(dir_path)
                    
                    # Create files
                    for f in files_to_create:
                        file_path = os.path.join(self.working_dir, f['path'])
                        # Ensure parent directory exists
                        parent_dir = os.path.dirname(file_path)
                        if parent_dir and not os.path.exists(parent_dir):
                            self.file_ops.create_directory(parent_dir)
                        self.file_ops.write_file(file_path, f['content'])
                
                elif confirm.lower() == 'select':
                    # Let user select which operations to perform
                    for d in directories_to_create:
                        sel = input(f"{Colors.CYAN}Create directory '{d}'? (y/n): {Colors.RESET}")
                        if sel.lower() in ['y', 'yes']:
                            dir_path = os.path.join(self.working_dir, d)
                            self.file_ops.create_directory(dir_path)
                    
                    for f in files_to_create:
                        sel = input(f"{Colors.CYAN}Create file '{f['path']}'? (y/n): {Colors.RESET}")
                        if sel.lower() in ['y', 'yes']:
                            file_path = os.path.join(self.working_dir, f['path'])
                            parent_dir = os.path.dirname(file_path)
                            if parent_dir and not os.path.exists(parent_dir):
                                self.file_ops.create_directory(parent_dir)
                            self.file_ops.write_file(file_path, f['content'])
                else:
                    print(f"{Colors.YELLOW}Operations cancelled.{Colors.RESET}")
    
    def chat(self, user_input):
        """Send message to AI and get response"""
        if not self.ollama.current_model:
            print(f"\n{Colors.YELLOW}No model selected. Use /models to select one.{Colors.RESET}\n")
            return
        
        print(f"\n{Colors.GREEN}AquaDev:{Colors.RESET} ", end='')
        
        # Use the chat API with system prompt - history is managed by OllamaClient
        response = self.ollama.chat(user_input, system_prompt=self.system_prompt, stream=True)
        
        # Save to local history for reference
        self.conversation_history.append({
            'user': user_input,
            'assistant': response
        })
        
        # Process response for file operations
        self.process_ai_response(response, user_input)
        
        print()
    
    def run(self):
        """Main run loop"""
        self.ui.clear_screen()
        self.ui.print_banner()
        
        # Check if new user
        if self.config.is_new_user():
            if not self.setup_first_run():
                return
        
        # Check Ollama
        if not self.ollama.is_running():
            print(f"{Colors.RED}Warning: Ollama is not running!{Colors.RESET}")
            print(f"{Colors.YELLOW}Start Ollama with: 'ollama serve'{Colors.RESET}\n")
        
        # Load default model or select one
        default_model = self.config.get_default_model()
        if default_model and default_model in self.ollama.get_models():
            self.ollama.set_model(default_model)
            print(f"{Colors.GREEN}Loaded model: {default_model}{Colors.RESET}\n")
        else:
            self.select_model()
        
        self.ui.print_welcome()
        
        # Main loop
        while True:
            try:
                user_input = input(f"{Colors.CYAN}>>> {Colors.RESET}").strip()
                
                if not user_input:
                    continue
                
                # Check for commands
                if user_input.startswith('/') or user_input.lower() in ['help', 'version', 'clear', 'exit', 'quit']:
                    result = self.handle_command(user_input)
                    if result is None:
                        # Not a command, send to AI
                        self.chat(user_input)
                    elif result is False:
                        # Exit command
                        print(f"\n{Colors.CYAN}Goodbye! Thanks for using AquaDev.{Colors.RESET}\n")
                        break
                else:
                    # Regular chat
                    self.chat(user_input)
                    
            except KeyboardInterrupt:
                print(f"\n\n{Colors.CYAN}Goodbye! Thanks for using AquaDev.{Colors.RESET}\n")
                break
            except Exception as e:
                print(f"\n{Colors.RED}Error: {e}{Colors.RESET}\n")

if __name__ == "__main__":
    agent = AquaDev()
    agent.run()