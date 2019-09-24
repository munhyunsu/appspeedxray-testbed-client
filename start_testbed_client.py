import os
import configparser
import logging
import sys
import http.client

FLAGS = None


def main(config_path):
    """
    args: configuration file path
    """
    config = configparser.ConfigParser()
    config.read(config_path)

    conn = http.client.HTTPConnection(config['Testbed']['URL'],
                                      config['Testbed']['Port'])
    conn.request('GET', 'registration')
    logging.info(conn.getresponse().read().decode('utf-8'))



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str,
                        help='Configuration file path',
                        default='config.ini')
    parser.add_argument('-v', '--verbose', action='count')

    FLAGS, _ = parser.parse_known_args()

    # Convert relative path to absolute path
    FLAGS.config = os.path.abspath(os.path.expanduser(FLAGS.config))
    
    # Set logging level
    dlvl = logging.INFO
    if FLAGS.verbose is not None:
        if FLAGS.verbose > 0:
            dlvl = logging.DEBUG
    logging.basicConfig(stream=sys.stdout, level=dlvl)

    main(FLAGS.config)

