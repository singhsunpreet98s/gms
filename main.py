from container import Container;
from pathlib import Path;
import constants;
import os;
import logging;
import keyboard;
import time;

from commands.admin_commands import AdminCommand;

def configure_logs():
   log_path = Path(f"{Path.cwd()}/storage/logs");
   if not log_path.exists():
      log_path.mkdir(parents=True, exist_ok=True);

   logging.basicConfig(
         level=logging.DEBUG,
         filename=f"{Path.cwd()}/storage/logs/app.log",
         format="%(asctime)s - %(levelname)s - %(message)s",
         filemode="a"
         );

def main():
   configure_logs();
   container = Container();
   admin_cmd = AdminCommand(container);
   try :
      while True:
         os.system("cls")
         admin_cmd.run();
         print("Press q to exit and enter to continue");
         if keyboard.is_pressed('q'):
            exit;
         time.sleep(5)
   except Exception as err:
      logging.debug(err)
      print("There was some error")  

   

    

if __name__ == "__main__":
    main();