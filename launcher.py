"""
Ancient Inscription OCR - Unified Software Launcher
"""
import os
import sys
import subprocess
import webbrowser
import time

# Path Setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def launch_module(folder_name, port, entry_file, is_python_script=False):
    module_path = os.path.join(PARENT_DIR, folder_name)
    
    if not os.path.exists(module_path):
        print(f"\n❌ Error: Folder '{folder_name}' not found at {module_path}")
        input("Press Enter to continue...")
        return

    os.chdir(module_path)
    print(f"\n🚀 Starting {folder_name}...")
    print(f"🌐 Access URL: http://localhost:{port}")
    print("🛑 Press Ctrl+C to stop the module and return to menu.")
    
    time.sleep(1)
    webbrowser.open(f"http://localhost:{port}/{entry_file}")
    
    try:
        if is_python_script:
            subprocess.run([sys.executable, entry_file])
        else:
            subprocess.run([sys.executable, "-m", "http.server", str(port)])
    except KeyboardInterrupt:
        print("\nModule stopped.")

def main():
    while True:
        clear_screen()
        print("==========================================================")
        print("   🏛️  ANCIENT INSCRIPTION OCR - FINAL PROJECT SOFTWARE   ")
        print("==========================================================")
        print(" [1] Data Explorer (Search & Browse 2,043 Inscriptions)")
        print(" [2] ML Model Dashboard (Inference & Performance)")
        print(" [3] Read Instruction Manual")
        print(" [0] Exit Application")
        print("==========================================================")
        
        choice = input("\nSelect Option > ")
        
        if choice == '1':
            launch_module("OCR_Data_Software_Package", 8000, "index.html")
        elif choice == '2':
            # Pointing to the main demo in the ML package
            launch_module("OCR_Software_Package", 8080, "run_demo.py", is_python_script=True)
        elif choice == '3':
            manual_path = os.path.join(BASE_DIR, "MANUAL.md")
            if os.name == 'nt':
                os.startfile(manual_path)
            else:
                subprocess.run(['open', manual_path])
        elif choice == '0':
            print("\nThank you for using the OCR Software. Goodbye!")
            time.sleep(1)
            break
        else:
            print("\nInvalid choice, please try again.")
            time.sleep(1)

    # Reset path before exiting
    os.chdir(BASE_DIR)

if __name__ == "__main__":
    main()