import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solarPanels = False
        self.dataCollected = 0

    def rotate(self, direction):
        try:
            if direction in ["North", "South", "East", "West"]:
                self.orientation = direction
                logging.info(f"Orientation set to {self.orientation}")
            else:
                raise ValueError(f"Invalid rotation direction: {direction}")
        except ValueError as e:
            logging.error(e)

    def activatePanels(self):
        try:
            if not self.solarPanels:
                self.solarPanels = True
                logging.info("Solar panels activated")
            else:
                raise Warning("Solar panels are already active")
        except Warning as w:
            logging.warning(w)

    def deactivatePanels(self):
        try:
            if self.solarPanels:
                self.solarPanels = False
                logging.info("Solar panels deactivated")
            else:
                raise Warning("Solar panels are already inactive")
        except Warning as w:
            logging.warning(w)

    def collectData(self):
        try:
            if self.solarPanels:
                self.dataCollected += 10
                logging.info(f"Data collected: {self.dataCollected}")
            else:
                raise PermissionError("Cannot collect data: Solar panels are inactive")
        except PermissionError as pe:
            logging.error(pe)

def main():
    satellite = Satellite()
    while True:
        try:
            command = input("Enter command (rotate, activatePanels, deactivatePanels, collectData, exit): ").strip().lower()

            if command == 'exit':
                logging.info("Exiting the Satellite Command System")
                break
            elif command.startswith('rotate'):
                _, direction = command.split()
                satellite.rotate(direction.capitalize())
            elif command == 'activatepanels':
                satellite.activatePanels()
            elif command == 'deactivatepanels':
                satellite.deactivatePanels()
            elif command == 'collectdata':
                satellite.collectData()
            else:
                raise ValueError(f"Invalid command: {command}")
        except ValueError as ve:
            logging.error(ve)
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
