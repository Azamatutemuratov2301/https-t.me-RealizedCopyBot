import yaml
import logging
from mt5_connector import MT5Connector
from copy_logic import CopyLogic

def main():
    logging.basicConfig(level=logging.INFO, filename='activity.log', format='%(asctime)s - %(message)s')
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    master_conf = config['master']
    slaves_conf = config['slaves']
    connector = MT5Connector(master_conf, slaves_conf)
    connector.initialize_all()
    copy_logic = CopyLogic(connector)
    copy_logic.run()

if __name__ == '__main__':
    main()
